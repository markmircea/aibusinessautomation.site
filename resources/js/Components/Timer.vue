<script setup>
import { ref, onMounted, onUnmounted } from 'vue';

const props = defineProps({
  initialTime: {
    type: Number,
    required: true
  }
});

const emit = defineEmits(['expired']);

const timeRemaining = ref(props.initialTime);
let timer;

const formatTime = (seconds) => {
  const minutes = Math.floor(seconds / 60);
  const remainingSeconds = seconds % 60;
  return `${minutes.toString().padStart(2, '0')}:${remainingSeconds.toString().padStart(2, '0')}`;
};

const startTimer = () => {
  timer = setInterval(() => {
    if (timeRemaining.value > 0) {
      timeRemaining.value--;
    } else {
      clearInterval(timer);
      emit('expired');
    }
  }, 1000);
};

onMounted(() => {
  startTimer();
});

onUnmounted(() => {
  clearInterval(timer);
});

const timerColor = () => {
  if (timeRemaining.value > 300) { // More than 5 minutes
    return 'text-green-600 dark:text-green-400';
  } else if (timeRemaining.value > 60) { // Between 1 and 5 minutes
    return 'text-yellow-600 dark:text-yellow-400';
  } else { // Less than 1 minute
    return 'text-red-600 dark:text-red-400';
  }
};
</script>

<template>
  <div class="bg-white dark:bg-gray-800 shadow-md rounded-lg p-4 mb-6">
    <div class="text-2xl font-bold" :class="timerColor()">
      Time Remaining: {{ formatTime(timeRemaining) }}
    </div>
  </div>
</template>

<style scoped>
/* Add any additional styles here */
</style>