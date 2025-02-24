<?php

namespace App\Http\Controllers;

use App\Models\Contact;
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

        try {
            // Save to database
            $contact = Contact::create($data);

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
