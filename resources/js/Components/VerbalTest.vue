<template>
    <section id="verbal-test" class="mb-12 animate-on-scroll" :class="{ '': isIntersecting }">
        <h2 class="text-4xl font-bold mb-6 bg-gradient-to-r from-blue-600 to-blue-800 dark:from-blue-400 dark:to-blue-600 bg-clip-text text-transparent">
      CCAT Verbal Test
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
                  <path strokeLinecap="round" strokeLinejoin="round" strokeWidth="2" d="M12 6V4m0 2a2 2 0 100 4m0-4a2 2 0 110 4m-6 8a2 2 0 100-4m0 4a2 2 0 110-4m0 4v2m0-6V4m6 6v10m6-2a2 2 0 100-4m0 4a2 2 0 110-4m0 4v2m0-6V4" />
                </svg>
              </div>
              <div>
                <p class="font-bold text-xl mb-2 text-gray-800 dark:text-gray-100">Test Format</p>
                <p class="text-gray-600 dark:text-gray-300">CCAT verbal test typically contains <strong>17 questions</strong>, challenging candidates to identify word meanings, relationships, and contextual usage.</p>
              </div>
            </div>
          </div>
          <div class="bg-white dark:bg-gray-800 rounded-xl p-6 shadow-md hover:shadow-lg transition duration-300">
            <div class="flex items-start space-x-4">
              <div class="bg-green-100 dark:bg-green-900 rounded-lg p-3">
                <svg class="w-6 h-6 text-green-600 dark:text-green-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path strokeLinecap="round" strokeLinejoin="round" strokeWidth="2" d="M3 10h10a8 8 0 018 8v2M3 10l6 6m-6-6l6-6" />
                </svg>
              </div>
              <div>
                <p class="font-bold text-xl mb-2 text-gray-800 dark:text-gray-100">Important Note</p>
                <p class="text-gray-600 dark:text-gray-300">For both native and non-native English speakers, it's necessary to get familiar with different question types in CCAT. If English is not your first language, your English should be properly improved to pass this verbal test.</p>
              </div>
            </div>
          </div>
        </div>

      <!-- Question Types Section -->
<div class="bg-white dark:bg-gray-800 rounded-xl p-6 shadow-md hover:shadow-lg transition duration-300 border-l-4 border-blue-500 mb-8">
  <div class="flex items-center mb-4">
    <div class="bg-blue-100 dark:bg-blue-900 rounded-full p-3 mr-3">
      <svg class="w-6 h-6 text-blue-600 dark:text-blue-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
        <path strokeLinecap="round" strokeLinejoin="round" strokeWidth="2" d="M4 6h16M4 10h16M4 14h16M4 18h16" />
      </svg>
    </div>
    <h4 class="text-xl font-bold text-gray-800 dark:text-gray-100">Types of Verbal Test Questions</h4>
  </div>
  <ul class="list-disc text-gray-600 dark:text-gray-300 list-inside space-y-1 ml-11">
    <li>Synonyms and Antonyms</li>
    <li>Analogies</li>
    <li>Sentence Completion</li>
    <li>Reading Comprehension</li>
  </ul>
</div>

        <!-- Example Questions -->
        <div class="space-y-8">
          <div class="bg-white dark:bg-gray-800 rounded-xl p-6 shadow-md hover:shadow-lg transition duration-300">
            <h4 class="text-xl font-bold mb-4 text-gray-800 dark:text-gray-100">Example 1: Word Relationships</h4>
            <LazyImage
              src="/storage/img/1669372162795_ccat_assessments4_1500_x938.png"
              alt="CCAT Verbal Example 1"
              :width="1500"
              :height="938"
              class="rounded-lg shadow-md mx-auto mb-4"
            />
            <p class="text-center mb-4 text-gray-600 dark:text-gray-300">Source: CCAT</p>

            <div class="bg-blue-50 dark:bg-blue-900/20 rounded-xl p-6 mt-4">
              <div class="flex items-start space-x-4">
                <div class="bg-blue-100 dark:bg-blue-900 rounded-lg p-2">
                  <svg class="w-5 h-5 text-blue-600 dark:text-blue-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path strokeLinecap="round" strokeLinejoin="round" strokeWidth="2" d="M13 16h-1v-4h-1m1-4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z" />
                  </svg>
                </div>
                <div>
                  <p class="font-bold mb-2 text-gray-800 dark:text-gray-100">Solution</p>
                  <p class="text-gray-600 dark:text-gray-300"><strong>Answer:</strong> ESTEEMED is to SEEDY</p>
                  <p class="text-gray-600 dark:text-gray-300"><strong>Explanation:</strong> The relationship between DELUSIONAL and GROUNDED is antonym because they have opposite meanings. Similarly, ESTEEMED (respected and admired) is opposite to SEEDY (bad and terrible).</p>
                </div>
              </div>
            </div>
          </div>

          <div class="bg-white dark:bg-gray-800 rounded-xl p-6 shadow-md hover:shadow-lg transition duration-300">
            <h4 class="text-xl font-bold mb-4 text-gray-800 dark:text-gray-100">Example 2: Antonyms</h4>
            <LazyImage
              src="/storage/img/1669372162795_ccat_assessments5_1500_x938.png"
              alt="CCAT Verbal Example 2"
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
                  <p class="text-gray-600 dark:text-gray-300"><strong>Answer:</strong> repulsion</p>
                  <p class="text-gray-600 dark:text-gray-300"><strong>Explanation:</strong> "repulsion" means pushing each other away, while "allure" means being attractive.</p>
                </div>
              </div>
            </div>
          </div>

          <div class="bg-white dark:bg-gray-800 rounded-xl p-6 shadow-md hover:shadow-lg transition duration-300">
            <h4 class="text-xl font-bold mb-4 text-gray-800 dark:text-gray-100">Example 3: Word Pairs</h4>
            <LazyImage
              src="/storage/img/1669372162795_ccat_assessments6_1500_x938.png"
              alt="CCAT Verbal Example 3"
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
                  <p class="text-gray-600 dark:text-gray-300"><strong>Answer:</strong> supercilious .. insolence</p>
                  <p class="text-gray-600 dark:text-gray-300"><strong>Explanation:</strong> "supercilious" means showing other people that you're better than them; "insolence" means showing a lack of respect for other people.</p>
                </div>
              </div>
            </div>
          </div>

          <!-- Resource Link Card -->
          <div class="bg-blue-50 dark:bg-blue-900/20 rounded-xl p-6 border-l-4 border-blue-500">
            <div class="flex items-start space-x-4">
              <div class="bg-blue-100 dark:bg-blue-900 rounded-lg p-3">
                <svg class="w-6 h-6 text-blue-600 dark:text-blue-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path strokeLinecap="round" strokeLinejoin="round" strokeWidth="2" d="M13 10V3L4 14h7v7l9-11h-7z" />
                </svg>
              </div>
              <div>
                <p class="text-gray-700 dark:text-gray-300">
                  Ready to practice? Try our <a href="https:/CCATtest.com/verbal-test" class="text-blue-600 dark:text-blue-400 hover:underline font-semibold">verbal practice test</a> which includes similar question types!
                </p>
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

    const section = document.getElementById('verbal-test');
    if (section) {
      observer.observe(section);
    }

    return () => observer.disconnect();
  });
  </script>

  <style scoped>

  </style>
