<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;
use Illuminate\Support\Facades\Http;

class OpenRouterController extends Controller
{
    private $apiUrl = 'https://openrouter.ai/api/v1/chat/completions';

    public function generateQuestion(Request $request)
    {
        try {
            $response = Http::withHeaders([
                'Authorization' => 'Bearer ' . env('OPENROUTER_API_KEY'),
                'HTTP-Referer' => 'https://ccattest.com',
                'X-Title' => 'CCAT',
                'Content-Type' => 'application/json',
            ])->post($this->apiUrl, [
                'model' => 'anthropic/claude-3.5-sonnet',
                'messages' => [
                    [
                        'role' => 'user',
                        'content' => $request->input('prompt')
                    ]
                ]
            ]);

            if (!$response->successful()) {
                return response()->json([
                    'error' => 'Failed to get response from OpenRouter API',
                    'details' => $response->json()
                ], $response->status());
            }

            $responseData = $response->json();

            // Extract the content from the response
            $content = $responseData['choices'][0]['message']['content'] ?? null;
            if (!$content) {
                return response()->json([
                    'error' => 'Invalid response format from OpenRouter API'
                ], 500);
            }

            // Try to extract and validate JSON from the content
            preg_match('/{.*}/s', $content, $matches);
            if (empty($matches)) {
                return response()->json([
                    'error' => 'Could not extract JSON from response'
                ], 500);
            }

            $questionData = json_decode($matches[0], true);
            if (!$questionData ||
                !isset($questionData['question']) ||
                !isset($questionData['options']) ||
                !isset($questionData['correctAnswer']) ||
                !isset($questionData['explanation']) ||
                !is_array($questionData['options'])) {
                return response()->json([
                    'error' => 'Invalid question data format'
                ], 500);
            }

            // Store the response data in session (optional, if you still need it)
            session([
                'current_question' => $questionData['question'],
                'current_options' => $questionData['options'],
                'current_answer' => $questionData['correctAnswer'],
                'current_explanation' => $questionData['explanation']
            ]);

            return response()->json([
                'choices' => [
                    [
                        'message' => [
                            'content' => json_encode($questionData)
                        ]
                    ]
                ]
            ]);

        } catch (\Exception $e) {
            return response()->json([
                'error' => 'Server error',
                'message' => $e->getMessage()
            ], 500);
        }
    }
}
