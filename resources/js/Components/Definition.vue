<template>
  <section id="definition" class="mb-12 animate-on-scroll" :class="{ '': isIntersecting }">
    <h2 class="text-4xl font-bold mb-6 bg-gradient-to-r from-blue-600 to-blue-800 dark:from-blue-400 dark:to-blue-600 bg-clip-text text-transparent">
      What are CCAT assessments?
    </h2>
    <div class="bg-gradient-to-br from-blue-50 to-white dark:from-gray-800 dark:to-gray-900 rounded-2xl shadow-xl p-8">
      <p class="mb-6 text-gray-600 dark:text-gray-300 leading-relaxed">
        <strong class="text-gray-800 dark:text-white text-lg">CCAT – Criteria Cognitive Aptitude Test</strong>
        measures candidates' learning, critical thinking, and problem-solving skills (
        <strong class="text-gray-800 dark:text-white">50 questions</strong> under a time limit of
        <strong class="text-gray-800 dark:text-white">15 minutes</strong>). This test has 3 types of questions:
        <a href="https://CCATtest.com/verbal-reasoning-tests-ultimate-guide"
           class="text-blue-600 dark:text-blue-400 hover:underline transition-colors duration-200">
           <strong>Verbal</strong>
        </a>,
        <a href="https://CCATtest.com/guide-to-numerical-reasoning-tests"
           class="text-blue-600 dark:text-blue-400 hover:underline transition-colors duration-200">
           <strong>Math and Logic</strong>
        </a>, and
        <a href="https://CCATtest.com/what-is-a-spatial-reasoning-test"
           class="text-blue-600 dark:text-blue-400 hover:underline transition-colors duration-200">
           <strong>Spatial Reasoning</strong>
        </a>.
        During the test, English is the only language used, and calculators are NOT allowed. Some leading employers using CCAT in their hiring process include Crossover, Vista Equity, Lambda School, etc.
      </p>

      <p class="mb-8 text-gray-600 dark:text-gray-300 leading-relaxed">
        CCAT is published by
        <a href="https://www.criteriacorp.com/"
           class="text-blue-600 dark:text-blue-400 hover:underline transition-colors duration-200">
           Criteria Corp
        </a>, which is a reliable assessment provider in Los Angeles. Since its establishment in 2016, the company has provided more than 25 million tests across 60 countries.
      </p>

      <div class="bg-white dark:bg-gray-800 rounded-xl shadow-lg p-6 mb-8">
        <LazyImage
          src="/storage/img/1669372150373_ccat_assessments_2_1500_x751.png"
          alt="CCAT Math & Logic Example 1"
          :width="1500"
          :height="751"
          class="rounded-lg shadow-md mx-auto mb-4"
        />
        <p class="text-center italic text-gray-600 dark:text-gray-400">Source: CCAT</p>
      </div>

      <div class="space-y-6">
        <p class="text-gray-600 dark:text-gray-300 leading-relaxed bg-blue-50 dark:bg-blue-900/20 rounded-xl p-6 border-l-4 border-blue-500">
          We will provide you with the tools you need to study and pass the exam! To get hired at Crossover for Work you need to score in the 85 percentile or top 15%. (MINIMUM 35 / 50 CORRECT)
        </p>

        <p class="text-gray-600 dark:text-gray-300 leading-relaxed bg-green-50 dark:bg-green-900/20 rounded-xl p-6 border-l-4 border-green-500">
          Signing up for our paid exam will prepare you for ALL the questions on the test, make a small investment today for a greater future tomorrow.
        </p>

        <p class="text-gray-600 dark:text-gray-300 leading-relaxed bg-purple-50 dark:bg-purple-900/20 rounded-xl p-6 border-l-4 border-purple-500">
          You will gain access to 10 FULL PRACTICE TESTS, as well as thousands of additional questions from each question category (Math/Logic, Verbal, Spatial). The access is a lifetime membership. You will be able to take the 50 question test as many times as you want, unlimited access, each time the test will provide you with different questions of the same type just like what you will experience on crossover.
        </p>
      </div>

      <div class="mt-8 bg-white dark:bg-gray-800 rounded-xl shadow-lg p-6">
        <LazyImage
          src="/storage/img/crossoversteps.png"
          alt="Crossover Steps"
          class="rounded-lg shadow-md mx-auto mb-4"
        />
        <p class="text-center italic text-gray-600 dark:text-gray-400">Source: CCAT</p>
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

  const section = document.getElementById('definition');
  if (section) {
    observer.observe(section);
  }

  return () => observer.disconnect();
});
</script>
<style scoped>

</style>
