<script setup>
import { ref, onMounted } from 'vue';
import AppLayout from '@/Layouts/AppLayout.vue';
import Question from '@/Components/Question.vue';
import axios from 'axios';

const testStarted = ref(false);
const currentQuestion = ref(null);
const userAnswer = ref(null);
const loadingQuestion = ref(false);
const error = ref('');
const answerSubmitted = ref(false);
const previousQuestions = ref([]);

const startTest = () => {
  testStarted.value = true;
  fetchNextQuestion();
};

const fetchNextQuestion = async () => {
  loadingQuestion.value = true;
  answerSubmitted.value = false;
  userAnswer.value = null;
  currentQuestion.value = null;
  error.value = '';

  try {
    const response = await axios.post('/api/generate-question', {
      prompt: `Generate a verbal Spatial reasoning question with multiple choice answers. Follow these steps:

1. First, create a clear spatial reasoning question that tests one of these skills:
   - Mental rotation
   - Pattern completion
   - Spatial visualization
   - Shape relationships
   - Spatial orientation
   - Visual sequence completion
2. Create 4 multiple choice options labeled a, b, c, or d
3. Create an explanation object that MUST follow this EXACT structure:
   {
     "correctAnswerExplanation": "A detailed step-by-step explanation of the correct spatial relationship or pattern and why the correct answer is right",
     "commonMisconceptions": [
       "First common error in spatial perception that might lead to a wrong answer",
       "Second common spatial reasoning mistake or misunderstanding"
     ],
     "keyConcepts": [
       "First key spatial reasoning skill or concept tested in this problem",
       "Second key spatial visualization technique or principle needed"
     ]
   }
4. Double-check that the answer in the solution explanation answer matches your multiple choice correct answer and its a option thats actually available in the multiple choice options, if it doesnt go back and fix it to make it so
5. Shuffle Answers a,b,c,d and then format the complete response as JSON with EXACTLY this structure:
   {
     "question": "The complete question text",
     "options": ["option a", "option b", "option c", "option d"],
     "correctAnswer": "a/b/c/d",
     "explanation": {
       "correctAnswerExplanation": "step-by-step explanation",
       "commonMisconceptions": ["misconception 1", "misconception 2"],
       "keyConcepts": ["concept 1", "concept 2"]
     }
   }
6. Look at the question again from a different perspective, resolve it and explain it step by step, compare these steps and answer to the previous explanations steps and answer. If you came to a different conclusion this time, find out which explanation is the correct one and use that for correctAnswerExplanation instead of what youve had previously.
7. Shuffle Answers a,b,c,d again to randomize the position of the correct answer`  });

    const data = response.data;
    if (!data.choices?.[0]?.message?.content) {
      throw new Error('Invalid response format');
    }

    const questionData = JSON.parse(data.choices[0].message.content);
    if (!questionData.question ||
        !Array.isArray(questionData.options) ||
        !questionData.correctAnswer ||
        !questionData.explanation ||
        !questionData.explanation.correctAnswerExplanation ||
        !Array.isArray(questionData.explanation.commonMisconceptions) ||
        !Array.isArray(questionData.explanation.keyConcepts)) {
      throw new Error('Invalid question data format');
    }

    currentQuestion.value = {
      text: questionData.question,
      options: questionData.options,
      correctAnswer: questionData.correctAnswer,
      explanation: questionData.explanation
    };
    previousQuestions.value.push(questionData.question);
  } catch (error) {
    console.error('Error fetching question:', error);
    error.value = error.response?.data?.error || error.message || 'Error fetching question. Please try again.';
  }
  loadingQuestion.value = false;
};

const submitAnswer = (answer) => {
  userAnswer.value = answer;
  answerSubmitted.value = true;
};
</script>

