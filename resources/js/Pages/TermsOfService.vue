<script setup>
import { Head } from '@inertiajs/vue3';
import AuthenticationCardLogo from '@/Components/AuthenticationCardLogo.vue';

defineProps({
    policy: String,
});


const goBack = () => {
    window.close();
};
</script>

<template>
    <Head title="Terms & Policy" />

    <div class="min-h-screen bg-gray-100 dark:bg-gray-900 text-gray-800 dark:text-gray-200">
        <div class="pt-6 sm:pt-0">
            <div class="flex flex-col items-center">
                <div class="mt-4">
                    <AuthenticationCardLogo />
                </div>
                <h1 class="mt-6 text-3xl font-bold">Terms & Policy</h1>
            </div>

            <div class="mt-8 sm:mx-auto sm:w-full sm:max-w-4xl">
                <div class="grid grid-cols-1 md:grid-cols-2 gap-6 px-4">
                    <div class="bg-white dark:bg-gray-800 overflow-hidden shadow-md sm:rounded-lg">
                        <div class="p-6">
                            <h2 class="text-xl font-semibold mb-4 flex items-center">
                                <svg class="w-6 h-6 mr-2 text-blue-500" fill="currentColor" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg">
                                    <path fill-rule="evenodd" d="M4 2a1 1 0 011 1v2.101a7.002 7.002 0 0111.601 2.566 1 1 0 11-1.885.666A5.002 5.002 0 005.999 7H9a1 1 0 010 2H4a1 1 0 01-1-1V3a1 1 0 011-1zm.008 9.057a1 1 0 011.276.61A5.002 5.002 0 0014.001 13H11a1 1 0 110-2h5a1 1 0 011 1v5a1 1 0 11-2 0v-2.101a7.002 7.002 0 01-11.601-2.566 1 1 0 01.61-1.276z" clip-rule="evenodd" />
                                </svg>
                                Refund Policy
                            </h2>
                            <p class="text-sm">
                                Within 15 days of purchase, if you find the quality of our materials unsatisfactory and can provide specific complaints, you may request a partial or full refund. For failed tests, we offer up to a 50% refund. Note that refunds are not applicable to coach-provided products and services. To claim a refund, please visit our <a href="/refund-requests" class="text-blue-500 hover:underline">refund request page</a>.
                            </p>
                        </div>
                    </div>

                    <div class="bg-white dark:bg-gray-800 overflow-hidden shadow-md sm:rounded-lg">
                        <div class="p-6">
                            <h2 class="text-xl font-semibold mb-4 flex items-center">
                                <svg class="w-6 h-6 mr-2 text-green-500" fill="currentColor" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg">
                                    <path d="M4 4a2 2 0 00-2 2v1h16V6a2 2 0 00-2-2H4z" />
                                    <path fill-rule="evenodd" d="M18 9H2v5a2 2 0 002 2h12a2 2 0 002-2V9zM4 13a1 1 0 011-1h1a1 1 0 110 2H5a1 1 0 01-1-1zm5-1a1 1 0 100 2h1a1 1 0 100-2H9z" clip-rule="evenodd" />
                                </svg>
                                Payment & Pricing
                            </h2>
                            <p class="text-sm">
                                All transactions are powered and protected by PayPal. You can purchase our products using credit/debit cards or a PayPal account. If you encounter any issues, please contact us at <a href="mailto:support@CCATtest.com" class="text-blue-500 hover:underline">support@CCATtest.com</a>.
                            </p>
                        </div>
                    </div>

                    <div class="bg-white dark:bg-gray-800 overflow-hidden shadow-md sm:rounded-lg">
                        <div class="p-6">
                            <h2 class="text-xl font-semibold mb-4 flex items-center">
                                <svg class="w-6 h-6 mr-2 text-yellow-500" fill="currentColor" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg">
                                    <path fill-rule="evenodd" d="M5 9V7a5 5 0 0110 0v2a2 2 0 012 2v5a2 2 0 01-2 2H5a2 2 0 01-2-2v-5a2 2 0 012-2zm8-2v2H7V7a3 3 0 016 0z" clip-rule="evenodd" />
                                </svg>
                                Accessing Purchased Products
                            </h2>
                            <p class="text-sm">
                                After payment, you'll receive an email with links to your purchased products. These are also accessible through your User Dashboard via the profile icon in the top-right corner of the screen.
                            </p>
                        </div>
                    </div>

                    <div class="bg-white dark:bg-gray-800 overflow-hidden shadow-md sm:rounded-lg">
                        <div class="p-6">
                            <h2 class="text-xl font-semibold mb-4 flex items-center">
                                <svg class="w-6 h-6 mr-2 text-purple-500" fill="currentColor" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg">
                                    <path fill-rule="evenodd" d="M18 10a8 8 0 11-16 0 8 8 0 0116 0zm-8-3a1 1 0 00-.867.5 1 1 0 11-1.731-1A3 3 0 0113 8a3.001 3.001 0 01-2 2.83V11a1 1 0 11-2 0v-1a1 1 0 011-1 1 1 0 100-2zm0 8a1 1 0 100-2 1 1 0 000 2z" clip-rule="evenodd" />
                                </svg>
                                Contact Us for Support
                            </h2>
                            <p class="text-sm mb-2">For assistance, please contact us:</p>
                            <ul class="list-disc list-inside text-sm">
                                <li>Course content: <a href="mailto:support@CCATtest.com" class="text-blue-500 hover:underline">support@CCATtest.com</a></li>
                                <li>Technical issues: <a href="https://discord.com/invite/Dcb4FXKeqq" target="_blank" class="text-blue-500 hover:underline">Discord support channel</a></li>
                            </ul>
                            <p class="text-sm mt-2 font-semibold">We'll respond within 24 hours!</p>
                        </div>
                    </div>
                </div>
 <!-- Back Button -->
 <div class="mt-6 flex justify-center">
                    <button
                        @click="goBack"
                        class="inline-flex items-center px-4 py-2 bg-gray-800 dark:bg-gray-200 border border-transparent rounded-md font-semibold text-xs text-white dark:text-gray-800 uppercase tracking-widest hover:bg-gray-700 dark:hover:bg-white focus:bg-gray-700 dark:focus:bg-white active:bg-gray-900 dark:active:bg-gray-300 focus:outline-none focus:ring-2 focus:ring-indigo-500 focus:ring-offset-2 dark:focus:ring-offset-gray-800 transition ease-in-out duration-150"
                    >
                        <svg class="w-5 h-5 mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 19l-7-7m0 0l7-7m-7 7h18"></path>
                        </svg>
                        Close Tab
                    </button>
                </div>
            </div>
        </div>
    </div>
</template>
