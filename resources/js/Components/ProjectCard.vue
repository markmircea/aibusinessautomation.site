<script setup>
import { computed } from 'vue';
import Icon from '@/Components/Icon.vue';

const props = defineProps({
  name: String,
  category: String,
  tagline: String,
  description: String,
  techStack: { type: Array, default: () => [] },
  features: { type: Array, default: () => [] },
  status: { type: String, default: '' },
  icon: { type: String, default: 'Sparkles' },
  link: { type: String, default: '' },
  animationDelay: { type: String, default: '0s' },
});

// Deterministic tile gradient: same project always gets the same treatment,
// but every project on a page looks distinct. All hues stay inside the brand
// navy -> indigo range, so six cards read as one system rather than a rainbow.
const palettes = [
  { from: '#1B2A6B', to: '#5B6CFF' },
  { from: '#131D4D', to: '#2F4BC4' },
  { from: '#2F4BC4', to: '#7C89FF' },
  { from: '#1B2A6B', to: '#4658E8' },
  { from: '#101736', to: '#6B82E8' },
  { from: '#233A8F', to: '#8A97FF' },
];

const tile = computed(() => {
  let hash = 0;
  for (const char of props.name ?? '') {
    hash = (hash * 31 + char.charCodeAt(0)) >>> 0;
  }
  const palette = palettes[hash % palettes.length];
  return { ...palette, angle: 110 + (hash % 5) * 15, id: `g${hash.toString(36)}` };
});

const statusClasses = {
  'Production': 'bg-positive/15 text-positive ring-1 ring-inset ring-positive/30',
  'Production-ready': 'bg-positive/15 text-positive ring-1 ring-inset ring-positive/30',
  'Beta': 'bg-warning/15 text-warning ring-1 ring-inset ring-warning/30',
  'In Development': 'bg-accent-400/15 text-accent-400 ring-1 ring-inset ring-accent-400/30',
};
</script>

<template>
  <article
    class="project-card group flex flex-col rounded-card bg-surface ring-1 ring-inset ring-line overflow-hidden shadow-e2 transition-colors duration-300 hover:ring-accent-500/40 animate-fade-in"
    :style="{ animationDelay: animationDelay }"
  >
    <!-- Generated cover tile. Swap for a real screenshot when one exists. -->
    <div class="relative aspect-[16/9] w-full overflow-hidden border-b border-line">
      <svg class="absolute inset-0 h-full w-full" viewBox="0 0 320 180" preserveAspectRatio="xMidYMid slice" aria-hidden="true">
        <defs>
          <linearGradient :id="tile.id" :gradientTransform="`rotate(${tile.angle} 0.5 0.5)`">
            <stop offset="0%" :stop-color="tile.from" />
            <stop offset="100%" :stop-color="tile.to" />
          </linearGradient>
          <pattern :id="`${tile.id}-dots`" width="16" height="16" patternUnits="userSpaceOnUse">
            <circle cx="1" cy="1" r="1" fill="#ffffff" fill-opacity="0.16" />
          </pattern>
        </defs>
        <rect width="320" height="180" :fill="`url(#${tile.id})`" />
        <rect width="320" height="180" :fill="`url(#${tile.id}-dots)`" />
      </svg>

      <div class="relative flex h-full items-center justify-center">
        <Icon :name="icon" class="h-12 w-12 text-white/85" :stroke-width="1.5" />
      </div>

      <span
        v-if="status"
        class="absolute top-3 right-3 text-[11px] font-semibold px-2 py-1 rounded-full backdrop-blur-sm"
        :class="statusClasses[status] || statusClasses['In Development']"
      >
        {{ status }}
      </span>
    </div>

    <div class="flex flex-1 flex-col p-6">
      <span class="text-xs font-semibold uppercase tracking-[0.12em] text-accent-400 mb-2">
        {{ category }}
      </span>
      <h3 class="text-xl font-bold text-content mb-2">{{ name }}</h3>
      <p class="text-sm font-medium text-content-muted mb-3">{{ tagline }}</p>
      <p class="text-sm text-content-subtle mb-5">{{ description }}</p>

      <div v-if="features && features.length" class="mb-5">
        <span class="text-xs font-semibold uppercase tracking-[0.12em] text-content-subtle">Highlights</span>
        <ul class="mt-2 space-y-1.5">
          <li v-for="feature in features" :key="feature" class="text-sm text-content-muted flex items-start">
            <Icon name="Check" class="h-4 w-4 mt-0.5 mr-2 flex-shrink-0 text-accent-400" />
            <span>{{ feature }}</span>
          </li>
        </ul>
      </div>

      <div v-if="techStack && techStack.length" class="mt-auto pt-4 border-t border-line">
        <span class="text-xs font-semibold uppercase tracking-[0.12em] text-content-subtle">Tech Stack</span>
        <div class="mt-2 flex flex-wrap gap-1.5">
          <span
            v-for="tech in techStack"
            :key="tech"
            class="inline-flex items-center px-2 py-1 text-xs font-medium rounded-control bg-surface-2 text-content-muted ring-1 ring-inset ring-line"
          >
            {{ tech }}
          </span>
        </div>
      </div>

      <div v-if="link" class="mt-5">
        <a
          :href="link"
          target="_blank"
          rel="noopener noreferrer"
          class="inline-flex items-center text-sm font-semibold text-accent-400 hover:text-accent-500 transition-colors focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-accent-400 focus-visible:ring-offset-2 focus-visible:ring-offset-surface rounded-control"
        >
          Visit project
          <Icon name="ArrowRight" class="h-4 w-4 ml-1" />
        </a>
      </div>
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
