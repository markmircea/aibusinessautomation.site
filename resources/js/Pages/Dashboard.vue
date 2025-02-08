<script setup>
import { ref } from 'vue';
import AppLayout from '@/Layouts/AppLayout.vue';
import { Link } from '@inertiajs/vue3';
import DashboardHeader from '@/Components/DashboardHeader.vue';
import UpgradeAccount from '@/Components/UpgradeAccount.vue';
import LifetimePlan from '@/Components/LifetimePlan.vue';
import Definition from '@/Components/Definition.vue';
import MathLogicTest from '@/Components/MathLogicTest.vue';
import VerbalTest from '@/Components/VerbalTest.vue';
import SpatialReasoningTest from '@/Components/SpatialReasoningTest.vue';
import CompaniesUsingCCAT from '@/Components/CompaniesUsingCCAT.vue';
import PracticeWithCCATtest from '@/Components/PracticeWithCCATtest.vue';
import GetHiredAtCrossover from '@/Components/GetHiredAtCrossover.vue';

import FAQ from '@/Components/FAQ.vue';

import StarRating from '@/Components/Stars.vue';

const rating = ref(4.7);
const totalReviews = ref(26);
const props = defineProps({
    isSubscribed: Boolean
});

const isIntersecting = ref({});
</script>

<template>
    <AppLayout title="CCAT Cognitive Aptitude Assessments">
        <div class="bg-gradient-to-b from-gray-200 to-gray-50 dark:from-gray-900 dark:to-gray-800 min-h-screen">
            <DashboardHeader :isSubscribed="props.isSubscribed" />
            <main class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-12">
                <nav class="bg-white dark:bg-gray-800 shadow-lg rounded-lg p-4 mb-8 animate-fade-in">
                    <p class="font-semibold mb-2 text-lg text-gray-800 dark:text-gray-300">Table of Contents</p>
                    <ul class="space-y-2">
                        <li v-for="(item, index) in ['lifetime-plan','get-hired-at-crossover', 'definition', 'math-and-logic-test', 'verbal-test', 'spatial-reasoning-test', 'companies-using-ccat', 'practice-with-CCATtest', 'FAQ']"
                            :key="index">
                            <a :href="`#${item}`"
                                class="text-blue-600 dark:text-blue-400 hover:underline transition-colors duration-200 flex items-center">
                                <svg class="w-4 h-4 mr-2" fill="currentColor" viewBox="0 0 20 20">
                                    <path fill-rule="evenodd"
                                        d="M7.293 14.707a1 1 0 010-1.414L10.586 10 7.293 6.707a1 1 0 011.414-1.414l4 4a1 1 0 010 1.414l-4 4a1 1 0 01-1.414 0z"
                                        clip-rule="evenodd"></path>
                                </svg>
                                {{ item.split('-').map(word => word.charAt(0).toUpperCase() + word.slice(1)).join(' ')
                                }}
                            </a>
                        </li>
                    </ul>
                </nav>

                <UpgradeAccount v-if="!props.isSubscribed" />
                <LifetimePlan v-if="props.isSubscribed" :subscriptionStartDate="$page.props.auth.user.subscription_started_at" />
                <get-hired-at-crossover/>
                <Definition />
                <MathLogicTest />
                <VerbalTest />
                <SpatialReasoningTest />
                <CompaniesUsingCCAT />
                <PracticeWithCCATtest />

                <section id="FAQ" class="mb-12 animate-on-scroll"
                    :class="{ 'animate-fade-in-up': isIntersecting['faqs'] }">
                    <FAQ />
                </section>

                <section id="free-practice-test" class="animate-on-scroll" :class="{ 'animate-fade-in-up': isIntersecting['free-practice-test'] }">
        <div class="bg-gradient-to-r from-blue-600 to-indigo-700 rounded-xl shadow-2xl p-8 relative overflow-hidden">
            <!-- Background decoration -->
            <div class="absolute inset-0 bg-[radial-gradient(circle_at_30%_-20%,rgba(255,255,255,0.1),transparent)]" />

            <div class="relative">
                <!-- Header and Rating -->
                <div class="space-y-4 mb-8">
                    <h2 class="text-3xl font-bold text-white">Try our Free Practice Test</h2>
                    <div class="flex items-center gap-3 bg-white/10 backdrop-blur-sm rounded-full px-4 py-2 w-fit">
                        <StarRating :rating="rating" :readonly="true" size="md" />
                        <div class="text-sm font-medium text-white/90">
                            {{ rating.toFixed(1) }}
                        </div>
                        <a href="/free-practice-test#reviews" class="text-sm text-white/70 hover:text-white transition-colors">
                            ({{ totalReviews.toLocaleString() }} {{ totalReviews === 1 ? 'review' : 'reviews' }})
                        </a>
                    </div>
                </div>

                <!-- Description -->
                <p class="text-white/90 text-lg mb-6">
                    Want to experience what a CCAT is like before committing to a full test? We
                    offer a free practice test that simulates the CCAT experience. This shorter version includes
                    25 questions to be completed in 7:30 minutes, covering verbal, math and logic, and spatial
                    reasoning questions.
                </p>

                <!-- Features -->
                <ul class="grid grid-cols-1 md:grid-cols-2 gap-4 mb-8">
                    <li v-for="feature in [
                        '25 questions in 7:30 minutes',
                        'Covers all CCAT question types',
                        'No registration required',
                        'Immediate results and explanations'
                    ]" :key="feature" class="flex items-center text-white/90">
                        <svg class="w-5 h-5 mr-2 text-emerald-400" viewBox="0 0 20 20" fill="currentColor">
                            <path fill-rule="evenodd"
                                d="M16.707 5.293a1 1 0 010 1.414l-8 8a1 1 0 01-1.414 0l-4-4a1 1 0 011.414-1.414L8 12.586l7.293-7.293a1 1 0 011.414 0z"
                                clip-rule="evenodd" />
                        </svg>
                        {{ feature }}
                    </li>
                </ul>

                <!-- CTA Button -->
                <Link :href="route('free.practice.test')"
                    class="inline-flex items-center px-6 py-3 text-base font-medium rounded-lg bg-white text-indigo-600 hover:bg-indigo-50 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-white/20 transition-all duration-200 shadow-lg hover:shadow-xl transform hover:-translate-y-0.5">
                    Start Free Practice Test
                    <svg class="ml-2 -mr-1 w-5 h-5" fill="currentColor" viewBox="0 0 20 20">
                        <path fill-rule="evenodd"
                            d="M10.293 3.293a1 1 0 011.414 0l6 6a1 1 0 010 1.414l-6 6a1 1 0 01-1.414-1.414L14.586 11H3a1 1 0 110-2h11.586l-4.293-4.293a1 1 0 010-1.414z"
                            clip-rule="evenodd" />
                    </svg>
                </Link>
            </div>
        </div>
    </section>
            </main>
        </div>
    </AppLayout>
</template>

<style scoped>
.animate-fade-in-up {
    animation: fadeInUp 0.6s ease-out;
}

.animate-fade-in {
    animation: fadeIn 0.6s ease-out;
}

@keyframes fadeInUp {
    from {
        opacity: 0;
        transform: translateY(20px);
    }

    to {
        opacity: 1;
        transform: translateY(0);
    }
}

@keyframes fadeIn {
    from {
        opacity: 0;
    }

    to {
        opacity: 1;
    }
}

.group:hover .group-hover\:translate-x-1 {
    transform: translateX(0.25rem);
}

.group {
    transition: background-color 0.3s ease;
}
</style>
