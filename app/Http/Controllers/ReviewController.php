<?php
// app/Http/Controllers/ReviewController.php
namespace App\Http\Controllers;

use App\Models\Review;
use Illuminate\Http\Request;
use Illuminate\Support\Facades\Log;

namespace App\Http\Controllers;

use App\Models\Review;
use Illuminate\Http\Request;
use Illuminate\Support\Facades\DB;

class ReviewController extends Controller
{
    public function store(Request $request)
    {
        try {
            $validated = $request->validate([
                'reviewer_name' => 'required|string|max:255',
                'reviewer_email' => 'nullable|email|max:255',
                'rating' => 'required|integer|min:1|max:5',
                'comment' => 'nullable|string|max:1000',
            ]);

            $review = Review::create([
                ...$validated,
                'created_at' => now(),
                'updated_at' => now(),
            ]);

            return response()->json([
                'message' => 'Review submitted successfully!',
                'review' => $review
            ], 201);
        } catch (\Exception $e) {
            return response()->json([
                'message' => 'Error submitting review',
                'errors' => $e->getMessage()
            ], 422);
        }
    }

    public function getReviews(Request $request)
    {
        $reviews = Review::latest()
            ->paginate(10);

        $allReviews = Review::all();
        $averageRating = $allReviews->avg('rating');

        $ratingDistribution = [
            5 => $allReviews->where('rating', 5)->count(),
            4 => $allReviews->where('rating', 4)->count(),
            3 => $allReviews->where('rating', 3)->count(),
            2 => $allReviews->where('rating', 2)->count(),
            1 => $allReviews->where('rating', 1)->count(),
        ];

        return response()->json([
            'reviews' => $reviews->items(),
            'pagination' => [
                'total' => $reviews->total(),
                'per_page' => $reviews->perPage(),
                'current_page' => $reviews->currentPage(),
                'last_page' => $reviews->lastPage(),
            ],
            'averageRating' => round($averageRating, 1),
            'totalReviews' => $allReviews->count(),
            'ratingDistribution' => $ratingDistribution,
        ]);
    }
}
