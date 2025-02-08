<?php

namespace App\Http\Controllers;

use App\Http\Controllers\Controller;
use Codedge\Fpdf\Fpdf\Fpdf;
use Illuminate\Support\Facades\Storage;
use ZipArchive;
use Illuminate\Support\Facades\Log;

class QuestionPDF extends Fpdf
{
    function Header()
    {
        $this->SetFont('Arial', 'B', 15);
        $this->Cell(0, 10, 'Question Paper', 0, 1, 'C');
        $this->Ln(10);
    }

    function Footer()
    {
        $this->SetY(-15);
        $this->SetFont('Arial', 'I', 8);
        $this->Cell(0, 10, 'Page ' . $this->PageNo(), 0, 0, 'C');
    }

    function Question($num, $question)
    {
        $this->SetFont('Arial', 'B', 12);
        $this->Cell(0, 10, "Question $num:", 0, 1);
        $this->SetFont('Arial', '', 12);
        $this->MultiCell(0, 10, $question['text']);

        if (isset($question['image'])) {
            // Remove '/storage' from the beginning of the image path if it exists
            $imagePath = preg_replace('/^\/storage/', '', $question['image']);
            $fullImagePath = public_path('storage' . $imagePath);

            Log::info("Attempting to load image: $fullImagePath");

            if (file_exists($fullImagePath)) {
                $this->Image($fullImagePath, 10, $this->GetY() + 5, 90);
                $this->Ln(100); // Adjust based on image size
            } else {
                Log::warning("Image not found: $fullImagePath");
                $this->MultiCell(0, 10, "Image not found: " . $question['image']);
            }
        }

        $this->SetFont('Arial', 'B', 12);
        $this->Cell(0, 10, 'Options:', 0, 1);
        $this->SetFont('Arial', '', 12);
        foreach ($question['options'] as $option) {
            $this->MultiCell(0, 10, "- $option");
        }

        $this->SetFont('Arial', 'B', 12);
        $this->Cell(0, 10, 'Correct Answer:', 0, 1);
        $this->SetFont('Arial', '', 12);
        $this->MultiCell(0, 10, $question['correctAnswer']);

        $this->SetFont('Arial', 'B', 12);
        $this->Cell(0, 10, 'Explanation:', 0, 1);
        $this->SetFont('Arial', '', 12);
        $this->MultiCell(0, 10, $question['explanation']);

        $this->AddPage();
    }
}
