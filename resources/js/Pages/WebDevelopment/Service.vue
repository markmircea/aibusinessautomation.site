<script setup>
import { computed, ref } from 'vue';
import AppLayout from '@/Layouts/AppLayout.vue';
import PageHero from '@/Components/PageHero.vue';
import ContactSection from '@/Components/ContactSection.vue';
import Icon from '@/Components/Icon.vue';
import Lightbox from '@/Components/Lightbox.vue';
import { getService } from '@/data/webDevelopmentServices';

const props = defineProps({
  slug: { type: String, required: true },
});

const service = computed(() => getService(props.slug));

// One shared lightbox for the example campaigns' images.
const lightbox = ref({ images: [], index: null });
const openExample = (example, i = 0) => {
  lightbox.value = { images: example.images, index: i };
};
</script>

<template>
  <AppLayout>
    <div v-if="service" class="min-h-screen bg-ink">
      <PageHero
        :eyebrow="service.eyebrow"
        :title="service.title"
        :description="service.description"
        :pills="service.heroPills"
        :primary-cta="{ label: 'Get a Quote', href: '#contact' }"
        :secondary-cta="{ label: 'See our work', href: '/portfolio' }"
      />

      <!-- Overview -->
      <section class="py-20 bg-ink">
        <div class="max-w-3xl mx-auto px-4 sm:px-6 lg:px-8">
          <h2 class="text-3xl sm:text-4xl font-bold tracking-tight text-content mb-6">Service overview</h2>
          <p v-for="para in service.overview" :key="para" class="text-lg text-content-muted mb-4">
            {{ para }}
          </p>

          <div class="grid gap-4 sm:grid-cols-2 mt-10">
            <div class="p-6 rounded-card bg-surface ring-1 ring-inset ring-line">
              <h3 class="text-xs font-semibold uppercase tracking-[0.12em] text-content-subtle mb-2">Our focus</h3>
              <p class="text-content-muted">{{ service.focus }}</p>
            </div>
            <div class="p-6 rounded-card bg-surface ring-1 ring-inset ring-line">
              <h3 class="text-xs font-semibold uppercase tracking-[0.12em] text-content-subtle mb-2">Key benefit</h3>
              <p class="text-content-muted">{{ service.keyPoint }}</p>
            </div>
          </div>
        </div>
      </section>

      <!-- Key features -->
      <section class="py-20 bg-surface/30 border-y border-line">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <h2 class="text-3xl sm:text-4xl font-bold tracking-tight text-content text-center mb-12">Key features</h2>
          <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
            <div
              v-for="feature in service.features"
              :key="feature.title"
              class="p-6 rounded-card bg-surface ring-1 ring-inset ring-line shadow-e2 transition-colors duration-300 hover:ring-accent-500/40"
            >
              <h3 class="text-lg font-bold text-content mb-2">{{ feature.title }}</h3>
              <p class="text-sm text-content-muted">{{ feature.body }}</p>
            </div>
          </div>
        </div>
      </section>

      <!-- Technologies -->
      <section class="py-20 bg-ink">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div class="text-center mb-12">
            <h2 class="text-3xl sm:text-4xl font-bold tracking-tight text-content mb-4">Technologies</h2>
            <p class="max-w-2xl mx-auto text-lg text-content-muted">
              The stack we reach for on this kind of build.
            </p>
          </div>

          <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-6">
            <div
              v-for="group in service.technologies"
              :key="group.group"
              class="p-6 rounded-card bg-surface ring-1 ring-inset ring-line"
            >
              <h3 class="text-xs font-semibold uppercase tracking-[0.12em] text-accent-400 mb-3">{{ group.group }}</h3>
              <div class="flex flex-wrap gap-1.5">
                <span
                  v-for="item in group.items"
                  :key="item"
                  class="inline-flex items-center px-2 py-1 text-xs font-medium rounded-control bg-surface-2 text-content-muted ring-1 ring-inset ring-line"
                >
                  {{ item }}
                </span>
              </div>
            </div>
          </div>
        </div>
      </section>

      <!-- Process -->
      <section class="py-20 bg-surface/30 border-y border-line">
        <div class="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8">
          <h2 class="text-3xl sm:text-4xl font-bold tracking-tight text-content text-center mb-12">How we build it</h2>
          <ol class="space-y-8">
            <li v-for="(step, i) in service.process" :key="step.title" class="flex items-start gap-5">
              <span
                class="flex-shrink-0 h-10 w-10 rounded-full bg-accent-500/12 ring-1 ring-inset ring-accent-500/30 text-accent-400 flex items-center justify-center font-bold"
                aria-hidden="true"
              >{{ i + 1 }}</span>
              <div>
                <h3 class="text-lg font-semibold text-content">{{ step.title }}</h3>
                <p class="text-content-muted mt-1">{{ step.body }}</p>
              </div>
            </li>
          </ol>
        </div>
      </section>

      <!-- Benefits -->
      <section class="py-20 bg-ink">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <h2 class="text-3xl sm:text-4xl font-bold tracking-tight text-content text-center mb-12">What you get</h2>
          <div class="grid grid-cols-1 md:grid-cols-2 gap-x-10 gap-y-8">
            <div v-for="benefit in service.benefits" :key="benefit.title" class="flex items-start gap-4">
              <Icon name="Check" class="h-5 w-5 mt-1 flex-shrink-0 text-accent-400" />
              <div>
                <h3 class="text-lg font-semibold text-content">{{ benefit.title }}</h3>
                <p class="text-content-muted mt-1">{{ benefit.body }}</p>
              </div>
            </div>
          </div>
        </div>
      </section>

      <!-- Example campaigns -->
      <section v-if="service.examples?.length" class="py-20 bg-surface/30 border-y border-line">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div class="text-center mb-12">
            <span class="inline-flex items-center gap-2 px-3 py-1 mb-5 rounded-full border border-line bg-surface/60 text-xs font-semibold uppercase tracking-[0.14em] text-warning">Illustrative examples</span>
            <h2 class="text-3xl sm:text-4xl font-bold tracking-tight text-content mb-4">Example campaigns</h2>
            <p class="max-w-3xl mx-auto text-lg text-content-muted">
              How we would approach four typical briefs. The brands are fictional and the figures are the targets we would set, not results from client work.
            </p>
          </div>

          <div class="grid gap-8 lg:grid-cols-2">
            <article
              v-for="ex in service.examples"
              :key="ex.brand"
              class="flex flex-col rounded-card bg-surface ring-1 ring-inset ring-line overflow-hidden shadow-e2"
            >
              <button
                type="button"
                @click="openExample(ex)"
                :aria-label="`View ${ex.brand} example images`"
                class="group relative block aspect-[16/9] w-full overflow-hidden bg-surface-2 focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-accent-400"
              >
                <img
                  :src="`${ex.images[0].src}-800.webp`"
                  :srcset="`${ex.images[0].src}-800.webp 800w, ${ex.images[0].src}.webp 1600w`"
                  sizes="(min-width: 1024px) 50vw, 100vw"
                  :alt="ex.images[0].alt"
                  loading="lazy"
                  decoding="async"
                  class="h-full w-full object-cover transition-transform duration-500 group-hover:scale-[1.03]"
                >
                <span class="absolute top-3 left-3 rounded-full bg-ink/85 backdrop-blur-sm px-2.5 py-1 text-[11px] font-semibold text-content ring-1 ring-inset ring-line">Example campaign — illustrative, not client work</span>
                <span class="absolute bottom-3 right-3 rounded-full bg-ink/85 px-2.5 py-1 text-[11px] font-semibold text-content-muted ring-1 ring-inset ring-line">{{ ex.images.length }} images</span>
              </button>

              <div class="flex flex-1 flex-col p-6">
                <p class="text-xs font-semibold uppercase tracking-[0.12em] text-accent-400 mb-1">{{ ex.industry }}</p>
                <h3 class="text-xl font-bold text-content mb-3">{{ ex.brand }}</h3>
                <div class="flex flex-wrap gap-1.5 mb-5">
                  <span
                    v-for="item in ex.services"
                    :key="item"
                    class="inline-flex items-center px-2 py-1 text-xs font-medium rounded-control bg-surface-2 text-content-muted ring-1 ring-inset ring-line"
                  >
                    {{ item }}
                  </span>
                </div>
                <dl class="space-y-4 text-sm mb-6">
                  <div>
                    <dt class="text-xs font-semibold uppercase tracking-[0.12em] text-content-subtle mb-1">The brief</dt>
                    <dd class="text-content-muted">{{ ex.challenge }}</dd>
                  </div>
                  <div>
                    <dt class="text-xs font-semibold uppercase tracking-[0.12em] text-content-subtle mb-1">Our approach</dt>
                    <dd class="text-content-muted">{{ ex.approach }}</dd>
                  </div>
                </dl>

                <div class="mt-auto pt-5 border-t border-line grid grid-cols-3 gap-4">
                  <div v-for="target in ex.targets" :key="target.label">
                    <p class="text-xl font-bold text-content">{{ target.value }}</p>
                    <p class="text-xs text-content-subtle leading-snug">{{ target.label }}</p>
                    <span class="mt-1 inline-block text-[10px] font-semibold uppercase tracking-wider text-warning">Target</span>
                  </div>
                </div>
              </div>
            </article>
          </div>

          <Lightbox :images="lightbox.images" v-model:index="lightbox.index" />
        </div>
      </section>

      <ContactSection :solution="service.title" />
    </div>
  </AppLayout>
</template>
