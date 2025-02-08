<!--
<template>
    <button
      @click="toggleDarkMode"
      class="fixed bottom-4 right-4 p-2 rounded-full bg-gray-200 dark:bg-gray-700 text-gray-800 dark:text-gray-200 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-offset-gray-100 focus:ring-blue-500"
      aria-label="Toggle dark mode"
    >
      <svg
        v-if="isDarkMode"
        xmlns="http://www.w3.org/2000/svg"
        class="h-6 w-6"
        fill="none"
        viewBox="0 0 24 24"
        stroke="currentColor"
      >
        <path
          stroke-linecap="round"
          stroke-linejoin="round"
          stroke-width="2"
          d="M12 3v1m0 16v1m9-9h-1M4 12H3m15.364 6.364l-.707-.707M6.343 6.343l-.707-.707m12.728 0l-.707.707M6.343 17.657l-.707.707M16 12a4 4 0 11-8 0 4 4 0 018 0z"
        />
      </svg>
      <svg
        v-else
        xmlns="http://www.w3.org/2000/svg"
        class="h-6 w-6"
        fill="none"
        viewBox="0 0 24 24"
        stroke="currentColor"
      >
        <path
          stroke-linecap="round"
          stroke-linejoin="round"
          stroke-width="2"
          d="M20.354 15.354A9 9 0 018.646 3.646 9.003 9.003 0 0012 21a9.003 9.003 0 008.354-5.646z"
        />
      </svg>
    </button>
  </template>
-->
  <script setup>
  import { ref, onMounted, watch } from 'vue';

  const isDarkMode = ref(true);

  const toggleDarkMode = () => {
    isDarkMode.value = !isDarkMode.value;
    updateDarkMode();
  };

  const updateDarkMode = () => {
    if (isDarkMode.value) {
      document.documentElement.classList.add('dark');
      localStorage.setItem('darkMode', 'true');
    } else {
      document.documentElement.classList.remove('dark');
      localStorage.setItem('darkMode', 'false');
    }
  };

  onMounted(() => {
    const savedDarkMode = localStorage.getItem('darkMode');
    if (savedDarkMode !== null) {
      // isDarkMode.value = savedDarkMode === 'true';
      isDarkMode.value = true;
    } else {
     // isDarkMode.value = window.matchMedia('(prefers-color-scheme: dark)').matches;
     isDarkMode.value = true;

    }
    updateDarkMode();
  });

  watch(() => isDarkMode.value, updateDarkMode);
  </script>
