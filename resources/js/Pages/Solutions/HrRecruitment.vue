<script setup>
import SolutionLayout from './SolutionLayout.vue';

const solutionData = {
    title: 'AI-Powered HR & Recruitment',
    description: 'Transform your talent acquisition and HR operations with intelligent automation that reduces hiring time and improves employee experience.',
    focus: 'Intelligent recruitment, employee onboarding automation, and HR operations streamlining.',
    keyPoint: '75% reduction in hiring time and 80% less HR administrative work.',
};
</script>

<template>
    <SolutionLayout v-bind="solutionData">
        <div class="space-y-8">
            <!-- Features Section -->
            <section>
                <h2 class="text-2xl font-bold text-gray-900 dark:text-white mb-6">Key Features</h2>
                <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
                    <div class="flex items-start">
                        <div class="flex-shrink-0">
                            <div class="flex items-center justify-center h-12 w-12 rounded-md bg-blue-500 text-white">
                                <svg class="h-6 w-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17 20h5v-2a3 3 0 00-5.356-1.857M17 20H7m10 0v-2c0-.656-.126-1.283-.356-1.857M7 20H2v-2a3 3 0 015.356-1.857M7 20v-2c0-.656.126-1.283.356-1.857m0 0a5.002 5.002 0 019.288 0M15 7a3 3 0 11-6 0 3 3 0 016 0zm6 3a2 2 0 11-4 0 2 2 0 014 0zM7 10a2 2 0 11-4 0 2 2 0 014 0z" />
                                </svg>
                            </div>
                        </div>
                        <div class="ml-4">
                            <h3 class="text-lg font-medium text-gray-900 dark:text-white">Intelligent Recruitment</h3>
                            <p class="mt-2 text-gray-600 dark:text-gray-300">AI-powered resume screening, automated candidate communication, and bias-free assessments.</p>
                        </div>
                    </div>

                    <div class="flex items-start">
                        <div class="flex-shrink-0">
                            <div class="flex items-center justify-center h-12 w-12 rounded-md bg-blue-500 text-white">
                                <svg class="h-6 w-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2m-6 9l2 2 4-4" />
                                </svg>
                            </div>
                        </div>
                        <div class="ml-4">
                            <h3 class="text-lg font-medium text-gray-900 dark:text-white">Employee Onboarding</h3>
                            <p class="mt-2 text-gray-600 dark:text-gray-300">Digital document collection, automated background checks, and training schedule automation.</p>
                        </div>
                    </div>

                    <div class="flex items-start">
                        <div class="flex-shrink-0">
                            <div class="flex items-center justify-center h-12 w-12 rounded-md bg-blue-500 text-white">
                                <svg class="h-6 w-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 19v-6a2 2 0 00-2-2H5a2 2 0 00-2 2v6a2 2 0 002 2h2a2 2 0 002-2zm0 0V9a2 2 0 012-2h2a2 2 0 012 2v10m-6 0a2 2 0 002 2h2a2 2 0 002-2m0 0V5a2 2 0 012-2h2a2 2 0 012 2v14a2 2 0 01-2 2h-2a2 2 0 01-2-2z" />
                                </svg>
                            </div>
                        </div>
                        <div class="ml-4">
                            <h3 class="text-lg font-medium text-gray-900 dark:text-white">HR Operations</h3>
                            <p class="mt-2 text-gray-600 dark:text-gray-300">Leave management, timesheet processing, and performance review automation.</p>
                        </div>
                    </div>

                    <div class="flex items-start">
                        <div class="flex-shrink-0">
                            <div class="flex items-center justify-center h-12 w-12 rounded-md bg-blue-500 text-white">
                                <svg class="h-6 w-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M16 8v8m-4-5v5m-4-2v2m-2 4h12a2 2 0 002-2V6a2 2 0 00-2-2H6a2 2 0 00-2 2v12a2 2 0 002 2z" />
                                </svg>
                            </div>
                        </div>
                        <div class="ml-4">
                            <h3 class="text-lg font-medium text-gray-900 dark:text-white">Analytics & Reporting</h3>
                            <p class="mt-2 text-gray-600 dark:text-gray-300">Recruitment metrics, employee satisfaction tracking, and compliance reporting.</p>
                        </div>
                    </div>
                </div>
            </section>

            <!-- Analytics Features -->
            <section class="mt-12">
                <h2 class="text-2xl font-bold text-gray-900 dark:text-white mb-6">Advanced Analytics</h2>
                <div class="bg-gray-50 dark:bg-gray-700/50 rounded-lg p-6">
                    <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
                        <div class="flex items-center space-x-3">
                            <svg class="h-6 w-6 text-blue-500" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 7h8m0 0v8m0-8l-8 8-4-4-6 6" />
                            </svg>
                            <span class="text-gray-700 dark:text-gray-300">Recruitment funnel metrics</span>
                        </div>
                        <div class="flex items-center space-x-3">
                            <svg class="h-6 w-6 text-blue-500" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z" />
                            </svg>
                            <span class="text-gray-700 dark:text-gray-300">Time-to-hire tracking</span>
                        </div>
                        <div class="flex items-center space-x-3">
                            <svg class="h-6 w-6 text-blue-500" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M14.828 14.828a4 4 0 01-5.656 0M9 10h.01M15 10h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z" />
                            </svg>
                            <span class="text-gray-700 dark:text-gray-300">Employee satisfaction scores</span>
                        </div>
                        <div class="flex items-center space-x-3">
                            <svg class="h-6 w-6 text-blue-500" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 19v-6a2 2 0 00-2-2H5a2 2 0 00-2 2v6a2 2 0 002 2h2a2 2 0 002-2zm0 0V9a2 2 0 012-2h2a2 2 0 012 2v10m-6 0a2 2 0 002 2h2a2 2 0 002-2m0 0V5a2 2 0 012-2h2a2 2 0 012 2v14a2 2 0 01-2 2h-2a2 2 0 01-2-2z" />
                            </svg>
                            <span class="text-gray-700 dark:text-gray-300">Retention rate analytics</span>
                        </div>
                    </div>
                </div>
            </section>

            <!-- ROI Metrics -->
            <section class="mt-12">
                <h2 class="text-2xl font-bold text-gray-900 dark:text-white mb-6">ROI Metrics</h2>
                <div class="bg-gradient-to-r from-blue-500 to-blue-600 rounded-lg p-6 text-white">
                    <div class="grid grid-cols-2 md:grid-cols-4 gap-6">
                        <div class="text-center">
                            <div class="text-3xl font-bold">80%</div>
                            <div class="text-sm mt-1">Faster Screening</div>
                        </div>
                        <div class="text-center">
                            <div class="text-3xl font-bold">60%</div>
                            <div class="text-sm mt-1">Onboarding Time</div>
                        </div>
                        <div class="text-center">
                            <div class="text-3xl font-bold">75%</div>
                            <div class="text-sm mt-1">Less Admin Work</div>
                        </div>
                        <div class="text-center">
                            <div class="text-3xl font-bold">50%</div>
                            <div class="text-sm mt-1">Lower Cost-per-Hire</div>
                        </div>
                    </div>
                </div>
            </section>

            <!-- Call to Action -->
            <div class="mt-12 text-center">
                <a href="#contact" class="inline-flex items-center px-6 py-3 border border-transparent text-base font-medium rounded-md text-white bg-blue-600 hover:bg-blue-700 transition duration-150 ease-in-out">
                    Get Your HR Efficiency Score
                    <svg class="ml-2 -mr-1 w-5 h-5" fill="currentColor" viewBox="0 0 20 20">
                        <path fill-rule="evenodd" d="M10.293 3.293a1 1 0 011.414 0l6 6a1 1 0 010 1.414l-6 6a1 1 0 01-1.414-1.414L14.586 11H3a1 1 0 110-2h11.586l-4.293-4.293a1 1 0 010-1.414z" clip-rule="evenodd" />
                    </svg>
                </a>
            </div>
        </div>
    </SolutionLayout>
</template>
