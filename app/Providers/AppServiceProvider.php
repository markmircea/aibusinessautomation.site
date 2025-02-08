<?php

namespace App\Providers;

use Illuminate\Support\ServiceProvider;
use Inertia\Inertia;


class AppServiceProvider extends ServiceProvider
{
    /**
     * Register any application services.
     */
    public function register(): void
    {
        //
    }

    /**
     * Bootstrap any application services.
     */
    public function boot()
    {
        Inertia::share([
            'component' => function () {
                return request()->route()->getName();
            },
            'url' => function () {
                return url()->current();
            },
            'flash' => function () {
                return [
                    'success' => session()->get('success'),
                    'error' => session()->get('error'),
                    'message' => session()->get('message'),
                ];
            },
        ]);
    }
}
