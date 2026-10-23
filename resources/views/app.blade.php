<!DOCTYPE html>
<html lang="{{ str_replace('_', '-', app()->getLocale()) }}" class="dark">

<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <meta name="csrf-token" content="{{ csrf_token() }}">

    {{-- Rendered here because link previews (WhatsApp, Slack, LinkedIn, Facebook, X) don't run JavaScript. $seo comes
         from AppServiceProvider::seoFor; in the browser DynamicSEO.vue takes these tags over by their inertia keys. --}}
    <title inertia>{{ $seo['title'] }}</title>
    <meta inertia="description" name="description" content="{{ $seo['description'] }}">
    <link inertia="canonical" rel="canonical" href="{{ $seo['url'] }}">
    <meta inertia="og:type" property="og:type" content="website">
    <meta inertia="og:site_name" property="og:site_name" content="{{ $seo['site'] }}">
    <meta inertia="og:url" property="og:url" content="{{ $seo['url'] }}">
    <meta inertia="og:title" property="og:title" content="{{ $seo['title'] }}">
    <meta inertia="og:description" property="og:description" content="{{ $seo['description'] }}">
    <meta inertia="og:image" property="og:image" content="{{ $seo['image'] }}">
    @if ($seo['imageWidth'])
    <meta inertia="og:image:width" property="og:image:width" content="{{ $seo['imageWidth'] }}">
    <meta inertia="og:image:height" property="og:image:height" content="{{ $seo['imageHeight'] }}">
    @endif
    <meta inertia="og:image:alt" property="og:image:alt" content="{{ $seo['imageAlt'] }}">
    <meta inertia="twitter:card" name="twitter:card" content="summary_large_image">
    <meta inertia="twitter:title" name="twitter:title" content="{{ $seo['title'] }}">
    <meta inertia="twitter:description" name="twitter:description" content="{{ $seo['description'] }}">
    <meta inertia="twitter:image" name="twitter:image" content="{{ $seo['image'] }}">
    <meta inertia="twitter:image:alt" name="twitter:image:alt" content="{{ $seo['imageAlt'] }}">
    <link rel="icon" type="image/svg+xml" href="{{ asset('favicon.svg') }}">

    <!-- Fonts -->
    <link rel="preconnect" href="https://fonts.bunny.net">
    <link href="https://fonts.bunny.net/css?family=figtree:400,500,600,700,800&display=swap" rel="stylesheet" />

    {{-- Paint the dark surface before CSS/JS arrives so there is no white flash. --}}
    <style>html{background-color:#0B1020}</style>

    <!-- Scripts -->
    @routes
    @vite(['resources/js/app.js', "resources/js/Pages/{$page['component']}.vue"])
    @inertiaHead

</head>

<body class="font-sans antialiased">
    @inertia
</body>

</html>
