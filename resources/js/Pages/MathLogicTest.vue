<script setup>
import AppLayout from '@/Layouts/AppLayout.vue';
import LazyImage from '@/Components/LazyImage.vue';
import { Link } from '@inertiajs/vue3';

</script>

<template>
    <AppLayout title="Math and Logic  ">
        <template #header>
            <h2 class="font-semibold text-xl text-gray-800 dark:text-gray-200 leading-tight">
                Math and Logic  : Overview and Practice
            </h2>
        </template>

        <div class="py-12">
            <div class="max-w-7xl mx-auto sm:px-6 lg:px-8">
                <div class="bg-white dark:bg-gray-800 overflow-hidden shadow-xl sm:rounded-lg">
                    <div class="p-6 text-gray-900 dark:text-gray-100">
                        <h1 class="text-3xl font-bold mb-4">Math and Logic  : Overview and Practice</h1>
                        <hr class="mb-4">
                        <div class="space-y-4">
                            <p>The Math and Logic Test is a critical component of many cognitive aptitude assessments, including the CCAT. It evaluates your ability to solve mathematical problems, recognize patterns, and apply logical reasoning to various scenarios.</p>

                            <div class="bg-gray-100 dark:bg-gray-700 p-4 rounded-lg">
                                <p class="font-semibold mb-2">Table of Contents</p>
                                <ul class="list-disc list-inside space-y-1">
                                    <li><a href="#overview" class="text-blue-600 dark:text-blue-400 hover:underline">Overview of Math and Logic Tests</a></li>
                                    <li><a href="#question-types" class="text-blue-600 dark:text-blue-400 hover:underline">Types of Math and Logic Questions</a></li>
                                    <li><a href="#examples" class="text-blue-600 dark:text-blue-400 hover:underline">Example Questions</a></li>
                                    <li><a href="#tips" class="text-blue-600 dark:text-blue-400 hover:underline">Tips for Success</a></li>
                                    <li><a href="#practice" class="text-blue-600 dark:text-blue-400 hover:underline">Practice Resources</a></li>
                                </ul>
                            </div>

                            <h2 id="overview" class="text-2xl font-semibold mt-6 mb-2">Overview of Math and Logic Tests</h2>
                            <p>Math and Logic tests assess your fundamental algebra skills, ability to solve word problems, and logical reasoning capabilities. These skills are crucial in many professional settings, especially those requiring problem-solving and analytical thinking.</p>

                            <h2 id="question-types" class="text-2xl font-semibold mt-6 mb-2">Types of Math and Logic Questions</h2>
                            <p>Common types of math and logic test questions include:</p>
                            <ul class="list-disc list-inside space-y-1">
                                <li>Basic Arithmetic</li>
                                <li>Algebra</li>
                                <li>Word Problems</li>
                                <li>Data Interpretation (graphs, tables)</li>
                                <li>Pattern Recognition</li>
                                <li>Logical Reasoning</li>
                            </ul>

                            <h2 id="examples" class="text-2xl font-semibold mt-6 mb-2">Example Questions</h2>
                            <p>Here are some examples of math and logic test questions:</p>

                            <LazyImage src="/storage/img/1669372150373_ccat_assessments_2_1500_x751.png" alt="CCAT Math & Logic Example" class="content-image" />

                            <p class="text-center italic">Source: CCAT</p>
                            <p><strong>Answer: </strong>120</p>
                            <p><strong>Explanation: </strong>The number of customers the cashier can ring up in eight hours: 15 x 8 = 120.</p>

                            <h2 id="tips" class="text-2xl font-semibold mt-6 mb-2">Tips for Success</h2>
                            <ul class="list-disc list-inside space-y-1">
                                <li>Practice mental math to improve calculation speed</li>
                                <li>Familiarize yourself with common mathematical concepts and formulas</li>
                                <li>Work on pattern recognition exercises</li>
                                <li>Practice interpreting data from graphs and tables</li>
                                <li>Take timed practice tests to improve your speed and accuracy</li>
                            </ul>

                            <h2 id="practice" class="text-2xl font-semibold mt-6 mb-2">Practice Resources</h2>
                            <p>To improve your math and logic skills, practice with the continuously generated unlimited questions below:</p>

                            <div class="mt-8 flex justify-center space-x-4">
                                <Link
                                    href="/math-test-json-start"
                                    class="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded"
                                >
                                    Start Math & Logic Practice
                                </Link>
                                <Link
                                    href="/math-test-start"
                                    class="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded"
                                >
                                    Start Math & Logic Practice AI
                                </Link>

                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </AppLayout>
</template>

<style scoped>
.content-image {
    max-width: 80%;
    height: auto;
    margin: 1rem auto;
    display: block;
    border-radius: 8px;
    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
}
</style>
