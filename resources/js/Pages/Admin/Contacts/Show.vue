<script setup>
import { ref } from 'vue';
import AppLayout from '@/Layouts/AppLayout.vue';
import { Head, Link } from '@inertiajs/vue3';

const props = defineProps({
    contact: Object,
});

const formatDate = (dateString) => {
    if (!dateString) return '';
    const date = new Date(dateString);
    return date.toLocaleDateString() + ' ' + date.toLocaleTimeString();
};
</script>

<template>
    <AppLayout title="Contact Details">
        <Head title="Contact Details" />

        <div class="py-12">
            <div class="max-w-7xl mx-auto sm:px-6 lg:px-8">
                <div class="mb-6 flex justify-between items-center">
                    <h1 class="text-2xl font-semibold text-gray-900 dark:text-white">Contact Details</h1>
                    <Link :href="route('admin.contacts.index')" class="px-4 py-2 bg-gray-200 dark:bg-gray-700 rounded-md text-gray-700 dark:text-gray-300 text-sm font-medium hover:bg-gray-300 dark:hover:bg-gray-600 transition-colors duration-200">
                        Back to Contacts
                    </Link>
                </div>

                <!-- Contact Details -->
                <div class="bg-white dark:bg-gray-800 overflow-hidden shadow-xl sm:rounded-lg p-6">
                    <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
                        <div>
                            <h3 class="text-sm font-medium text-gray-500 dark:text-gray-400">Submission Date</h3>
                            <p class="mt-1 text-base text-gray-900 dark:text-white">{{ formatDate(contact.created_at) }}</p>
                        </div>
                        
                        <div v-if="contact.referral_code">
                            <h3 class="text-sm font-medium text-gray-500 dark:text-gray-400">Referral Code</h3>
                            <p class="mt-1">
                                <span class="px-2 py-1 inline-flex text-sm leading-5 font-semibold rounded-full bg-green-100 text-green-800 dark:bg-green-900 dark:text-green-300">
                                    {{ contact.referral_code }}
                                </span>
                            </p>
                        </div>
                        
                        <div>
                            <h3 class="text-sm font-medium text-gray-500 dark:text-gray-400">Name</h3>
                            <p class="mt-1 text-base text-gray-900 dark:text-white">{{ contact.name || 'Not provided' }}</p>
                        </div>
                        
                        <div>
                            <h3 class="text-sm font-medium text-gray-500 dark:text-gray-400">Email</h3>
                            <p class="mt-1 text-base text-gray-900 dark:text-white">{{ contact.email }}</p>
                        </div>
                        
                        <div>
                            <h3 class="text-sm font-medium text-gray-500 dark:text-gray-400">Company</h3>
                            <p class="mt-1 text-base text-gray-900 dark:text-white">{{ contact.company || 'Not provided' }}</p>
                        </div>
                        
                        <div v-if="contact.solution">
                            <h3 class="text-sm font-medium text-gray-500 dark:text-gray-400">Solution</h3>
                            <p class="mt-1 text-base text-gray-900 dark:text-white">{{ contact.solution }}</p>
                        </div>
                    </div>
                    
                    <div class="mt-6">
                        <h3 class="text-sm font-medium text-gray-500 dark:text-gray-400">Tech Stack</h3>
                        <p class="mt-1 text-base text-gray-900 dark:text-white whitespace-pre-line">{{ contact.tech_stack || 'Not provided' }}</p>
                    </div>
                    
                    <div class="mt-6">
                        <h3 class="text-sm font-medium text-gray-500 dark:text-gray-400">Message</h3>
                        <div class="mt-1 p-4 bg-gray-50 dark:bg-gray-700 rounded-md">
                            <p class="text-base text-gray-900 dark:text-white whitespace-pre-line">{{ contact.message }}</p>
                        </div>
                    </div>
                    
                    <!-- Actions -->
                    <div class="mt-8 flex justify-end">
                        <a :href="`mailto:${contact.email}`" class="inline-flex items-center px-4 py-2 bg-blue-600 border border-transparent rounded-md font-semibold text-xs text-white uppercase tracking-widest hover:bg-blue-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-blue-500 transition-colors duration-200">
                            Reply via Email
                        </a>
                    </div>
                </div>
            </div>
        </div>
    </AppLayout>
</template>
