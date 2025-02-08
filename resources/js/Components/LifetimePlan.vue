<template>
  <section id="lifetime-plan" class="mb-12 animate-on-scroll" :class="{ 'animate-fade-in-up': isIntersecting }">
    <h2 class="text-3xl font-bold mb-4 text-gray-800 dark:text-white">Your Lifetime Plan</h2>
    <div class="bg-white dark:bg-gray-800 rounded-lg shadow-lg p-6">
      <p class="mb-4 text-gray-800 dark:text-gray-300">
        <strong>Unlimited Access</strong>
      </p>
      <ul class="list-disc list-inside mb-4 text-gray-800 dark:text-gray-300">
        <li>Full Practice tests (500 Questions) & PDFs</li>
        <li>Verbal practice questions</li>
        <li>Math & Logic practice questions</li>
        <li>Spatial Reasoning practice questions</li>

      </ul>
      <p class="mb-4 text-gray-800 dark:text-gray-300">
        More practice questions are added weekly.
      </p>
      <p class="text-sm text-gray-600 dark:text-gray-400">
        Subscription started: {{ subscriptionStartDate }}
      </p>
    </div>
  </section>
</template>

<script setup>
import { ref, onMounted } from 'vue';

const props = defineProps({
  subscriptionStartDate: String
});

const isIntersecting = ref(false);

onMounted(() => {
  const observer = new IntersectionObserver(
    ([entry]) => {
      isIntersecting.value = entry.isIntersecting;
    },
    { threshold: 0.1 }
  );

  const section = document.getElementById('lifetime-plan');
  if (section) {
    observer.observe(section);
  }

  return () => observer.disconnect();
});
</script>

<style scoped>
.animate-fade-in-up {
  animation: fadeInUp 0.6s ease-out;
}

@keyframes fadeInUp {
  from {
    opacity: 0;
    transform: translateY(20px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}
</style>
