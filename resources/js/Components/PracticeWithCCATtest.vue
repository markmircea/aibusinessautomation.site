<template>
    <section id="practice-with-CCATtest" class="mb-12 animate-on-scroll" :class="{ 'animate-fade-in-up': isIntersecting }">
        <h2 class="text-4xl font-bold mb-6 bg-gradient-to-r from-blue-600 to-blue-800 dark:from-blue-400 dark:to-blue-600 bg-clip-text text-transparent">
            Practice CCAT assessments with CCATtest
    </h2>
      <div class="relative overflow-hidden bg-gradient-to-br from-blue-50 to-white dark:from-gray-800 dark:to-gray-900 rounded-2xl shadow-xl p-8">
        <!-- Header Section -->
        <div class="relative z-10">
          <h2 class="text-4xl font-bold mb-2 bg-gradient-to-r from-blue-600 to-blue-800 dark:from-blue-400 dark:to-blue-600 bg-clip-text text-transparent">
          </h2>
          <h3 class="text-2xl font-bold mb-6 text-gray-700 dark:text-gray-300">Comprehensive Test Preparation</h3>
        </div>

        <!-- Features Cards -->
        <div class="grid md:grid-cols-2 gap-6 mb-8">
          <div class="bg-white dark:bg-gray-800 rounded-xl p-6 shadow-md hover:shadow-lg transition duration-300">
            <div class="flex items-start space-x-4">
              <div class="bg-blue-100 dark:bg-blue-900 rounded-lg p-3">
                <svg class="w-6 h-6 text-blue-600 dark:text-blue-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path strokeLinecap="round" strokeLinejoin="round" strokeWidth="2" d="M19 21V5a2 2 0 00-2-2H7a2 2 0 00-2 2v16m14 0h2m-2 0h-5m-9 0H3m2 0h5M9 7h1m-1 4h1m4-4h1m-1 4h1m-5 10v-5a1 1 0 011-1h2a1 1 0 011 1v5m-4 0h4" />
                </svg>
              </div>
              <div>
                <p class="font-bold text-xl mb-2 text-gray-800 dark:text-gray-100">Premium Test Package</p>
                <p class="text-gray-600 dark:text-gray-300">After months of research on popular test providers (including Criteria Corp), CCATtest has designed an aptitude test package.<br><br> Our unique selling point is that these practice questions are comparatively difficult compared to other products on the market. Plus, you'll get the A to Z approach to numerical, verbal and logical reasoning tests with our in-depth study guides into specific assessments.</p>
              </div>
            </div>
          </div>
          <div class="bg-white dark:bg-gray-800 rounded-xl p-6 shadow-md hover:shadow-lg transition duration-300">
            <div class="flex items-start space-x-4">
              <div class="bg-green-100 dark:bg-green-900 rounded-lg p-3">
                <svg class="w-6 h-6 text-green-600 dark:text-green-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path strokeLinecap="round" strokeLinejoin="round" strokeWidth="2" d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z" />
                </svg>
              </div>
              <div>
                <p class="font-bold text-xl mb-2 text-gray-800 dark:text-gray-100">Lifetime Access</p>
                <p class="text-gray-600 dark:text-gray-300">Pay once for unlimited access to our continuously expanding question bank, complete with in-depth study guides for all assessment types.<br><br> What's more, we keep updating the number of questions – you pay once, you'll have lifetime access to the question bank. CCATtest aims to help candidates get through any aptitude tests.</p>
              </div>
            </div>
          </div>
        </div>

        <!-- Free Practice Section -->
        <div class="bg-white dark:bg-gray-800 rounded-xl p-6 shadow-md hover:shadow-lg transition duration-300 border-l-4 border-blue-500 mb-8">
          <div class="flex items-start space-x-4">
            <div class="bg-blue-100 dark:bg-blue-900 rounded-lg p-3">
              <svg class="w-6 h-6 text-blue-600 dark:text-blue-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path strokeLinecap="round" strokeLinejoin="round" strokeWidth="2" d="M12 6v6m0 0v6m0-6h6m-6 0H6" />
              </svg>
            </div>
            <div>
              <h4 class="text-xl font-bold mb-2 text-gray-800 dark:text-gray-100">Try Before You Buy</h4>
              <p class="text-gray-600 dark:text-gray-300">
                Get started with our <a href="/free-practice-test" class="text-blue-600 dark:text-blue-400 hover:underline">free questions</a> to experience the quality and format of our tests firsthand.
              </p>
            </div>
          </div>
        </div>

        <!-- Timing Image Section -->
        <div class="bg-white dark:bg-gray-800 rounded-xl p-6 shadow-md hover:shadow-lg transition duration-300">
          <h4 class="text-xl font-bold mb-4 text-gray-800 dark:text-gray-100">Assessment Timing</h4>
          <LazyImage
            src="/storage/img/1669372162795_ccat_assessments8_1500_x938.png"
            alt="CCAT Assessment Timing"
            :width="1500"
            :height="938"
            class="rounded-lg shadow-md mx-auto mb-4"
          />
          <p class="text-center italic text-gray-600 dark:text-gray-300">Source: CCAT</p>
        </div>
      </div>
    </section>
  </template>

  <script setup>
  import { ref, onMounted } from 'vue';
  import LazyImage from './LazyImage.vue';

  const isIntersecting = ref(false);

  onMounted(() => {
    const observer = new IntersectionObserver(
      ([entry]) => {
        isIntersecting.value = entry.isIntersecting;
      },
      { threshold: 0.1 }
    );

    const section = document.getElementById('practice-with-CCATtest');
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
