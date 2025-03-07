<script setup>
import { ref } from 'vue';
import AppLayout from '@/Layouts/AppLayout.vue';
import { Head, useForm, Link } from '@inertiajs/vue3';

const props = defineProps({
    referral: Object,
});

const form = useForm({
    status: props.referral.status,
    contract_amount: props.referral.contract_amount || '',
    notes: props.referral.notes || '',
});

const calculateCommission = () => {
    if (form.contract_amount) {
        return parseFloat(form.contract_amount) * 0.1;
    }
    return 0;
};

const formatCurrency = (amount) => {
    if (amount === null || amount === undefined || amount === '') return '-';
    return new Intl.NumberFormat('en-US', { style: 'currency', currency: 'USD' }).format(amount);
};

const formatDate = (dateString) => {
    if (!dateString) return '';
    const date = new Date(dateString);
    return date.toLocaleDateString();
};

const submit = () => {
    form.put(route('admin.referrals.update', props.referral.id));
};
</script>

<template>
    <AppLayout title="Edit Referral">
        <Head title="Edit Referral" />

        <div class="py-12">
            <div class="max-w-7xl mx-auto sm:px-6 lg:px-8">
                <div class="mb-6 flex justify-between items-center">
                    <h1 class="text-2xl font-semibold text-gray-900 dark:text-white">Edit Referral</h1>
                    <Link :href="route('admin.referrals.index')" class="px-4 py-2 bg-gray-200 dark:bg-gray-700 rounded-md text-gray-700 dark:text-gray-300 text-sm font-medium hover:bg-gray-300 dark:hover:bg-gray-600 transition-colors duration-200">
                        Back to List
                    </Link>
                </div>

                <!-- Referral Details -->
                <div class="bg-white dark:bg-gray-800 overflow-hidden shadow-xl sm:rounded-lg p-6 mb-6">
                    <h2 class="text-lg font-medium text-gray-900 dark:text-white mb-4">Referral Details</h2>
                    
                    <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
                        <div>
                            <h3 class="text-sm font-medium text-gray-500 dark:text-gray-400">Referrer</h3>
                            <div class="mt-1">
                                <p class="text-base text-gray-900 dark:text-white">{{ referral.referrer?.name || 'Unknown' }}</p>
                                <p class="text-sm text-gray-500 dark:text-gray-400">{{ referral.referrer?.email || 'No email' }}</p>
                            </div>
                        </div>
                        
                        <div>
                            <h3 class="text-sm font-medium text-gray-500 dark:text-gray-400">Contact</h3>
                            <div class="mt-1">
                                <p class="text-base text-gray-900 dark:text-white">{{ referral.contact?.name || 'Unknown' }}</p>
                                <p class="text-sm text-gray-500 dark:text-gray-400">{{ referral.contact?.email || 'No email' }}</p>
                            </div>
                        </div>
                        
                        <div>
                            <h3 class="text-sm font-medium text-gray-500 dark:text-gray-400">Created Date</h3>
                            <p class="mt-1 text-base text-gray-900 dark:text-white">{{ formatDate(referral.created_at) }}</p>
                        </div>
                        
                        <div>
                            <h3 class="text-sm font-medium text-gray-500 dark:text-gray-400">Current Status</h3>
                            <p class="mt-1 text-base text-gray-900 dark:text-white">{{ referral.status.charAt(0).toUpperCase() + referral.status.slice(1) }}</p>
                        </div>
                    </div>
                </div>

                <!-- Edit Form -->
                <div class="bg-white dark:bg-gray-800 overflow-hidden shadow-xl sm:rounded-lg p-6">
                    <form @submit.prevent="submit">
                        <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
                            <div>
                                <label for="status" class="block text-sm font-medium text-gray-700 dark:text-gray-300">Status</label>
                                <select
                                    id="status"
                                    v-model="form.status"
                                    class="mt-1 block w-full pl-3 pr-10 py-2 text-base border-gray-300 focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm rounded-md dark:bg-gray-700 dark:border-gray-600 dark:text-white"
                                >
                                    <option value="pending">Pending</option>
                                    <option value="converted">Converted</option>
                                    <option value="paid">Paid</option>
                                </select>
                                <div v-if="form.errors.status" class="mt-1 text-sm text-red-600">{{ form.errors.status }}</div>
                            </div>
                            
                            <div>
                                <label for="contract_amount" class="block text-sm font-medium text-gray-700 dark:text-gray-300">Contract Amount</label>
                                <div class="mt-1 relative rounded-md shadow-sm">
                                    <div class="absolute inset-y-0 left-0 pl-3 flex items-center pointer-events-none">
                                        <span class="text-gray-500 dark:text-gray-400 sm:text-sm">$</span>
                                    </div>
                                    <input
                                        type="number"
                                        id="contract_amount"
                                        v-model="form.contract_amount"
                                        step="0.01"
                                        min="0"
                                        class="pl-7 block w-full pr-12 sm:text-sm border-gray-300 rounded-md focus:ring-indigo-500 focus:border-indigo-500 dark:bg-gray-700 dark:border-gray-600 dark:text-white"
                                        placeholder="0.00"
                                    />
                                </div>
                                <div v-if="form.errors.contract_amount" class="mt-1 text-sm text-red-600">{{ form.errors.contract_amount }}</div>
                                
                                <div v-if="form.contract_amount" class="mt-2 text-sm text-gray-500 dark:text-gray-400">
                                    Commission (10%): {{ formatCurrency(calculateCommission()) }}
                                </div>
                            </div>
                            
                            <div class="md:col-span-2">
                                <label for="notes" class="block text-sm font-medium text-gray-700 dark:text-gray-300">Notes</label>
                                <textarea
                                    id="notes"
                                    v-model="form.notes"
                                    rows="4"
                                    class="mt-1 block w-full sm:text-sm border-gray-300 rounded-md focus:ring-indigo-500 focus:border-indigo-500 dark:bg-gray-700 dark:border-gray-600 dark:text-white"
                                    placeholder="Add any notes about this referral..."
                                ></textarea>
                                <div v-if="form.errors.notes" class="mt-1 text-sm text-red-600">{{ form.errors.notes }}</div>
                            </div>
                        </div>
                        
                        <div class="mt-6 flex justify-end">
                            <Link
                                :href="route('admin.referrals.index')"
                                class="inline-flex items-center px-4 py-2 border border-gray-300 rounded-md shadow-sm text-sm font-medium text-gray-700 dark:text-gray-300 bg-white dark:bg-gray-700 hover:bg-gray-50 dark:hover:bg-gray-600 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500 mr-3"
                            >
                                Cancel
                            </Link>
                            <button
                                type="submit"
                                class="inline-flex items-center px-4 py-2 border border-transparent rounded-md shadow-sm text-sm font-medium text-white bg-indigo-600 hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500"
                                :disabled="form.processing"
                            >
                                Save Changes
                            </button>
                        </div>
                    </form>
                </div>
            </div>
        </div>
    </AppLayout>
</template>
