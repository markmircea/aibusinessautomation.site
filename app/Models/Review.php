<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Model;

class Review extends Model
{
    protected $fillable = [
        'reviewer_name',
        'reviewer_email',
        'rating',
        'comment',
        'created_at',
        'updated_at'
    ];
}
