<script setup>
import { Head } from '@inertiajs/vue3';
import AppLayout from '@/Layouts/AppLayout.vue';
import { ref, onMounted } from 'vue';

const props = defineProps({
    title: String,
    description: String,
    focus: String,
    keyPoint: String,
    sections: {
        type: Array,
        default: () => []
    }
});

const activeSection = ref('');

const updateActiveSection = () => {
    const sections = document.querySelectorAll('[data-section]');
    const scrollPosition = window.scrollY + 100;

    for (const section of sections) {
        if (section.offsetTop <= scrollPosition && 
            section.offsetTop + section.offsetHeight > scrollPosition) {
            activeSection.value = section.getAttribute('data-section');
            break;
        }
    }
};

const scrollToSection = (sectionId) => {
    const element = document.querySelector(`[data-section="${sectionId}"]`);
    if (element) {
        window.scrollTo({
            top: element.offsetTop - 80,
            behavior: 'smooth'
        });
    }
};

onMounted(() => {
    window.addEventListener('scroll', updateActiveSection);
    updateActiveSection();
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

                <!-- Main Content with Navigation -->
                <div class="relative flex gap-8">
                    <!-- Navigation Sidebar -->
                    <div v-if="sections.length" class="hidden lg:block w-64 sticky top-8 h-fit">
                        <nav class="bg-white dark:bg-gray-800 rounded-lg shadow-lg p-4">
                            <h3 class="text-lg font-semibold text-gray-900 dark:text-white mb-4">On this page</h3>
                            <ul class="space-y-2">
                                <li v-for="section in sections" :key="section.id">
                                    <button 
                                        @click="scrollToSection(section.id)"
                                        class="w-full text-left px-3 py-2 rounded-md text-sm transition-colors duration-200"
                                        :class="{
                                            'text-blue-600 dark:text-blue-400 bg-blue-50 dark:bg-blue-900/20 font-medium': 
                                                activeSection === section.id,
                                            'text-gray-600 dark:text-gray-300 hover:text-blue-600 dark:hover:text-blue-400 hover:bg-gray-50 dark:hover:bg-gray-700/50': 
                                                activeSection !== section.id
                                        }">
                                        {{ section.title }}
                                    </button>
                                </li>
                            </ul>
                        </nav>
                    </div>

                    <!-- Content Section -->
                    <div class="flex-1">
                        <div class="bg-white dark:bg-gray-800 overflow-hidden shadow-xl sm:rounded-lg">
                            <div class="p-6">
                                <slot></slot>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </AppLayout>
</template>

<style scoped>
.sticky {
    position: sticky;
    top: 2rem;
}
</style>
