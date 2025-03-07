<?php

namespace App\Http\Controllers;

use App\Models\Contact;
use App\Models\Referral;
use App\Models\User;
use App\Mail\ContactFormSubmission;
use Illuminate\Http\Request;
use Illuminate\Support\Facades\Auth;
use Illuminate\Support\Facades\Log;
use Illuminate\Support\Facades\Mail;
use Inertia\Inertia;

class ContactController extends Controller
{
    public function submit(Request $request)
    {
        // Validate the request
        $data = $request->validate([
            'name' => 'nullable|string|max:255',
            'email' => 'required|email|max:255',
            'company' => 'nullable|string|max:255',
            'solution' => 'nullable|string|max:255',
            'tech_stack' => 'nullable|string',
            'message' => 'required|string',
        ]);

        // Add user_id if user is authenticated
        if (Auth::check()) {
            $data['user_id'] = Auth::id();
        }

        // Check if there's a referral code in the session
        if (session()->has('referral_code')) {
            $data['referral_code'] = session('referral_code');
        }
        
        // Determine the solution based on the referer URL
        $referer = $request->headers->get('referer');
        if (empty($data['solution'])) {
            if (strpos($referer, 'web-development') !== false) {
                $data['solution'] = 'Web Development';
            } else {
                $data['solution'] = 'AI Automation';
            }
        }

        try {
            // Save to database
            $contact = Contact::create($data);

            // If there's a referral code, create a referral record
            if (isset($data['referral_code'])) {
                $referrerUser = User::where('referral_code', $data['referral_code'])->first();
                
                if ($referrerUser) {
                    // Create a new referral record
                    Referral::create([
                        'referrer_id' => $referrerUser->id,
                        'contact_id' => $contact->id,
                        'status' => 'pending'
                    ]);
                }
            }

            // Send email notification
            Mail::send(new ContactFormSubmission($contact));

            return redirect()->route('welcome')->with('success', 'Thank you for your message! We will get back to you soon.');
        } catch (\Exception $e) {
            // Log the error
            Log::error('Contact form submission error: ' . $e->getMessage());
            
            return redirect()->back()
                ->withInput()
                ->with('error', 'Sorry, there was an error submitting your message. Please try again later.');
        }
    }
}
