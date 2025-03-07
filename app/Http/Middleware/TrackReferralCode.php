<?php

namespace App\Http\Middleware;

use Closure;
use Illuminate\Http\Request;
use Symfony\Component\HttpFoundation\Response;

class TrackReferralCode
{
    /**
     * Handle an incoming request.
     *
     * @param  \Closure(\Illuminate\Http\Request): (\Symfony\Component\HttpFoundation\Response)  $next
     */
    public function handle(Request $request, Closure $next): Response
    {
        // Check if the request has a referral code
        if ($request->has('ref')) {
            $referralCode = $request->get('ref');
            
            // Store the referral code in the session
            session(['referral_code' => $referralCode]);
        }

        return $next($request);
    }
}
