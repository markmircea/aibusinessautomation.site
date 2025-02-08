<template>
    <section id="spatial-reasoning-test" class="mb-12 animate-on-scroll" :class="{ '': isIntersecting }">
        <h2 class="text-4xl font-bold mb-6 bg-gradient-to-r from-blue-600 to-blue-800 dark:from-blue-400 dark:to-blue-600 bg-clip-text text-transparent">
            CCAT Spatial Reasoning Test
    </h2>
      <div class="relative overflow-hidden bg-gradient-to-br from-blue-50 to-white dark:from-gray-800 dark:to-gray-900 rounded-2xl shadow-xl p-8">
        <!-- Header Section -->
        <div class="relative z-10">
          <h2 class="text-4xl font-bold mb-2 bg-gradient-to-r from-blue-600 to-blue-800 dark:from-blue-400 dark:to-blue-600 bg-clip-text text-transparent">
          </h2>
          <h3 class="text-2xl font-bold mb-6 text-gray-700 dark:text-gray-300">Overview</h3>
        </div>

        <!-- Introduction Cards -->
        <div class="grid md:grid-cols-2 gap-6 mb-8">
          <div class="bg-white dark:bg-gray-800 rounded-xl p-6 shadow-md hover:shadow-lg transition duration-300">
            <div class="flex items-start space-x-4">
              <div class="bg-blue-100 dark:bg-blue-900 rounded-lg p-3">
                <svg class="w-6 h-6 text-blue-600 dark:text-blue-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path strokeLinecap="round" strokeLinejoin="round" strokeWidth="2" d="M14 10l-2 1m0 0l-2-1m2 1v2.5M20 7l-2 1m2-1l-2-1m2 1v2.5M14 4l-2-1-2 1M4 7l2-1M4 7l2 1M4 7v2.5M12 21l-2-1m2 1l2-1m-2 1v-2.5M6 18l-2-1v-2.5M18 18l2-1v-2.5" />
                </svg>
              </div>
              <div>
                <p class="font-bold text-xl mb-2 text-gray-800 dark:text-gray-100">Test Format</p>
                <p class="text-gray-600 dark:text-gray-300">CCAT spatial tests typically include <strong>11 questions</strong>, requiring you to flip or rotate objects in your head, spot patterns and find the odd one out.</p>
              </div>
            </div>
          </div>
          <div class="bg-white dark:bg-gray-800 rounded-xl p-6 shadow-md hover:shadow-lg transition duration-300">
            <div class="flex items-start space-x-4">
              <div class="bg-green-100 dark:bg-green-900 rounded-lg p-3">
                <svg class="w-6 h-6 text-green-600 dark:text-green-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path strokeLinecap="round" strokeLinejoin="round" strokeWidth="2" d="M9 12l2 2 4-4M7.835 4.697a3.42 3.42 0 001.946-.806 3.42 3.42 0 014.438 0 3.42 3.42 0 001.946.806 3.42 3.42 0 013.138 3.138 3.42 3.42 0 00.806 1.946 3.42 3.42 0 010 4.438 3.42 3.42 0 00-.806 1.946 3.42 3.42 0 01-3.138 3.138 3.42 3.42 0 00-1.946.806 3.42 3.42 0 01-4.438 0 3.42 3.42 0 00-1.946-.806 3.42 3.42 0 01-3.138-3.138 3.42 3.42 0 00-.806-1.946 3.42 3.42 0 010-4.438 3.42 3.42 0 00.806-1.946 3.42 3.42 0 013.138-3.138z" />
                </svg>
              </div>
              <div>
                <p class="font-bold text-xl mb-2 text-gray-800 dark:text-gray-100">Skills Measured</p>
                <p class="text-gray-600 dark:text-gray-300">These spatial reasoning questions measure your innate aptitude and the ability to learn, solve problems, and leverage new information properly.</p>
              </div>
            </div>
          </div>
        </div>

        <!-- Question Types Section -->
<!-- Question Types Section -->
<div class="bg-white dark:bg-gray-800 rounded-xl p-6 shadow-md hover:shadow-lg transition duration-300 border-l-4 border-blue-500 mb-8">
  <div class="flex items-center mb-4">
    <div class="bg-blue-100 dark:bg-blue-900 rounded-full p-3 mr-3">
      <svg class="w-6 h-6 text-blue-600 dark:text-blue-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
        <path strokeLinecap="round" strokeLinejoin="round" strokeWidth="2" d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2" />
      </svg>
    </div>
    <h4 class="text-xl font-bold text-gray-800 dark:text-gray-100">Types of Spatial Reasoning Questions</h4>
  </div>
  <ul class="list-disc text-gray-600 dark:text-gray-300 list-inside space-y-1 ml-11">
    <li>Mental Rotation</li>
    <li>Mirror Images</li>
    <li>Paper Folding</li>
    <li>Pattern Recognition</li>
    <li>Spatial Visualization</li>
    <li>Block Counting</li>
  </ul>
</div>

        <!-- Example Question -->
        <div class="bg-white dark:bg-gray-800 rounded-xl p-6 shadow-md hover:shadow-lg transition duration-300">
          <h4 class="text-xl font-bold mb-4 text-gray-800 dark:text-gray-100">Example Question</h4>
          <LazyImage
            src="/storage/img/1669372162795_ccat_assessments7_1500_x938.png"
            alt="CCAT Spatial Reasoning Example"
            :width="1500"
            :height="938"
            class="rounded-lg shadow-md mx-auto mb-4"
          />
          <p class="text-center italic mb-4 text-gray-600 dark:text-gray-300">Source: CCAT</p>

          <div class="bg-blue-50 dark:bg-blue-900/20 rounded-xl p-6 mt-4">
            <div class="flex items-start space-x-4">
              <div class="bg-blue-100 dark:bg-blue-900 rounded-lg p-2">
                <svg class="w-5 h-5 text-blue-600 dark:text-blue-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path strokeLinecap="round" strokeLinejoin="round" strokeWidth="2" d="M13 16h-1v-4h-1m1-4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z" />
                </svg>
              </div>
              <div>
                <p class="font-bold mb-2 text-gray-800 dark:text-gray-100">Solution</p>
                <p class="text-gray-600 dark:text-gray-300"><strong>Answer:</strong> C</p>
                <p class="text-gray-600 dark:text-gray-300"><strong>Explanation:</strong> All four options A, B, D, and E have a quadrangle in the center. Only option C contains a square in its center. So, the one that does not belong is option C.</p>
              </div>
            </div>
          </div>
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

    const section = document.getElementById('spatial-reasoning-test');
    if (section) {
      observer.observe(section);
    }

    return () => observer.disconnect();
  });
  </script>

  <style scoped>

  </style>
