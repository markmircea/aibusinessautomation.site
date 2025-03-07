<?php

use Illuminate\Foundation\Application;
use Illuminate\Support\Facades\Route;
use Inertia\Inertia;
use App\Http\Controllers\OpenRouterController;
use App\Http\Controllers\UpgradeAccountController;
use App\Http\Controllers\Auth\CustomRegisterController;
use App\Http\Controllers\Auth\GoogleController;
use App\Http\Controllers\PdfDownloadController;
use Illuminate\Support\Facades\Auth;
use App\Http\Controllers\ReviewController;

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

// Google Login Routes
Route::get('auth/google', [GoogleController::class, 'redirectToGoogle'])->name('auth.google');
Route::get('auth/google/callback', [GoogleController::class, 'handleGoogleCallback']);

// Override the default registration route
Route::get('/register', [CustomRegisterController::class, 'create'])
    ->middleware(['guest'])
    ->name('register');

// Landing page route
Route::get('/', function () {
    return Inertia::render('Welcome', [
        'canLogin' => Route::has('login'),
        'canRegister' => Route::has('register'),
    ]);
})->name('welcome');

// Web Development routes
Route::prefix('web-development')->name('web-development.')->group(function () {
    Route::get('/ecommerce', function () {
        return Inertia::render('WebDevelopment/Ecommerce');
    })->name('ecommerce');

    Route::get('/presentation', function () {
        return Inertia::render('WebDevelopment/Presentation');
    })->name('presentation');

    Route::get('/mobile', function () {
        return Inertia::render('WebDevelopment/Mobile');
    })->name('mobile');

    Route::get('/automation', function () {
        return Inertia::render('WebDevelopment/Automation');
    })->name('automation');
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

// Dashboard route for authenticated users
// Route::get('/dashboard', function () {
//     $user = Auth::user();
//     $isSubscribed = $user ? $user->isSubscribed() : false;

//     return Inertia::render('Dashboard', [
//         'isSubscribed' => $isSubscribed,
//     ]);
// })->name('dashboard')->middleware(['auth:sanctum', config('jetstream.auth_session'), 'verified']);

// Free Practice Test route accessible to all users
Route::get('/free-practice-test', function () {
    return Inertia::render('FreePracticeTestStart');
})->name('free.practice.test');

Route::get('/full-practice-test', function () {
    return Inertia::render('FullPracticeTest');
})->name('full.practice.test');

Route::get('/upgrade-account', [UpgradeAccountController::class, 'show'])->name('upgrade.account');
Route::post('/upgrade-account', [UpgradeAccountController::class, 'process'])->name('upgrade.account.process');

// New route for completing registration after payment
Route::post('/complete-registration', [UpgradeAccountController::class, 'completeRegistration'])->name('complete.registration');

Route::post('/reviews', [ReviewController::class, 'store']);
Route::get('/api/reviews', [ReviewController::class, 'getReviews']);

use App\Http\Controllers\ContactController;

// Contact form submission
Route::post('/contact', [ContactController::class, 'submit'])->name('contact.submit');

// Authenticated routes group
Route::middleware([
    'auth:sanctum',
    config('jetstream.auth_session'),
    'verified',
])->group(function () {
    // Referral routes
    Route::get('/referrals', [App\Http\Controllers\ReferralController::class, 'index'])->name('referrals.index');
    
    // Admin routes
    Route::middleware(['can:admin'])->prefix('admin')->name('admin.')->group(function () {
        // Admin Dashboard
        Route::get('/dashboard', function () {
            return Inertia::render('Admin/Dashboard');
        })->name('dashboard');
        
        // Referrals Management
        Route::get('/referrals', [App\Http\Controllers\Admin\ReferralController::class, 'index'])->name('referrals.index');
        Route::get('/referrals/{referral}/edit', [App\Http\Controllers\Admin\ReferralController::class, 'edit'])->name('referrals.edit');
        Route::put('/referrals/{referral}', [App\Http\Controllers\Admin\ReferralController::class, 'update'])->name('referrals.update');
        
        // Contacts Management
        Route::get('/contacts', [App\Http\Controllers\Admin\ContactController::class, 'index'])->name('contacts.index');
        Route::get('/contacts/{contact}', [App\Http\Controllers\Admin\ContactController::class, 'show'])->name('contacts.show');
    });
});

// Paid user routes group
Route::middleware([
    'auth:sanctum',
    config('jetstream.auth_session'),
    'verified',
    'paid.user',
])->group(function () {
    Route::post('/api/generate-question', [OpenRouterController::class, 'generateQuestion'])->name('generate.question');
    Route::post('/api/generate-explanation', [OpenRouterController::class, 'generateExplanation'])->name('generate.explanation');

    Route::get('/verbal-test', function () {
        return Inertia::render('VerbalTest');
    })->name('verbal.test');

    Route::get('/verbal-test-start', function () {
        return Inertia::render('VerbalTestStart');
    })->name('verbal.test.start');

    Route::get('/verbal-test-json-start', function () {
        return Inertia::render('VerbalJsonStart');
    })->name('verbal.json.test.start');

    Route::get('/math-logic-test', function () {
        return Inertia::render('MathLogicTest');
    })->name('math.logic.test');

    Route::get('/math-test-start', function () {
        return Inertia::render('MathLogicTestStart');
    })->name('math.test.start');

    Route::get('/math-test-json-start', function () {
        return Inertia::render('MathLogicJsonStart');
    })->name('math.json.test.start');

    Route::get('/spatial-reasoning-test', function () {
        return Inertia::render('SpatialReasoningTest');
    })->name('spatial.reasoning.test');

    Route::get('/spatial-test-start', function () {
        return Inertia::render('SpatialReasoningTestStart');
    })->name('spatial.test.start');

    Route::get('/spatial-test-json-start', function () {
        return Inertia::render('SpatialReasoningJsonStart');
    })->name('spatial.json.start');

    Route::get('/full-practice-test-start', function () {
        return Inertia::render('FullPracticeTestStart');
    })->name('full-practice-test-start');



    // Full Practice Test routes
    for ($i = 1; $i <= 10; $i++) {
        Route::get("/full-practice-test-{$i}", function () use ($i) {
            return Inertia::render('FullTest', ['testNumber' => $i]);
        })->name("full.practice.test.{$i}");

        Route::get("/full-practice-test-{$i}-start", function () use ($i) {
            return Inertia::render('FullPracticeTestStart', ['testNumber' => $i]);
        })->name("full.practice.test.{$i}.start");
    }

    Route::get('/download-pdf/{filename}', [PdfDownloadController::class, 'download'])->name('download.pdf');

});

Route::fallback(function () {
    return redirect('/');
});

// Route::get('/generate-pdfs', [QuestionPDFController::class, 'generatePDFs'])->name('generate.pdf');
