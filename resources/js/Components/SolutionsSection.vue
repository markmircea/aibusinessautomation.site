<script setup>
import BusinessSolutionCard from '@/Components/BusinessSolutionCard.vue';

const solutions = [
  {
    title: 'Document Processing & Data Entry',
    focus: 'Automated document handling, data extraction, form processing',
    keyPoint: '80% reduction in processing time',
    icon: 'FileText',
    routeName: 'solutions.document-processing',
    animationDelay: '0s',
    useCase: 'Generate SEO-friendly content with images with DeepSeek R1 (or V3), publish it on WordPress, and update a Google Sheets document with the details of the created post.',
    integrations: ['Azure Document', 'SharePoint AI', 'Box Intelligence'],
    platforms: ['OCR Systems', 'ERP Software', 'Document Management']
  },
  {
    title: 'Customer Service',
    focus: '24/7 support automation, multi-channel communication',
    keyPoint: '70% query resolution without human intervention',
    icon: 'MessagesSquare',
    routeName: 'solutions.customer-service',
    animationDelay: '0.1s',
    useCase: 'Advanced customer support automation using OpenAI/Claude for natural language understanding, multi-channel support via Zendesk AI, and intelligent routing with automated response generation and contextual knowledge base integration.',
    integrations: ['Microsoft Teams', 'Zendesk AI', 'Omnichannel Support'],
    platforms: ['CRM Systems', 'Chat Platforms', 'Knowledge Bases']
  },
  {
    title: 'Financial Operations',
    focus: 'AP/AR automation, expense management, reporting',
    keyPoint: '90% reduction in processing time',
    icon: 'Wallet',
    routeName: 'solutions.financial-operations',
    animationDelay: '0.2s',
    useCase: 'Physical invoice/receipt processing system using OCR (Optical Character Recognition) and SharePoint integration for automated extraction, classification, and documentation with direct integration to multiple enterprise systems. Comprehensive financial process automation for real-time expense analytics, automated fraud detection, intelligent cash flow forecasting, and automated reconciliation with machine learning-powered anomaly detection.',
    integrations: ['AWS Bedrock', 'Snowflake', 'Azure Sentinel'],
    platforms: ['Accounting Software', 'Banking APIs', 'Payment Gateways']
  },
  {
    title: 'HR & Recruitment',
    focus: 'Hiring automation, onboarding, HR operations',
    keyPoint: '75% reduction in hiring time',
    icon: 'Users',
    routeName: 'solutions.hr-recruitment',
    animationDelay: '0.3s',
    useCase: 'End-to-end recruitment automation using AI for resume analysis, skill assessment, automated video interview analysis, AI text/voice interviews, qualification classification and reviews. Intelligent onboarding workflow management from A-Z',
    integrations: ['Azure OpenAI', 'Azure Cognitive Services', 'Microsoft Teams', 'Document AI'],
    platforms: ['ATS Systems', 'Calendar Apps', 'HR Management Software']
  },
  {
    title: 'Sales & Marketing',
    focus: 'Lead management, campaign automation, analytics',
    keyPoint: '50% increase in conversion rates',
    icon: 'TrendingUp',
    routeName: 'solutions.sales-marketing',
    animationDelay: '0.4s',
    useCase: 'Intelligent sales automation using Salesforce AI and HubSpot for predictive lead scoring, personalized content generation, automated multi-channel campaign orchestration, and real-time analytics with ML-powered conversion optimization.',
    integrations: ['Salesforce', 'HubSpot', 'Azure Analytics', 'Social Media Integration'],
    platforms: ['Marketing Platforms', 'CRM Systems', 'Analytics Tools']
  },
  {
    title: 'Supply Chain & Inventory',
    focus: 'Inventory optimization, supplier management, logistics',
    keyPoint: '30% cost reduction',
    icon: 'Factory',
    routeName: 'solutions.supply-chain',
    animationDelay: '0.5s',
    useCase: 'Advanced supply chain optimization using AWS and Azure ML services for predictive inventory management, intelligent supplier relationship management, automated demand forecasting, and real-time logistics optimization with Grafana analytics.',
    integrations: ['AWS SageMaker', 'Azure ML', 'Grafana'],
    platforms: ['ERP Systems', 'Logistics Software', 'Supplier Portals']
  }
];
</script>

<template>
  
  <section id="solutions" class="py-20 bg-ink">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      <div class="text-center mb-16">
        <h2 class="text-3xl sm:text-4xl font-bold tracking-tight text-content mb-4">
          Custom AI Solutions for Every Department
        </h2>
        <p class="max-w-3xl mx-auto text-lg text-content-muted">
          Transform your business operations with tailored AI automation solutions. Each department gets a dedicated project manager and development team to build custom solutions that fit your unique needs.
        </p>
      </div>

      <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
        <BusinessSolutionCard
          v-for="solution in solutions"
          :key="solution.title"
          v-bind="solution"
        />
      </div>

      <!-- Call to Action -->
      <div class="mt-16 text-center">
        <a 
          href="#contact"
          class="inline-flex items-center px-8 py-4 text-base font-semibold rounded-control text-white bg-accent-500 hover:bg-accent-600 shadow-e2 transition-colors duration-200 focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-accent-400 focus-visible:ring-offset-2 focus-visible:ring-offset-ink"
        >
          Get a Quote
          <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 ml-2" viewBox="0 0 20 20" fill="currentColor">
            <path fill-rule="evenodd" d="M10.293 5.293a1 1 0 011.414 0l4 4a1 1 0 010 1.414l-4 4a1 1 0 01-1.414-1.414L12.586 11H3a1 1 0 110-2h11.586l-2.293-2.293a1 1 0 010-1.414z" clip-rule="evenodd" />
          </svg>
        </a>
      </div>
    </div>
  </section>
</template>
