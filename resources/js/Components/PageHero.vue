<script setup>
import { onMounted } from 'vue';
import { gsap } from 'gsap';
import Icon from '@/Components/Icon.vue';

// Shared hero treatment for the homepage and every section landing page.
// Two static background layers only — the previous heroes ran three infinite
// loops (gradient / pulse / breathe) at once.
defineProps({
  eyebrow: { type: String, default: '' },
  eyebrowDot: { type: Boolean, default: false },
  title: { type: String, required: true },
  highlight: { type: String, default: '' },
  description: { type: String, default: '' },
  pills: { type: Array, default: () => [] },
  primaryCta: { type: Object, default: () => ({ label: 'Get a Quote', href: '#contact' }) },
  secondaryCta: { type: Object, default: null },
  stats: { type: Array, default: () => [] },
});

onMounted(() => {
  if (window.matchMedia('(prefers-reduced-motion: reduce)').matches) return;

  gsap.from('.hero-text', {
    duration: 0.8,
    y: 24,
    opacity: 0,
    stagger: 0.12,
    ease: 'power2.out',
  });
});
</script>

<template>
  <section class="relative overflow-hidden bg-ink">
    <div class="absolute inset-0 hero-mesh" aria-hidden="true"></div>
    <div class="absolute inset-0 hero-grid opacity-[0.07]" aria-hidden="true"></div>

    <!-- Optional extra backdrop (e.g. the Tetris animation on /web-development) -->
    <slot name="background" />

    <div class="absolute inset-x-0 bottom-0 h-20 bg-gradient-to-b from-transparent to-ink" aria-hidden="true"></div>

    <div class="relative max-w-7xl mx-auto px-4 sm:px-6 lg:px-8" :class="stats.length ? 'py-24 sm:py-32' : 'py-20 sm:py-24'">
      <div class="text-center">
        <p
          v-if="eyebrow"
          class="hero-text inline-flex items-center gap-2 px-3 py-1 mb-8 rounded-full border border-line bg-surface/60 text-xs font-semibold uppercase tracking-[0.14em] text-content-muted"
        >
          <span v-if="eyebrowDot" class="h-1.5 w-1.5 rounded-full bg-positive"></span>
          {{ eyebrow }}
        </p>

        <h1 class="hero-text text-4xl sm:text-5xl md:text-6xl font-extrabold tracking-tight text-content mb-6">
          {{ title }}
          <span v-if="highlight" class="block text-accent-400">{{ highlight }}</span>
        </h1>

        <p v-if="description" class="hero-text mx-auto max-w-2xl text-lg sm:text-xl text-content-muted mb-10">
          {{ description }}
        </p>

        <ul v-if="pills.length" class="hero-text flex flex-wrap justify-center gap-2 mb-10">
          <li
            v-for="pill in pills"
            :key="pill"
            class="px-3 py-1.5 rounded-full border border-line bg-surface/60 text-sm text-content-muted"
          >
            {{ pill }}
          </li>
        </ul>

        <div class="hero-text flex flex-wrap justify-center gap-4">
          <a
            v-if="primaryCta"
            :href="primaryCta.href"
            class="inline-flex items-center px-7 py-3.5 text-base font-semibold rounded-control text-white bg-accent-500 hover:bg-accent-600 shadow-e2 transition-colors duration-200 focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-accent-400 focus-visible:ring-offset-2 focus-visible:ring-offset-ink"
          >
            {{ primaryCta.label }}
            <Icon name="ArrowRight" class="h-5 w-5 ml-2" />
          </a>

          <a
            v-if="secondaryCta"
            :href="secondaryCta.href"
            class="inline-flex items-center px-7 py-3.5 text-base font-semibold rounded-control text-content border border-line hover:border-accent-400 hover:text-white transition-colors duration-200 focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-accent-400 focus-visible:ring-offset-2 focus-visible:ring-offset-ink"
          >
            {{ secondaryCta.label }}
          </a>
        </div>

        <dl v-if="stats.length" class="hero-text mt-20 grid grid-cols-2 gap-8 md:grid-cols-4 border-t border-line pt-10">
          <div v-for="stat in stats" :key="stat.label" class="text-center">
            <dt class="sr-only">{{ stat.label }}</dt>
            <dd>
              <span class="block text-3xl font-bold text-content">{{ stat.value }}</span>
              <span class="block mt-1 text-sm text-content-subtle">{{ stat.label }}</span>
            </dd>
          </div>
        </dl>
      </div>
    </div>
  </section>
</template>

<style scoped>
.hero-mesh {
  background:
    radial-gradient(60% 55% at 50% 0%, rgba(91, 108, 255, 0.28) 0%, transparent 70%),
    radial-gradient(45% 45% at 12% 18%, rgba(47, 75, 196, 0.22) 0%, transparent 70%),
    radial-gradient(45% 45% at 88% 22%, rgba(27, 42, 107, 0.35) 0%, transparent 70%);
}

.hero-grid {
  background-image: radial-gradient(circle, #ffffff 1px, transparent 1px);
  background-size: 32px 32px;
}
</style>
