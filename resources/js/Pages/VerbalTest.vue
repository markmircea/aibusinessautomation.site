<script setup>
import AppLayout from '@/Layouts/AppLayout.vue';
import LazyImage from '@/Components/LazyImage.vue';
import { Link } from '@inertiajs/vue3';
</script>

<template>
    <AppLayout title="Verbal  ">
        <template #header>
            <h2 class="font-semibold text-xl text-gray-800 dark:text-gray-200 leading-tight">
                Verbal  : Overview and Practice
            </h2>
        </template>

        <div class="py-12">
            <div class="max-w-7xl mx-auto sm:px-6 lg:px-8">
                <div class="bg-white dark:bg-gray-800 overflow-hidden shadow-xl sm:rounded-lg">
                    <div class="p-6 text-gray-900 dark:text-gray-100">
                        <h1 class="text-3xl font-bold mb-4">Verbal  : Overview and Practice</h1>
                        <hr class="mb-4">
                        <div class="space-y-4">
                            <p>The Verbal Test is a crucial component of many cognitive aptitude assessments, including the CCAT. It measures your ability to understand and analyze written information, identify relationships between words, and select appropriate words in specific contexts.</p>

                            <div class="bg-gray-100 dark:bg-gray-700 p-4 rounded-lg">
                                <p class="font-semibold mb-2">Table of Contents</p>
                                <ul class="list-disc list-inside space-y-1">
                                    <li><a href="#overview" class="text-blue-600 dark:text-blue-400 hover:underline">Overview of Verbal Tests</a></li>
                                    <li><a href="#question-types" class="text-blue-600 dark:text-blue-400 hover:underline">Types of Verbal Test Questions</a></li>
                                    <li><a href="#examples" class="text-blue-600 dark:text-blue-400 hover:underline">Example Questions</a></li>
                                    <li><a href="#tips" class="text-blue-600 dark:text-blue-400 hover:underline">Tips for Success</a></li>
                                    <li><a href="#practice" class="text-blue-600 dark:text-blue-400 hover:underline">Practice Resources</a></li>
                                </ul>
                            </div>

                            <h2 id="overview" class="text-2xl font-semibold mt-6 mb-2">Overview of Verbal Tests</h2>
                            <p>Verbal tests typically assess your vocabulary, reading comprehension, and ability to understand relationships between words. These skills are crucial in many professional settings, especially those requiring clear communication and analysis of written information.</p>

                            <h2 id="question-types" class="text-2xl font-semibold mt-6 mb-2">Types of Verbal Test Questions</h2>
                            <p>Common types of verbal test questions include:</p>
                            <ul class="list-disc list-inside space-y-1">
                                <li>Synonyms and Antonyms</li>
                                <li>Analogies</li>
                                <li>Sentence Completion</li>
                                <li>Reading Comprehension</li>
                            </ul>

                            <h2 id="examples" class="text-2xl font-semibold mt-6 mb-2">Example Questions</h2>
                            <p>Here are some examples of verbal test questions:</p>

                            <LazyImage src="/storage/img/1669372162795_ccat_assessments4_1500_x938.png" alt="CCAT Verbal Example 1" class="content-image" />

                            <p class="text-center italic">Source: CCAT</p>
                            <p><strong>Answer:</strong> ESTEEMED is to SEEDY</p>
                            <p><strong>Explanation:</strong> This question tests your ability to recognize relationships between words. The relationship between DELUSIONAL and GROUNDED is that of antonyms (opposites). Similarly, ESTEEMED (respected) and SEEDY (disreputable) are also antonyms.</p>

                            <h2 id="tips" class="text-2xl font-semibold mt-6 mb-2">Tips for Success</h2>
                            <ul class="list-disc list-inside space-y-1">
                                <li>Expand your vocabulary through regular reading</li>
                                <li>Practice identifying word relationships</li>
                                <li>Improve your reading speed and comprehension</li>
                                <li>Take practice tests to familiarize yourself with question formats</li>
                            </ul>

                            <h2 id="practice" class="text-2xl font-semibold mt-6 mb-2">Practice Resources</h2>
                            <p>To improve your verbal skills, practice with the continuously generated unlimited questions below:</p>


                            <div class="mt-8 flex justify-center space-x-4">
                                <Link
        href="/verbal-test-json-start"
        class="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded"
    >
        Start Verbal Practice
    </Link>
    <Link
        href="/verbal-test-start"
        class="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded"
    >
        Start Verbal Practice - AI Generated
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
