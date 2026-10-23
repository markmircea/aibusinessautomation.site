<script setup>
import { computed, onMounted, ref } from 'vue';
import { Link } from '@inertiajs/vue3';
import AppLayout from '@/Layouts/AppLayout.vue';
import PageHero from '@/Components/PageHero.vue';
import ProjectCard from '@/Components/ProjectCard.vue';
import ContactSection from '@/Components/ContactSection.vue';
import Icon from '@/Components/Icon.vue';
import { projects, CATEGORIES, getProject } from '@/data/portfolioMeta';

const active = ref('all');

onMounted(() => {
  const fromQuery = new URLSearchParams(window.location.search).get('c');
  if (fromQuery && CATEGORIES.some((c) => c.key === fromQuery)) active.value = fromQuery;
});

function setFilter(key) {
  active.value = key;
  window.history.replaceState(
    window.history.state,
    '',
    key === 'all' ? window.location.pathname : `?c=${key}`
  );
}

const counts = computed(() => {
  const result = {};
  CATEGORIES.forEach((c) => {
    result[c.key] = c.key === 'all' ? projects.length : projects.filter((p) => p.categories.includes(c.key)).length;
  });
  return result;
});

// A category only shows up in the filter bar when there is something to show for it.
const filters = computed(() => CATEGORIES.filter((c) => c.key === 'all' || counts.value[c.key] > 0));

const visible = computed(() =>
  active.value === 'all' ? projects : projects.filter((p) => p.categories.includes(active.value))
);

const flagship = getProject('selenix');

const capabilities = [
  { icon: 'Globe', label: 'E-commerce & Web Apps' },
  { icon: 'Smartphone', label: 'Mobile Apps' },
  { icon: 'Monitor', label: 'Desktop Apps' },
  { icon: 'Webhook', label: 'APIs & Backends' },
  { icon: 'Workflow', label: 'Automations' },
  { icon: 'BrainCircuit', label: 'Agentic AI Systems' },
  { icon: 'Gamepad2', label: 'Games & Real-time 3D' },
];
</script>

<template>
  <AppLayout>
    <div class="min-h-screen bg-ink">
      <PageHero
        eyebrow="Portfolio"
        title="Case studies"
        highlight="from the team that will build yours"
        description="Products we have shipped and systems we have built — web platforms, desktop and mobile apps, games, APIs and agentic AI. Every screenshot on these pages is real."
        :primary-cta="{ label: 'Get a Quote', href: '#contact' }"
        :secondary-cta="{ label: 'Browse case studies', href: '#case-studies' }"
      />

      <!-- Case studies -->
      <section id="case-studies" class="py-16 bg-surface/30 border-y border-line">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div role="group" aria-label="Filter case studies" class="flex flex-wrap justify-center gap-2 mb-10">
            <button
              v-for="c in filters"
              :key="c.key"
              type="button"
              :aria-pressed="active === c.key"
              class="inline-flex items-center rounded-full px-4 py-2 text-sm font-semibold transition-colors duration-200 focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-accent-400"
              :class="active === c.key
                ? 'bg-accent-500 text-white shadow-e1'
                : 'bg-surface text-content-muted ring-1 ring-inset ring-line hover:text-content'"
              @click="setFilter(c.key)"
            >
              {{ c.label }}
              <span class="ml-1.5 text-xs opacity-70">{{ counts[c.key] }}</span>
            </button>
          </div>

          <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
            <ProjectCard
              v-for="(p, i) in visible"
              :key="p.slug"
              :project="p"
              :animation-delay="`${i * 0.06}s`"
            />
          </div>
        </div>
      </section>

      <!-- Flagship spotlight -->
      <section v-if="flagship" class="py-16 bg-ink">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div class="grid lg:grid-cols-5 rounded-card bg-surface ring-1 ring-inset ring-line overflow-hidden shadow-e3">
            <div class="lg:col-span-3 relative aspect-[16/9] lg:aspect-auto overflow-hidden">
              <img
                v-if="flagship.cover"
                :src="`${flagship.cover.src}-800.webp`"
                :srcset="`${flagship.cover.src}-800.webp 800w, ${flagship.cover.src}.webp ${flagship.cover.width}w`"
                sizes="(min-width: 1024px) 60vw, 100vw"
                :alt="flagship.cover.alt"
                :width="flagship.cover.width"
                :height="flagship.cover.height"
                loading="lazy"
                decoding="async"
                class="object-cover h-full w-full"
              >
            </div>
            <div class="lg:col-span-2 p-8 flex flex-col justify-center">
              <span class="text-xs font-semibold uppercase tracking-[0.14em] text-accent-400 mb-3">Flagship platform</span>
              <h2 class="text-3xl font-bold text-content mb-3">{{ flagship.name }}</h2>
              <p class="text-content-muted mb-6">{{ flagship.tagline }}</p>
              <div class="space-y-2 mb-8">
                <div v-for="result in flagship.results" :key="result.label" class="flex items-baseline gap-2">
                  <span class="text-xl font-bold text-content">{{ result.value }}</span>
                  <span class="text-sm text-content-subtle">{{ result.label }}</span>
                </div>
              </div>
              <Link
                :href="route('portfolio.show', 'selenix')"
                class="inline-flex items-center self-start px-7 py-3.5 text-base font-semibold rounded-control text-white bg-accent-500 hover:bg-accent-600 shadow-e2 transition-colors duration-200 focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-accent-400 focus-visible:ring-offset-2 focus-visible:ring-offset-surface"
              >
                Read the case study
                <Icon name="ArrowRight" class="h-5 w-5 ml-2" />
              </Link>
            </div>
          </div>
        </div>
      </section>

      <!-- Capabilities band -->
      <section class="py-16 bg-surface/30 border-y border-line">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div class="text-center mb-10">
            <h2 class="text-2xl sm:text-3xl font-bold tracking-tight text-content mb-3">
              What we can build for you
            </h2>
            <p class="max-w-3xl mx-auto text-content-muted">
              The case studies above demonstrate capabilities across every category we offer.
            </p>
          </div>
          <div class="grid grid-cols-2 md:grid-cols-4 lg:grid-cols-7 gap-4">
            <div
              v-for="capability in capabilities"
              :key="capability.label"
              class="flex flex-col items-center gap-3 p-5 rounded-card bg-surface ring-1 ring-inset ring-line transition-colors duration-200 hover:ring-accent-500/40"
            >
              <Icon :name="capability.icon" class="h-6 w-6 text-accent-400" />
              <span class="text-sm font-semibold text-content text-center">{{ capability.label }}</span>
            </div>
          </div>
        </div>
      </section>

      <ContactSection solution="Portfolio enquiry" heading="Have a project like these in mind?" />
    </div>
  </AppLayout>
</template>
