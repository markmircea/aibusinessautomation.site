<template>
  <section id="companies-using-ccat" class="mb-12 animate-on-scroll" :class="{ 'animate-fade-in-up': isIntersecting }">
    <h2 class="text-4xl font-bold mb-6 bg-gradient-to-r from-blue-600 to-blue-800 dark:from-blue-400 dark:to-blue-600 bg-clip-text text-transparent">
        Companies Using CCAT
    </h2>
    <div class="relative overflow-hidden bg-gradient-to-br from-blue-50 to-white dark:from-gray-800 dark:to-gray-900 rounded-2xl shadow-xl p-8">
      <!-- Header Section -->
      <div class="relative z-10">
        <h2 class="text-4xl font-bold mb-2 bg-gradient-to-r from-blue-600 to-blue-800 dark:from-blue-400 dark:to-blue-600 bg-clip-text text-transparent">
        </h2>
        <h3 class="text-2xl font-bold mb-6 text-gray-700 dark:text-gray-300">Industry Leaders Trust CCAT</h3>
      </div>

      <!-- Introduction Card -->
      <div class="bg-white dark:bg-gray-800 rounded-xl p-6 shadow-md hover:shadow-lg transition duration-300 mb-8">
        <div class="flex items-start space-x-4">
          <div class="bg-blue-100 dark:bg-blue-900 rounded-lg p-3">
            <svg class="w-6 h-6 text-blue-600 dark:text-blue-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path strokeLinecap="round" strokeLinejoin="round" strokeWidth="2" d="M19 21V5a2 2 0 00-2-2H7a2 2 0 00-2 2v16m14 0h2m-2 0h-5m-9 0H3m2 0h5M9 7h1m-1 4h1m4-4h1m-1 4h1m-5 10v-5a1 1 0 011-1h2a1 1 0 011 1v5m-4 0h4" />
            </svg>
          </div>
          <div>
            <p class="text-gray-600 dark:text-gray-300">
              CCAT assessments are trusted by hundreds of employers around the world and used for high-level positions in technology, real estate, banking, and even nursing.
            </p>
          </div>
        </div>
      </div>

      <!-- Companies List -->
      <div class="bg-white dark:bg-gray-800 rounded-xl p-6 shadow-md hover:shadow-lg transition duration-300">
        <ul class="grid grid-cols-1 md:grid-cols-2 gap-3 text-gray-700 dark:text-gray-300">
          <li class="flex items-center space-x-2">
            <svg class="w-4 h-4 text-blue-600 dark:text-blue-400 flex-shrink-0" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path strokeLinecap="round" strokeLinejoin="round" strokeWidth="2" d="M9 12l2 2 4-4" />
            </svg>
            <span>Crossover</span>
          </li>
          <li class="flex items-center space-x-2">
            <svg class="w-4 h-4 text-blue-600 dark:text-blue-400 flex-shrink-0" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path strokeLinecap="round" strokeLinejoin="round" strokeWidth="2" d="M9 12l2 2 4-4" />
            </svg>
            <span>Lambda School</span>
          </li>
          <li class="flex items-center space-x-2">
            <svg class="w-4 h-4 text-blue-600 dark:text-blue-400 flex-shrink-0" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path strokeLinecap="round" strokeLinejoin="round" strokeWidth="2" d="M9 12l2 2 4-4" />
            </svg>
            <span>Equity Vista</span>
          </li>
          <li class="flex items-center space-x-2">
            <svg class="w-4 h-4 text-blue-600 dark:text-blue-400 flex-shrink-0" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path strokeLinecap="round" strokeLinejoin="round" strokeWidth="2" d="M9 12l2 2 4-4" />
            </svg>
            <span>Hirebridge</span>
          </li>
          <li class="flex items-center space-x-2">
            <svg class="w-4 h-4 text-blue-600 dark:text-blue-400 flex-shrink-0" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path strokeLinecap="round" strokeLinejoin="round" strokeWidth="2" d="M9 12l2 2 4-4" />
            </svg>
            <span>EAB</span>
          </li>
          <li class="flex items-center space-x-2">
            <svg class="w-4 h-4 text-blue-600 dark:text-blue-400 flex-shrink-0" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path strokeLinecap="round" strokeLinejoin="round" strokeWidth="2" d="M9 12l2 2 4-4" />
            </svg>
            <span>Cvent</span>
          </li>
          <li class="flex items-center space-x-2">
            <svg class="w-4 h-4 text-blue-600 dark:text-blue-400 flex-shrink-0" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path strokeLinecap="round" strokeLinejoin="round" strokeWidth="2" d="M9 12l2 2 4-4" />
            </svg>
            <span>Apteam</span>
          </li>
          <li class="flex items-center space-x-2">
            <svg class="w-4 h-4 text-blue-600 dark:text-blue-400 flex-shrink-0" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path strokeLinecap="round" strokeLinejoin="round" strokeWidth="2" d="M9 12l2 2 4-4" />
            </svg>
            <span>Finastra</span>
          </li>
          <li class="flex items-center space-x-2">
            <svg class="w-4 h-4 text-blue-600 dark:text-blue-400 flex-shrink-0" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path strokeLinecap="round" strokeLinejoin="round" strokeWidth="2" d="M9 12l2 2 4-4" />
            </svg>
            <span>Tibco</span>
          </li>
          <li class="flex items-center space-x-2">
            <svg class="w-4 h-4 text-blue-600 dark:text-blue-400 flex-shrink-0" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path strokeLinecap="round" strokeLinejoin="round" strokeWidth="2" d="M9 12l2 2 4-4" />
            </svg>
            <span>Powerschool</span>
          </li>
          <li class="flex items-center space-x-2">
            <svg class="w-4 h-4 text-blue-600 dark:text-blue-400 flex-shrink-0" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path strokeLinecap="round" strokeLinejoin="round" strokeWidth="2" d="M9 12l2 2 4-4" />
            </svg>
            <span>Infoblox</span>
          </li>
          <li class="flex items-center space-x-2">
            <svg class="w-4 h-4 text-blue-600 dark:text-blue-400 flex-shrink-0" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path strokeLinecap="round" strokeLinejoin="round" strokeWidth="2" d="M9 12l2 2 4-4" />
            </svg>
            <span>ICIMS/ Mindbody</span>
          </li>
          <li class="flex items-center space-x-2">
            <svg class="w-4 h-4 text-blue-600 dark:text-blue-400 flex-shrink-0" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path strokeLinecap="round" strokeLinejoin="round" strokeWidth="2" d="M9 12l2 2 4-4" />
            </svg>
            <span>Smuckers</span>
          </li>
          <li class="flex items-center space-x-2">
            <svg class="w-4 h-4 text-blue-600 dark:text-blue-400 flex-shrink-0" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path strokeLinecap="round" strokeLinejoin="round" strokeWidth="2" d="M9 12l2 2 4-4" />
            </svg>
            <span>Beachbody</span>
          </li>
        </ul>

      </div>
        <!-- Footer Note -->
        <div class="mt-8 bg-blue-50 dark:bg-blue-900/20 rounded-xl p-6 border-l-4 border-blue-500">
          <div class="flex items-start space-x-4">
            <div class="bg-blue-100 dark:bg-blue-900 rounded-lg p-2">
              <svg class="w-5 h-5 text-blue-600 dark:text-blue-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path strokeLinecap="round" strokeLinejoin="round" strokeWidth="2" d="M13 16h-1v-4h-1m1-4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z" />
              </svg>
            </div>
            <p class="text-gray-600 dark:text-gray-300">
              This is a partial list of companies that use CCAT assessments in their hiring process. Many other organizations also rely on CCAT for their recruitment needs.
            </p>
          </div>
        </div>
    </div>
  </section>
</template>

<script setup>
import { ref, onMounted } from 'vue';

const isIntersecting = ref(false);

onMounted(() => {
  const observer = new IntersectionObserver(
    ([entry]) => {
      isIntersecting.value = entry.isIntersecting;
    },
    { threshold: 0.1 }
  );

  const section = document.getElementById('companies-using-ccat');
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
