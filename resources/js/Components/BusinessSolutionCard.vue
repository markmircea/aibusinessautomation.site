<script setup>
import { Link } from '@inertiajs/vue3';
import Icon from '@/Components/Icon.vue';

const props = defineProps({
  title: String,
  focus: String,
  keyPoint: String,
  icon: { type: String, default: 'Sparkles' },
  routeName: String,
  useCase: { type: String, default: '' },
  timeline: { type: String, default: '2-4 weeks' },
  integrations: { type: Array, default: () => [] },
  platforms: { type: Array, default: () => [] },
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

    <h3 class="text-xl font-bold text-content mb-4">{{ title }}</h3>

    <dl class="space-y-4 text-sm">
      <div>
        <dt class="text-xs font-semibold uppercase tracking-[0.12em] text-content-subtle mb-1">Focus</dt>
        <dd class="text-content-muted">{{ focus }}</dd>
      </div>

      <div>
        <dt class="text-xs font-semibold uppercase tracking-[0.12em] text-content-subtle mb-1">Key benefit</dt>
        <dd class="text-accent-400 font-semibold">{{ keyPoint }}</dd>
      </div>

      <div v-if="useCase" class="pt-4 border-t border-line">
        <dt class="text-xs font-semibold uppercase tracking-[0.12em] text-content-subtle mb-1">Featured use case</dt>
        <dd class="text-content-muted">{{ useCase }}</dd>
      </div>

      <div v-if="integrations.length" class="pt-4 border-t border-line">
        <dt class="text-xs font-semibold uppercase tracking-[0.12em] text-content-subtle mb-2">Key integrations</dt>
        <dd class="flex flex-wrap items-center gap-1.5">
          <span
            v-for="integration in integrations"
            :key="integration"
            class="inline-flex items-center px-2 py-1 text-xs font-medium rounded-control bg-surface-2 text-content-muted ring-1 ring-inset ring-line"
          >
            {{ integration }}
          </span>
          <Link
            :href="route('solutions.ai-integrations')"
            class="inline-flex items-center gap-1 px-1 text-xs font-semibold text-accent-400 hover:text-accent-500 underline underline-offset-2 decoration-accent-400/40 transition-colors rounded-control focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-accent-400 focus-visible:ring-offset-2 focus-visible:ring-offset-surface"
          >
            See all
            <Icon name="ArrowRight" class="h-3 w-3" />
          </Link>
        </dd>
      </div>

      <div v-if="platforms.length" class="pt-4 border-t border-line">
        <dt class="text-xs font-semibold uppercase tracking-[0.12em] text-content-subtle mb-2">Compatible with</dt>
        <dd class="flex flex-wrap gap-1.5">
          <span
            v-for="platform in platforms"
            :key="platform"
            class="inline-flex items-center px-2 py-1 text-xs font-medium rounded-control bg-surface-2 text-content-muted ring-1 ring-inset ring-line"
          >
            {{ platform }}
          </span>
        </dd>
      </div>
    </dl>

    <div class="mt-auto pt-6">
      <!-- Was hardcoded to solutions.customer-service, so all six cards led to
           the same page. Now honours the routeName each card is given. -->
      <Link
        :href="route(routeName)"
        class="inline-flex w-full items-center justify-center gap-1.5 px-4 py-2.5 rounded-control bg-accent-500 hover:bg-accent-600 text-white text-sm font-semibold transition-colors duration-200 focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-accent-400 focus-visible:ring-offset-2 focus-visible:ring-offset-surface"
      >
        Explore solution
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
