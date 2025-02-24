<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <title>New Contact Form Submission</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            line-height: 1.6;
            color: #333;
            max-width: 600px;
            margin: 0 auto;
            padding: 20px;
        }
        .header {
            background-color: #007bff;
            color: white;
            padding: 20px;
            text-align: center;
            border-radius: 5px;
            margin-bottom: 20px;
        }
        .content {
            background-color: #f8f9fa;
            padding: 20px;
            border-radius: 5px;
        }
        .field {
            margin-bottom: 15px;
        }
        .label {
            font-weight: bold;
            color: #495057;
        }
        .value {
            margin-top: 5px;
        }
    </style>
</head>
<body>
    <div class="header">
        <h1>New Contact Form Submission</h1>
    </div>

    <div class="content">
        <div class="field">
            <div class="label">Name:</div>
            <div class="value">{{ $contact->name }}</div>
        </div>

        <div class="field">
            <div class="label">Email:</div>
            <div class="value">{{ $contact->email }}</div>
        </div>

        <div class="field">
            <div class="label">Company:</div>
            <div class="value">{{ $contact->company }}</div>
        </div>

        <div class="field">
            <div class="label">Solution:</div>
            <div class="value">{{ $contact->solution }}</div>
        </div>

        @if($contact->tech_stack)
        <div class="field">
            <div class="label">Tech Stack:</div>
            <div class="value">{{ $contact->tech_stack }}</div>
        </div>
        @endif

        <div class="field">
            <div class="label">Message:</div>
            <div class="value">{{ $contact->message }}</div>
        </div>
    </div>
</body>
</html>
