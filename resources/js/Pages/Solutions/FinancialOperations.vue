<script setup>
import SolutionLayout from './SolutionLayout.vue';

const solutionData = {
    title: 'AI-Powered Financial Operations',
    description: 'Transform your financial workflows with enterprise-grade AI automation that ensures accuracy, compliance, and real-time insights.',
    focus: 'AP/AR automation, expense management, and financial analytics with bank-grade security.',
    keyPoint: '90% reduction in processing time with 99.97% accuracy in financial data processing.',
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
                                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17 9V7a2 2 0 00-2-2H5a2 2 0 00-2 2v6a2 2 0 002 2h2m2 4h10a2 2 0 002-2v-6a2 2 0 00-2-2H9a2 2 0 00-2 2v6a2 2 0 002 2zm7-5a2 2 0 11-4 0 2 2 0 014 0z" />
                                </svg>
                            </div>
                        </div>
                        <div class="ml-4">
                            <h3 class="text-lg font-medium text-gray-900 dark:text-white">AP/AR Automation</h3>
                            <p class="mt-2 text-gray-600 dark:text-gray-300">Automated invoice matching, intelligent payment scheduling, and cash flow optimization.</p>
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
                            <h3 class="text-lg font-medium text-gray-900 dark:text-white">Expense Management</h3>
                            <p class="mt-2 text-gray-600 dark:text-gray-300">Smart receipt scanning, policy compliance checking, and automated expense reporting.</p>
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
                            <h3 class="text-lg font-medium text-gray-900 dark:text-white">Financial Analytics</h3>
                            <p class="mt-2 text-gray-600 dark:text-gray-300">Real-time dashboards, predictive analysis, and customizable KPI tracking.</p>
                        </div>
                    </div>

                    <div class="flex items-start">
                        <div class="flex-shrink-0">
                            <div class="flex items-center justify-center h-12 w-12 rounded-md bg-blue-500 text-white">
                                <svg class="h-6 w-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 15v2m-6 4h12a2 2 0 002-2v-6a2 2 0 00-2-2H6a2 2 0 00-2 2v6a2 2 0 002 2zm10-10V7a4 4 0 00-8 0v4h8z" />
                                </svg>
                            </div>
                        </div>
                        <div class="ml-4">
                            <h3 class="text-lg font-medium text-gray-900 dark:text-white">Security & Compliance</h3>
                            <p class="mt-2 text-gray-600 dark:text-gray-300">Bank-grade encryption, automated audit trails, and comprehensive compliance features.</p>
                        </div>
                    </div>
                </div>
            </section>

            <!-- Security Features -->
            <section class="mt-12">
                <h2 class="text-2xl font-bold text-gray-900 dark:text-white mb-6">Enterprise Security</h2>
                <div class="bg-gray-50 dark:bg-gray-700/50 rounded-lg p-6">
                    <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
                        <div class="flex items-center space-x-3">
                            <svg class="h-6 w-6 text-blue-500" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m5.618-4.016A11.955 11.955 0 0112 2.944a11.955 11.955 0 01-8.618 3.04A12.02 12.02 0 003 9c0 5.591 3.824 10.29 9 11.622 5.176-1.332 9-6.03 9-11.622 0-1.042-.133-2.052-.382-3.016z" />
                            </svg>
                            <span class="text-gray-700 dark:text-gray-300">Bank-level encryption (256-bit AES)</span>
                        </div>
                        <div class="flex items-center space-x-3">
                            <svg class="h-6 w-6 text-blue-500" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m5.618-4.016A11.955 11.955 0 0112 2.944a11.955 11.955 0 01-8.618 3.04A12.02 12.02 0 003 9c0 5.591 3.824 10.29 9 11.622 5.176-1.332 9-6.03 9-11.622 0-1.042-.133-2.052-.382-3.016z" />
                            </svg>
                            <span class="text-gray-700 dark:text-gray-300">SOC 2 Type II compliant</span>
                        </div>
                        <div class="flex items-center space-x-3">
                            <svg class="h-6 w-6 text-blue-500" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m5.618-4.016A11.955 11.955 0 0112 2.944a11.955 11.955 0 01-8.618 3.04A12.02 12.02 0 003 9c0 5.591 3.824 10.29 9 11.622 5.176-1.332 9-6.03 9-11.622 0-1.042-.133-2.052-.382-3.016z" />
                            </svg>
                            <span class="text-gray-700 dark:text-gray-300">GDPR and CCPA compliant</span>
                        </div>
                        <div class="flex items-center space-x-3">
                            <svg class="h-6 w-6 text-blue-500" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m5.618-4.016A11.955 11.955 0 0112 2.944a11.955 11.955 0 01-8.618 3.04A12.02 12.02 0 003 9c0 5.591 3.824 10.29 9 11.622 5.176-1.332 9-6.03 9-11.622 0-1.042-.133-2.052-.382-3.016z" />
                            </svg>
                            <span class="text-gray-700 dark:text-gray-300">Role-based access control</span>
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
                            <div class="text-3xl font-bold">90%</div>
                            <div class="text-sm mt-1">Processing Time Reduction</div>
                        </div>
                        <div class="text-center">
                            <div class="text-3xl font-bold">99.97%</div>
                            <div class="text-sm mt-1">Data Accuracy</div>
                        </div>
                        <div class="text-center">
                            <div class="text-3xl font-bold">65%</div>
                            <div class="text-sm mt-1">Cost Reduction</div>
                        </div>
                        <div class="text-center">
                            <div class="text-3xl font-bold">100%</div>
                            <div class="text-sm mt-1">Compliance Rate</div>
                        </div>
                    </div>
                </div>
            </section>

            <!-- Call to Action -->
            <div class="mt-12 text-center">
                <a href="#contact" class="inline-flex items-center px-6 py-3 border border-transparent text-base font-medium rounded-md text-white bg-blue-600 hover:bg-blue-700 transition duration-150 ease-in-out">
                    Schedule Financial Process Assessment
                    <svg class="ml-2 -mr-1 w-5 h-5" fill="currentColor" viewBox="0 0 20 20">
                        <path fill-rule="evenodd" d="M10.293 3.293a1 1 0 011.414 0l6 6a1 1 0 010 1.414l-6 6a1 1 0 01-1.414-1.414L14.586 11H3a1 1 0 110-2h11.586l-4.293-4.293a1 1 0 010-1.414z" clip-rule="evenodd" />
                    </svg>
                </a>
            </div>
        </div>
    </SolutionLayout>
</template>
