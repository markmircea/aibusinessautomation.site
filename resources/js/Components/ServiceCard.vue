<script setup>
import { Link } from '@inertiajs/vue3';
import Icon from '@/Components/Icon.vue';

// Same card contract as ProjectCard / BusinessSolutionCard: one surface,
// one ring, one accent. No per-card colour.
defineProps({
  title: String,
  tagline: String,
  description: String,
  icon: { type: String, default: 'Sparkles' },
  routeName: { type: String, required: true },
  highlights: { type: Array, default: () => [] },
  animationDelay: { type: String, default: '0s' },
});
</script>

<template>
  <article
    class="flex flex-col p-6 rounded-card bg-surface ring-1 ring-inset ring-line shadow-e2 transition-colors duration-300 hover:ring-accent-500/40 animate-fade-in"
    :style="{ animationDelay: animationDelay }"
  >
    <div class="h-12 w-12 rounded-control bg-accent-500/12 ring-1 ring-inset ring-accent-500/25 flex items-center justify-center mb-5">
      <Icon :name="icon" class="h-6 w-6 text-accent-400" />
    </div>

    <h3 class="text-xl font-bold text-content mb-2">{{ title }}</h3>
    <p v-if="tagline" class="text-sm font-medium text-content-muted mb-3">{{ tagline }}</p>
    <p class="text-sm text-content-subtle mb-5">{{ description }}</p>

    <ul v-if="highlights.length" class="space-y-1.5 mb-6">
      <li v-for="item in highlights" :key="item" class="text-sm text-content-muted flex items-start">
        <Icon name="Check" class="h-4 w-4 mt-0.5 mr-2 flex-shrink-0 text-accent-400" />
        <span>{{ item }}</span>
      </li>
    </ul>

    <div class="mt-auto">
      <Link
        :href="route(routeName)"
        class="inline-flex w-full items-center justify-center gap-1.5 px-4 py-2.5 rounded-control bg-accent-500 hover:bg-accent-600 text-white text-sm font-semibold transition-colors duration-200 focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-accent-400 focus-visible:ring-offset-2 focus-visible:ring-offset-surface"
      >
        Explore service
        <Icon name="ArrowRight" class="h-4 w-4" />
      </Link>
    </div>
  </article>
</template>

<style scoped>
@keyframes fadeIn {
  from { opacity: 0; transform: translateY(16px); }
  to   { opacity: 1; transform: translateY(0); }
}

.animate-fade-in {
  animation: fadeIn 0.6s ease-out forwards;
  opacity: 0;
}

@media (prefers-reduced-motion: reduce) {
  .animate-fade-in {
    animation: none;
    opacity: 1;
  }
}
</style>
