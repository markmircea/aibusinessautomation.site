<script setup>
import BusinessSolutionCard from '@/Components/BusinessSolutionCard.vue';

const solutions = [
  {
    title: 'Document Processing & Data Entry',
    focus: 'Automated document handling, data extraction, form processing',
    keyPoint: '80% reduction in processing time',
    icon: '📄',
    routeName: 'solutions.document-processing',
    delay: '0s'
  },
  {
    title: 'Customer Service',
    focus: '24/7 support automation, multi-channel communication',
    keyPoint: '70% query resolution without human intervention',
    icon: '💬',
    routeName: 'solutions.customer-service',
    delay: '0.1s'
  },
  {
    title: 'Financial Operations',
    focus: 'AP/AR automation, expense management, reporting',
    keyPoint: '90% reduction in processing time',
    icon: '💰',
    routeName: 'solutions.financial-operations',
    delay: '0.2s'
  },
  {
    title: 'HR & Recruitment',
    focus: 'Hiring automation, onboarding, HR operations',
    keyPoint: '75% reduction in hiring time',
    icon: '👥',
    routeName: 'solutions.hr-recruitment',
    delay: '0.3s'
  },
  {
    title: 'Sales & Marketing',
    focus: 'Lead management, campaign automation, analytics',
    keyPoint: '50% increase in conversion rates',
    icon: '📈',
    routeName: 'solutions.sales-marketing',
    delay: '0.4s'
  },
  {
    title: 'Supply Chain & Inventory',
    focus: 'Inventory optimization, supplier management, logistics',
    keyPoint: '30% cost reduction',
    icon: '🏭',
    routeName: 'solutions.supply-chain',
    delay: '0.5s'
  }
];
</script>

<template>
  <section id="solutions" class="py-20 bg-gray-50 dark:bg-gray-900">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      <div class="text-center mb-16">
        <h2 class="text-3xl sm:text-4xl font-bold text-gray-900 dark:text-white mb-4">
          AI-Powered Business Solutions
        </h2>
        <p class="max-w-2xl mx-auto text-lg text-gray-600 dark:text-gray-300">
          Discover how our AI automation solutions can transform your business operations and drive growth.
        </p>
      </div>

      <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
        <BusinessSolutionCard
          v-for="solution in solutions"
          :key="solution.title"
          v-bind="solution"
          :animation-delay="solution.delay"
        />
      </div>

      <!-- Call to Action -->
      <div class="mt-16 text-center">
        <a 
          href="#contact"
          class="inline-flex items-center px-8 py-4 border border-transparent text-lg font-medium rounded-md text-white bg-blue-600 hover:bg-blue-700 transition-colors duration-200"
        >
          Get Started with AI Automation
          <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 ml-2" viewBox="0 0 20 20" fill="currentColor">
            <path fill-rule="evenodd" d="M10.293 5.293a1 1 0 011.414 0l4 4a1 1 0 010 1.414l-4 4a1 1 0 01-1.414-1.414L12.586 11H3a1 1 0 110-2h11.586l-2.293-2.293a1 1 0 010-1.414z" clip-rule="evenodd" />
          </svg>
        </a>
      </div>
    </div>
  </section>
</template>
