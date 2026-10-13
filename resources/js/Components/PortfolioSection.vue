<script setup>
import { Link } from '@inertiajs/vue3';
import ProjectCard from '@/Components/ProjectCard.vue';

const featured = [
  {
    name: 'Selenix Platform',
    category: 'SaaS · Desktop · API',
    tagline: 'AI-powered browser-automation platform with 2,500+ subscribers.',
    description: 'A 3-tier flagship: Laravel SaaS backend, Electron desktop IDE, and OpenAI-compatible Claude proxy. Records, plays back, and AI-generates browser automations with 135+ commands.',
    techStack: ['Laravel', 'Electron', 'React', 'TypeScript', 'Vue 3', 'MCP', 'Claude'],
    features: [
      'Natural-language → automation commands',
      '3-tier architecture spanning web, desktop, and infra',
      'PayPal billing, AI-turn quotas, template marketplace'
    ],
    status: 'Production',
    icon: 'Workflow',
    accent: 'blue'
  },
  {
    name: 'ScorCorect Video Generator',
    category: 'AI Pipeline · Generative Video',
    tagline: 'Cinematic sports recap videos at ~$0 marginal cost.',
    description: 'Hybrid LTX-2.3 + PIL/MoviePy pipeline producing broadcast-quality 10-second match recaps. Dynamic goal-aware layouts and player cutout extraction via deep-learning segmentation.',
    techStack: ['Python', 'FastAPI', 'LTX-2.3', 'ComfyUI', 'MoviePy', 'rembg'],
    features: [
      '~$0 per video after one-time template generation',
      'Dynamic layouts adapt to 0/1/2/3+ goals',
      'Async job queue, multi-language client SDKs'
    ],
    status: 'In Development',
    icon: 'Clapperboard',
    accent: 'orange'
  },
  {
    name: 'Project ADAM',
    category: 'Agentic AI System',
    tagline: 'Community-driven AI that improves from contributions and votes.',
    description: 'Dual-stack (Python FastAPI + Laravel/Vue) experimental platform with a 9-table relational schema and ChromaDB vector retrieval over user-contributed knowledge.',
    techStack: ['Python', 'FastAPI', 'ChromaDB', 'Laravel', 'Filament', 'Vue 3'],
    features: [
      'Vector search over crowd-curated knowledge',
      'Polyglot architecture: Python backend + PHP frontend',
      'Voting/quality system with full audit trail'
    ],
    status: 'In Development',
    icon: 'BrainCircuit',
    accent: 'teal'
  }
];
</script>

<template>
  <section id="portfolio" class="py-20 bg-surface/30 border-y border-line">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      <div class="text-center mb-12">
        <span class="inline-block px-3 py-1 rounded-full border border-line bg-surface text-accent-400 text-xs font-semibold uppercase tracking-[0.14em] mb-4">
          Portfolio
        </span>
        <h2 class="text-3xl sm:text-4xl font-bold tracking-tight text-content mb-4">
          Real projects, shipped by the same team that will build yours
        </h2>
        <p class="max-w-3xl mx-auto text-lg text-content-muted">
          Featured work spanning SaaS platforms, generative AI pipelines, and agentic systems. Every category we offer — e-commerce, mobile, desktop, APIs, automations, and agentic AI — is backed by production code we've already shipped.
        </p>
      </div>

      <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
        <ProjectCard
          v-for="(project, idx) in featured"
          :key="project.name"
          v-bind="project"
          :animation-delay="`${idx * 0.1}s`"
        />
      </div>

      <div class="mt-12 text-center">
        <Link
          :href="route('portfolio')"
          class="inline-flex items-center px-8 py-4 text-base font-semibold rounded-control text-content border border-line hover:border-accent-400 hover:text-white transition-colors duration-200 focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-accent-400 focus-visible:ring-offset-2 focus-visible:ring-offset-ink"
        >
          See all projects
          <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 ml-2" viewBox="0 0 20 20" fill="currentColor">
            <path fill-rule="evenodd" d="M10.293 5.293a1 1 0 011.414 0l4 4a1 1 0 010 1.414l-4 4a1 1 0 01-1.414-1.414L12.586 11H3a1 1 0 110-2h11.586l-2.293-2.293a1 1 0 010-1.414z" clip-rule="evenodd" />
          </svg>
        </Link>
      </div>
    </div>
  </section>
</template>
