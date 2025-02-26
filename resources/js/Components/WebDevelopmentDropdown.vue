<script setup>
import { ref } from 'vue';
import { Link } from '@inertiajs/vue3';
import Dropdown from '@/Components/Dropdown.vue';
import DropdownLink from '@/Components/DropdownLink.vue';

const webDevServices = [
    { name: 'E-commerce Platforms', route: 'web-development.ecommerce' },
    { name: 'Presentation Sites', route: 'web-development.presentation' },
    { name: 'Mobile Applications', route: 'web-development.mobile' },
    { name: 'Web Scraping/Automation', route: 'web-development.automation' }
];
</script>

<template>
    <div class="inline-flex items-center px-1 pt-1 border-b-2 border-transparent text-sm font-medium leading-5 text-gray-500 dark:text-gray-400 hover:text-gray-700 dark:hover:text-gray-300 hover:border-gray-300 dark:hover:border-gray-700 focus:outline-none focus:text-gray-700 dark:focus:text-gray-300 focus:border-gray-300 dark:focus:border-gray-700 transition duration-150 ease-in-out">
        <Dropdown align="left" width="48">
            <template #trigger>
                <button class="inline-flex items-center px-3 py-2 text-sm font-medium text-gray-600 hover:text-gray-900 dark:text-gray-300 dark:hover:text-white focus:outline-none transition ease-in-out duration-150">
                    Web Development
                    <svg class="ms-2 -me-0.5 h-4 w-4" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor">
                        <path stroke-linecap="round" stroke-linejoin="round" d="M19.5 8.25l-7.5 7.5-7.5-7.5" />
                    </svg>
                </button>
            </template>

            <template #content>
                <div class="w-full p-2">
                    <div v-for="service in webDevServices" :key="service.route" class="w-full">
                        <Link :href="route(service.route)" class="block w-full px-4 py-2 text-sm leading-5 text-gray-700 dark:text-gray-300 hover:bg-gray-100 dark:hover:bg-gray-800 focus:outline-none focus:bg-gray-100 dark:focus:bg-gray-800 transition duration-150 ease-in-out">
                            {{ service.name }}
                        </Link>
                    </div>
                </div>
            </template>
        </Dropdown>
    </div>
</template>
