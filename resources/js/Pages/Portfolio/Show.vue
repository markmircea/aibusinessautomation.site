<script setup>
import { computed, ref } from 'vue';
import { Link } from '@inertiajs/vue3';
import AppLayout from '@/Layouts/AppLayout.vue';
import ContactSection from '@/Components/ContactSection.vue';
import Icon from '@/Components/Icon.vue';
import Lightbox from '@/Components/Lightbox.vue';
import { getProject, neighbours, categoryLabel, statusClasses } from '@/data/portfolioMeta';

const props = defineProps({
  slug: { type: String, required: true },
});

const project = getProject(props.slug);
const { prev, next } = neighbours(props.slug);

const openIndex = ref(null);
const galleryImages = computed(() => project?.gallery ?? []);

// Shaded bands alternate down the page. Which sections exist varies per project, so work out the order here.
const BAND = 'bg-surface/30 border-y border-line';
const band = computed(() => {
  if (!project) return {};
  const order = ['built', project.diagram && 'diagram', project.videos.length && 'videos', project.results.length && 'results',
    project.nextSteps.length && 'next', galleryImages.value.length && 'gallery'].filter(Boolean);
  return Object.fromEntries(order.map((key, i) => [key, i % 2 === 0 ? BAND : '']));
});
</script>

