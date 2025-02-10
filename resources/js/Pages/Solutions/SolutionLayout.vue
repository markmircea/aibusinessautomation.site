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
const expandedSections = ref(new Set());

const updateActiveSection = () => {
    const sections = document.querySelectorAll('[data-section]');
    const scrollPosition = window.scrollY + 100;

    for (const section of sections) {
        if (section.offsetTop <= scrollPosition && 
            section.offsetTop + section.offsetHeight > scrollPosition) {
            const sectionId = section.getAttribute('data-section');
            activeSection.value = sectionId;
            
            // Expand parent section if subsection is active
            if (sectionId.includes('-')) {
                const parentSection = sectionId.split('-')[0];
                expandedSections.value.add(parentSection);
            }
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

const toggleSection = (sectionId) => {
    if (expandedSections.value.has(sectionId)) {
        expandedSections.value.delete(sectionId);
    } else {
        expandedSections.value.add(sectionId);
    }
};

const isSectionExpanded = (sectionId) => {
    return expandedSections.value.has(sectionId);
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
            <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
                <div class="flex gap-8">
                    <!-- Navigation Sidebar -->
                    <div v-if="sections.length" class="hidden lg:block w-64 sticky" style="height: fit-content; top: 2rem;">
                        <nav class="bg-white dark:bg-gray-800 rounded-lg shadow-lg p-4">
                            <h3 class="text-lg font-semibold text-gray-900 dark:text-white mb-4">On this page</h3>
                            <ul class="space-y-2">
                                <li v-for="section in sections" :key="section.id" class="relative">
                                    <div class="flex items-center">
                                        <button v-if="section.subsections"
                                                @click="toggleSection(section.id)"
                                                class="absolute left-0 top-2 w-4 h-4 flex items-center justify-center">
                                            <svg class="w-3 h-3 transition-transform duration-200"
                                                 :class="{ 'rotate-90': isSectionExpanded(section.id) }"
                                                 fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7" />
                                            </svg>
                                        </button>
                                        <button 
                                            @click="scrollToSection(section.id)"
                                            class="w-full text-left px-3 py-2 rounded-md text-sm transition-colors duration-200"
                                            :class="{
                                                'pl-7': section.subsections,
                                                'text-blue-600 dark:text-blue-400 bg-blue-50 dark:bg-blue-900/20 font-medium': 
                                                    activeSection === section.id,
                                                'text-gray-600 dark:text-gray-300 hover:text-blue-600 dark:hover:text-blue-400 hover:bg-gray-50 dark:hover:bg-gray-700/50': 
                                                    activeSection !== section.id
                                            }">
                                            {{ section.title }}
                                        </button>
                                    </div>

                                    <!-- Subsections -->
                                    <ul v-if="section.subsections && isSectionExpanded(section.id)"
                                        class="mt-1 ml-4 pl-3 border-l border-gray-200 dark:border-gray-700 space-y-1">
                                        <li v-for="subsection in section.subsections" :key="subsection.id">
                                            <button 
                                                @click="scrollToSection(subsection.id)"
                                                class="w-full text-left px-3 py-1.5 rounded-md text-sm transition-colors duration-200"
                                                :class="{
                                                    'text-blue-600 dark:text-blue-400 bg-blue-50 dark:bg-blue-900/20 font-medium': 
                                                        activeSection === subsection.id,
                                                    'text-gray-500 dark:text-gray-400 hover:text-blue-600 dark:hover:text-blue-400 hover:bg-gray-50 dark:hover:bg-gray-700/50': 
                                                        activeSection !== subsection.id
                                                }">
                                                {{ subsection.title }}
                                            </button>
                                        </li>
                                    </ul>
                                </li>
                            </ul>
                        </nav>
                    </div>

                    <!-- Main Content -->
                    <div class="flex-1 max-w-5xl">
                        <!-- Hero Section
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
                        </div> -->

                        <!-- Content Section -->
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