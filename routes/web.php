<?php

use Illuminate\Foundation\Application;
use Illuminate\Support\Facades\Route;
use Inertia\Inertia;

/*
|--------------------------------------------------------------------------
| Web Routes
|--------------------------------------------------------------------------
|
| Here is where you can register web routes for your application. These
| routes are loaded by the RouteServiceProvider within a group which
| contains the "web" middleware group. Now create something great!
|
*/

// Landing page route
Route::get('/', function () {
    return Inertia::render('Welcome');
})->name('welcome');

// Legal pages. Previously unroutable: the components existed on disk but had
// no route and no link, leaving an EU-registered business collecting contact
// details with no reachable privacy policy.
Route::get('/privacy-policy', function () {
    return Inertia::render('PrivacyPolicy');
})->name('privacy-policy');

Route::get('/terms-of-service', function () {
    return Inertia::render('TermsOfService');
})->name('terms-of-service');

// Portfolio page
Route::get('/portfolio', function () {
    return Inertia::render('Portfolio');
})->name('portfolio');

// Web Development routes
Route::prefix('web-development')->name('web-development.')->group(function () {
    // Section landing page, reachable by clicking "Web Development" in the nav.
    Route::get('/', function () {
        return Inertia::render('WebDevelopment/Index');
    })->name('index');

    // All four services render the same component; content comes from
    // resources/js/data/webDevelopmentServices.js keyed by slug.
    foreach (['ecommerce', 'presentation', 'mobile', 'automation'] as $slug) {
        Route::get("/{$slug}", function () use ($slug) {
            return Inertia::render('WebDevelopment/Service', ['slug' => $slug]);
        })->name($slug);
    }
});

// Solution routes
Route::prefix('solutions')->name('solutions.')->group(function () {
    Route::get('/document-processing', function () {
        return Inertia::render('Solutions/DocumentProcessing');
    })->name('document-processing');

    Route::get('/customer-service', function () {
        return Inertia::render('Solutions/CustomerService');
    })->name('customer-service');

    Route::get('/financial-operations', function () {
        return Inertia::render('Solutions/FinancialOperations');
    })->name('financial-operations');

    Route::get('/hr-recruitment', function () {
        return Inertia::render('Solutions/HrRecruitment');
    })->name('hr-recruitment');

    Route::get('/sales-marketing', function () {
        return Inertia::render('Solutions/SalesMarketing');
    })->name('sales-marketing');

    Route::get('/supply-chain', function () {
        return Inertia::render('Solutions/SupplyChain');
    })->name('supply-chain');

    Route::get('/desktop-automation', function () {
        return Inertia::render('Solutions/DesktopAutomation');
    })->name('desktop-automation');

    Route::get('/ai-integrations', function () {
        return Inertia::render('Solutions/AIIntegrations');
    })->name('ai-integrations');
});

use App\Http\Controllers\ContactController;

// Contact form submission
Route::post('/contact', [ContactController::class, 'submit'])->name('contact.submit');

// The site is quote/info forms only: there are no user accounts. Fortify and
// Jetstream routes are switched off in their service providers, and the
// referral program and admin area (both account-based) are hidden until they
// come back. Their controllers and pages are kept for that.

Route::fallback(function () {
    return Inertia::render('Error', ['status' => 404])->toResponse(request())->setStatusCode(404);
});
