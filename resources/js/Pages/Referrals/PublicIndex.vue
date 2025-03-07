<script setup>
import { ref } from 'vue';
import { Head, Link } from '@inertiajs/vue3';
import AppLayout from '@/Layouts/AppLayout.vue';

</script>

<template>
    <AppLayout title="Referral Program">
        <Head title="Referral Program" />

        <div class="py-12">
            <div class="max-w-7xl mx-auto sm:px-6 lg:px-8">
                <!-- Hero Section -->
                <div class="bg-white dark:bg-gray-800 overflow-hidden shadow-xl sm:rounded-lg p-8 mb-8">
                    <div class="text-center mb-8">
                        <h1 class="text-3xl font-bold text-gray-900 dark:text-white mb-4">
                            Earn Money with Our Referral Program
                        </h1>
                        <p class="max-w-3xl mx-auto text-lg text-gray-600 dark:text-gray-300">
                            Refer clients to us and earn a 10% commission on every contract they sign.
                            It's that simple!
                        </p>
                    </div>

                    <div class="flex flex-col md:flex-row justify-center items-center gap-6 mt-8">
                        <Link :href="route('register')" class="inline-flex items-center px-6 py-3 border border-transparent text-base font-medium rounded-md shadow-sm text-white bg-blue-600 hover:bg-blue-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-blue-500 transition-colors duration-200">
                            Register Now to Start Referring
                            <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 ml-2" viewBox="0 0 20 20" fill="currentColor">
                                <path fill-rule="evenodd" d="M10.293 5.293a1 1 0 011.414 0l4 4a1 1 0 010 1.414l-4 4a1 1 0 01-1.414-1.414L12.586 11H5a1 1 0 110-2h7.586l-2.293-2.293a1 1 0 010-1.414z" clip-rule="evenodd" />
                            </svg>
                        </Link>
                        <Link :href="route('login')" class="inline-flex items-center px-6 py-3 border border-gray-300 shadow-sm text-base font-medium rounded-md text-gray-700 dark:text-gray-300 bg-white dark:bg-gray-700 hover:bg-gray-50 dark:hover:bg-gray-600 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500 transition-colors duration-200">
                            Already have an account? Log in
                        </Link>
                    </div>
                </div>

                <!-- How It Works Section -->
                <div class="bg-white dark:bg-gray-800 overflow-hidden shadow-xl sm:rounded-lg p-8 mb-8">
                    <h2 class="text-2xl font-semibold text-gray-900 dark:text-white mb-6">How It Works</h2>
                    
                    <div class="grid grid-cols-1 md:grid-cols-3 gap-8">
                        <div class="flex flex-col items-center text-center">
                            <div class="w-16 h-16 bg-blue-100 dark:bg-blue-900 rounded-full flex items-center justify-center mb-4">
                                <span class="text-2xl font-bold text-blue-600 dark:text-blue-300">1</span>
                            </div>
                            <h3 class="text-lg font-medium text-gray-900 dark:text-white mb-2">Create an Account</h3>
                            <p class="text-gray-600 dark:text-gray-300">
                                Register for a free account to get your unique referral link.
                            </p>
                        </div>
                        
                        <div class="flex flex-col items-center text-center">
                            <div class="w-16 h-16 bg-blue-100 dark:bg-blue-900 rounded-full flex items-center justify-center mb-4">
                                <span class="text-2xl font-bold text-blue-600 dark:text-blue-300">2</span>
                            </div>
                            <h3 class="text-lg font-medium text-gray-900 dark:text-white mb-2">Share Your Link</h3>
                            <p class="text-gray-600 dark:text-gray-300">
                                Share your referral link with potential clients who might need our services.
                            </p>
                        </div>
                        
                        <div class="flex flex-col items-center text-center">
                            <div class="w-16 h-16 bg-blue-100 dark:bg-blue-900 rounded-full flex items-center justify-center mb-4">
                                <span class="text-2xl font-bold text-blue-600 dark:text-blue-300">3</span>
                            </div>
                            <h3 class="text-lg font-medium text-gray-900 dark:text-white mb-2">Earn Commissions</h3>
                            <p class="text-gray-600 dark:text-gray-300">
                                When they sign a contract with us, you earn a 10% commission on the total contract value.
                            </p>
                        </div>
                    </div>
                </div>

                <!-- Terms and Conditions -->
                <div class="bg-white dark:bg-gray-800 overflow-hidden shadow-xl sm:rounded-lg p-8">
                    <h2 class="text-2xl font-semibold text-gray-900 dark:text-white mb-6">Referral Program Terms</h2>
                    
                    <div class="prose prose-blue max-w-none dark:prose-invert">
                        <h3>Eligibility</h3>
                        <ul>
                            <li>You must have a registered account on our platform to participate in the referral program.</li>
                            <li>Referrals must be new clients who have not previously contacted or worked with us.</li>
                        </ul>
                        
                        <h3>Commission Structure</h3>
                        <ul>
                            <li>You will earn a 10% commission on the total contract value for each successful referral.</li>
                            <li>A successful referral is defined as a client who signs a contract with us after being referred by you.</li>
                            <li>Commissions are paid after the project is initiated and the client has made their first payment.</li>
                        </ul>
                        
                        <h3>Referral Process</h3>
                        <ul>
                            <li>Each registered user receives a unique referral link that can be shared with potential clients.</li>
                            <li>When a potential client visits our site through your referral link and submits a contact form, they will be tracked as your referral.</li>
                            <li>You can track the status of your referrals and commissions through your account dashboard.</li>
                        </ul>
                        
                        <h3>Payment Terms</h3>
                        <ul>
                            <li>Commissions are paid within 30 days after the referred client's project has been initiated.</li>
                            <li>Minimum payout threshold is $50. Commissions below this amount will be held until the threshold is reached.</li>
                            <li>Payments are made via bank transfer or PayPal, as specified in your account settings.</li>
                        </ul>
                        
                        <h3>Program Changes</h3>
                        <ul>
                            <li>We reserve the right to modify or terminate the referral program at any time.</li>
                            <li>Any changes to the program will be communicated to participants via email.</li>
                        </ul>
                    </div>
                    
                    <div class="mt-8 text-center">
                        <Link :href="route('register')" class="inline-flex items-center px-6 py-3 border border-transparent text-base font-medium rounded-md shadow-sm text-white bg-blue-600 hover:bg-blue-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-blue-500 transition-colors duration-200">
                            Join Our Referral Program
                        </Link>
                    </div>
                </div>
            </div>
        </div>
    </AppLayout>
</template>