<template>
  <AppLayout>
    <div v-if="project" class="min-h-screen bg-ink">
      <!-- Header -->
      <section class="relative overflow-hidden bg-ink border-b border-line">
        <div class="absolute inset-0 hero-mesh" aria-hidden="true"></div>
        <div class="relative max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 pt-12 pb-14">
          <nav aria-label="Breadcrumb" class="mb-8 text-sm text-content-subtle">
            <Link
              :href="route('portfolio')"
              class="hover:text-content focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-accent-400 rounded-control"
            >
              Portfolio
            </Link>
            <span aria-hidden="true"> / </span>
            <span class="text-content-muted" aria-current="page">{{ project.name }}</span>
          </nav>

          <div class="flex flex-wrap items-center gap-3">
            <span class="rounded-full bg-ink/80 backdrop-blur-sm px-2.5 py-1 text-[11px] font-semibold text-content ring-1 ring-inset ring-line">
              {{ project.engagement }}
            </span>
            <span
              class="rounded-full px-2.5 py-1 text-[11px] font-semibold ring-1 ring-inset backdrop-blur-sm"
              :class="statusClasses[project.status]"
            >
              {{ project.status }}
            </span>
            <span
              v-for="category in project.categories"
              :key="category"
              class="text-xs font-semibold uppercase tracking-[0.12em] text-accent-400"
            >
              {{ categoryLabel(category) }}
            </span>
          </div>

          <h1 class="mt-5 text-4xl sm:text-5xl font-extrabold tracking-tight text-content">{{ project.name }}</h1>
          <p class="mt-4 max-w-3xl text-lg sm:text-xl text-content-muted">{{ project.tagline }}</p>

          <div class="mt-8 flex flex-wrap gap-3">
            <a
              v-for="link in project.links"
              :key="link.href"
              :href="link.href"
              target="_blank"
              rel="noopener noreferrer"
              class="inline-flex items-center px-7 py-3.5 text-base font-semibold rounded-control text-content border border-line hover:border-accent-400 hover:text-white transition-colors duration-200 focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-accent-400 focus-visible:ring-offset-2 focus-visible:ring-offset-ink"
            >
              {{ link.label }}
              <Icon name="ExternalLink" class="h-4 w-4 ml-2" />
            </a>
            <a
              href="#contact"
              class="inline-flex items-center px-7 py-3.5 text-base font-semibold rounded-control text-white bg-accent-500 hover:bg-accent-600 shadow-e2 transition-colors duration-200 focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-accent-400 focus-visible:ring-offset-2 focus-visible:ring-offset-ink"
            >
              Get a Quote
              <Icon name="ArrowRight" class="h-5 w-5 ml-2" />
            </a>
          </div>
        </div>
      </section>

      <!-- Cover -->
      <div v-if="project.cover" class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 -mt-px pt-10">
        <figure class="rounded-card overflow-hidden ring-1 ring-line shadow-e3">
          <img
            :src="`${project.cover.src}-800.webp`"
            :srcset="`${project.cover.src}-800.webp 800w, ${project.cover.src}.webp ${project.cover.width}w`"
            sizes="(min-width: 1280px) 1216px, 100vw"
            :alt="project.cover.alt"
            :width="project.cover.width"
            :height="project.cover.height"
            fetchpriority="high"
            decoding="async"
            class="w-full h-auto object-cover"
          >
        </figure>
      </div>

      <!-- Challenge + at a glance -->
      <section class="py-16">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 grid gap-10 lg:grid-cols-3">
          <div class="lg:col-span-2">
            <h2 class="text-3xl sm:text-4xl font-bold tracking-tight text-content mb-6">The challenge</h2>
            <p v-for="para in project.challenge" :key="para" class="text-lg text-content-muted mb-4">{{ para }}</p>
          </div>

          <aside class="rounded-card bg-surface ring-1 ring-inset ring-line p-6 h-fit">
            <h2 class="text-xs font-semibold uppercase tracking-[0.12em] text-content-subtle mb-4">At a glance</h2>
            <dl class="space-y-4">
              <div>
                <dt class="text-xs text-content-subtle">Engagement</dt>
                <dd class="text-content">{{ project.engagement }}</dd>
              </div>
              <div>
                <dt class="text-xs text-content-subtle">Status</dt>
                <dd class="text-content">{{ project.status }}</dd>
              </div>
              <div>
                <dt class="text-xs text-content-subtle">Timeline</dt>
                <dd class="text-content">{{ project.timeline }}</dd>
              </div>
              <div>
                <dt class="text-xs text-content-subtle">Role</dt>
                <dd class="text-content">{{ project.role }}</dd>
              </div>
              <div>
                <dt class="text-xs text-content-subtle">Platforms</dt>
                <dd class="text-content">{{ project.platforms.join(' · ') }}</dd>
              </div>
            </dl>

            <h2 class="text-xs font-semibold uppercase tracking-[0.12em] text-content-subtle mt-6 mb-3">Stack</h2>
            <div class="flex flex-wrap gap-1.5">
              <span
                v-for="tech in project.stack"
                :key="tech"
                class="inline-flex items-center px-2 py-1 text-xs font-medium rounded-control bg-surface-2 text-content-muted ring-1 ring-inset ring-line"
              >
                {{ tech }}
              </span>
            </div>
          </aside>
        </div>
      </section>

      <!-- What we built -->
      <section class="py-16" :class="band.built">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <h2 class="text-3xl sm:text-4xl font-bold tracking-tight text-content mb-10">What we built</h2>
          <ul class="grid md:grid-cols-2 gap-4">
            <li
              v-for="item in project.built"
              :key="item"
              class="flex gap-3 rounded-card bg-surface ring-1 ring-inset ring-line p-5"
            >
              <Icon name="Check" class="h-5 w-5 mt-0.5 shrink-0 text-accent-400" />
              <span class="text-content-muted">{{ item }}</span>
            </li>
          </ul>
        </div>
      </section>

      <!-- How it works -->
      <section v-if="project.diagram" class="py-16" :class="band.diagram">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <h2 class="text-3xl sm:text-4xl font-bold tracking-tight text-content mb-10">How it works</h2>
          <figure>
            <div class="rounded-card ring-1 ring-line overflow-hidden bg-surface">
              <img
                :src="`${project.diagram.src}-800.webp`"
                :srcset="`${project.diagram.src}-800.webp 800w, ${project.diagram.src}.webp ${project.diagram.width}w`"
                sizes="(min-width: 1280px) 1216px, 100vw"
                :alt="project.diagram.alt"
                :width="project.diagram.width"
                :height="project.diagram.height"
                loading="lazy"
                decoding="async"
                class="w-full h-auto object-contain"
              >
            </div>
            <figcaption class="mt-3 text-sm text-content-subtle">{{ project.diagram.caption }}</figcaption>
          </figure>
        </div>
      </section>

      <!-- Videos: real output of the system, when the case study has any -->
      <section v-if="project.videos.length" class="py-16" :class="band.videos">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <h2 class="text-3xl sm:text-4xl font-bold tracking-tight text-content mb-10">See it in action</h2>
          <div :class="project.videos.length > 1 ? 'grid gap-8 md:grid-cols-2' : 'flex justify-center'">
            <figure v-for="video in project.videos" :key="video.src" class="flex flex-col items-center">
              <video
                :src="video.src"
                :poster="video.poster"
                :width="video.width"
                :height="video.height"
                :aria-label="video.title"
                controls
                playsinline
                preload="metadata"
                class="max-h-[80vh] w-auto max-w-full h-auto rounded-card ring-1 ring-line shadow-e3 bg-ink"
              ></video>
              <figcaption class="mt-3 max-w-2xl text-center text-sm text-content-subtle">{{ video.caption }}</figcaption>
            </figure>
          </div>
        </div>
      </section>

      <!-- Results, then where the project stands today -->
      <section v-if="project.results.length" class="py-16" :class="band.results">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <h2 class="text-3xl sm:text-4xl font-bold tracking-tight text-content mb-10">Results</h2>
          <div class="grid grid-cols-2 lg:grid-cols-4 gap-4">
            <div
              v-for="result in project.results"
              :key="result.label"
              class="rounded-card bg-surface ring-1 ring-inset ring-line p-6"
            >
              <div class="text-3xl font-bold text-content">{{ result.value }}</div>
              <div class="mt-1 text-sm text-content-subtle">{{ result.label }}</div>
            </div>
          </div>
        </div>
      </section>

      <section v-if="project.nextSteps.length" class="py-16" :class="band.next">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <h2 class="text-3xl sm:text-4xl font-bold tracking-tight text-content mb-10">Status &amp; next steps</h2>
          <ul class="space-y-3 max-w-3xl">
            <li v-for="step in project.nextSteps" :key="step" class="flex items-start gap-3 text-content-muted">
              <Icon name="ArrowRight" class="h-5 w-5 mt-0.5 shrink-0 text-accent-400" />
              <span>{{ step }}</span>
            </li>
          </ul>
        </div>
      </section>

      <!-- Gallery -->
      <section v-if="galleryImages.length" class="py-16" :class="band.gallery">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <h2 class="text-3xl sm:text-4xl font-bold tracking-tight text-content mb-10">Gallery</h2>
          <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-5">
            <figure v-for="(img, i) in galleryImages" :key="img.src">
              <button
                type="button"
                :aria-label="`Open image: ${img.alt}`"
                class="group block w-full overflow-hidden rounded-card focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-accent-400"
                @click="openIndex = i"
              >
                <img
                  :src="`${img.src}-800.webp`"
                  :alt="img.alt"
                  :width="img.width"
                  :height="img.height"
                  loading="lazy"
                  decoding="async"
                  class="aspect-[16/10] w-full object-cover rounded-card ring-1 ring-line transition-transform duration-300 group-hover:scale-[1.02]"
                >
              </button>
              <figcaption v-if="img.caption" class="mt-2 text-sm text-content-subtle">{{ img.caption }}</figcaption>
            </figure>
          </div>
        </div>

        <Lightbox :images="galleryImages" v-model:index="openIndex" />
      </section>

      <!-- Previous / next -->
      <section v-if="prev && next" class="py-12 border-t border-line">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 grid sm:grid-cols-2 gap-4">
          <Link
            :href="route('portfolio.show', prev.slug)"
            class="rounded-card bg-surface ring-1 ring-inset ring-line p-6 hover:ring-accent-500/40 focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-accent-400 flex items-center gap-4"
          >
            <Icon name="ArrowLeft" class="h-5 w-5 shrink-0 text-accent-400" />
            <span>
              <span class="block text-xs font-semibold uppercase tracking-[0.12em] text-content-subtle">Previous case study</span>
              <span class="block text-lg font-bold text-content">{{ prev.name }}</span>
            </span>
          </Link>

          <Link
            :href="route('portfolio.show', next.slug)"
            class="rounded-card bg-surface ring-1 ring-inset ring-line p-6 hover:ring-accent-500/40 focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-accent-400 flex items-center justify-end gap-4 text-right"
          >
            <span>
              <span class="block text-xs font-semibold uppercase tracking-[0.12em] text-content-subtle">Next case study</span>
              <span class="block text-lg font-bold text-content">{{ next.name }}</span>
            </span>
            <Icon name="ArrowRight" class="h-5 w-5 shrink-0 text-accent-400" />
          </Link>
        </div>
      </section>

      <ContactSection :solution="project.name" heading="Planning something similar?" />
    </div>
  </AppLayout>
</template>

<style scoped>
.hero-mesh {
  background:
    radial-gradient(60% 55% at 50% 0%, rgba(91, 108, 255, 0.28) 0%, transparent 70%),
    radial-gradient(45% 45% at 12% 18%, rgba(47, 75, 196, 0.22) 0%, transparent 70%),
    radial-gradient(45% 45% at 88% 22%, rgba(27, 42, 107, 0.35) 0%, transparent 70%);
}
</style>
