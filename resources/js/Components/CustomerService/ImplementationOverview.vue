<script setup>
const features = [
    {
        title: 'Advanced AI-powered chat interface',
        description: 'Real-time response generation',
        icon: 'M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z'
    },
    {
        title: 'Amazon Bedrock integration',
        description: 'Contextual knowledge retrieval',
        icon: 'M13 10V3L4 14h7v7l9-11h-7z'
    },
    {
        title: 'Real-time monitoring',
        description: 'Performance tracking and debugging',
        icon: 'M9 19v-6a2 2 0 00-2-2H5a2 2 0 00-2 2v6a2 2 0 002 2h2a2 2 0 002-2zm0 0V9a2 2 0 012-2h2a2 2 0 012 2v10m-6 0a2 2 0 002 2h2a2 2 0 002-2m0 0V5a2 2 0 012-2h2a2 2 0 012 2v14a2 2 0 01-2 2h-2a2 2 0 01-2-2z'
    },
    {
        title: 'Knowledge base visualization',
        description: 'Source tracking and attribution',
        icon: 'M4 6a2 2 0 012-2h2a2 2 0 012 2v2a2 2 0 01-2 2H6a2 2 0 01-2-2V6zM14 6a2 2 0 012-2h2a2 2 0 012 2v2a2 2 0 01-2 2h-2a2 2 0 01-2-2V6zM4 16a2 2 0 012-2h2a2 2 0 012 2v2a2 2 0 01-2 2H6a2 2 0 01-2-2v-2zM14 16a2 2 0 012-2h2a2 2 0 012 2v2a2 2 0 01-2 2h-2a2 2 0 01-2-2v-2z'
    },
    {
        title: 'Intelligent routing',
        description: 'User mood detection and smart escalation',
        icon: 'M14.828 14.828a4 4 0 01-5.656 0M9 10h.01M15 10h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z'
    },
    {
        title: 'Enterprise UI components',
        description: 'Fully customizable interface',
        icon: 'M4 5a1 1 0 011-1h14a1 1 0 011 1v2a1 1 0 01-1 1H5a1 1 0 01-1-1V5zM4 13a1 1 0 011-1h6a1 1 0 011 1v6a1 1 0 01-1 1H5a1 1 0 01-1-1v-6zM16 13a1 1 0 011-1h2a1 1 0 011 1v6a1 1 0 01-1 1h-2a1 1 0 01-1-1v-6z'
    }
];
</script>

<template>
    <section class="mt-16">
        <h2 class="text-2xl font-bold text-gray-900 dark:text-white mb-8">Use Case Example: AI Support With AWS Knowledge Base Integration</h2>
        
        <div class="bg-white dark:bg-gray-800 shadow-sm rounded-xl overflow-hidden mb-8 transform hover:shadow-lg transition-all duration-300">
            <div class="p-6">
                <h3 class="text-xl font-semibold text-gray-900 dark:text-white mb-4">Solution Overview</h3>
                <p class="text-gray-600 dark:text-gray-300 mb-6">
                    This example demonstrates how AIBrainL.ink integrates with Amazon Bedrock Knowledge Bases to create an intelligent customer support system. This implementation showcases just one of many possible configurations that can be customized to your needs.
                </p>
                
                <div class="space-y-6">
                    <h4 class="text-lg font-medium text-gray-900 dark:text-white">Key Features</h4>
                    <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
                        <div v-for="(feature, index) in features" :key="index" 
                             class="group bg-gray-50 dark:bg-gray-700/50 rounded-xl p-6 hover:bg-blue-50 dark:hover:bg-blue-900/20 transition-colors duration-300">
                            <div class="flex items-start">
                                <svg class="h-6 w-6 text-blue-500 mr-3 flex-shrink-0 transform group-hover:scale-110 transition-transform duration-300" 
                                     fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" :d="feature.icon" />
                                </svg>
                                <div>
                                    <h5 class="font-medium text-gray-900 dark:text-white">{{ feature.title }}</h5>
                                    <p class="mt-1 text-sm text-gray-600 dark:text-gray-300">{{ feature.description }}</p>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </section>
</template>

<style scoped>
.group {
    transition: all 0.3s ease-in-out;
}
.group:hover {
    transform: translateY(-2px);
}
</style>
