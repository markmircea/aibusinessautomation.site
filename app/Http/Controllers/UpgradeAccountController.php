<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;
use Inertia\Inertia;
use App\Models\User;
use Illuminate\Support\Facades\Http;
use Illuminate\Support\Facades\Hash;
use Illuminate\Support\Str;

class UpgradeAccountController extends Controller
{
    public function show()
    {
        return Inertia::render('UpgradeAccount', [
            'paypalClientId' => config('services.paypal.client_id'),
        ]);
    }

    public function process(Request $request)
    {
        $request->validate([
            'paypal_order_id' => 'required|string',
        ]);

        $orderId = $request->input('paypal_order_id');

        // Verify the PayPal payment
        $response = Http::withBasicAuth(config('services.paypal.client_id'), config('services.paypal.secret'))
        ->withOptions([
            'verify' => false, // Only use this for local development!
        ])
         ->get("https://api-m.sandbox.paypal.com/v2/checkout/orders/{$orderId}");
        //->get("https://api-m.paypal.com/v2/checkout/orders/{$orderId}");

        if ($response->successful() && $response['status'] === 'COMPLETED') {
            if (auth()->check()) {
                $this->upgradeUser(auth()->user());
                return redirect()->route('dashboard')->with('success', 'Congratulations! Your account has been successfully upgraded. You now have access to all premium features.');
            } else {
                // Store payment info in session for later use
                session(['pending_upgrade' => true]);
                return redirect()->route('register')->with('success', 'Payment successful! Please create an account to complete your upgrade.');
            }
        }

        return back()->with('error', 'There was an error processing your payment. Please try again or contact our support team for assistance.');
    }

    public function completeRegistration(Request $request)
    {
        $request->validate([
            'name' => 'required|string|max:255',
            'email' => 'required|string|email|max:255|unique:users',
            'password' => 'required|string|min:8|confirmed',
        ]);

        $user = User::create([
            'name' => $request->name,
            'email' => $request->email,
            'password' => Hash::make($request->password),
        ]);

        if (session('pending_upgrade')) {
            $this->upgradeUser($user);
            session()->forget('pending_upgrade');
        }

        auth()->login($user);

        return redirect()->route('dashboard')->with('success', 'Your account has been created and upgraded successfully!');
    }

    private function upgradeUser(User $user)
    {
        $user->has_paid_subscription = true;
        $user->subscription_started_at = now();
        $user->save();
    }
}
