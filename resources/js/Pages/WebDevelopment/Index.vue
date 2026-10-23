<script setup>
import AppLayout from '@/Layouts/AppLayout.vue';
import PageHero from '@/Components/PageHero.vue';
import ServiceCard from '@/Components/ServiceCard.vue';
import ContactSection from '@/Components/ContactSection.vue';
import TetrisAnimation from '@/Components/WebDevelopment/TetrisAnimation.vue';
import Icon from '@/Components/Icon.vue';
import { webDevelopmentServices, serviceOrder } from '@/data/webDevelopmentServices';

const services = serviceOrder.map((slug) => webDevelopmentServices[slug]);

const pills = ['E-commerce', 'Marketing sites', 'Mobile apps', 'Scraping & automation', 'Digital marketing'];

// Stated once here rather than repeated on every service page.
const approach = [
  { icon: 'MessagesSquare', title: 'Scope before code', body: 'We agree the problem, the constraints and what "done" means before anyone opens an editor.' },
  { icon: 'LayoutTemplate', title: 'Design in the open', body: 'Wireframes and visual design reviewed with you, not delivered as a surprise at the end.' },
  { icon: 'Workflow', title: 'Ship in increments', body: 'Short iterations with something reviewable at the end of each, so direction changes stay cheap.' },
  { icon: 'Check', title: 'Support after launch', body: 'Monitoring, fixes and iteration once real users are on it — launch is the midpoint, not the finish.' },
];
</script>

<template>
  <AppLayout>
    <div class="min-h-screen bg-ink">
      <PageHero
        eyebrow="Web Development"
        title="Web that earns its keep"
        highlight="designed, built and maintained"
        description="Storefronts, marketing sites, mobile apps, automation pipelines and the marketing that grows them, built and run by the team that also ships our own products."
        :pills="pills"
        :primary-cta="{ label: 'Get a Quote', href: '#contact' }"
        :secondary-cta="{ label: 'See our work', href: '/portfolio' }"
      >
        <template #background>
          <!-- Masked so blocks fade out behind the headline: at full strength
               they fell straight through the hero text and hurt legibility. -->
          <div class="absolute inset-0 tetris-backdrop" aria-hidden="true">
            <TetrisAnimation />
          </div>
        </template>
      </PageHero>

      <!-- Services -->
      <section class="py-20 bg-surface/30 border-y border-line">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div class="text-center mb-12">
            <h2 class="text-3xl sm:text-4xl font-bold tracking-tight text-content mb-4">
              Five services, one team
            </h2>
            <p class="max-w-3xl mx-auto text-lg text-content-muted">
              Each one is a full engagement, from the first workshop to launch and the growth work after it.
            </p>
          </div>

          <div class="flex flex-wrap justify-center gap-6">
            <div
              v-for="(service, idx) in services"
              :key="service.slug"
              class="w-full md:w-[calc(50%-0.75rem)] lg:w-[calc(33.333%-1rem)] flex"
            >
              <ServiceCard
                class="w-full"
                :title="service.title"
                :tagline="service.eyebrow"
                :description="service.description"
                :icon="service.icon"
                :route-name="service.routeName"
                :animation-delay="`${idx * 0.08}s`"
              />
            </div>
          </div>
        </div>
      </section>

      <!-- How we work -->
      <section class="py-20 bg-ink">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div class="text-center mb-12">
            <h2 class="text-3xl sm:text-4xl font-bold tracking-tight text-content mb-4">How we work</h2>
            <p class="max-w-3xl mx-auto text-lg text-content-muted">
              The same approach on every engagement, whichever service you start with.
            </p>
          </div>

          <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">
            <div
              v-for="step in approach"
              :key="step.title"
              class="p-6 rounded-card bg-surface ring-1 ring-inset ring-line transition-colors duration-200 hover:ring-accent-500/40"
            >
              <div class="h-12 w-12 rounded-control bg-accent-500/12 ring-1 ring-inset ring-accent-500/25 flex items-center justify-center mb-4">
                <Icon :name="step.icon" class="h-6 w-6 text-accent-400" />
              </div>
              <h3 class="text-lg font-semibold text-content mb-2">{{ step.title }}</h3>
              <p class="text-sm text-content-muted">{{ step.body }}</p>
            </div>
          </div>
        </div>
      </section>

      <ContactSection solution="Web Development" heading="Tell us about your project" />
    </div>
  </AppLayout>
</template>

<style scoped>
/* Keep the animation to the edges: transparent in the middle third where the
   headline, subhead and CTAs sit. */
.tetris-backdrop {
  opacity: 0.45;
  -webkit-mask-image: radial-gradient(ellipse 46% 42% at 50% 42%, transparent 0%, transparent 55%, #000 100%);
  mask-image: radial-gradient(ellipse 46% 42% at 50% 42%, transparent 0%, transparent 55%, #000 100%);
}
</style>
