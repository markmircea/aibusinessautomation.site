<script setup>
import { ref, onMounted } from 'vue';
import AppLayout from '@/Layouts/AppLayout.vue';
import Question from '@/Components/Question.vue';

const mathQuestions = ref([]);
const testStarted = ref(false);
const currentQuestion = ref(null);
const userAnswer = ref(null);
const loadingQuestion = ref(false);
const error = ref('');
const answerSubmitted = ref(false);
const previousQuestions = ref([]);

// Load questions from public folder
const loadQuestions = async () => {
  try {
    const response = await fetch('/verbal.json');

    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`);
    }

    const data = await response.json();
    // Since the JSON is directly an array, we can assign it directly
    mathQuestions.value = Array.isArray(data) ? data : [];

    if (mathQuestions.value.length === 0) {
      throw new Error('No questions loaded from JSON file');
    }

    console.log('Successfully loaded questions:', mathQuestions.value.length);
  } catch (err) {
    console.error('Error loading questions:', err);
    error.value = `Error loading questions: ${err.message}. Please refresh the page.`;
  }
};

onMounted(() => {
  loadQuestions();
});

const startTest = () => {
  if (mathQuestions.value.length === 0) {
    error.value = 'Questions are still loading. Please wait.';
    return;
  }
  testStarted.value = true;
  fetchNextQuestion();
};

const getRandomQuestion = () => {
  // Filter out questions that have already been asked
  const availableQuestions = mathQuestions.value.filter(q =>
    !previousQuestions.value.includes(q.id)
  );

  // If all questions have been asked, reset the previous questions
  if (availableQuestions.length === 0) {
    previousQuestions.value = [];
    return mathQuestions.value[Math.floor(Math.random() * mathQuestions.value.length)];
  }

  return availableQuestions[Math.floor(Math.random() * availableQuestions.length)];
};

const fetchNextQuestion = () => {
  loadingQuestion.value = true;
  answerSubmitted.value = false;
  userAnswer.value = null;
  currentQuestion.value = null;
  error.value = '';

  try {
    const questionData = getRandomQuestion();

    currentQuestion.value = {
      text: questionData.text,
      options: questionData.options,
      correctAnswer: questionData.correctAnswer,
      explanation: {
        correctAnswerExplanation: questionData.explanation,
        commonMisconceptions: [
          "Take care to read the question carefully",
          "Double-check your calculations"
        ],
        keyConcepts: [
          "Problem-solving methodology",
          "Careful analysis of the question"
        ]
      }
    };

    // If there's an image, add it to the current question
    if (questionData.image) {
      currentQuestion.value.image = questionData.image;
    }

    previousQuestions.value.push(questionData.id);
  } catch (error) {
    console.error('Error selecting question:', error);
    error.value = 'Error selecting question. Please try again.';
  }

  loadingQuestion.value = false;
};

const submitAnswer = (answer) => {
  userAnswer.value = answer;
  answerSubmitted.value = true;
};
</script>

<template>
  <AppLayout title="Verbal Practice Test">
    <template #header>
      <h2 class="font-semibold text-xl text-gray-800 dark:text-gray-200 leading-tight">
        Verbal Practice Test
      </h2>
    </template>

    <div class="py-12">
      <div class="max-w-7xl mx-auto sm:px-6 lg:px-8">
        <div class="bg-white dark:bg-gray-800 overflow-hidden shadow-xl sm:rounded-lg">
          <div class="p-6 sm:px-20 bg-white dark:bg-gray-800 border-b border-gray-200 dark:border-gray-700">
            <!-- Start Screen -->
            <div v-if="!testStarted" class="text-center">
              <h1 class="text-3xl font-bold mb-6 text-gray-900 dark:text-gray-100">Verbal Practice Test</h1>
              <p class="mb-4 text-gray-600 dark:text-gray-400">Test your verbal skills with our practice questions. Each question is designed to challenge different aspects of verbal thinking.</p>

              <!-- Error Display -->
              <div v-if="error" class="mb-4 p-4 bg-red-100 text-red-700 rounded-lg">
                {{ error }}
              </div>

              <!-- Loading State -->
              <div v-if="mathQuestions.length === 0 && !error" class="mb-4">
                <div class="loader mx-auto"></div>
                <p class="mt-2 text-gray-600 dark:text-gray-400">Loading questions...</p>
              </div>

              <button
                @click="startTest"
                :disabled="mathQuestions.length === 0"
                class="inline-flex items-center px-6 py-3 bg-blue-600 border border-transparent rounded-md font-semibold text-base text-white uppercase tracking-widest hover:bg-blue-500 active:bg-blue-700 focus:outline-none focus:border-blue-700 focus:ring ring-blue-300 disabled:opacity-25 transition ease-in-out duration-150"
              >
                Start Practice
              </button>
            </div>

            <!-- Test Content -->
            <div v-else class="text-center">
              <!-- Question and Answer Section -->
              <div v-if="currentQuestion">
                <!-- Question Component -->
                <div class="mb-6">
                  <Question
                    :question="currentQuestion"
                    @answer-submitted="submitAnswer"
                    :disabled="answerSubmitted"
                  />
                </div>

                <!-- Answer Results Section -->
                <div v-if="answerSubmitted" class="mt-4">
                  <!-- Result Banner -->
                  <div class="p-4 mb-6 rounded-lg" :class="[
                    userAnswer === currentQuestion.correctAnswer
                      ? 'bg-green-100 dark:bg-green-900'
                      : 'bg-red-100 dark:bg-red-900'
                  ]">
                    <div class="flex items-center justify-center gap-4">
                      <div class="text-center">
                        <p class="text-gray-900 dark:text-gray-100 font-medium">
                          Your answer: {{ userAnswer }}
                        </p>
                        <p class="text-gray-900 dark:text-gray-100 font-medium">
                          Correct answer: {{ currentQuestion.correctAnswer }}
                        </p>
                      </div>
                    </div>
                  </div>

                  <!-- Explanation Section -->
                  <div class="bg-white dark:bg-gray-700 rounded-lg p-4 shadow-sm">
                    <h3 class="text-lg font-semibold text-gray-900 dark:text-gray-100 mb-2">
                      Solution Explanation
                    </h3>
                    <p class="text-gray-700 dark:text-gray-300 whitespace-pre-line">
                      {{ currentQuestion.explanation.correctAnswerExplanation }}
                    </p>
                  </div>

                  <!-- Next Question Button -->
                  <button
                    @click="fetchNextQuestion"
                    class="mt-6 w-full inline-flex justify-center rounded-md border border-transparent px-4 py-2 bg-indigo-600 text-base font-medium text-white shadow-sm hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500 sm:text-sm"
                  >
                    Next Question
                  </button>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </AppLayout>
</template>

<style>
.loader {
  width: 50px;
  aspect-ratio: 1;
  display: grid;
  border-radius: 50%;
  background: conic-gradient(#25b09b 25%,#f03355 0 50%,#514b82 0 75%,#ffa516 0);
  animation: l22 2s infinite linear;
}
.loader::before,
.loader::after {
   content: "";
   grid-area: 1/1;
   margin: 15%;
   border-radius: 50%;
   background: inherit;
   animation: inherit;
}
.loader::after {
   margin: 25%;
   animation-duration: 3s;
}
@keyframes l22 {
  100% {transform: rotate(1turn)}
}
</style>
