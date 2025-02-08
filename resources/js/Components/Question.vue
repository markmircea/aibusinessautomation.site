<script setup>
import { ref } from 'vue';

const props = defineProps({
  question: {
    type: Object,
    required: true
  },
  questionNumber: {
    type: Number,
    required: true
  },
  totalQuestions: {
    type: Number,
    required: true
  }
});

const emit = defineEmits(['answer-submitted']);

const selectedAnswer = ref(null);

const submitAnswer = () => {
  if (selectedAnswer.value) {
    emit('answer-submitted', selectedAnswer.value);
    selectedAnswer.value = null;
  }
};
</script>

<template>
  <div class="max-w-3xl mx-auto bg-white dark:bg-gray-500 shadow-md rounded-lg overflow-hidden">
    <div class="p-6">
      <div class="mb-6">
        <p class="text-lg text-gray-800 dark:text-gray-200 mb-4">{{ question.text }}</p>
        <img v-if="question.image" :src="question.image" :alt="'Image for question ' + questionNumber" class="mb-4 max-w-full h-auto rounded-lg mx-auto">
      </div>
      <div class="space-y-4">
        <label v-for="option in question.options" :key="option" class="flex items-center p-2 rounded-md hover:bg-gray-100 dark:hover:bg-gray-700 transition-colors duration-150 cursor-pointer">
          <input
            type="radio"
            :value="option"
            v-model="selectedAnswer"
            class="form-radio h-5 w-5 text-indigo-600 transition duration-150 ease-in-out"
          >
          <span class="ml-3 block text-sm leading-5 text-gray-700 dark:text-gray-300 flex-grow">
            {{ option }}
          </span>
        </label>
      </div>
      <button
        @click="submitAnswer"
        :disabled="!selectedAnswer"
        class="mt-6 w-full inline-flex justify-center rounded-md border border-transparent px-4 py-2 bg-indigo-600 text-base font-medium text-white shadow-sm hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500 sm:text-sm disabled:opacity-50 disabled:cursor-not-allowed transition-colors duration-150"
      >
        Submit Answer
      </button>
    </div>
  </div>
</template>

<style scoped>
.form-radio {
  -webkit-appearance: none;
  -moz-appearance: none;
  appearance: none;
  display: inline-block;
  vertical-align: middle;
  background-origin: border-box;
  user-select: none;
  flex-shrink: 0;
  border-radius: 100%;
  border-width: 2px;
}

.form-radio:checked {
  background-image: url("data:image/svg+xml,%3csvg viewBox='0 0 16 16' fill='white' xmlns='http://www.w3.org/2000/svg'%3e%3ccircle cx='8' cy='8' r='3'/%3e%3c/svg%3e");
  border-color: transparent;
  background-color: currentColor;
  background-size: 100% 100%;
  background-position: center;
  background-repeat: no-repeat;
}

@media not print {
  .form-radio::-ms-check {
    border-width: 1px;
    color: transparent;
    background: inherit;
    border-color: inherit;
    border-radius: inherit;
  }
}

.form-radio:focus {
  outline: none;
  box-shadow: 0 0 0 3px rgba(164, 202, 254, 0.45);
  border-color: #a4cafe;
}
</style>
