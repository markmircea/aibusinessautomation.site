<script setup>
const awsFeatures = [
    {
        title: 'Seamless Knowledge Base Connection',
        description: 'Direct integration with AWS Knowledge Bases for contextual information retrieval',
        icon: 'M13 10V3L4 14h7v7l9-11h-7z'
    },
    {
        title: 'Multi-Knowledge Base Support',
        description: 'Support for multiple knowledge bases with automatic source attribution',
        icon: 'M4 7v10c0 2.21 3.582 4 8 4s8-1.79 8-4V7M4 7c0 2.21 3.582 4 8 4s8-1.79 8-4M4 7c0-2.21 3.582-4 8-4s8 1.79 8 4m0 5c0 2.21-3.582 4-8 4s-8-1.79-8-4'
    },
    {
        title: 'Real-time Synchronization',
        description: 'Real-time knowledge base updates and synchronization',
        icon: 'M4 4v5h.582m15.356 2A8.001 8.001 0 004.582 9m0 0H9m11 11v-5h-.581m0 0a8.003 8.003 0 01-15.357-2m15.357 2H15'
    }
];

const configOptions = [
    'Full interface with analytics',
    'Chat-only deployment',
    'Custom UI layouts',
    'Multiple knowledge base support'
];

const enterpriseFeatures = [
    'SSO integration',
    'Role-based access control',
    'Audit logging',
    'Performance monitoring'
];
</script>

<template>
    <div class="bg-white dark:bg-gray-800 shadow-sm rounded-xl overflow-hidden mb-8 transform hover:shadow-lg transition-all duration-300">
        <div class="p-6">
            <h3 class="text-xl font-semibold text-gray-900 dark:text-white mb-6">Technical Integration</h3>
            
            <div class="space-y-8">
                <!-- AWS Integration -->
                <div>
                    <h4 class="text-lg font-medium text-gray-900 dark:text-white mb-4">Amazon Bedrock Integration</h4>
                    <div class="group bg-gray-50 dark:bg-gray-700/50 rounded-xl p-6 hover:bg-blue-50 dark:hover:bg-blue-900/20 transition-colors duration-300">
                        <ul class="space-y-4">
                            <li v-for="(feature, index) in awsFeatures" :key="index" class="flex items-start">
                                <svg class="h-6 w-6 text-blue-500 mr-3 flex-shrink-0 transform group-hover:scale-110 transition-transform duration-300" 
                                     fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" :d="feature.icon" />
                                </svg>
                                <div>
                                    <span class="font-medium text-gray-900 dark:text-white">{{ feature.title }}</span>
                                    <p class="mt-1 text-gray-600 dark:text-gray-300">{{ feature.description }}</p>
                                </div>
                            </li>
                        </ul>
                    </div>
                </div>

                <!-- Deployment Options -->
                <div>
                    <h4 class="text-lg font-medium text-gray-900 dark:text-white mb-4">Flexible Deployment</h4>
                    <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
                        <div class="group bg-gray-50 dark:bg-gray-700/50 rounded-xl p-6 hover:bg-blue-50 dark:hover:bg-blue-900/20 transition-colors duration-300">
                            <h5 class="font-medium text-gray-900 dark:text-white mb-4 flex items-center">
                                <svg class="h-5 w-5 text-blue-500 mr-2 transform group-hover:scale-110 transition-transform duration-300" 
                                     fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" 
                                          d="M10.325 4.317c.426-1.756 2.924-1.756 3.35 0a1.724 1.724 0 002.573 1.066c1.543-.94 3.31.826 2.37 2.37a1.724 1.724 0 001.065 2.572c1.756.426 1.756 2.924 0 3.35a1.724 1.724 0 00-1.066 2.573c.94 1.543-.826 3.31-2.37 2.37a1.724 1.724 0 00-2.572 1.065c-.426 1.756-2.924 1.756-3.35 0a1.724 1.724 0 00-2.573-1.066c-1.543.94-3.31-.826-2.37-2.37a1.724 1.724 0 00-1.065-2.572c-1.756-.426-1.756-2.924 0-3.35a1.724 1.724 0 001.066-2.573c-.94-1.543.826-3.31 2.37-2.37.996.608 2.296.07 2.572-1.065z" />
                                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" 
                                          d="M15 12a3 3 0 11-6 0 3 3 0 016 0z" />
                                </svg>
                                Configuration Options
                            </h5>
                            <ul class="space-y-2 text-gray-600 dark:text-gray-300">
                                <li v-for="(option, index) in configOptions" :key="index" class="flex items-center">
                                    <svg class="h-4 w-4 text-blue-500 mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7" />
                                    </svg>
                                    {{ option }}
                                </li>
                            </ul>
                        </div>
                        <div class="group bg-gray-50 dark:bg-gray-700/50 rounded-xl p-6 hover:bg-blue-50 dark:hover:bg-blue-900/20 transition-colors duration-300">
                            <h5 class="font-medium text-gray-900 dark:text-white mb-4 flex items-center">
                                <svg class="h-5 w-5 text-blue-500 mr-2 transform group-hover:scale-110 transition-transform duration-300" 
                                     fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" 
                                          d="M9 12l2 2 4-4m5.618-4.016A11.955 11.955 0 0112 2.944a11.955 11.955 0 01-8.618 3.04A12.02 12.02 0 003 9c0 5.591 3.824 10.29 9 11.622 5.176-1.332 9-6.03 9-11.622 0-1.042-.133-2.052-.382-3.016z" />
                                </svg>
                                Enterprise Features
                            </h5>
                            <ul class="space-y-2 text-gray-600 dark:text-gray-300">
                                <li v-for="(feature, index) in enterpriseFeatures" :key="index" class="flex items-center">
                                    <svg class="h-4 w-4 text-blue-500 mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7" />
                                    </svg>
                                    {{ feature }}
                                </li>
                            </ul>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<style scoped>
.group {
    transition: all 0.3s ease-in-out;
}
.group:hover {
    transform: translateY(-2px);
}
</style>
