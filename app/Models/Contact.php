<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Factories\HasFactory;
use Illuminate\Database\Eloquent\Model;

class Contact extends Model
{
    use HasFactory;

    /**
     * The attributes that are mass assignable.
     *
     * @var array<int, string>
     */
    protected $fillable = [
        'user_id',
        'name',
        'email',
        'company',
        'solution',
        'message'
    ];

    /**
     * Get the user that created the contact form submission.
     */
    public function user()
    {
        return $this->belongsTo(User::class);
    }
}
