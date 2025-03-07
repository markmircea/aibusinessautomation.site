<?php

namespace App\Models;

use Illuminate\Contracts\Auth\MustVerifyEmail;
use Illuminate\Database\Eloquent\Factories\HasFactory;
use Illuminate\Foundation\Auth\User as Authenticatable;
use Illuminate\Notifications\Notifiable;
use Laravel\Fortify\TwoFactorAuthenticatable;
use Laravel\Jetstream\HasProfilePhoto;
use Laravel\Jetstream\HasTeams;
use Laravel\Sanctum\HasApiTokens;

class User extends Authenticatable
{
    use HasApiTokens;
    use HasFactory;
    use HasProfilePhoto;
    use HasTeams;
    use Notifiable;
    use TwoFactorAuthenticatable;

    /**
     * The attributes that are mass assignable.
     *
     * @var array<int, string>
     */
    protected $fillable = [
        'name', 'email', 'password', 'has_paid_subscription', 'subscription_started_at','google_id',
    ];

    /**
     * The attributes that should be hidden for serialization.
     *
     * @var array<int, string>
     */
    protected $hidden = [
        'password',
        'remember_token',
        'two_factor_recovery_codes',
        'two_factor_secret',
    ];

    /**
     * The attributes that should be cast.
     *
     * @var array<string, string>
     */
    protected $casts = [
        'email_verified_at' => 'datetime',
        'has_paid_subscription' => 'boolean',
        'subscription_started_at' => 'datetime',
    ];

    /**
     * The accessors to append to the model's array form.
     *
     * @var array<int, string>
     */
    protected $appends = [
        'profile_photo_url',
    ];

    /**
     * Boot the model.
     */
    protected static function boot()
    {
        parent::boot();

        static::creating(function ($user) {
            // Generate a unique referral code if not already set
            if (!$user->referral_code) {
                $user->referral_code = self::generateUniqueReferralCode();
            }
        });
    }

    /**
     * Generate a unique referral code.
     *
     * @return string
     */
    protected static function generateUniqueReferralCode()
    {
        $characters = '23456789ABCDEFGHJKLMNPQRSTUVWXYZ';
        $length = 8;
        
        do {
            $referralCode = '';
            for ($i = 0; $i < $length; $i++) {
                $referralCode .= $characters[random_int(0, strlen($characters) - 1)];
            }
        } while (self::where('referral_code', $referralCode)->exists());
        
        return $referralCode;
    }

    /**
     * Check if the user has an active paid subscription (lifetime plan).
     *
     * @return bool
     */
    public function isSubscribed()
    {
        return $this->has_paid_subscription;
    }

    /**
     * Get the referrals created by this user.
     */
    public function referrals()
    {
        return $this->hasMany(Referral::class, 'referrer_id');
    }

    /**
     * Get the user who referred this user.
     */
    public function referredBy()
    {
        return $this->belongsTo(User::class, 'referred_by_user_id');
    }

    /**
     * Get users referred by this user.
     */
    public function referredUsers()
    {
        return $this->hasMany(User::class, 'referred_by_user_id');
    }

    /**
     * Get the full referral URL for this user.
     *
     * @return string
     */
    public function getReferralLink()
    {
        return url('/?ref=' . $this->referral_code);
    }

    /**
     * Get the date when the subscription (lifetime plan) started.
     *
     * @return \Illuminate\Support\Carbon|null
     */
    public function subscriptionStartDate()
    {
        return $this->subscription_started_at;
    }
}
