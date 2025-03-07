<?php

namespace App\Providers;

use Illuminate\Support\Facades\Gate;
use Illuminate\Foundation\Support\Providers\AuthServiceProvider as ServiceProvider;

class AuthServiceProvider extends ServiceProvider
{
    /**
     * The model to policy mappings for the application.
     *
     * @var array<class-string, class-string>
     */
    protected $policies = [
        // 'App\Models\Model' => 'App\Policies\ModelPolicy',
    ];

    /**
     * Register any authentication / authorization services.
     */
    public function boot(): void
    {
        $this->registerPolicies();

        // Define admin gate - for now, hardcode admin emails
        // In a production app, you would use a role/permission system
        Gate::define('admin', function ($user) {
            $adminEmails = [
                'admin@example.com',
                // Add more admin emails as needed
            ];
            
            return in_array($user->email, $adminEmails);
        });
    }
}
