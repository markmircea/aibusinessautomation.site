<?php

namespace App\Http\Controllers;

use App\Http\Controllers\Controller;
use Codedge\Fpdf\Fpdf\Fpdf;
use Illuminate\Support\Facades\Storage;
use ZipArchive;
use Illuminate\Support\Facades\Log;

class QuestionPDFController extends Controller
{
    private function loadQuestions($files)
    {
        $allQuestions = [
            'test2' => [],
            'others' => []
        ];

        foreach ($files as $index => $file) {
            Log::info("Attempting to load file: $file");

            if (!Storage::exists($file)) {
                Log::error("File not found: $file");
                continue;
            }

            $content = Storage::get($file);
            $questions = json_decode($content, true);

            if (json_last_error() !== JSON_ERROR_NONE) {
                Log::error("JSON decode error for file $file: " . json_last_error_msg());
                continue;
            }

            if (!is_array($questions)) {
                Log::error("Decoded content is not an array for file $file");
                continue;
            }

            Log::info("Successfully loaded " . count($questions) . " questions from $file");

            if ($index === 0) {
                $allQuestions['test2'] = $questions;
            } else {
                $allQuestions['others'] = array_merge($allQuestions['others'], $questions);
            }
        }

        Log::info("Total questions loaded: test2 - " . count($allQuestions['test2']) . ", others - " . count($allQuestions['others']));

        return $allQuestions;
    }

    private function selectQuestions($allQuestions)
    {
        $test2Count = min(18, count($allQuestions['test2']));
        $othersCount = min(32, count($allQuestions['others']));

        Log::info("Selecting questions: test2 - $test2Count, others - $othersCount");

        $test2Questions = array_slice($allQuestions['test2'], 0, $test2Count);
        $otherQuestions = array_slice($allQuestions['others'], 0, $othersCount);

        $selectedQuestions = array_merge($test2Questions, $otherQuestions);
        shuffle($selectedQuestions);

        Log::info("Total questions selected: " . count($selectedQuestions));

        return $selectedQuestions;
    }

    public function generatePDFs()
    {
        Log::info("Starting PDF generation process");

        $files = ['test2.json', 'test3.json', 'test4.json', 'test5.json'];
        $allQuestions = $this->loadQuestions($files);

        if (empty($allQuestions['test2']) && empty($allQuestions['others'])) {
            Log::error("No questions could be loaded from the JSON files.");
            return response()->json(['error' => 'No questions could be loaded from the JSON files.'], 500);
        }

        $zipFileName = 'question_papers.zip';
        $zip = new ZipArchive();
        $zip->open(storage_path('app/public/' . $zipFileName), ZipArchive::CREATE | ZipArchive::OVERWRITE);

        $pdfCount = 0;

        for ($i = 1; $i <= 10; $i++) {
            $selectedQuestions = $this->selectQuestions($allQuestions);
            if (empty($selectedQuestions)) {
                Log::warning("No questions selected for PDF $i");
                continue;
            }

            $pdf = new QuestionPDF();

            foreach ($selectedQuestions as $index => $question) {
                $pdf->AddPage();
                $pdf->Question($index + 1, $question);
            }

            $pdfContent = $pdf->Output('S');
            $pdfFileName = "question_paper_$i.pdf";
            Storage::put("public/pdfs/$pdfFileName", $pdfContent);

            $zip->addFromString($pdfFileName, $pdfContent);
            $pdfCount++;

            Log::info("Generated PDF $i with " . count($selectedQuestions) . " questions");
        }

        $zip->close();

        if ($pdfCount == 0) {
            Log::error("No PDFs could be generated due to insufficient questions.");
            return response()->json(['error' => 'No PDFs could be generated due to insufficient questions.'], 500);
        }

        Log::info("Successfully generated $pdfCount PDFs");

        return response()->download(storage_path('app/public/' . $zipFileName))->deleteFileAfterSend(true);
    }
}
