<script setup>
const capabilities = {
    automation: [
        {
            title: 'Intelligent Query Resolution',
            description: 'Advanced natural language understanding for accurate, context-aware responses to customer inquiries across multiple languages.',
            icon: 'M8 10h.01M12 10h.01M16 10h.01M9 16H5a2 2 0 01-2-2V6a2 2 0 012-2h14a2 2 0 012 2v8a2 2 0 01-2 2h-5l-5 5v-5z'
        },
        {
            title: 'Smart Routing',
            description: 'Automated ticket assignment and prioritization based on content, urgency, and available resources.',
            icon: 'M13 10V3L4 14h7v7l9-11h-7z'
        }
    ],
    integration: [
        {
            title: 'Knowledge Integration',
            description: 'Seamless connection with your existing knowledge bases and documentation for accurate, up-to-date customer support.',
            icon: 'M19 11H5m14 0a2 2 0 012 2v6a2 2 0 01-2 2H5a2 2 0 01-2-2v-6a2 2 0 012-2m14 0V9a2 2 0 00-2-2M5 11V9a2 2 0 012-2m0 0V5a2 2 0 012-2h6a2 2 0 012 2v2M7 7h10'
        },
        {
            title: 'Omnichannel Support',
            description: 'Consistent customer service across all channels - chat, email, social media, and more - with unified conversation history.',
            icon: 'M4 6a2 2 0 012-2h2a2 2 0 012 2v2a2 2 0 01-2 2H6a2 2 0 01-2-2V6zM14 6a2 2 0 012-2h2a2 2 0 012 2v2a2 2 0 01-2 2h-2a2 2 0 01-2-2V6zM4 16a2 2 0 012-2h2a2 2 0 012 2v2a2 2 0 01-2 2H6a2 2 0 01-2-2v-2zM14 16a2 2 0 012-2h2a2 2 0 012 2v2a2 2 0 01-2 2h-2a2 2 0 01-2-2v-2z'
        }
    ],
    learning: [
        {
            title: 'Continuous Learning',
            description: 'AI system that learns from each interaction, improving response accuracy and adapting to new support scenarios.',
            icon: 'M13 10V3L4 14h7v7l9-11h-7z'
        },
        {
            title: 'Performance Optimization',
            description: 'Self-improving system that analyzes patterns and optimizes response strategies based on success metrics.',
            icon: 'M9 19v-6a2 2 0 00-2-2H5a2 2 0 00-2 2v6a2 2 0 002 2h2a2 2 0 002-2zm0 0V9a2 2 0 012-2h2a2 2 0 012 2v10m-6 0a2 2 0 002 2h2a2 2 0 002-2m0 0V5a2 2 0 012-2h2a2 2 0 012 2v14a2 2 0 01-2 2h-2a2 2 0 01-2-2z'
        }
    ]
};
</script>

<template>
    <section data-section="capabilities">
        <div class="mb-8">
            <h2 class="text-2xl font-bold text-gray-900 dark:text-white">Core Capabilities</h2>
            <p class="mt-2 text-gray-600 dark:text-gray-300">Our AI integration platform empowers businesses to transform their operations through intelligent automation. We help organizations cut costs, improve performance, and streamline workflows by seamlessly integrating AI into their existing processes. While customer service automation is one powerful use case, our solutions can be tailored to an infinite number of business scenarios, each customized to your specific needs and objectives.</p>
        </div>

        <!-- Automation Features -->
        <div data-section="capabilities-automation" class="mb-12">
            <h3 class="text-xl font-semibold text-gray-900 dark:text-white mb-6">Automation Features</h3>
            <div class="grid grid-cols-1 md:grid-cols-2 gap-8">
                <div v-for="capability in capabilities.automation" :key="capability.title" 
                     class="group bg-white dark:bg-gray-800 rounded-xl p-6 shadow-sm hover:shadow-md transition-all duration-300">
                    <div class="flex items-start space-x-4">
                        <div class="flex-shrink-0">
                            <div class="flex items-center justify-center h-12 w-12 rounded-md bg-blue-500 text-white group-hover:bg-blue-600 transition-colors duration-300">
                                <svg class="h-6 w-6 transform group-hover:scale-110 transition-transform duration-300" 
                                     fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" :d="capability.icon" />
                                </svg>
                            </div>
                        </div>
                        <div>
                            <h4 class="text-lg font-medium text-gray-900 dark:text-white group-hover:text-blue-500 transition-colors duration-300">
                                {{ capability.title }}
                            </h4>
                            <p class="mt-2 text-gray-600 dark:text-gray-300">{{ capability.description }}</p>
                        </div>
                    </div>
                </div>
            </div>
        </div>

        <!-- Integration Options -->
        <div data-section="capabilities-integration" class="mb-12">
            <h3 class="text-xl font-semibold text-gray-900 dark:text-white mb-6">Integration Options</h3>
            <div class="grid grid-cols-1 md:grid-cols-2 gap-8">
                <div v-for="capability in capabilities.integration" :key="capability.title" 
                     class="group bg-white dark:bg-gray-800 rounded-xl p-6 shadow-sm hover:shadow-md transition-all duration-300">
                    <div class="flex items-start space-x-4">
                        <div class="flex-shrink-0">
                            <div class="flex items-center justify-center h-12 w-12 rounded-md bg-blue-500 text-white group-hover:bg-blue-600 transition-colors duration-300">
                                <svg class="h-6 w-6 transform group-hover:scale-110 transition-transform duration-300" 
                                     fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" :d="capability.icon" />
                                </svg>
                            </div>
                        </div>
                        <div>
                            <h4 class="text-lg font-medium text-gray-900 dark:text-white group-hover:text-blue-500 transition-colors duration-300">
                                {{ capability.title }}
                            </h4>
                            <p class="mt-2 text-gray-600 dark:text-gray-300">{{ capability.description }}</p>
                        </div>
                    </div>
                </div>
            </div>
        </div>

        <!-- Learning System -->
        <div data-section="capabilities-learning" class="mb-12">
            <h3 class="text-xl font-semibold text-gray-900 dark:text-white mb-6">Learning System</h3>
            <div class="grid grid-cols-1 md:grid-cols-2 gap-8">
                <div v-for="capability in capabilities.learning" :key="capability.title" 
                     class="group bg-white dark:bg-gray-800 rounded-xl p-6 shadow-sm hover:shadow-md transition-all duration-300">
                    <div class="flex items-start space-x-4">
                        <div class="flex-shrink-0">
                            <div class="flex items-center justify-center h-12 w-12 rounded-md bg-blue-500 text-white group-hover:bg-blue-600 transition-colors duration-300">
                                <svg class="h-6 w-6 transform group-hover:scale-110 transition-transform duration-300" 
                                     fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" :d="capability.icon" />
                                </svg>
                            </div>
                        </div>
                        <div>
                            <h4 class="text-lg font-medium text-gray-900 dark:text-white group-hover:text-blue-500 transition-colors duration-300">
                                {{ capability.title }}
                            </h4>
                            <p class="mt-2 text-gray-600 dark:text-gray-300">{{ capability.description }}</p>
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
