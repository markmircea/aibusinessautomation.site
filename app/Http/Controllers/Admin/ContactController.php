<?php

namespace App\Http\Controllers\Admin;

use App\Http\Controllers\Controller;
use App\Models\Contact;
use Illuminate\Http\Request;
use Inertia\Inertia;

class ContactController extends Controller
{
    /**
     * Display a listing of the contacts.
     */
    public function index()
    {
        $contacts = Contact::orderBy('created_at', 'desc')->get();
        
        return Inertia::render('Admin/Contacts/Index', [
            'contacts' => $contacts,
        ]);
    }

    /**
     * Display the specified contact.
     */
    public function show(Contact $contact)
    {
        return Inertia::render('Admin/Contacts/Show', [
            'contact' => $contact,
        ]);
    }
}
