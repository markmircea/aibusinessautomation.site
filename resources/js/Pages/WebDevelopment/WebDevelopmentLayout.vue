<script setup>
import { Head } from '@inertiajs/vue3';
import AppLayout from '@/Layouts/AppLayout.vue';
import { onMounted } from 'vue';
import { gsap } from 'gsap';

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

onMounted(() => {
    // Add animation for content sections
    gsap.from('.content-section', {
        duration: 0.8,
        y: 30,
        opacity: 0,
        stagger: 0.2,
        ease: 'power2.out',
        scrollTrigger: {
            trigger: '.content-section',
            start: 'top 80%',
        }
    });
});
</script>

<template>
    <AppLayout>
        <Head>
            <title>{{ title }} - AIBrainL.ink</title>
            <meta name="description" :content="description" />
        </Head>

        <div class="min-h-screen bg-white dark:bg-gray-900">
            <!-- Main Content -->
            <div class="w-full">
                <slot></slot>
            </div>

            <!-- Quick Navigation Dots (Optional) -->
            <div v-if="sections.length" class="fixed right-4 top-1/2 transform -translate-y-1/2 z-50 hidden lg:block">
                <div class="flex flex-col items-center space-y-4">
                    <a v-for="section in sections" :key="section.id" 
                       :href="`#${section.id}`"
                       class="w-3 h-3 rounded-full bg-gray-300 dark:bg-gray-600 hover:bg-blue-500 dark:hover:bg-blue-400 transition-colors duration-200"
                       :title="section.title"></a>
                </div>
            </div>
        </div>
    </AppLayout>
</template>

<style scoped>
html {
    scroll-behavior: smooth;
}

.content-section {
    opacity: 0; /* Start invisible for animation */
}
</style>
