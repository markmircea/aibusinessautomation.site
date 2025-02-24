<script setup>
import { ref } from 'vue';
import { useForm } from '@inertiajs/vue3';

const form = useForm({
    name: '',
    email: '',
    company: '',
    message: '',
    solution: '',
    tech_stack: ''
});


import { usePage } from '@inertiajs/vue3';

const page = usePage();

const handleSubmit = () => {
    form.post(route('contact.submit'), {
        preserveScroll: true,
        preserveState: false,
        onSuccess: () => {
            form.reset();
        }
    });
};
</script>

<template>
    <section id="contact" class="py-20 bg-white dark:bg-gray-800">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
            <div class="text-center mb-16">
                <h2 class="text-3xl sm:text-4xl font-bold text-gray-900 dark:text-white mb-4">
                    Start Your Custom AI Journey
                </h2>
                <p class="max-w-3xl mx-auto text-lg text-gray-600 dark:text-gray-300 mb-4">
                    Ready to transform your business with personalized AI automation? Schedule a consultation with our experts and get a custom solution tailored to your needs.
                </p>
                <div class="flex flex-wrap justify-center gap-4 text-sm text-gray-500 dark:text-gray-400">
                    <div class="flex items-center">
                        <svg class="w-5 h-5 mr-2 text-green-500" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7" />
                        </svg>
                        Free Initial Consultation
                    </div>
                    <div class="flex items-center">
                        <svg class="w-5 h-5 mr-2 text-green-500" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7" />
                        </svg>
                        Dedicated Project Manager
                    </div>
                    <div class="flex items-center">
                        <svg class="w-5 h-5 mr-2 text-green-500" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7" />
                        </svg>
                        Custom Solution Design
                    </div>
                </div>
            </div>

            <div class="max-w-3xl mx-auto bg-gray-50 dark:bg-gray-700 rounded-lg shadow-xl overflow-hidden">
                <div class="p-8">
                    <form @submit.prevent="handleSubmit" class="space-y-6">
                        <div class="grid grid-cols-1 gap-6 sm:grid-cols-2">
                            <div>
                                <label for="name" class="block text-sm font-medium text-gray-700 dark:text-gray-300">Name</label>
                                <input
                                    type="text"
                                    id="name"
                                    v-model="form.name"
                                    class="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-blue-500 focus:ring-blue-500 dark:bg-gray-800 dark:border-gray-600 dark:text-white sm:text-sm"
                                >
                                <div v-if="form.errors.name" class="mt-1 text-sm text-red-600">{{ form.errors.name }}</div>
                            </div>

                            <div>
                                <label for="email" class="block text-sm font-medium text-gray-700 dark:text-gray-300">Email <span class="text-red-500">*</span></label>
                                <input
                                    type="email"
                                    id="email"
                                    v-model="form.email"
                                    class="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-blue-500 focus:ring-blue-500 dark:bg-gray-800 dark:border-gray-600 dark:text-white sm:text-sm"
                                    required
                                >
                                <div v-if="form.errors.email" class="mt-1 text-sm text-red-600">{{ form.errors.email }}</div>
                            </div>
                        </div>

                        <div>
                            <label for="company" class="block text-sm font-medium text-gray-700 dark:text-gray-300">Company</label>
                            <input
                                type="text"
                                id="company"
                                v-model="form.company"
                                class="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-blue-500 focus:ring-blue-500 dark:bg-gray-800 dark:border-gray-600 dark:text-white sm:text-sm"
                            >
                            <div v-if="form.errors.company" class="mt-1 text-sm text-red-600">{{ form.errors.company }}</div>
                        </div>

                        <div>
                            <label for="tech_stack" class="block text-sm font-medium text-gray-700 dark:text-gray-300">Current Tech Stack</label>
                            <p class="text-xs text-gray-500 dark:text-gray-400 mb-2">
                                List your current tools and systems that need integration (e.g., Salesforce, SAP, Microsoft 365)
                            </p>
                            <textarea
                                id="tech_stack"
                                v-model="form.tech_stack"
                                rows="2"
                                placeholder="E.g., Salesforce CRM, SAP ERP, Microsoft 365, Custom internal tools..."
                                class="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-blue-500 focus:ring-blue-500 dark:bg-gray-800 dark:border-gray-600 dark:text-white sm:text-sm"
                            ></textarea>
                            <div v-if="form.errors.tech_stack" class="mt-1 text-sm text-red-600">{{ form.errors.tech_stack }}</div>
                        </div>

                        <div>
                            <label for="message" class="block text-sm font-medium text-gray-700 dark:text-gray-300">Tell us about your needs <span class="text-red-500">*</span></label>
                            <p class="text-xs text-gray-500 dark:text-gray-400 mb-2">
                                Share your current challenges, processes you'd like to automate, and any specific requirements. We'll create custom integrations to fit your needs.
                            </p>
                            <textarea
                                id="message"
                                v-model="form.message"
                                rows="4"
                                placeholder="E.g., We're looking to automate our invoice processing system and integrate it with our current ERP. We need custom workflows for approval processes..."
                                class="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-blue-500 focus:ring-blue-500 dark:bg-gray-800 dark:border-gray-600 dark:text-white sm:text-sm"
                                required
                            ></textarea>
                            <div v-if="form.errors.message" class="mt-1 text-sm text-red-600">{{ form.errors.message }}</div>
                        </div>

                        <div class="flex justify-center">
                            <button
                                type="submit"
                                class="inline-flex items-center px-8 py-4 border border-transparent text-lg font-medium rounded-md shadow-sm text-white bg-blue-600 hover:bg-blue-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-blue-500 transition-colors duration-200 w-full sm:w-auto justify-center"
                                :disabled="form.processing"
                            >
                                <span v-if="form.processing">Sending...</span>
                                <span v-else>Schedule Free Consultation</span>
                                <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 ml-2" viewBox="0 0 20 20" fill="currentColor">
                                    <path fill-rule="evenodd" d="M10.293 3.293a1 1 0 011.414 0l6 6a1 1 0 010 1.414l-6 6a1 1 0 01-1.414-1.414L14.586 11H3a1 1 0 110-2h11.586l-4.293-4.293a1 1 0 010-1.414z" clip-rule="evenodd" />
                                </svg>
                            </button>
                        </div>
                    </form>
                </div>
            </div>

            <!-- Contact Information -->
            <div class="mt-16 grid grid-cols-1 gap-8 sm:grid-cols-3">
                <div class="text-center">
                    <div class="flex justify-center items-center mb-4">
                        <div class="p-3 bg-blue-100 dark:bg-blue-900 rounded-full">
                            <svg class="h-6 w-6 text-blue-600 dark:text-blue-300" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 5a2 2 0 012-2h3.28a1 1 0 01.948.684l1.498 4.493a1 1 0 01-.502 1.21l-2.257 1.13a11.042 11.042 0 005.516 5.516l1.13-2.257a1 1 0 011.21-.502l4.493 1.498a1 1 0 01.684.949V19a2 2 0 01-2 2h-1C9.716 21 3 14.284 3 6V5z" />
                            </svg>
                        </div>
                    </div>
                    <h3 class="text-lg font-medium text-gray-900 dark:text-white">Phone (SMS)</h3>
                    <p class="mt-2 text-base text-gray-600 dark:text-gray-300">+1 (248) 387-9399</p>
                </div>

                <div class="text-center">
                    <div class="flex justify-center items-center mb-4">
                        <div class="p-3 bg-blue-100 dark:bg-blue-900 rounded-full">
                            <svg class="h-6 w-6 text-blue-600 dark:text-blue-300" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 8l7.89 5.26a2 2 0 002.22 0L21 8M5 19h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v10a2 2 0 002 2z" />
                            </svg>
                        </div>
                    </div>
                    <h3 class="text-lg font-medium text-gray-900 dark:text-white">Email</h3>
                    <p class="mt-2 text-base text-gray-600 dark:text-gray-300">support@aibrainl.ink</p>
                </div>

                <div class="text-center">
                    <div class="flex justify-center items-center mb-4">
                        <div class="p-3 bg-blue-100 dark:bg-blue-900 rounded-full">
                            <svg class="h-6 w-6 text-blue-600 dark:text-blue-300" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17.657 16.657L13.414 20.9a1.998 1.998 0 01-2.827 0l-4.244-4.243a8 8 0 1111.314 0z" />
                                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 11a3 3 0 11-6 0 3 3 0 016 0z" />
                            </svg>
                        </div>
                    </div>
                    <h3 class="text-lg font-medium text-gray-900 dark:text-white">Location</h3>
                    <p class="mt-2 text-base text-gray-600 dark:text-gray-300">San Francisco, CA</p>
                </div>
            </div>
        </div>
    </section>
</template>

<style scoped>
input, select, textarea {
    @apply dark:placeholder-gray-400;
}
</style>