<template>
  <AppLayout title="Spatial Reasoning Practice Test">
    <template #header>
      <h2 class="font-semibold text-xl text-gray-800 dark:text-gray-200 leading-tight">
        Spatial Reasoning Practice Test
      </h2>
    </template>

    <div class="py-12">
      <div class="max-w-7xl mx-auto sm:px-6 lg:px-8">
        <div class="bg-white dark:bg-gray-800 overflow-hidden shadow-xl sm:rounded-lg">
          <div class="p-6 sm:px-20 bg-white dark:bg-gray-800 border-b border-gray-200 dark:border-gray-700">
            <!-- Start Screen -->
            <div v-if="!testStarted" class="text-center">
              <h1 class="text-3xl font-bold mb-6 text-gray-900 dark:text-gray-100">Spatial Reasoning Practice Test</h1>
              <p class="mb-4 text-gray-600 dark:text-gray-400">This practice test will help you prepare for the Spatial Reasoning portion of the CCAT. Questions will be generated dynamically, and you can practice as many as you like.</p>
              <button @click="startTest" class="inline-flex items-center px-6 py-3 bg-blue-600 border border-transparent rounded-md font-semibold text-base text-white uppercase tracking-widest hover:bg-blue-500 active:bg-blue-700 focus:outline-none focus:border-blue-700 focus:ring ring-blue-300 disabled:opacity-25 transition ease-in-out duration-150">
                Start Practice
              </button>
            </div>

            <!-- Test Content -->
            <div v-else class="text-center">
              <!-- Loading Initial Question -->
              <div v-if="loadingQuestion && !currentQuestion" class="my-4 flex flex-col items-center">
                <p class="text-gray-600 dark:text-gray-400">Loading question...</p>
                <div class="loader"></div>
              </div>

              <!-- Error State -->
              <div v-if="error" class="my-4 text-red-600">
                {{ error }}
              </div>

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

                <!-- Answer Results -->
                <div v-if="answerSubmitted" class="mt-4">
                  <!-- Result Banner -->
                  <div class="p-4 mb-6 rounded-lg" :class="[
                    userAnswer === currentQuestion.correctAnswer
                      ? 'bg-green-100 dark:bg-yellow-900'
                      : 'bg-red-100 dark:bg-yellow-900'
                  ]">
                    <div class="flex items-center justify-center gap-4">
                      <div class="text-2xl">

                      </div>
                      <div class="text-center">
                        <p class="text-gray-900 dark:text-gray-100 font-medium">
                          Your answer: {{ userAnswer }}
                        </p>

                      </div>
                    </div>
                  </div>

                  <!-- Explanation Sections -->
                  <div class="space-y-6 text-left">
                    <!-- Main Explanation -->
                    <div class="bg-white dark:bg-gray-700 rounded-lg p-4 shadow-sm">
                      <h3 class="text-lg font-semibold text-gray-900 dark:text-gray-100 mb-2">
                        Solution Explanation
                      </h3>
                      <p class="text-gray-700 dark:text-gray-300 whitespace-pre-line">
                        {{ currentQuestion.explanation.correctAnswerExplanation }}
                      </p>
                    </div>

                    <!-- Common Misconceptions -->
                    <div class="bg-white dark:bg-gray-700 rounded-lg p-4 shadow-sm">
                      <h3 class="text-lg font-semibold text-gray-900 dark:text-gray-100 mb-2">
                        Common Misconceptions
                      </h3>
                      <ul class="list-disc ml-4 space-y-2 text-gray-700 dark:text-gray-300">
                        <li v-for="(misconception, index) in currentQuestion.explanation.commonMisconceptions"
                            :key="index"
                            class="pl-2">
                          {{ misconception }}
                        </li>
                      </ul>
                    </div>

                    <!-- Key Concepts -->
                    <div class="bg-white dark:bg-gray-700 rounded-lg p-4 shadow-sm">
                      <h3 class="text-lg font-semibold text-gray-900 dark:text-gray-100 mb-2">
                        Key Concepts
                      </h3>
                      <ul class="list-disc ml-4 space-y-2 text-gray-700 dark:text-gray-300">
                        <li v-for="(concept, index) in currentQuestion.explanation.keyConcepts"
                            :key="index"
                            class="pl-2">
                          {{ concept }}
                        </li>
                      </ul>
                    </div>
                  </div>

                  <!-- Next Question Button -->
                  <button
                    @click="fetchNextQuestion"
                    class="mt-6 w-full inline-flex justify-center rounded-md border border-transparent px-4 py-2 bg-indigo-600 text-base font-medium text-white shadow-sm hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500 sm:text-sm disabled:opacity-50 disabled:cursor-not-allowed transition-colors duration-150"
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
