<template>
    <section id="upgrade-account" class="px-4 md:px-0 mb-12" :class="{ 'opacity-100 translate-y-0': isIntersecting }">
      <div class="relative overflow-hidden bg-gradient-to-br from-blue-600 via-blue-700 to-indigo-800 rounded-3xl shadow-2xl">
        <!-- Decorative backgrounds -->
        <div class="absolute inset-0 bg-[radial-gradient(circle_at_30%_-20%,rgba(255,255,255,0.2),transparent)]"></div>
        <div class="absolute top-0 right-0 w-48 md:w-96 h-48 md:h-96 bg-yellow-300/30 rounded-full blur-3xl transform translate-x-1/3 -translate-y-1/2"></div>
        <div class="absolute bottom-0 left-0 w-48 md:w-96 h-48 md:h-96 bg-pink-400/20 rounded-full blur-3xl transform -translate-x-1/2 translate-y-1/2"></div>

        <div class="relative p-4 sm:p-6 md:p-8 lg:p-12">
          <!-- Header -->
          <div class="max-w-3xl">
            <h1 class="text-3xl sm:text-4xl md:text-5xl font-bold text-white mb-4 md:mb-6 [text-wrap:balance]">
              <span class="inline-block border-b-4 border-yellow-400 pb-2">
                Checkout what we offer!
              </span>
            </h1>

            <p class="text-lg sm:text-xl md:text-2xl text-white/90 mb-6 md:mb-8 leading-relaxed">
              Supercharge your CCAT preparation with unlimited lifetime access to all our practice tests and questions!
            </p>
          </div>

          <!-- Features -->
          <div class="grid grid-cols-1 md:grid-cols-2 gap-4 md:gap-6 mb-8 md:mb-12">
            <div
              v-for="(feature, index) in features"
              :key="index"
              class="flex items-start space-x-3 md:space-x-4 p-3 md:p-4 bg-white/10 backdrop-blur-sm rounded-xl md:rounded-2xl border border-white/10 hover:bg-white/20 transition-colors duration-300"
            >
              <div class="flex-shrink-0 w-8 md:w-10 h-8 md:h-10 flex items-center justify-center rounded-lg md:rounded-xl bg-green-400/20">
                <svg class="h-5 w-5 md:h-6 md:w-6 text-green-400" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z" />
                </svg>
              </div>
              <span class="text-base md:text-lg text-white/90">{{ feature }}</span>
            </div>
          </div>

          <!-- Success Rate -->
          <div class="mb-6 md:mb-8 transform hover:scale-105 transition-transform duration-300">
            <div class="bg-white/10 backdrop-blur-sm rounded-xl md:rounded-2xl p-4 md:p-6 border border-white/10">
              <p class="text-xl sm:text-2xl md:text-3xl font-bold text-white text-center">
                <span class="text-yellow-300">98%</span> OF OUR USERS REPORTED PASSING THEIR EXAMS USING OUR PREP SOLUTION
              </p>
            </div>
          </div>

          <!-- Latest Version -->
          <div class="mb-6 md:mb-8">
            <p class="text-lg md:text-xl text-white/90 text-center font-medium">
              LATEST VERSION CCAT <strong class="text-pink-300">{{ currentMonthYear }}</strong> EXAMS!
            </p>
          </div>

          <!-- CTA Button -->
          <div class="text-center">
            <Link
              :href="route('upgrade.account')"
              class="group inline-flex items-center px-6 md:px-8 py-3 md:py-4 text-base md:text-lg font-semibold rounded-xl md:rounded-2xl bg-white text-blue-700 hover:bg-blue-50 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-blue-500 transition-all duration-300 transform hover:-translate-y-1 hover:shadow-xl"
            >
              Upgrade Now
              <svg
                class="ml-2 md:ml-3 -mr-1 w-5 h-5 md:w-6 md:h-6 transition-transform duration-300 group-hover:translate-x-2"
                fill="currentColor"
                viewBox="0 0 20 20"
              >
                <path
                  fill-rule="evenodd"
                  d="M10.293 3.293a1 1 0 011.414 0l6 6a1 1 0 010 1.414l-6 6a1 1 0 01-1.414-1.414L14.586 11H3a1 1 0 110-2h11.586l-4.293-4.293a1 1 0 010-1.414z"
                  clip-rule="evenodd"
                />
              </svg>
            </Link>
          </div>
        </div>
      </div>
    </section>
  </template>

  <script setup>
  import { ref, onMounted } from 'vue';
  import { Link } from '@inertiajs/vue3';

  const isIntersecting = ref(false);
  const currentMonthYear = ref("");

  const features = [
    "10 Full Practice tests with timers (500 Questions, Answers and Explanations)",
    "10 Additional Full PDF files with Questions and Answers (500 Questions and Answers)",
    "1000+ Verbal practice questions with AI assisted explanations",
    "1000+ Math & Logic practice questions with AI assisted explanations",
    "1000+ Spatial Reasoning practice questions with AI assisted explanations",
    "Detailed Explanations for ALL Questions, (if the answer you selected is incorrect, the AI model will explain to you why its incorrect)",
    "AI Powered Tutoring",
    "Original Tests",
    "Same Practice Conditions",
    "Weekly updates with new questions",
    "24/7 Support via E-mail or Chat!",
  ];

  onMounted(() => {
    // Set current month and year
    const monthNames = [
      "January", "February", "March", "April", "May", "June",
      "July", "August", "September", "October", "November", "December"
    ];
    const now = new Date();
    const month = monthNames[now.getMonth()];
    const year = now.getFullYear();
    currentMonthYear.value = `${month.toUpperCase()} ${year}`;

    // Set up intersection observer
    const observer = new IntersectionObserver(
      ([entry]) => {
        isIntersecting.value = entry.isIntersecting;
      },
      { threshold: 0.1 }
    );

    const section = document.getElementById('upgrade-account');
    if (section) {
      observer.observe(section);
    }

    return () => observer.disconnect();
  });
  </script>

  <style scoped>
  section {
    opacity: 0;
    transform: translateY(20px);
    transition: all 0.6s cubic-bezier(0.4, 0, 0.2, 1);
  }

  .opacity-100 {
    opacity: 1;
    transform: translateY(0);
  }

  @keyframes float {
    0%, 100% {
      transform: translateY(0);
    }
    50% {
      transform: translateY(-10px);
    }
  }

  @keyframes pulse {
    0%, 100% {
      opacity: 0.2;
    }
    50% {
      opacity: 0.5;
    }
  }
  </style>
