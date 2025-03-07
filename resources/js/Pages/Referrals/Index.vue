<script setup>
import { ref, computed } from 'vue';
import AppLayout from '@/Layouts/AppLayout.vue';
import { Head } from '@inertiajs/vue3';
import { ClipboardIcon, CheckIcon } from '@heroicons/vue/24/outline';

const props = defineProps({
    referrals: Array,
    stats: Object,
    referralLink: String,
    referralCode: String
});

const copied = ref(false);

const copyToClipboard = () => {
    navigator.clipboard.writeText(props.referralLink);
    copied.value = true;
    setTimeout(() => {
        copied.value = false;
    }, 2000);
};

const statusColor = (status) => {
    switch (status) {
        case 'pending':
            return 'bg-yellow-100 text-yellow-800 dark:bg-yellow-900 dark:text-yellow-300';
        case 'converted':
            return 'bg-green-100 text-green-800 dark:bg-green-900 dark:text-green-300';
        case 'paid':
            return 'bg-blue-100 text-blue-800 dark:bg-blue-900 dark:text-blue-300';
        default:
            return 'bg-gray-100 text-gray-800 dark:bg-gray-700 dark:text-gray-300';
    }
};

const formatDate = (dateString) => {
    if (!dateString) return '';
    const date = new Date(dateString);
    return date.toLocaleDateString();
};

const formatCurrency = (amount) => {
    if (amount === null || amount === undefined) return '-';
    return new Intl.NumberFormat('en-US', { style: 'currency', currency: 'USD' }).format(amount);
};
</script>

