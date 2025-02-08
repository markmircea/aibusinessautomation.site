<script setup>
import { Head } from '@inertiajs/vue3';
import AppLayout from '@/Layouts/AppLayout.vue';

defineProps({
    title: String,
    description: String,
    focus: String,
    keyPoint: String,
});
</script>

<template>
    <AppLayout>
        <Head>
            <title>{{ title }} - AutomateAI</title>
            <meta name="description" :content="description" />
        </Head>

        <div class="py-12">
            <div class="max-w-7xl mx-auto sm:px-6 lg:px-8">
                <!-- Hero Section -->
                <div class="bg-gradient-to-r from-blue-600 to-blue-800 rounded-lg shadow-xl p-8 mb-8 text-white">
                    <h1 class="text-3xl font-bold mb-4">{{ title }}</h1>
                    <p class="text-xl text-blue-100">{{ description }}</p>
                    <div class="mt-6 grid grid-cols-1 md:grid-cols-2 gap-4">
                        <div class="bg-white/10 rounded-lg p-4">
                            <h3 class="font-semibold text-lg mb-2">Focus Areas</h3>
                            <p>{{ focus }}</p>
                        </div>
                        <div class="bg-white/10 rounded-lg p-4">
                            <h3 class="font-semibold text-lg mb-2">Key Benefits</h3>
                            <p>{{ keyPoint }}</p>
                        </div>
                    </div>
                </div>

                <!-- Content Section -->
                <div class="bg-white dark:bg-gray-800 overflow-hidden shadow-xl sm:rounded-lg">
                    <div class="p-6">
                        <slot></slot>
                    </div>
                </div>
            </div>
        </div>
    </AppLayout>
</template>
