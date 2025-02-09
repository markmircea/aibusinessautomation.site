<script setup>
const tools = [
    {
        category: 'Language & Communication',
        tools: [
            {
                name: 'OpenAI Integration',
                description: 'Advanced language models for natural customer interactions and content generation',
                uses: ['Customer inquiry processing', 'Response generation', 'Sentiment analysis']
            },
            {
                name: 'Claude AI',
                description: 'Sophisticated text processing and reasoning for complex customer support scenarios',
                uses: ['Context-aware responses', 'Multi-turn conversations', 'Complex problem solving']
            },
            {
                name: 'Multilingual Support',
                description: 'Language models supporting 200+ languages for global customer service',
                uses: ['Cross-language communication', 'Translation services', 'Cultural context awareness']
            }
        ]
    },
    {
        category: 'Knowledge Integration',
        tools: [
            {
                name: 'AWS Bedrock',
                description: 'Enterprise knowledge base integration for comprehensive support',
                uses: ['Documentation search', 'Context retrieval', 'Source attribution']
            },
            {
                name: 'Vector Search',
                description: 'Advanced search capabilities using Pinecone/Weaviate for accurate information retrieval',
                uses: ['Similar case finding', 'Knowledge base search', 'Relevant document retrieval']
            },
            {
                name: 'Document AI',
                description: 'Intelligent document processing for support documentation',
                uses: ['Document analysis', 'Information extraction', 'Content organization']
            }
        ]
    },
    {
        category: 'Customer Service Platforms',
        tools: [
            {
                name: 'Zendesk AI',
                description: 'Intelligent customer service automation and ticket management',
                uses: ['Ticket routing', 'Response prioritization', 'Customer history tracking']
            },
            {
                name: 'Salesforce Integration',
                description: 'CRM integration for comprehensive customer support',
                uses: ['Customer data management', 'Case history', 'Support analytics']
            },
            {
                name: 'Omnichannel Support',
                description: 'Multi-platform support integration',
                uses: ['Email support', 'Chat integration', 'Social media support']
            }
        ]
    },
    {
        category: 'Analytics & Monitoring',
        tools: [
            {
                name: 'Performance Analytics',
                description: 'Comprehensive support metrics and analysis',
                uses: ['Response time tracking', 'Customer satisfaction monitoring', 'Agent performance analytics']
            },
            {
                name: 'Sentiment Analysis',
                description: 'Real-time customer sentiment tracking',
                uses: ['Emotion detection', 'Satisfaction tracking', 'Priority routing']
            },
            {
                name: 'Quality Assurance',
                description: 'Automated response quality monitoring',
                uses: ['Response accuracy', 'Compliance checking', 'Style consistency']
            }
        ]
    }
];
</script>

<template>
    <section data-section="ai-tools" class="space-y-8">
        <h2 class="text-2xl font-bold text-gray-900 dark:text-white mb-6">Available AI Tools</h2>
        <p class="text-gray-600 dark:text-gray-300 mb-8">
            Our platform integrates with industry-leading AI tools to create powerful customer service automation solutions. Here are the key tools available for customer support implementation:
        </p>

        <div class="space-y-8">
            <div v-for="category in tools" :key="category.category" 
                 class="bg-white dark:bg-gray-800 rounded-xl shadow-sm overflow-hidden">
                <div class="p-6">
                    <h3 class="text-xl font-semibold text-gray-900 dark:text-white mb-6">{{ category.category }}</h3>
                    <div class="grid grid-cols-1 lg:grid-cols-3 gap-6">
                        <div v-for="tool in category.tools" :key="tool.name"
                             class="bg-gray-50 dark:bg-gray-700/50 rounded-xl p-6 hover:bg-blue-50 dark:hover:bg-blue-900/20 transition-all duration-300">
                            <h4 class="text-lg font-medium text-gray-900 dark:text-white mb-2">{{ tool.name }}</h4>
                            <p class="text-gray-600 dark:text-gray-300 mb-4">{{ tool.description }}</p>
                            <div class="space-y-2">
                                <p class="text-sm font-medium text-gray-900 dark:text-white">Common Uses:</p>
                                <ul class="space-y-1">
                                    <li v-for="use in tool.uses" :key="use" 
                                        class="flex items-start text-sm">
                                        <svg class="h-5 w-5 text-blue-500 mr-2 flex-shrink-0" 
                                             fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" 
                                                  d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z" />
                                        </svg>
                                        <span class="text-gray-600 dark:text-gray-300">{{ use }}</span>
                                    </li>
                                </ul>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </section>
</template>

<style scoped>
.hover\:bg-blue-50:hover {
    background-color: rgba(59, 130, 246, 0.05);
}
</style>
