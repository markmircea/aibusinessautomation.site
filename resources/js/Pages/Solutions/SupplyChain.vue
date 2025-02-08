<script setup>
import SolutionLayout from './SolutionLayout.vue';

const solutionData = {
    title: 'AI-Powered Supply Chain Management',
    description: 'Transform your supply chain with predictive AI intelligence that optimizes inventory, reduces costs, and prevents disruptions.',
    focus: 'Inventory optimization, supplier management, and predictive analytics for supply chain operations.',
    keyPoint: '30% reduction in inventory costs and 40% fewer stockouts.',
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
                                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M20 7l-8-4-8 4m16 0l-8 4m8-4v10l-8 4m0-10L4 7m8 4v10M4 7v10l8 4" />
                                </svg>
                            </div>
                        </div>
                        <div class="ml-4">
                            <h3 class="text-lg font-medium text-gray-900 dark:text-white">Inventory Management</h3>
                            <p class="mt-2 text-gray-600 dark:text-gray-300">Real-time tracking, automated reordering, and demand forecasting.</p>
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
                            <h3 class="text-lg font-medium text-gray-900 dark:text-white">Supply Chain Optimization</h3>
                            <p class="mt-2 text-gray-600 dark:text-gray-300">Route planning, delivery prediction, and cost optimization.</p>
                        </div>
                    </div>

                    <div class="flex items-start">
                        <div class="flex-shrink-0">
                            <div class="flex items-center justify-center h-12 w-12 rounded-md bg-blue-500 text-white">
                                <svg class="h-6 w-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m5.618-4.016A11.955 11.955 0 0112 2.944a11.955 11.955 0 01-8.618 3.04A12.02 12.02 0 003 9c0 5.591 3.824 10.29 9 11.622 5.176-1.332 9-6.03 9-11.622 0-1.042-.133-2.052-.382-3.016z" />
                                </svg>
                            </div>
                        </div>
                        <div class="ml-4">
                            <h3 class="text-lg font-medium text-gray-900 dark:text-white">Risk Management</h3>
                            <p class="mt-2 text-gray-600 dark:text-gray-300">Supplier risk assessment, disruption prediction, and mitigation planning.</p>
                        </div>
                    </div>

                    <div class="flex items-start">
                        <div class="flex-shrink-0">
                            <div class="flex items-center justify-center h-12 w-12 rounded-md bg-blue-500 text-white">
                                <svg class="h-6 w-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 17v-2m3 2v-4m3 4v-6m2 10H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z" />
                                </svg>
                            </div>
                        </div>
                        <div class="ml-4">
                            <h3 class="text-lg font-medium text-gray-900 dark:text-white">Documentation Automation</h3>
                            <p class="mt-2 text-gray-600 dark:text-gray-300">Automated shipping documents, customs documentation, and compliance reports.</p>
                        </div>
                    </div>
                </div>
            </section>

            <!-- Advanced Features -->
            <section class="mt-12">
                <h2 class="text-2xl font-bold text-gray-900 dark:text-white mb-6">Advanced Features</h2>
                <div class="bg-gray-50 dark:bg-gray-700/50 rounded-lg p-6">
                    <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
                        <div class="flex items-center space-x-3">
                            <svg class="h-6 w-6 text-blue-500" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 10V3L4 14h7v7l9-11h-7z" />
                            </svg>
                            <span class="text-gray-700 dark:text-gray-300">IoT integration for real-time tracking</span>
                        </div>
                        <div class="flex items-center space-x-3">
                            <svg class="h-6 w-6 text-blue-500" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 20l4-16m4 4l4 4-4 4M6 16l-4-4 4-4" />
                            </svg>
                            <span class="text-gray-700 dark:text-gray-300">Blockchain-enabled transparency</span>
                        </div>
                        <div class="flex items-center space-x-3">
                            <svg class="h-6 w-6 text-blue-500" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 7h8m0 0v8m0-8l-8 8-4-4-6 6" />
                            </svg>
                            <span class="text-gray-700 dark:text-gray-300">Predictive maintenance</span>
                        </div>
                        <div class="flex items-center space-x-3">
                            <svg class="h-6 w-6 text-blue-500" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 15a4 4 0 004 4h9a5 5 0 10-.1-9.999 5.002 5.002 0 10-9.78 2.096A4.001 4.001 0 003 15z" />
                            </svg>
                            <span class="text-gray-700 dark:text-gray-300">Weather impact analysis</span>
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
                            <div class="text-3xl font-bold">30%</div>
                            <div class="text-sm mt-1">Inventory Cost Reduction</div>
                        </div>
                        <div class="text-center">
                            <div class="text-3xl font-bold">40%</div>
                            <div class="text-sm mt-1">Fewer Stockouts</div>
                        </div>
                        <div class="text-center">
                            <div class="text-3xl font-bold">25%</div>
                            <div class="text-sm mt-1">Delivery Time Improvement</div>
                        </div>
                        <div class="text-center">
                            <div class="text-3xl font-bold">50%</div>
                            <div class="text-sm mt-1">Less Manual Documentation</div>
                        </div>
                    </div>
                </div>
            </section>

            <!-- Call to Action -->
            <div class="mt-12 text-center">
                <a href="#contact" class="inline-flex items-center px-6 py-3 border border-transparent text-base font-medium rounded-md text-white bg-blue-600 hover:bg-blue-700 transition duration-150 ease-in-out">
                    Get Your Supply Chain Assessment
                    <svg class="ml-2 -mr-1 w-5 h-5" fill="currentColor" viewBox="0 0 20 20">
                        <path fill-rule="evenodd" d="M10.293 3.293a1 1 0 011.414 0l6 6a1 1 0 010 1.414l-6 6a1 1 0 01-1.414-1.414L14.586 11H3a1 1 0 110-2h11.586l-4.293-4.293a1 1 0 010-1.414z" clip-rule="evenodd" />
                    </svg>
                </a>
            </div>
        </div>
    </SolutionLayout>
</template>
