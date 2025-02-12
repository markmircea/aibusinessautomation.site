<script setup>
import { computed } from 'vue';
import { Head, usePage } from '@inertiajs/vue3';

const page = usePage();
const currentRoute = computed(() => page.props.component);
const currentUrl = computed(() => page.props.url);
const baseUrl = computed(() => window.location.origin);


const title = computed(() => {
  switch (currentRoute.value) {
    case 'Solutions/AIIntegrations':
      return 'Enterprise AI Integration Hub | AI Business Automation | aibrainl.ink';
    case 'Solutions/CustomerService':
      return 'AI-Powered Customer Service Solutions | aibrainl.ink';
    case 'Solutions/DataAnalytics':
      return 'Intelligent Data Analytics & Business Intelligence | aibrainl.ink';
    case 'Solutions/DocumentProcessing':
      return 'AI Document Processing & Automation | aibrainl.ink';
    case 'Solutions/SecurityCompliance':
      return 'AI Security & Compliance Automation | aibrainl.ink';
    case 'Solutions/DevelopmentDevOps':
      return 'AI-Enhanced Development & DevOps Solutions | aibrainl.ink';
    case 'contact':
      return 'Contact Us | AI Business Automation | aibrainl.ink';
    default:
      return 'AI Business Process Automation Solutions | aibrainl.ink';
  }
});

const description = computed(() => {
  switch (currentRoute.value) {
    case 'Solutions/AIIntegrations':
      return 'Transform your business processes with our extensive suite of AI integrations. We provide enterprise-grade solutions that seamlessly connect with your existing workflows, enabling intelligent automation and enhanced decision-making capabilities across cloud services, data analytics, business tools, development, and security.';
    case 'Solutions/CustomerService':
      return 'Revolutionize your customer service with AI-powered automation. 24/7 intelligent support, automated ticket routing, sentiment analysis, and personalized customer interactions for enhanced satisfaction and efficiency.';
    case 'Solutions/DataAnalytics':
      return 'Harness the power of AI for advanced data analytics and business intelligence. Real-time insights, predictive analytics, automated reporting, and intelligent data visualization for informed decision-making.';
    case 'Solutions/DocumentProcessing':
      return 'Streamline document processing with AI automation. Intelligent data extraction, classification, routing, and integration with your existing systems for efficient document management.';
    case 'Solutions/SecurityCompliance':
      return 'Enhance security and ensure compliance with AI-powered automation. Intelligent threat detection, automated compliance monitoring, and security controls for enterprise-grade protection.';
    case 'Solutions/DevelopmentDevOps':
      return 'Accelerate development and DevOps with AI-enhanced tools. Automated code analysis, intelligent testing, and streamlined deployment processes for improved efficiency.';
    case 'contact':
      return 'Connect with our AI automation experts. Let\'s discuss how we can transform your business processes with custom AI solutions tailored to your unique needs.';
    default:
      return 'Transform any business process with our enterprise AI automation solutions. Custom-built integrations, intelligent workflows, and enhanced decision-making capabilities for your unique business needs.';
  }
});

const canonicalUrl = computed(() => currentUrl.value);
const ogImage = computed(() => `${baseUrl.value}/img/main.png`);

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
