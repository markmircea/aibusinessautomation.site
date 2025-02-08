<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;
use Illuminate\Support\Facades\Storage;
use Illuminate\Support\Facades\Auth;


class PdfDownloadController extends Controller
{
    public function download($filename)
    {
        $path = 'public/pdfs/' . $filename;
        $user = Auth::user();

        if (!Storage::exists($path)) {
            abort(404);
        }
        if ($user)
        {

            return Storage::download($path);
        } else {
            return abort(402);
        }
    }
}
