<script setup>
import { computed } from 'vue';
import { Head, usePage } from '@inertiajs/vue3';

const page = usePage();
// page.component is the Inertia component name ('Solutions/CustomerService').
const currentRoute = computed(() => page.component);
const currentUrl = computed(() => page.props.url);
const baseUrl = computed(() => (typeof window !== 'undefined' ? window.location.origin : ''));

// Single source of truth for page titles and descriptions. Pages must NOT set
// their own <Head><title>, or two Head components race and the winner varies.
const meta = {
  'Welcome': {
    title: 'Software Development Agency | Web, Mobile, APIs & AI | AIBrainL.ink',
    description: 'We design and ship e-commerce web apps, mobile and desktop apps, APIs, automation pipelines and agentic AI systems — end to end, with a dedicated project manager on every engagement.',
  },
  'Portfolio': {
    title: 'Case Studies — Portfolio | AIBrainL.ink',
    description: 'Case studies from our team: web platforms, desktop and mobile apps, games, APIs and agentic AI — with real screenshots and the stack behind each one.',
  },
  'WebDevelopment/Index': {
    title: 'Web Development Services | AIBrainL.ink',
    description: 'E-commerce platforms, marketing sites, mobile apps and scraping/automation pipelines — designed, built and maintained end to end.',
  },
  'WebDevelopment/Ecommerce': {
    title: 'E-commerce Platform Development | AIBrainL.ink',
    description: 'Custom e-commerce builds on Shopify, WooCommerce, Magento, BigCommerce or Laravel — secure payments, inventory, and integrations with the systems you already run.',
  },
  'WebDevelopment/Presentation': {
    title: 'Presentation & Marketing Site Development | AIBrainL.ink',
    description: 'Fast, accessible marketing sites built to convert — custom design, CMS integration, and performance budgets that hold up after launch.',
  },
  'WebDevelopment/Mobile': {
    title: 'Mobile Application Development | AIBrainL.ink',
    description: 'Native and cross-platform mobile apps, from product definition through store release and ongoing support.',
  },
  'WebDevelopment/DigitalMarketing': {
    title: 'Digital Marketing Services | AIBrainL.ink',
    description: 'SEO, paid search and social, email automation, analytics and conversion optimization — run by the team that builds the site.',
  },
  'WebDevelopment/Automation': {
    title: 'Web Scraping & Automation Development | AIBrainL.ink',
    description: 'Resilient scraping and browser-automation pipelines with scheduling, monitoring and structured output your systems can consume.',
  },
  'Solutions/AIIntegrations': {
    title: 'Enterprise AI Integration Hub | AIBrainL.ink',
    description: 'Connect AI to the tools you already run. Cloud services, data platforms, business software, developer tooling and security — integrated into your existing workflows.',
  },
  'Solutions/CustomerService': {
    title: 'AI-Powered Customer Service Automation | AIBrainL.ink',
    description: '24/7 intelligent support, automated ticket routing, sentiment analysis and personalised customer interactions built on your knowledge base.',
  },
  'Solutions/DocumentProcessing': {
    title: 'AI Document Processing & Automation | AIBrainL.ink',
    description: 'Intelligent data extraction, classification and routing, integrated with the document systems you already use.',
  },
  'Solutions/FinancialOperations': {
    title: 'Financial Operations Automation | AIBrainL.ink',
    description: 'AP/AR automation, expense management, reconciliation and reporting with ML-powered anomaly detection.',
  },
  'Solutions/HrRecruitment': {
    title: 'HR & Recruitment Automation | AIBrainL.ink',
    description: 'Resume analysis, skill assessment, interview automation and onboarding workflow management, wired into your ATS.',
  },
  'Solutions/SalesMarketing': {
    title: 'Sales & Marketing Automation | AIBrainL.ink',
    description: 'Predictive lead scoring, personalised content generation and multi-channel campaign orchestration with real-time analytics.',
  },
  'Solutions/SupplyChain': {
    title: 'Supply Chain & Inventory Automation | AIBrainL.ink',
    description: 'Predictive inventory management, supplier relationship management, demand forecasting and logistics optimisation.',
  },
  'Solutions/DesktopAutomation': {
    title: 'AI Desktop Automation | AIBrainL.ink',
    description: 'Automate desktop workflows across the applications your team already runs, with scheduling and monitoring built in.',
  },
  'PrivacyPolicy': {
    title: 'Privacy Policy | AIBrainL.ink',
    description: 'How AIBrainL.ink (MarkIT S.R.L.) collects, uses and protects personal information.',
  },
  'TermsOfService': {
    title: 'Terms of Service | AIBrainL.ink',
    description: 'The terms governing use of AIBrainL.ink services.',
  },
  'Error': {
    title: 'Page not found | AIBrainL.ink',
    description: 'The page you were looking for does not exist.',
  },
};

const fallback = {
  title: 'Software Development Agency | AIBrainL.ink',
  description: 'Custom software built end to end — web, mobile, desktop, APIs, automation pipelines and agentic AI systems.',
};

// The service pages all render the same component (WebDevelopment/Service),
// so resolve them by their slug prop instead of the component name.
const metaKey = computed(() => {
  if (currentRoute.value === 'WebDevelopment/Service') {
    const slug = page.props.slug ?? '';
    // kebab-case slug -> PascalCase key: 'digital-marketing' -> 'DigitalMarketing'
    return 'WebDevelopment/' + slug.split('-').map((w) => w.charAt(0).toUpperCase() + w.slice(1)).join('');
  }
  return currentRoute.value;
});

// Pages with server-built SEO (portfolio case studies) pass a `seo` prop; everything else uses the map above.
const current = computed(() => (page.props.seo?.title ? page.props.seo : (meta[metaKey.value] ?? fallback)));
const title = computed(() => current.value.title);
const description = computed(() => current.value.description);
const canonicalUrl = computed(() => currentUrl.value);
// File on disk is main.png (lowercase). It was referenced as main.png while the
// file was main.PNG, which 404s on case-sensitive production filesystems.
const ogImage = computed(() => page.props.seo?.image ?? `${baseUrl.value}/img/main.png`);
</script>

<template>
  <Head>
    <title>{{ title }}</title>
    <meta name="description" :content="description">
    <link rel="canonical" :href="canonicalUrl">

    <!-- Open Graph / Facebook -->
    <meta property="og:type" content="website">
    <meta property="og:site_name" content="AIBrainL.ink">
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
