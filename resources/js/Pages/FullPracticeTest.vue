<script setup>
import { ref } from 'vue';
import AppLayout from '@/Layouts/AppLayout.vue';
import { Link } from '@inertiajs/vue3';
import { ChevronRightIcon, DocumentArrowDownIcon } from '@heroicons/vue/24/solid';

const fullPracticeTests = [
    { name: 'Full Practice Test 1', route: 'full.practice.test.1', pdfFile: 'CCATtest.COM1.pdf' },
    { name: 'Full Practice Test 2', route: 'full.practice.test.2', pdfFile: 'CCATtest.COM2.pdf' },
    { name: 'Full Practice Test 3', route: 'full.practice.test.3', pdfFile: 'CCATtest.COM3.pdf' },
    { name: 'Full Practice Test 4', route: 'full.practice.test.4', pdfFile: 'CCATtest.COM4.pdf' },
    { name: 'Full Practice Test 5', route: 'full.practice.test.5', pdfFile: 'CCATtest.COM5.pdf' },
    { name: 'Full Practice Test 6', route: 'full.practice.test.6', pdfFile: 'CCATtest.COM6.pdf' },
    { name: 'Full Practice Test 7', route: 'full.practice.test.7', pdfFile: 'CCATtest.COM7.pdf' },
    { name: 'Full Practice Test 8', route: 'full.practice.test.8', pdfFile: 'CCATtest.COM8.pdf' },
    { name: 'Full Practice Test 9', route: 'full.practice.test.9', pdfFile: 'CCATtest.COM9.pdf' },
    { name: 'Full Practice Test 10', route: 'full.practice.test.10', pdfFile: 'CCATtest.COM10.pdf' },
];

const getTestNumber = (route) => {
    return parseInt(route.split('.').pop());
};

const downloadPdf = (event, filename) => {
    event.preventDefault();
    window.location.href = route('download.pdf', { filename: filename });
};

const sections = ref([
    { id: 'overview', title: 'Test Overview' },
    { id: 'structure', title: 'Test Structure' },
    { id: 'instructions', title: 'Test Instructions' },
    { id: 'tips', title: 'Tips for Taking the Full Practice Test' },
    { id: 'available-tests', title: 'Available Full Practice Tests' },
]);
</script>

