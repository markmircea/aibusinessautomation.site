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
          Transform Your Business with
          <span class="block text-blue-400">Custom AI Automation</span>
        </h1>
        
        <p class="hero-text mx-auto max-w-2xl text-xl sm:text-2xl text-blue-100 mb-6">
          Get personalized AI solutions with dedicated project managers and development teams for your unique business needs. We transform any business process into an efficient, automated workflow.
        </p>

        <p class="hero-text mx-auto max-w-2xl text-lg text-blue-200 mb-6">
          Your journey includes a dedicated project manager, custom-built solutions, and continuous support throughout our collaboration.
        </p>

        <div class="hero-text mx-auto max-w-3xl text-center mb-10">
          <p class="text-lg text-blue-200 mb-4">
            Seamlessly integrate with your existing tools or let us build custom integrations:
          </p>
          <div class="flex flex-wrap justify-center gap-4 text-sm">
            <span class="px-3 py-1 bg-blue-900/30 rounded-full text-blue-100">AWS</span>
            <span class="px-3 py-1 bg-blue-900/30 rounded-full text-blue-100">Salesforce</span>
            <span class="px-3 py-1 bg-blue-900/30 rounded-full text-blue-100">Zendesk</span>
            <span class="px-3 py-1 bg-blue-900/30 rounded-full text-blue-100">Microsoft Teams</span>
            <span class="px-3 py-1 bg-blue-900/30 rounded-full text-blue-100">HubSpot</span>
            <span class="px-3 py-1 bg-green-900/30 rounded-full text-green-100">+ Custom Integrations</span>
          </div>
        </div>

        <div class="hero-text flex flex-wrap justify-center gap-4">
          <a href="#solutions" class="inline-flex items-center px-6 py-3 border border-transparent text-base font-medium rounded-md text-white bg-blue-600 hover:bg-blue-700 transition-colors duration-200">
            Explore Solutions
            <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 ml-2" viewBox="0 0 20 20" fill="currentColor">
              <path fill-rule="evenodd" d="M10.293 5.293a1 1 0 011.414 0l4 4a1 1 0 010 1.414l-4 4a1 1 0 01-1.414-1.414L12.586 11H5a1 1 0 110-2h7.586l-2.293-2.293a1 1 0 010-1.414z" clip-rule="evenodd" />
            </svg>
          </a>
          <a href="#contact" class="inline-flex items-center px-6 py-3 border border-blue-400 text-base font-medium rounded-md text-blue-100 hover:bg-blue-800/50 transition-colors duration-200">
            Contact Us
          </a>
          <a href="#contact" class="inline-flex items-center px-6 py-3 border border-transparent text-base font-medium rounded-md text-white bg-green-600 hover:bg-green-700 transition-colors duration-200">
            Book a Custom Demo
            <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 ml-2" viewBox="0 0 20 20" fill="currentColor">
              <path d="M10 12a2 2 0 100-4 2 2 0 000 4z" />
              <path fill-rule="evenodd" d="M.458 10C1.732 5.943 5.522 3 10 3s8.268 2.943 9.542 7c-1.274 4.057-5.064 7-9.542 7S1.732 14.057.458 10zM14 10a4 4 0 11-8 0 4 4 0 018 0z" clip-rule="evenodd" />
            </svg>
          </a>
        </div>

        <!-- Stats -->
        <div class="hero-text mt-16 grid grid-cols-2 gap-8 md:grid-cols-4">
          <div class="text-center transform hover:scale-105 transition-transform duration-300">
            <div class="text-3xl font-bold text-white">24/7</div>
            <div class="text-sm text-blue-200">Automated Operations</div>
          </div>
          <div class="text-center transform hover:scale-105 transition-transform duration-300">
            <div class="text-3xl font-bold text-white">100%</div>
            <div class="text-sm text-blue-200">Custom Solutions</div>
          </div>
          <div class="text-center transform hover:scale-105 transition-transform duration-300">
            <div class="text-3xl font-bold text-white">&lt;2wk</div>
            <div class="text-sm text-blue-200">Implementation Time</div>
          </div>
          <div class="text-center transform hover:scale-105 transition-transform duration-300">
            <div class="text-3xl font-bold text-white">80%</div>
            <div class="text-sm text-blue-200">Average Cost Savings</div>
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
