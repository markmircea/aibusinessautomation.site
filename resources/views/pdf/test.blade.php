<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Full Practice Test {{ $testNumber ?? 'Unknown' }}</title>
    <style>
        body { font-family: Arial, sans-serif; }
        .question { page-break-after: always; margin-bottom: 20px; }
        .options { margin-left: 20px; }
        .correct-answer { font-weight: bold; color: green; }
        .explanation { font-style: italic; margin-top: 10px; }
        img { max-width: 100%; height: auto; }
        .error { color: red; font-weight: bold; }
    </style>
</head>
<body>
    <h1>Full Practice Test {{ $testNumber ?? 'Unknown' }}</h1>
    @if(isset($questions) && is_array($questions) && !empty($questions))
        @foreach($questions as $index => $question)
            <div class="question">
                <h2>Question {{ $index + 1 }}</h2>
                <p>{{ $question['text'] ?? 'Question text not available' }}</p>
                @if(isset($question['image']))
                    <img src="{{ public_path($question['image']) }}" alt="Question Image">
                @endif
                <div class="options">
                    @foreach($question['options'] ?? [] as $option)
                        <p>{{ $option }}</p>
                    @endforeach
                </div>
                <p class="correct-answer">Correct Answer: {{ $question['correctAnswer'] ?? 'Not available' }}</p>
                <p class="explanation">Explanation: {{ $question['explanation'] ?? 'Not available' }}</p>
            </div>
        @endforeach
    @else
        <p class="error">Error: No questions available for this test. Please contact support.</p>
    @endif
</body>
</html>
