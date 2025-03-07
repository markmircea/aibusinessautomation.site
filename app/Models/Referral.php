<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Factories\HasFactory;
use Illuminate\Database\Eloquent\Model;

class Referral extends Model
{
    use HasFactory;

    /**
     * The attributes that are mass assignable.
     *
     * @var array<int, string>
     */
    protected $fillable = [
        'referrer_id',
        'contact_id',
        'status',
        'contract_amount',
        'commission_amount',
        'notes',
    ];

    /**
     * The attributes that should be cast.
     *
     * @var array<string, string>
     */
    protected $casts = [
        'contract_amount' => 'decimal:2',
        'commission_amount' => 'decimal:2',
    ];

    /**
     * Get the user who referred (the referrer).
     */
    public function referrer()
    {
        return $this->belongsTo(User::class, 'referrer_id');
    }

    /**
     * Get the contact associated with this referral.
     */
    public function contact()
    {
        return $this->belongsTo(Contact::class);
    }

    /**
     * Calculate the commission amount (10% of contract amount).
     */
    public function calculateCommission()
    {
        if ($this->contract_amount) {
            $this->commission_amount = $this->contract_amount * 0.1;
            return $this->commission_amount;
        }
        
        return 0;
    }
}