<template>
    <AppLayout title="Full Practice Test">
        <template #header>
            <h2 class="text-3xl font-bold text-gray-800 dark:text-gray-200">
                Full Practice Tests: Comprehensive Assessments
            </h2>
        </template>

        <div class="py-12 bg-gray-50 dark:bg-gray-900">
            <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
                <div class="bg-white dark:bg-gray-800 shadow-xl rounded-lg overflow-hidden">
                    <div class="p-6 sm:p-10">
                        <div class="prose dark:prose-invert max-w-none">
                            <p class="text-xl text-gray-600 dark:text-gray-300 mb-8">
                                Welcome to the Full Practice Tests. These comprehensive assessments cover all areas of
                                the CCAT, including verbal reasoning, math and logic, and spatial reasoning. It's
                                designed to
                                give
                                you a complete practice experience exactly like the actual test.
                            </p>

                            <div class="bg-blue-50 dark:bg-blue-900 p-4 rounded-lg mb-4">
                                <h3 class="text-2xl font-semibold text-blue-800 dark:text-blue-200 mb-4">Table of
                                    Contents</h3>
                                <ul class="space-y-2 list-none p-6">
                                    <li v-for="section in sections" :key="section.id">
                                        <a :href="`#${section.id}`"
                                            class="flex items-center text-blue-600 dark:text-blue-300 hover:text-blue-800 dark:hover:text-blue-100 transition-colors duration-200 animated-link">
                                            <ChevronRightIcon class="h-4 w-4 mr-2 flex-shrink-0" />
                                            <span>{{ section.title }}</span>
                                        </a>
                                    </li>
                                </ul>
                            </div>

                            <section v-for="section in sections" :key="section.id" :id="section.id" class="mb-12">
                                <h2 class="text-3xl font-bold text-gray-800 dark:text-gray-100 mb-6">{{ section.title }}
                                </h2>

                                <div v-if="section.id === 'overview'">
                                    <p>This Full Practice Test mirrors the structure and difficulty of the actual CCAT.
                                        It includes questions from all three main areas: Verbal, Math and Logic, and
                                        Spatial Reasoning. The test is timed and scored, providing you with a realistic
                                        assessment of your preparedness.</p>
                                </div>

                                <div v-else-if="section.id === 'structure'">
                                    <ul class="list-disc list-inside space-y-2 text-gray-600 dark:text-gray-300">
                                        <li>Total Questions: 50</li>
                                        <li>Time Limit: 15 minutes</li>
                                        <li>Question Types: Verbal, Math and Logic, Spatial Reasoning</li>
                                        <li>Scoring: One point per correct answer, no penalty for wrong answers</li>
                                    </ul>
                                </div>

                                <div v-else-if="section.id === 'instructions'">
                                    <ol class="list-decimal list-inside space-y-2 text-gray-600 dark:text-gray-300">
                                        <li>Read each question carefully before answering.</li>
                                        <li>You have 15 minutes to complete all 50 questions.</li>
                                        <li>You can skip questions and return to them later if time allows.</li>
                                        <li>Guess if you're unsure - there's no penalty for wrong answers.</li>
                                        <li>Your score will be displayed immediately after completing the test along
                                            with the answers for the incorrect responses.</li>
                                    </ol>
                                </div>

                                <div v-else-if="section.id === 'tips'">
                                    <ul class="list-disc list-inside space-y-2 text-gray-600 dark:text-gray-300">
                                        <li>Find a quiet place where you won't be interrupted.</li>
                                        <li>Use a timer to keep track of your 15 minutes.</li>
                                        <li>Answer easier questions first to maximize your score.</li>
                                        <li>Practice your pacing - aim to spend no more than 18 seconds per question.
                                        </li>
                                        <li>Review your answers and analyze your performance after the test.</li>
                                    </ul>
                                </div>

                                <div v-else-if="section.id === 'available-tests'">
                                    <p class="mb-6 text-gray-600 dark:text-gray-300">We offer multiple full practice
                                        tests to help you prepare thoroughly. Each test contains a unique set of
                                        questions while
                                        maintaining the same structure and difficulty level. Choose any test below to
                                        begin:</p>

                                    <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-4 mb-8">
                                        <div v-for="test in fullPracticeTests" :key="test.route" class="flex flex-col">
                                            <div class="bg-gray-100 dark:bg-gray-700 rounded-lg p-4">
                                                <Link :href="route(test.route)"
                                                    class="flex items-center justify-between text-gray-800 dark:text-gray-200 hover:text-blue-600 dark:hover:text-blue-400 transition duration-300 mb-2 animated-link">
                                                <span>{{ test.name }}</span>
                                                <ChevronRightIcon class="h-5 w-5" />
                                                </Link>

                                            </div>
                                        </div>
                                    </div>
                                    <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-4 mb-8">
                                        <div v-for="(test, index) in fullPracticeTests" :key="test.route"
                                            class="flex flex-col">
                                            <div class="bg-gray-100 dark:bg-gray-700 rounded-lg p-4">
                                                <a href=""
                                                    class="flex items-center justify-between text-gray-800 dark:text-gray-200 hover:text-blue-600 dark:hover:text-blue-400 transition duration-300 mb-2 animated-link"
                                                    @click="(event) => downloadPdf(event, test.pdfFile)">
                                                    <div class="flex items-center">
                                                        <DocumentArrowDownIcon class="h-5 w-5 mr-2" />
                                                        <span>Download PDF {{ index + 1 }} - Questions, Answers and
                                                            Explanations</span>
                                                    </div>
                                                    <ChevronRightIcon class="h-5 w-5" />
                                                </a>
                                            </div>
                                        </div>
                                    </div>

                                    <div class="mt-8 flex justify-center">
                                        <Link :href="route('full-practice-test-start')"
                                            class=" text-white font-bold py-2 px-4 rounded animated-link">
                                        Start Randomized Test
                                        </Link>
                                    </div>
                                    <p class="text-center mt-4 text-sm text-gray-600 dark:text-gray-400">
                                        (Generates Random Questions from our pool of 500+ questions)
                                    </p>
                                </div>
                            </section>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </AppLayout>
</template>

<style scoped>
@import 'tailwindcss/base';
@import 'tailwindcss/components';
@import 'tailwindcss/utilities';

.prose h2 {
    @apply text-3xl font-bold text-gray-800 dark:text-gray-100 mb-6;
}

.prose p {
    @apply text-lg text-gray-600 dark:text-gray-300 mb-4;
}

.prose ul,
.prose ol {
    @apply my-4;
}

.prose li {
    @apply mb-2;
}

.prose a {
    @apply text-blue-600 dark:text-blue-300 hover:text-blue-800 dark:hover:text-blue-100 transition-colors duration-200;
}

.animated-link {
    position: relative;
    overflow: hidden;
}

.animated-link::after {
    content: '';
    position: absolute;
    bottom: 0;
    left: 0;
    width: 100%;
    height: 2px;
    background-color: currentColor;
    transform: scaleX(0);
    transform-origin: right;
    transition: transform 0.3s ease;
}

.animated-link:hover::after {
    transform: scaleX(1);
    transform-origin: left;
}
</style>
