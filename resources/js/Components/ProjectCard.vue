<script setup>
import { Link } from '@inertiajs/vue3';
import Icon from '@/Components/Icon.vue';
import { categoryLabel, statusClasses } from '@/data/portfolioMeta';

// Whole card is one link to the case study — no nested links inside it.
defineProps({
  project: { type: Object, required: true },
  animationDelay: { type: String, default: '0s' },
});
</script>

<template>
  <Link
    :href="route('portfolio.show', project.slug)"
    class="group flex flex-col rounded-card bg-surface ring-1 ring-inset ring-line overflow-hidden shadow-e2 transition-colors duration-300 hover:ring-accent-500/40 focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-accent-400 animate-fade-in"
    :style="{ animationDelay }"
  >
    <div class="relative aspect-[16/9] w-full overflow-hidden border-b border-line bg-surface-2">
      <img
        v-if="project.cover"
        :src="`${project.cover.src}-800.webp`"
        :srcset="`${project.cover.src}-800.webp 800w, ${project.cover.src}.webp ${project.cover.width}w`"
        sizes="(min-width: 1024px) 33vw, (min-width: 768px) 50vw, 100vw"
        :alt="project.cover.alt"
        :width="project.cover.width"
        :height="project.cover.height"
        loading="lazy"
        decoding="async"
        class="h-full w-full object-cover transition-transform duration-500 group-hover:scale-[1.03]"
      >

      <!-- Placeholder tile for case studies without a screenshot yet. -->
      <div v-else class="absolute inset-0 bg-gradient-to-br from-brand-700 to-accent-600 flex items-center justify-center">
        <Icon name="Sparkles" class="h-12 w-12 text-white/85" />
      </div>

      <span class="absolute top-3 left-3 rounded-full bg-ink/80 backdrop-blur-sm px-2.5 py-1 text-[11px] font-semibold text-content ring-1 ring-inset ring-line">
        {{ project.engagement }}
      </span>

      <span
        class="absolute top-3 right-3 rounded-full px-2.5 py-1 text-[11px] font-semibold ring-1 ring-inset backdrop-blur-sm"
        :class="statusClasses[project.status]"
      >
        {{ project.status }}
      </span>
    </div>

    <div class="flex flex-1 flex-col p-6">
      <!-- Two categories at most, so the label stays on one line; the filters still use them all. -->
      <span class="text-xs font-semibold uppercase tracking-[0.12em] text-accent-400 mb-2">
        {{ project.categories.slice(0, 2).map(categoryLabel).join(' · ') }}
      </span>

      <h3 class="text-xl font-bold text-content mb-2">{{ project.name }}</h3>
      <p class="text-sm text-content-muted mb-5">{{ project.tagline }}</p>

      <div class="mt-auto flex flex-wrap gap-1.5">
        <span
          v-for="tech in project.stack.slice(0, 3)"
          :key="tech"
          class="inline-flex items-center px-2 py-1 text-xs font-medium rounded-control bg-surface-2 text-content-muted ring-1 ring-inset ring-line"
        >
          {{ tech }}
        </span>
        <span
          v-if="project.stack.length > 3"
          class="inline-flex items-center px-2 py-1 text-xs font-medium rounded-control bg-surface-2 text-content-muted ring-1 ring-inset ring-line"
        >
          +{{ project.stack.length - 3 }}
        </span>
      </div>

      <span class="mt-5 inline-flex items-center gap-1.5 text-sm font-semibold text-accent-400">
        Read case study
        <Icon name="ArrowRight" class="h-4 w-4 transition-transform duration-200 group-hover:translate-x-1" />
      </span>
    </div>
  </Link>
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
