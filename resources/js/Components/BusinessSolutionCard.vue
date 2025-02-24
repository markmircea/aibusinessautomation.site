<script setup>
import { Link } from '@inertiajs/vue3';

const props = defineProps({
  title: String,
  focus: String,
  keyPoint: String,
  icon: String,
  routeName: String,
  useCase: {
    type: String,
    default: ''
  },
  timeline: {
    type: String,
    default: '2-4 weeks'
  },
  integrations: {
    type: Array,
    default: () => []
  },
  platforms: {
    type: Array,
    default: () => []
  },
  animationDelay: {
    type: String,
    default: '0'
  }
});
</script>

<template>
  <div 
    class="scale-100 p-6 bg-white dark:bg-gray-800/50 dark:bg-gradient-to-bl from-gray-700/50 via-transparent dark:ring-1 dark:ring-inset dark:ring-white/5 rounded-lg shadow-2xl shadow-gray-500/20 dark:shadow-none flex flex-col"
    :class="[
      'animate-fade-in',
      'motion-safe:hover:scale-[1.01]',
      'transition-all duration-300'
    ]"
    :style="{ animationDelay: animationDelay }"
  >
    <div class="h-16 w-16 bg-blue-50 dark:bg-blue-800/20 flex items-center justify-center rounded-full mb-6">
      <span class="text-3xl" v-html="icon"></span>
    </div>

    <h2 class="text-xl font-bold text-gray-900 dark:text-white mb-2">{{ title }}</h2>
    
    <div class="text-gray-600 dark:text-gray-300 mb-4 space-y-3">
      <div class="mb-2">
        <span class="font-semibold text-blue-600 dark:text-blue-400">Focus:</span> 
        {{ focus }}
      </div>
      <div>
        <span class="font-semibold text-green-600 dark:text-green-400">Key Benefit:</span>
        {{ keyPoint }}
      </div>
      <div v-if="useCase" class="pt-2 border-t border-gray-200 dark:border-gray-700">
        <span class="font-semibold text-purple-600 dark:text-purple-400">Featured Use Case:</span>
        <p class="mt-1 text-sm">{{ useCase }}</p>
      </div>
      <div class="pt-2 border-t border-gray-200 dark:border-gray-700">
        <span class="font-semibold text-indigo-600 dark:text-indigo-400">Key Integrations:</span>
        <div class="mt-1 flex flex-wrap gap-2">
          <span v-for="integration in integrations" :key="integration"
                class="inline-flex items-center px-2 py-1 text-xs font-medium rounded bg-indigo-100 dark:bg-indigo-900 text-indigo-700 dark:text-indigo-300">
            {{ integration }}
          </span>
          <Link :href="route('solutions.ai-integrations')"
                class="inline-flex items-center px-2 py-1 text-xs font-medium rounded bg-green-100 dark:bg-green-900 text-green-700 dark:text-green-300 hover:bg-green-200 dark:hover:bg-green-800 transition-colors duration-200">
            + More
          </Link>
        </div>
      </div>
      <div class="pt-2 border-t border-gray-200 dark:border-gray-700">
        <span class="font-semibold text-teal-600 dark:text-teal-400">Compatible With:</span>
        <div class="mt-1 flex flex-wrap gap-2">
          <span v-for="platform in platforms" :key="platform"
                class="inline-flex items-center px-2 py-1 text-xs font-medium rounded bg-teal-100 dark:bg-teal-900 text-teal-700 dark:text-teal-300">
            {{ platform }}
          </span>
        </div>
      </div>
    </div>

    <div class="mt-auto">
      <Link 
        :href="route('solutions.customer-service')"
        class="inline-flex items-center px-4 py-2 bg-blue-600 dark:bg-blue-700 text-white rounded-md hover:bg-blue-700 dark:hover:bg-blue-800 transition-colors duration-200 w-full justify-center"
      >
        <span class="text-sm font-semibold">Explore Solution</span>
        <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4 ml-1" viewBox="0 0 20 20" fill="currentColor">
          <path fill-rule="evenodd" d="M10.293 5.293a1 1 0 011.414 0l4 4a1 1 0 010 1.414l-4 4a1 1 0 01-1.414-1.414L12.586 11H5a1 1 0 110-2h7.586l-2.293-2.293a1 1 0 010-1.414z" clip-rule="evenodd" />
        </svg>
      </Link>
    </div>
  </div>
</template>

<style scoped>
@keyframes fadeIn {
  from {
    opacity: 0;
    transform: translateY(20px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

.animate-fade-in {
  animation: fadeIn 0.6s ease-out forwards;
  opacity: 0;
}
</style>
