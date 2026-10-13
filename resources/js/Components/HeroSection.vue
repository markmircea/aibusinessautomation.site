<script setup>
import PageHero from '@/Components/PageHero.vue';

const capabilities = [
  'E-commerce & Web Apps',
  'Mobile & Desktop Apps',
  'APIs & Backends',
  'Automation Pipelines',
  'Agentic AI Systems',
];

const stats = [
  { value: '10+', label: 'Years shipping production software' },
  { value: '2,500+', label: 'Subscribers on our flagship product' },
  { value: '15+', label: 'Languages & frameworks in house' },
  { value: '6', label: 'Active flagship projects' },
];
</script>

<template>
  <PageHero
    eyebrow="Available for new projects"
    :eyebrow-dot="true"
    title="A software development agency"
    highlight="that ships"
    description="Web, mobile, desktop, APIs and agentic AI — built end-to-end by a team that has already shipped production platforms to thousands of users."
    :pills="capabilities"
    :primary-cta="{ label: 'Get a Quote', href: '#contact' }"
    :secondary-cta="{ label: 'See our work', href: '#portfolio' }"
    :stats="stats"
  />
</template>
