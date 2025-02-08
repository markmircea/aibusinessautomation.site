<script setup>
import { computed } from 'vue';
import { Head, usePage } from '@inertiajs/vue3';

const page = usePage();
const currentRoute = computed(() => page.props.component);
const currentUrl = computed(() => page.props.url);
const baseUrl = computed(() => window.location.origin);


const title = computed(() => {
  switch (currentRoute.value) {
    case 'dashboard':
      return 'CCAT Cognitive Aptitude Assessments | CCATtest.com';
    case 'free.practice.test':
      return 'Free CCAT Practice Test | CCATtest.com';
    case 'verbal.test':
    case 'verbal.test.start':
      return 'CCAT Verbal Test Practice | CCATtest.com';
    case 'math.logic.test':
    case 'math.test.start':
      return 'CCAT Math and Logic Test Practice | CCATtest.com';
    case 'spatial.reasoning.test':
      return 'CCAT Spatial Reasoning Test Practice | CCATtest.com';
    case 'full.practice.test':
    case 'full-practice-test-start':
      return 'Full CCAT Practice Test | CCATtest.com';
    case 'upgrade.account':
      return 'Upgrade Your Account | CCATtest.com';
    default:
      return 'CCATtest.com | CCAT Crossover Aptitude Test Preparation';
  }
});

const description = computed(() => {
  switch (currentRoute.value) {
    case 'dashboard':
      return 'Prepare for your CCAT with CCATtest.com\'s comprehensive practice tests. Improve your verbal, math, logic, and spatial reasoning skills for Crossover, Vista Equity, Lambda School, and more.';
    case 'free.practice.test':
      return 'Take our FREE CCAT practice test. Experience verbal, math and logic, and spatial reasoning questions similar to the real CCAT.';
    case 'verbal.test':
    case 'verbal.test.start':
      return 'Practice CCAT verbal test questions with CCATtest.com. Improve your word meanings, relationships, and context skills for the Criteria Cognitive Aptitude Test.';
    case 'math.logic.test':
    case 'math.test.start':
      return 'Enhance your CCAT math and logic skills with CCATtest.com\'s practice tests. Prepare for algebra, word problems, and data interpretation questions.';
    case 'spatial.reasoning.test':
      return 'Boost your CCAT spatial reasoning abilities with CCATtest.com. Practice object rotation, pattern recognition, and spatial visualization for the test.';
    case 'full.practice.test':
    case 'full-practice-test-start':
      return 'Experience a full CCAT practice test with CCATtest.com. Get comprehensive practice across verbal, math, logic, and spatial reasoning sections.';
    case 'upgrade.account':
      return 'Upgrade your CCATtest.com account for full access to all CCAT practice tests and materials. Boost your preparation and increase your chances of success.';
    default:
      return 'CCATtest.com offers comprehensive CCAT test preparation materials. Improve your cognitive aptitude and ace your Criteria Cognitive Aptitude Test.';
  }
});

const canonicalUrl = computed(() => currentUrl.value);
const ogImage = computed(() => `${baseUrl.value}/storage/img/openg.jpeg`);

//console.log('DynamicSEO Component - Computed Title:', title.value);
//console.log('DynamicSEO Component - Computed Description:', description.value);
//console.log('DynamicSEO Component - Computed Canonical URL:', canonicalUrl.value);
//console.log('DynamicSEO Component - Computed OG Image:', ogImage.value);
</script>

<template>
  <Head>
    <title>{{ title }}</title>
    <meta name="description" :content="description">
    <link rel="canonical" :href="canonicalUrl">

    <!-- Open Graph / Facebook -->
    <meta property="og:type" content="website">
    <meta property="og:url" :content="canonicalUrl">
    <meta property="og:title" :content="title">
    <meta property="og:description" :content="description">
    <meta property="og:image" :content="ogImage">

    <!-- Twitter -->
    <meta property="twitter:card" content="summary_large_image">
    <meta property="twitter:url" :content="canonicalUrl">
    <meta property="twitter:title" :content="title">
    <meta property="twitter:description" :content="description">
    <meta property="twitter:image" :content="ogImage">
  </Head>
</template>
