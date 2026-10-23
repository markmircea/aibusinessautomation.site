<script setup>
import { Link } from '@inertiajs/vue3';
import ProjectCard from '@/Components/ProjectCard.vue';
import { projects } from '@/data/portfolioMeta';

const featured = projects.filter((p) => p.featured).slice(0, 3);
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
          :key="project.slug"
          :project="project"
          :animation-delay="`${idx * 0.1}s`"
        />
      </div>

      <div class="mt-12 text-center">
        <Link
          :href="route('portfolio')"
          class="inline-flex items-center px-8 py-4 text-base font-semibold rounded-control text-content border border-line hover:border-accent-400 hover:text-white transition-colors duration-200 focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-accent-400 focus-visible:ring-offset-2 focus-visible:ring-offset-ink"
        >
          See all case studies
          <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 ml-2" viewBox="0 0 20 20" fill="currentColor">
            <path fill-rule="evenodd" d="M10.293 5.293a1 1 0 011.414 0l4 4a1 1 0 010 1.414l-4 4a1 1 0 01-1.414-1.414L12.586 11H3a1 1 0 110-2h11.586l-2.293-2.293a1 1 0 010-1.414z" clip-rule="evenodd" />
          </svg>
        </Link>
      </div>
    </div>
  </section>
</template>
