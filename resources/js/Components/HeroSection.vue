<script setup>
import { onMounted } from 'vue';
import { gsap } from 'gsap';

onMounted(() => {
  gsap.from('.hero-text', {
    duration: 1,
    y: 30,
    opacity: 0,
    stagger: 0.2,
    ease: 'power2.out'
  });
});
</script>

<template>
  <div class="relative overflow-hidden animated-bg">
    <!-- Animated background elements -->
    <div class="absolute inset-0">
      <div class="absolute inset-0 bg-grid-pattern opacity-10"></div>
      <div class="absolute inset-0 bg-gradient-radial from-blue-500/30 to-transparent"></div>
    </div>

    <div class="relative max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-24 sm:py-32">
      <div class="text-center">
        <h1 class="hero-text text-4xl sm:text-5xl md:text-6xl font-extrabold text-white mb-6">
          Transform Your Business
          <span class="block text-blue-400">With Complete AI Automation</span>
        </h1>
        
        <p class="hero-text mx-auto max-w-2xl text-xl sm:text-2xl text-blue-100 mb-10">
          Streamline operations and boost efficiency with our cutting-edge AI solutions. Any business process you can think of, we can automate it - optimizing your workforce, reducing costs, and improving quality and response times.
        </p>

        <div class="hero-text flex justify-center gap-4">
          <a href="#solutions" class="inline-flex items-center px-6 py-3 border border-transparent text-base font-medium rounded-md text-white bg-blue-600 hover:bg-blue-700 transition-colors duration-200">
            Explore Solutions
            <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 ml-2" viewBox="0 0 20 20" fill="currentColor">
              <path fill-rule="evenodd" d="M10.293 5.293a1 1 0 011.414 0l4 4a1 1 0 010 1.414l-4 4a1 1 0 01-1.414-1.414L12.586 11H5a1 1 0 110-2h7.586l-2.293-2.293a1 1 0 010-1.414z" clip-rule="evenodd" />
            </svg>
          </a>
          <a href="#contact" class="inline-flex items-center px-6 py-3 border border-blue-400 text-base font-medium rounded-md text-blue-100 hover:bg-blue-800/50 transition-colors duration-200">
            Contact Us
          </a>
        </div>

        <!-- Stats -->
        <div class="hero-text mt-16 grid grid-cols-2 gap-8 md:grid-cols-4">
          <div class="text-center">
            <div class="text-3xl font-bold text-white">80%</div>
            <div class="text-sm text-blue-200">Cost Reduction</div>
          </div>
          <div class="text-center">
            <div class="text-3xl font-bold text-white">90%</div>
            <div class="text-sm text-blue-200">Financial Operation Speed</div>
          </div>
          <div class="text-center">
            <div class="text-3xl font-bold text-white">70%</div>
            <div class="text-sm text-blue-200">Process Automation</div>
          </div>
          <div class="text-center">
            <div class="text-3xl font-bold text-white">50%</div>
            <div class="text-sm text-blue-200">Increased Conversion Rate</div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>
.bg-grid-pattern {
  background-image: radial-gradient(circle, #ffffff 1px, transparent 1px);
  background-size: 30px 30px;
  animation: pulse 8s ease-in-out infinite;
}

.bg-gradient-radial {
  background: radial-gradient(circle at center, var(--tw-gradient-from), var(--tw-gradient-to));
  animation: breathe 15s ease-in-out infinite;
}

@keyframes pulse {
  0%, 100% {
    opacity: 0.1;
  }
  50% {
    opacity: 0.25;
  }
}

@keyframes breathe {
  0%, 100% {
    transform: scale(1);
  }
  50% {
    transform: scale(1.05);
  }
}

@keyframes float {
  0%, 100% {
    transform: translateY(0);
  }
  50% {
    transform: translateY(-20px);
  }
}
</style>

<style>
.animated-bg {
  background: linear-gradient(135deg, #1e3a8a, #1e40af, #1e3a8a);
  background-size: 400% 400%;
  animation: gradient 15s ease infinite;
}

.dark .animated-bg {
  background: linear-gradient(135deg, #111827, #1f2937, #111827);
  background-size: 400% 400%;
  animation: gradient 15s ease infinite;
}

@keyframes gradient {
  0% {
    background-position: 0% 50%;
  }
  50% {
    background-position: 100% 50%;
  }
  100% {
    background-position: 0% 50%;
  }
}
</style>
