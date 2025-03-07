<?php

namespace App\Http\Controllers;

use App\Models\Referral;
use App\Models\User;
use Illuminate\Http\Request;
use Illuminate\Support\Facades\Auth;
use Inertia\Inertia;

class ReferralController extends Controller
{
    /**
     * Display the user's referrals.
     */
    public function index()
    {
        $user = Auth::user();
        
        $referrals = Referral::with('contact')
            ->where('referrer_id', $user->id)
            ->orderBy('created_at', 'desc')
            ->get();
            
        $stats = [
            'total' => $referrals->count(),
            'pending' => $referrals->where('status', 'pending')->count(),
            'converted' => $referrals->where('status', 'converted')->count(),
            'paid' => $referrals->where('status', 'paid')->count(),
            'totalCommission' => $referrals->where('status', 'paid')->sum('commission_amount'),
            'pendingCommission' => $referrals->where('status', 'converted')->sum('commission_amount'),
        ];
        
        return Inertia::render('Referrals/Index', [
            'referrals' => $referrals,
            'stats' => $stats,
            'referralLink' => $user->getReferralLink(),
            'referralCode' => $user->referral_code,
        ]);
    }
}