<template>
    <AppLayout title="My Referrals">
        <Head title="My Referrals" />

        <div class="py-12">
            <div class="max-w-7xl mx-auto sm:px-6 lg:px-8">
                <!-- Referral Link Section -->
                <div class="bg-white dark:bg-gray-800 overflow-hidden shadow-xl sm:rounded-lg p-6 mb-6">
                    <h2 class="text-2xl font-semibold text-gray-900 dark:text-white mb-4">Your Referral Link</h2>
                    <p class="text-gray-600 dark:text-gray-300 mb-4">
                        Share this link with potential clients. When they submit a contact form through your link, you'll earn a 10% commission on any contract signed.
                    </p>
                    
                    <div class="flex flex-col sm:flex-row gap-4 items-start sm:items-center">
                        <div class="flex-grow bg-gray-100 dark:bg-gray-700 rounded-md p-3 text-sm text-gray-800 dark:text-gray-200 font-mono break-all">
                            {{ referralLink }}
                        </div>
                        <button 
                            @click="copyToClipboard" 
                            class="inline-flex items-center px-4 py-2 bg-blue-600 border border-transparent rounded-md font-semibold text-xs text-white uppercase tracking-widest hover:bg-blue-700 focus:bg-blue-700 active:bg-blue-900 focus:outline-none focus:ring-2 focus:ring-indigo-500 focus:ring-offset-2 transition ease-in-out duration-150"
                        >
                            <ClipboardIcon v-if="!copied" class="w-4 h-4 mr-2" />
                            <CheckIcon v-else class="w-4 h-4 mr-2" />
                            {{ copied ? 'Copied!' : 'Copy Link' }}
                        </button>
                    </div>
                    
                    <div class="mt-4 text-sm text-gray-600 dark:text-gray-400">
                        Your referral code: <span class="font-semibold">{{ referralCode }}</span>
                    </div>
                </div>

                <!-- Stats Cards -->
                <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6 mb-6">
                    <div class="bg-white dark:bg-gray-800 overflow-hidden shadow-sm sm:rounded-lg p-6">
                        <div class="text-sm font-medium text-gray-500 dark:text-gray-400">Total Referrals</div>
                        <div class="mt-1 text-3xl font-semibold text-gray-900 dark:text-white">{{ stats.total }}</div>
                    </div>
                    
                    <div class="bg-white dark:bg-gray-800 overflow-hidden shadow-sm sm:rounded-lg p-6">
                        <div class="text-sm font-medium text-gray-500 dark:text-gray-400">Pending</div>
                        <div class="mt-1 text-3xl font-semibold text-yellow-600 dark:text-yellow-400">{{ stats.pending }}</div>
                    </div>
                    
                    <div class="bg-white dark:bg-gray-800 overflow-hidden shadow-sm sm:rounded-lg p-6">
                        <div class="text-sm font-medium text-gray-500 dark:text-gray-400">Converted</div>
                        <div class="mt-1 text-3xl font-semibold text-green-600 dark:text-green-400">{{ stats.converted }}</div>
                    </div>
                    
                    <div class="bg-white dark:bg-gray-800 overflow-hidden shadow-sm sm:rounded-lg p-6">
                        <div class="text-sm font-medium text-gray-500 dark:text-gray-400">Total Commission</div>
                        <div class="mt-1 text-3xl font-semibold text-blue-600 dark:text-blue-400">{{ formatCurrency(stats.totalCommission) }}</div>
                    </div>
                </div>

                <!-- Referrals Table -->
                <div class="bg-white dark:bg-gray-800 overflow-hidden shadow-xl sm:rounded-lg">
                    <div class="p-6 border-b border-gray-200 dark:border-gray-700">
                        <h3 class="text-lg font-medium text-gray-900 dark:text-white">Your Referrals</h3>
                    </div>
                    
                    <div class="overflow-x-auto">
                        <table class="min-w-full divide-y divide-gray-200 dark:divide-gray-700">
                            <thead class="bg-gray-50 dark:bg-gray-700">
                                <tr>
                                    <th scope="col" class="px-6 py-3 text-left text-xs font-medium text-gray-500 dark:text-gray-300 uppercase tracking-wider">Date</th>
                                    <th scope="col" class="px-6 py-3 text-left text-xs font-medium text-gray-500 dark:text-gray-300 uppercase tracking-wider">Contact</th>
                                    <th scope="col" class="px-6 py-3 text-left text-xs font-medium text-gray-500 dark:text-gray-300 uppercase tracking-wider">Status</th>
                                    <th scope="col" class="px-6 py-3 text-left text-xs font-medium text-gray-500 dark:text-gray-300 uppercase tracking-wider">Contract Amount</th>
                                    <th scope="col" class="px-6 py-3 text-left text-xs font-medium text-gray-500 dark:text-gray-300 uppercase tracking-wider">Commission (10%)</th>
                                </tr>
                            </thead>
                            <tbody class="bg-white dark:bg-gray-800 divide-y divide-gray-200 dark:divide-gray-700">
                                <tr v-if="referrals.length === 0">
                                    <td colspan="5" class="px-6 py-4 text-center text-sm text-gray-500 dark:text-gray-400">
                                        No referrals yet. Share your referral link to get started!
                                    </td>
                                </tr>
                                <tr v-for="referral in referrals" :key="referral.id" class="hover:bg-gray-50 dark:hover:bg-gray-700">
                                    <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-500 dark:text-gray-400">
                                        {{ formatDate(referral.created_at) }}
                                    </td>
                                    <td class="px-6 py-4 whitespace-nowrap">
                                        <div class="text-sm font-medium text-gray-900 dark:text-white">{{ referral.contact?.name || 'Unknown' }}</div>
                                        <div class="text-sm text-gray-500 dark:text-gray-400">{{ referral.contact?.email || 'No email' }}</div>
                                    </td>
                                    <td class="px-6 py-4 whitespace-nowrap">
                                        <span :class="[statusColor(referral.status), 'px-2 inline-flex text-xs leading-5 font-semibold rounded-full']">
                                            {{ referral.status.charAt(0).toUpperCase() + referral.status.slice(1) }}
                                        </span>
                                    </td>
                                    <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-500 dark:text-gray-400">
                                        {{ formatCurrency(referral.contract_amount) }}
                                    </td>
                                    <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-500 dark:text-gray-400">
                                        {{ formatCurrency(referral.commission_amount) }}
                                    </td>
                                </tr>
                            </tbody>
                        </table>
                    </div>
                </div>
                
                <!-- How It Works Section -->
                <div class="mt-8 bg-white dark:bg-gray-800 overflow-hidden shadow-xl sm:rounded-lg p-6">
                    <h3 class="text-lg font-medium text-gray-900 dark:text-white mb-4">How It Works</h3>
                    
                    <ol class="list-decimal list-inside space-y-3 text-gray-600 dark:text-gray-300">
                        <li>Share your unique referral link with potential clients who might need our services.</li>
                        <li>When they visit our site through your link and submit a contact form, they'll be tracked as your referral.</li>
                        <li>If they sign a contract with us, you'll earn a 10% commission on the total contract value.</li>
                        <li>Commissions are paid after the project is initiated.</li>
                        <li>There's no limit to how many people you can refer!</li>
                    </ol>
                    
                    <div class="mt-4 p-4 bg-blue-50 dark:bg-blue-900 rounded-md">
                        <div class="flex">
                            <div class="flex-shrink-0">
                                <svg class="h-5 w-5 text-blue-400" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20" fill="currentColor" aria-hidden="true">
                                    <path fill-rule="evenodd" d="M18 10a8 8 0 11-16 0 8 8 0 0116 0zm-7-4a1 1 0 11-2 0 1 1 0 012 0zM9 9a1 1 0 000 2v3a1 1 0 001 1h1a1 1 0 100-2v-3a1 1 0 00-1-1H9z" clip-rule="evenodd" />
                                </svg>
                            </div>
                            <div class="ml-3 flex-1 md:flex md:justify-between">
                                <p class="text-sm text-blue-700 dark:text-blue-300">
                                    Questions about the referral program? Contact us at <a href="mailto:support@aibrainl.ink" class="font-medium underline">support@aibrainl.ink</a>
                                </p>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </AppLayout>
</template>
