<script setup>
import { Link } from '@inertiajs/vue3';

defineProps({
  title: String,
  focus: String,
  keyPoint: String,
  icon: String,
  routeName: String,
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
    
    <div class="text-gray-600 dark:text-gray-300 mb-4">
      <div class="mb-2">
        <span class="font-semibold text-blue-600 dark:text-blue-400">Focus:</span> 
        {{ focus }}
      </div>
      <div>
        <span class="font-semibold text-green-600 dark:text-green-400">Key Benefit:</span>
        {{ keyPoint }}
      </div>
    </div>

    <Link 
      :href="route(routeName)"
      class="mt-auto flex items-center text-blue-600 dark:text-blue-400 hover:text-blue-800 dark:hover:text-blue-300 transition-colors duration-200"
    >
      <span class="text-sm font-semibold">Learn more</span>
      <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4 ml-1" viewBox="0 0 20 20" fill="currentColor">
        <path fill-rule="evenodd" d="M10.293 5.293a1 1 0 011.414 0l4 4a1 1 0 010 1.414l-4 4a1 1 0 01-1.414-1.414L12.586 11H5a1 1 0 110-2h7.586l-2.293-2.293a1 1 0 010-1.414z" clip-rule="evenodd" />
      </svg>
    </Link>
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
