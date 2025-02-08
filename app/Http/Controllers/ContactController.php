<?php

namespace App\Http\Controllers;

use App\Models\Contact;
use Illuminate\Http\Request;
use Illuminate\Support\Facades\Auth;
use Inertia\Inertia;

class ContactController extends Controller
{
    public function submit(Request $request)
    {
        // Validate the request
        $data = $request->validate([
            'name' => 'required|string|max:255',
            'email' => 'required|email|max:255',
            'company' => 'required|string|max:255',
            'solution' => 'required|string|max:255',
            'message' => 'required|string',
        ]);

        // Add user_id if user is authenticated
        if (Auth::check()) {
            $data['user_id'] = Auth::id();
        }

        // Save to database
        Contact::create($data);

        return redirect()->route('welcome')->with('success', 'Thank you for your message! We will get back to you soon.');

    }
}
