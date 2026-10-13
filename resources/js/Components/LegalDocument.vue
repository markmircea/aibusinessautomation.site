<script setup>
import AppLayout from '@/Layouts/AppLayout.vue';
import PageHero from '@/Components/PageHero.vue';

// Shared shell for Privacy Policy / Terms of Service. Sections render as plain
// prose rather than an accordion so the text is scannable, printable and fully
// visible to crawlers.
defineProps({
  title: { type: String, required: true },
  description: { type: String, default: '' },
  lastUpdated: { type: String, required: true },
  intro: { type: String, default: '' },
  sections: { type: Array, required: true }, // [{ heading, paragraphs: [], list: [] }]
});
</script>

<template>
  <AppLayout>
    <div class="min-h-screen bg-ink">
      <PageHero
        eyebrow="Legal"
        :title="title"
        :description="description"
        :primary-cta="null"
        :secondary-cta="{ label: 'Back to home', href: '/' }"
      />

      <section class="py-16 bg-surface/30 border-y border-line">
        <div class="max-w-3xl mx-auto px-4 sm:px-6 lg:px-8">
          <p class="text-sm text-content-subtle mb-10">Last updated: {{ lastUpdated }}</p>

          <p v-if="intro" class="text-lg text-content-muted mb-12">{{ intro }}</p>

          <!-- Contents -->
          <nav aria-label="Contents" class="mb-12 p-6 rounded-card bg-surface ring-1 ring-inset ring-line">
            <h2 class="text-xs font-semibold uppercase tracking-[0.12em] text-content-subtle mb-3">Contents</h2>
            <ol class="space-y-1.5 text-sm">
              <li v-for="(section, i) in sections" :key="section.heading">
                <a
                  :href="`#s-${i + 1}`"
                  class="text-content-muted hover:text-accent-400 transition-colors rounded-control focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-accent-400"
                >
                  {{ i + 1 }}. {{ section.heading }}
                </a>
              </li>
            </ol>
          </nav>

          <div class="space-y-12">
            <section v-for="(section, i) in sections" :key="section.heading" :id="`s-${i + 1}`" class="scroll-mt-24">
              <h2 class="text-xl font-bold text-content mb-4">
                <span class="text-accent-400">{{ i + 1 }}.</span> {{ section.heading }}
              </h2>

              <p
                v-for="para in section.paragraphs"
                :key="para"
                class="text-content-muted mb-4 last:mb-0"
              >{{ para }}</p>

              <ul v-if="section.list && section.list.length" class="mt-4 space-y-2">
                <li
                  v-for="item in section.list"
                  :key="item"
                  class="text-content-muted flex gap-3"
                >
                  <span class="mt-2 h-1 w-1 rounded-full bg-accent-400 shrink-0" aria-hidden="true"></span>
                  <span>{{ item }}</span>
                </li>
              </ul>
            </section>
          </div>

          <p class="mt-14 pt-8 border-t border-line text-sm text-content-subtle">
            Questions about this document? Email
            <a href="mailto:support@aibrainl.ink" class="text-accent-400 hover:text-accent-500 underline underline-offset-2">support@aibrainl.ink</a>.
          </p>
        </div>
      </section>
    </div>
  </AppLayout>
</template>
