<script setup>
import { Head, Link, usePage } from '@inertiajs/vue3';
import AppLayout from '@/Layouts/AppLayout.vue';
import HeroSection from '@/Components/HeroSection.vue';
import LogoSlider from '@/Components/LogoSlider.vue';
import SolutionsSection from '@/Components/SolutionsSection.vue';
import ContactSection from '@/Components/ContactSection.vue';

defineProps({
    canLogin: Boolean,
    canRegister: Boolean,
});
</script>

<template>
    <AppLayout>
        <Head>
            <title>AI Business Automation Solutions</title>
            <meta name="description" content="Transform your business operations with AI automation. Streamline processes, reduce costs, and boost efficiency with our cutting-edge solutions." />
        </Head>

        <div class="min-h-screen bg-white dark:bg-gray-900">
            <!-- Main Content -->
            <!-- Hero Section -->
            <HeroSection />

            <!-- Logo Slider -->
            <LogoSlider />

            <!-- Solutions Section -->
            <SolutionsSection />

            <!-- Benefits Section -->
            <section id="benefits" class="py-20 bg-white dark:bg-gray-800">
                <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
                    <div class="text-center mb-16">
                        <h2 class="text-3xl sm:text-4xl font-bold text-gray-900 dark:text-white mb-4">
                            Your Custom AI Automation Journey
                        </h2>
                        <p class="max-w-3xl mx-auto text-lg text-gray-600 dark:text-gray-300">
                            Experience a personalized approach to AI automation with dedicated support and custom-built solutions tailored to your unique business needs.
                        </p>
                    </div>

                    <div class="grid grid-cols-1 md:grid-cols-4 gap-8">
                        <div class="p-6 bg-gray-50 dark:bg-gray-700 rounded-lg transform hover:scale-105 transition-transform duration-300">
                            <div class="w-12 h-12 bg-purple-100 dark:bg-purple-800 rounded-lg flex items-center justify-center mb-4">
                                <svg class="w-6 h-6 text-purple-600 dark:text-purple-300" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2" />
                                </svg>
                            </div>
                            <h3 class="text-xl font-semibold text-gray-900 dark:text-white mb-2">Personalized Assessment</h3>
                            <p class="text-gray-600 dark:text-gray-300">In-depth analysis of your current processes and custom strategy development.</p>
                        </div>

                        <div class="p-6 bg-gray-50 dark:bg-gray-700 rounded-lg transform hover:scale-105 transition-transform duration-300">
                            <div class="w-12 h-12 bg-blue-100 dark:bg-blue-800 rounded-lg flex items-center justify-center mb-4">
                                <svg class="w-6 h-6 text-blue-600 dark:text-blue-300" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 4.354a4 4 0 110 5.292M15 21H3v-1a6 6 0 0112 0v1zm0 0h6v-1a6 6 0 00-9-5.197M13 7a4 4 0 11-8 0 4 4 0 018 0z" />
                                </svg>
                            </div>
                            <h3 class="text-xl font-semibold text-gray-900 dark:text-white mb-2">Dedicated Team</h3>
                            <p class="text-gray-600 dark:text-gray-300">Your personal project manager and development team throughout the journey.</p>
                        </div>

                        <div class="p-6 bg-gray-50 dark:bg-gray-700 rounded-lg transform hover:scale-105 transition-transform duration-300">
                            <div class="w-12 h-12 bg-green-100 dark:bg-green-800 rounded-lg flex items-center justify-center mb-4">
                                <svg class="w-6 h-6 text-green-600 dark:text-green-300" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 10V3L4 14h7v7l9-11h-7z" />
                                </svg>
                            </div>
                            <h3 class="text-xl font-semibold text-gray-900 dark:text-white mb-2">Seamless Integration</h3>
                            <p class="text-gray-600 dark:text-gray-300">Custom-built solutions that integrate perfectly with your existing systems.</p>
                        </div>

                        <div class="p-6 bg-gray-50 dark:bg-gray-700 rounded-lg transform hover:scale-105 transition-transform duration-300">
                            <div class="w-12 h-12 bg-orange-100 dark:bg-orange-800 rounded-lg flex items-center justify-center mb-4">
                                <svg class="w-6 h-6 text-orange-600 dark:text-orange-300" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 19v-6a2 2 0 00-2-2H5a2 2 0 00-2 2v6a2 2 0 002 2h2a2 2 0 002-2zm0 0V9a2 2 0 012-2h2a2 2 0 012 2v10m-6 0a2 2 0 002 2h2a2 2 0 002-2m0 0V5a2 2 0 012-2h2a2 2 0 012 2v14a2 2 0 01-2 2h-2a2 2 0 01-2-2z" />
                                </svg>
                            </div>
                            <h3 class="text-xl font-semibold text-gray-900 dark:text-white mb-2">Continuous Support</h3>
                            <p class="text-gray-600 dark:text-gray-300">Ongoing optimization and support to ensure long-term success.</p>
                        </div>
                    </div>

                    <!-- Process Timeline -->
                    <div class="mt-20">
                        <h3 class="text-2xl font-bold text-center text-gray-900 dark:text-white mb-12">Our Process</h3>
                        <div class="relative">
                            <!-- Timeline Line -->
                            <div class="absolute left-1/2 transform -translate-x-1/2 h-full w-1 bg-blue-200 dark:bg-blue-800"></div>
                            
                            <!-- Timeline Items -->
                            <div class="space-y-12">
                                <div class="flex items-center justify-center">
                                    <div class="w-1/2 pr-8 text-right">
                                        <h4 class="text-lg font-semibold text-blue-600 dark:text-blue-400">Initial Consultation</h4>
                                        <p class="text-gray-600 dark:text-gray-400">Understanding your business needs and objectives</p>
                                    </div>
                                    <div class="w-4 h-4 bg-blue-500 rounded-full"></div>
                                    <div class="w-1/2 pl-8"></div>
                                </div>
                                
                                <div class="flex items-center justify-center">
                                    <div class="w-1/2 pr-8"></div>
                                    <div class="w-4 h-4 bg-blue-500 rounded-full"></div>
                                    <div class="w-1/2 pl-8">
                                        <h4 class="text-lg font-semibold text-blue-600 dark:text-blue-400">Custom Solution Design</h4>
                                        <p class="text-gray-600 dark:text-gray-400">Tailoring AI solutions to your specific requirements</p>
                                    </div>
                                </div>
                                
                                <div class="flex items-center justify-center">
                                    <div class="w-1/2 pr-8 text-right">
                                        <h4 class="text-lg font-semibold text-blue-600 dark:text-blue-400">Development & Integration</h4>
                                        <p class="text-gray-600 dark:text-gray-400">Building and implementing your custom solution</p>
                                    </div>
                                    <div class="w-4 h-4 bg-blue-500 rounded-full"></div>
                                    <div class="w-1/2 pl-8"></div>
                                </div>
                                
                                <div class="flex items-center justify-center">
                                    <div class="w-1/2 pr-8"></div>
                                    <div class="w-4 h-4 bg-blue-500 rounded-full"></div>
                                    <div class="w-1/2 pl-8">
                                        <h4 class="text-lg font-semibold text-blue-600 dark:text-blue-400">Continuous Optimization</h4>
                                        <p class="text-gray-600 dark:text-gray-400">Ongoing support and performance improvements</p>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </section>

            <ContactSection />

        </div>
    </AppLayout>
</template>

<style>
html {
    scroll-behavior: smooth;
}
</style>
