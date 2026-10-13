<script setup>
import { Link } from '@inertiajs/vue3';
import AppLayout from '@/Layouts/AppLayout.vue';
import Icon from '@/Components/Icon.vue';

const props = defineProps({
  status: { type: Number, default: 404 },
});

const copy = {
  404: { title: 'Page not found', body: "That page doesn't exist — it may have moved or never been here." },
  403: { title: 'Not authorised', body: "You don't have access to this page." },
  500: { title: 'Something broke', body: 'Something went wrong on our end. We have been notified.' },
  503: { title: 'Back shortly', body: 'We are performing maintenance. Please try again in a few minutes.' },
};

const current = copy[props.status] ?? copy[404];
</script>

<template>
  <AppLayout>
    <section class="relative flex min-h-[70vh] items-center justify-center bg-ink px-4 py-24">
      <div class="absolute inset-0 error-mesh" aria-hidden="true"></div>

      <div class="relative text-center max-w-xl">
        <p class="text-7xl sm:text-8xl font-extrabold tracking-tight text-accent-400 mb-4">{{ status }}</p>
        <h1 class="text-3xl sm:text-4xl font-bold tracking-tight text-content mb-4">{{ current.title }}</h1>
        <p class="text-lg text-content-muted mb-10">{{ current.body }}</p>

        <div class="flex flex-wrap justify-center gap-4">
          <Link
            :href="route('welcome')"
            class="inline-flex items-center px-7 py-3.5 text-base font-semibold rounded-control text-white bg-accent-500 hover:bg-accent-600 shadow-e2 transition-colors duration-200 focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-accent-400 focus-visible:ring-offset-2 focus-visible:ring-offset-ink"
          >
            Back to home
          </Link>
          <Link
            :href="route('portfolio')"
            class="inline-flex items-center px-7 py-3.5 text-base font-semibold rounded-control text-content border border-line hover:border-accent-400 hover:text-white transition-colors duration-200 focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-accent-400 focus-visible:ring-offset-2 focus-visible:ring-offset-ink"
          >
            See our work
            <Icon name="ArrowRight" class="h-4 w-4 ml-2" />
          </Link>
        </div>
      </div>
    </section>
  </AppLayout>
</template>

<style scoped>
.error-mesh {
  background: radial-gradient(55% 50% at 50% 0%, rgba(91, 108, 255, 0.18) 0%, transparent 70%);
}
</style>
