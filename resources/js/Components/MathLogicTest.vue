<template>
    <section id="math-and-logic-test" class="mb-12 animate-on-scroll" :class="{ '': isIntersecting }">
        <h2 class="text-4xl font-bold mb-6 bg-gradient-to-r from-blue-600 to-blue-800 dark:from-blue-400 dark:to-blue-600 bg-clip-text text-transparent">
            CCAT Math & Logic Test
    </h2>
      <div class="relative overflow-hidden bg-gradient-to-br from-blue-50 to-white dark:from-gray-800 dark:to-gray-900 rounded-2xl shadow-xl p-8">
        <!-- Header Section -->
        <div class="relative z-10">
          <h2 class="text-4xl font-bold mb-2 bg-gradient-to-r from-blue-600 to-blue-800 dark:from-blue-400 dark:to-blue-600 bg-clip-text text-transparent">
          </h2>
          <h3 class="text-2xl font-bold mb-6 text-gray-700 dark:text-gray-300">Overview</h3>
        </div>

        <!-- Introduction Card -->
        <div class="grid md:grid-cols-2 gap-6 mb-8">
          <div class="bg-white dark:bg-gray-800 rounded-xl p-6 shadow-md hover:shadow-lg transition duration-300">
            <div class="flex items-start space-x-4">
              <div class="bg-blue-100 dark:bg-blue-900 rounded-lg p-3">
                <svg class="w-6 h-6 text-blue-600 dark:text-blue-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path strokeLinecap="round" strokeLinejoin="round" strokeWidth="2" d="M9 7h6m0 10v-3m-3 3h.01M9 17h.01M9 14h.01M12 14h.01M15 11h.01M12 11h.01M9 11h.01M7 21h10a2 2 0 002-2V5a2 2 0 00-2-2H7a2 2 0 00-2 2v14a2 2 0 002 2z" />
                </svg>
              </div>
              <div>
                <p class="font-bold text-xl mb-2 text-gray-800 dark:text-gray-100">Test Format</p>
                <p class="text-gray-600 dark:text-gray-300">CCAT math & logic test usually includes <strong>22 questions</strong>, assessing candidates' fundamental algebra skills and the ability to solve word problems.</p>
              </div>
            </div>
          </div>
          <div class="bg-white dark:bg-gray-800 rounded-xl p-6 shadow-md hover:shadow-lg transition duration-300">
            <div class="flex items-start space-x-4">
              <div class="bg-green-100 dark:bg-green-900 rounded-lg p-3">
                <svg class="w-6 h-6 text-green-600 dark:text-green-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path strokeLinecap="round" strokeLinejoin="round" strokeWidth="2" d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z" />
                </svg>
              </div>
              <div>
                <p class="font-bold text-xl mb-2 text-gray-800 dark:text-gray-100">Key Skills Tested</p>
                <p class="text-gray-600 dark:text-gray-300">Questions involve proportions, averages, percentages, graphs, tables, and ratios. NO calculators allowed - mental math skills required.</p>
              </div>
            </div>
          </div>
        </div>

  <!-- Question Types Section -->
<div class="bg-white dark:bg-gray-800 rounded-xl p-6 shadow-md hover:shadow-lg transition duration-300 border-l-4 border-blue-500 mb-8">
  <div class="flex items-center mb-4">
    <div class="bg-blue-100 dark:bg-blue-900 rounded-full p-3 mr-3">
      <svg class="w-6 h-6 text-blue-600 dark:text-blue-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
        <path strokeLinecap="round" strokeLinejoin="round" strokeWidth="2" d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2" />
      </svg>
    </div>
    <h4 class="text-xl font-bold text-gray-800 dark:text-gray-100">Types of Math and Logic Questions</h4>
  </div>
  <ul class="list-disc text-gray-600 dark:text-gray-300 list-inside space-y-1 ml-11">
    <li>Basic Arithmetic</li>
    <li>Algebra</li>
    <li>Word Problems</li>
    <li>Data Interpretation (graphs, tables)</li>
    <li>Pattern Recognition</li>
    <li>Logical Reasoning</li>
  </ul>
</div>

        <!-- Example Questions -->
        <div class="space-y-8">
          <div class="bg-white dark:bg-gray-800 rounded-xl p-6 shadow-md hover:shadow-lg transition duration-300">
            <h4 class="text-xl font-bold mb-4 text-gray-800 dark:text-gray-100">Example Questions</h4>
            <LazyImage
              src="/storage/img/1669372150373_ccat_assessments_2_1500_x751.png"
              alt="CCAT Math & Logic Example 1"
              :width="1500"
              :height="751"
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
                  <p class="text-gray-600 dark:text-gray-300"><strong>Answer: </strong>120</p>
                  <p class="text-gray-600 dark:text-gray-300"><strong>Explanation: </strong>The number of customers the cashier can ring up in eight hours: 15 x 8 = 120.</p>
                </div>
              </div>
            </div>
          </div>

          <div class="bg-white dark:bg-gray-800 rounded-xl p-6 shadow-md hover:shadow-lg transition duration-300">
            <LazyImage
              src="/storage/img/1669372162795_ccat_assessments3_1500_x938.png"
              alt="CCAT Math & Logic Example 2"
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
                  <p class="text-gray-600 dark:text-gray-300"><strong>Answer:</strong> E</p>
                  <p class="text-gray-600 dark:text-gray-300"><strong>Explanation: </strong>The pattern should be an upside-down triangle followed by a triangle. So, the question mark should be replaced by an upside-down triangle.</p>
                </div>
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

    const section = document.getElementById('math-and-logic-test');
    if (section) {
      observer.observe(section);
    }

    return () => observer.disconnect();
  });
  </script>

  <style scoped>

  </style>
