<?php

namespace App\Http\Controllers\Admin;

use App\Http\Controllers\Controller;
use App\Models\Referral;
use App\Models\User;
use Illuminate\Http\Request;
use Inertia\Inertia;

class ReferralController extends Controller
{
    /**
     * Display a listing of the referrals.
     */
    public function index()
    {
        $referrals = Referral::with(['referrer', 'contact'])
            ->orderBy('created_at', 'desc')
            ->get();
            
        $stats = [
            'total' => $referrals->count(),
            'pending' => $referrals->where('status', 'pending')->count(),
            'converted' => $referrals->where('status', 'converted')->count(),
            'paid' => $referrals->where('status', 'paid')->count(),
            'totalCommission' => $referrals->sum('commission_amount'),
            'pendingPayment' => $referrals->where('status', 'converted')->sum('commission_amount'),
        ];
        
        return Inertia::render('Admin/Referrals/Index', [
            'referrals' => $referrals,
            'stats' => $stats,
        ]);
    }

    /**
     * Show the form for editing the specified referral.
     */
    public function edit(Referral $referral)
    {
        $referral->load(['referrer', 'contact']);
        
        return Inertia::render('Admin/Referrals/Edit', [
            'referral' => $referral,
        ]);
    }

    /**
     * Update the specified referral in storage.
     */
    public function update(Request $request, Referral $referral)
    {
        $validated = $request->validate([
            'status' => 'required|in:pending,converted,paid',
            'contract_amount' => 'nullable|numeric|min:0',
            'notes' => 'nullable|string',
        ]);
        
        // If contract amount is provided and status is converted, calculate commission
        if (isset($validated['contract_amount']) && $validated['status'] === 'converted') {
            $referral->contract_amount = $validated['contract_amount'];
            $referral->commission_amount = $referral->calculateCommission();
        }
        
        $referral->status = $validated['status'];
        
        if (isset($validated['notes'])) {
            $referral->notes = $validated['notes'];
        }
        
        $referral->save();
        
        return redirect()->route('admin.referrals.index')
            ->with('success', 'Referral updated successfully.');
    }
}
