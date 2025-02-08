<script setup>
import AppLayout from '@/Layouts/AppLayout.vue';
import LazyImage from '@/Components/LazyImage.vue';
import { Link } from '@inertiajs/vue3';

</script>

<template>
    <AppLayout title="Spatial Reasoning">
        <template #header>
            <h2 class="font-semibold text-xl text-gray-800 dark:text-gray-200 leading-tight">
                Spatial Reasoning  : Overview and Practice
            </h2>
        </template>

        <div class="py-12">
            <div class="max-w-7xl mx-auto sm:px-6 lg:px-8">
                <div class="bg-white dark:bg-gray-800 overflow-hidden shadow-xl sm:rounded-lg">
                    <div class="p-6 text-gray-900 dark:text-gray-100">
                        <h1 class="text-3xl font-bold mb-4">Spatial Reasoning  : Overview and Practice</h1>
                        <hr class="mb-4">
                        <div class="space-y-4">
                            <p>The Spatial Reasoning Test is an important component of many cognitive aptitude assessments, including the CCAT. It evaluates your ability to visualize and manipulate objects in your mind, recognize patterns, and understand spatial relationships.</p>

                            <div class="bg-gray-100 dark:bg-gray-700 p-4 rounded-lg">
                                <p class="font-semibold mb-2">Table of Contents</p>
                                <ul class="list-disc list-inside space-y-1">
                                    <li><a href="#overview" class="text-blue-600 dark:text-blue-400 hover:underline">Overview of Spatial Reasoning Tests</a></li>
                                    <li><a href="#question-types" class="text-blue-600 dark:text-blue-400 hover:underline">Types of Spatial Reasoning Questions</a></li>
                                    <li><a href="#examples" class="text-blue-600 dark:text-blue-400 hover:underline">Example Questions</a></li>
                                    <li><a href="#tips" class="text-blue-600 dark:text-blue-400 hover:underline">Tips for Success</a></li>
                                    <li><a href="#practice" class="text-blue-600 dark:text-blue-400 hover:underline">Practice Resources</a></li>

                                </ul>
                            </div>

                            <h2 id="overview" class="text-2xl font-semibold mt-6 mb-2">Overview of Spatial Reasoning Tests</h2>
                            <p>Spatial reasoning tests assess your ability to mentally manipulate 2D and 3D objects, visualize movements and transformations, and recognize patterns in spatial arrangements. These skills are crucial in many fields, including engineering, architecture, design, and scientific research.</p>

                            <h2 id="question-types" class="text-2xl font-semibold mt-6 mb-2">Types of Spatial Reasoning Questions</h2>
                            <p>Common types of spatial reasoning test questions include:</p>
                            <ul class="list-disc list-inside space-y-1">
                                <li>Mental Rotation</li>
                                <li>Mirror Images</li>
                                <li>Paper Folding</li>
                                <li>Pattern Recognition</li>
                                <li>Spatial Visualization</li>
                                <li>Block Counting</li>
                            </ul>

                            <h2 id="examples" class="text-2xl font-semibold mt-6 mb-2">Example Questions</h2>
                            <p>Here's an example of a spatial reasoning test question:</p>

                            <LazyImage src="/storage/img/1669372162795_ccat_assessments7_1500_x938.png" alt="CCAT Spatial Reasoning Example" class="content-image" />

                            <p class="text-center italic">Source: CCAT</p>
                            <p><strong>Answer:</strong> C</p>
                            <p><strong>Explanation:</strong> All four options A, B, D, and E have a quadrangle in the center. Only option C contains a square in its center. So, the one that does not belong is option C.</p>

                            <h2 id="tips" class="text-2xl font-semibold mt-6 mb-2">Tips for Success</h2>
                            <ul class="list-disc list-inside space-y-1">
                                <li>Practice visualizing objects from different angles</li>
                                <li>Work on jigsaw puzzles and 3D puzzles</li>
                                <li>Play spatial reasoning games and apps</li>
                                <li>Study geometry and practice drawing 3D shapes</li>
                                <li>Take timed practice tests to improve your speed and accuracy</li>
                            </ul>
                            <h2 id="practice" class="text-2xl font-semibold mt-6 mb-2">Practice Resources</h2>
                            <p>To improve your spatial reasoning skills, practice with the continuously generated unlimited questions below:</p>

                            <div class="mt-8 flex justify-center space-x-4">
                                <Link
                                    href="/spatial-test-json-start"
                                    class="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded"
                                >
                                    Start Spatial & Logic Practice
                                </Link>
                                <Link
                                    href="/spatial-test-start"
                                    class="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded"
                                >
                                    Start Spatial & Logic Practice - AI Generated
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
