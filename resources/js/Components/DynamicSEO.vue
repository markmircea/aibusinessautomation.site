<script setup>
import { computed } from 'vue';
import { Head, usePage } from '@inertiajs/vue3';
import seo from '@/data/seo.json';

const page = usePage();
const baseUrl = computed(() => (typeof window !== 'undefined' ? window.location.origin : ''));

// Single source of truth for titles, descriptions and share images: resources/js/data/seo.json. The server renders
// the same tags into app.blade.php (AppServiceProvider::seoFor), because link previews (WhatsApp, Slack, LinkedIn,
// Facebook, X) never run JavaScript; each head-key below matches the inertia="..." key there, so in the browser
// Inertia replaces those tags instead of duplicating them. Pages must NOT set their own <Head><title>, or two Head
// components race and the winner varies.

// The service pages all render the same component (WebDevelopment/Service),
// so resolve them by their slug prop instead of the component name.
const metaKey = computed(() => {
  if (page.component === 'WebDevelopment/Service') {
    const slug = page.props.slug ?? '';
    // kebab-case slug -> PascalCase key: 'digital-marketing' -> 'DigitalMarketing'
    return 'WebDevelopment/' + slug.split('-').map((w) => w.charAt(0).toUpperCase() + w.slice(1)).join('');
  }
  return page.component;
});

// Pages with server-built SEO (portfolio case studies) pass a `seo` prop; everything else uses seo.json.
const current = computed(() => (page.props.seo?.title ? page.props.seo : (seo.pages[metaKey.value] ?? seo.fallback)));
const image = computed(() => current.value.image ?? seo.image);
const imageUrl = computed(() => baseUrl.value + image.value.src);
const canonicalUrl = computed(() => page.props.url);
</script>

<template>
  <Head>
    <title>{{ current.title }}</title>
    <meta head-key="description" name="description" :content="current.description">
    <link head-key="canonical" rel="canonical" :href="canonicalUrl">

    <!-- Open Graph (Facebook, LinkedIn, WhatsApp, Slack) -->
    <meta head-key="og:type" property="og:type" content="website">
    <meta head-key="og:site_name" property="og:site_name" :content="seo.site">
    <meta head-key="og:url" property="og:url" :content="canonicalUrl">
    <meta head-key="og:title" property="og:title" :content="current.title">
    <meta head-key="og:description" property="og:description" :content="current.description">
    <meta head-key="og:image" property="og:image" :content="imageUrl">
    <meta v-if="image.width" head-key="og:image:width" property="og:image:width" :content="image.width">
    <meta v-if="image.width" head-key="og:image:height" property="og:image:height" :content="image.height">
    <meta head-key="og:image:alt" property="og:image:alt" :content="image.alt">

    <!-- X (Twitter) -->
    <meta head-key="twitter:card" name="twitter:card" content="summary_large_image">
    <meta head-key="twitter:title" name="twitter:title" :content="current.title">
    <meta head-key="twitter:description" name="twitter:description" :content="current.description">
    <meta head-key="twitter:image" name="twitter:image" :content="imageUrl">
    <meta head-key="twitter:image:alt" name="twitter:image:alt" :content="image.alt">
  </Head>
</template>
