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
                name: 'Gemini',
                description: "Google's advanced language model for comprehensive customer support",
                uses: ['Multilingual support', 'Visual query handling', 'Complex reasoning']
            },
            {
                name: 'Mistral AI',
                description: 'High-performance language models for efficient customer interactions',
                uses: ['Fast response generation', 'Efficient processing', 'Accurate answers']
            },
            {
                name: 'Cohere',
                description: 'Enterprise-grade language AI for business applications',
                uses: ['Content classification', 'Semantic search', 'Customer intent analysis']
            },
            {
                name: 'LangChain',
                description: 'Framework for building sophisticated AI applications',
                uses: ['Custom workflow creation', 'Tool integration', 'Complex interaction handling']
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
                description: 'Advanced search using Pinecone/Weaviate/Qdrant for accurate information retrieval',
                uses: ['Similar case finding', 'Knowledge base search', 'Relevant document retrieval']
            },
            {
                name: 'Document AI',
                description: 'Intelligent document processing for support documentation',
                uses: ['Document analysis', 'Information extraction', 'Content organization']
            },
            {
                name: 'Elasticsearch',
                description: 'Intelligent search and analytics engine with ML capabilities',
                uses: ['Full-text search', 'Analytics', 'Real-time insights']
            },
            {
                name: 'Needle',
                description: 'Production-ready RAG for document search and retrieval',
                uses: ['Knowledge retrieval', 'Context management', 'Source tracking']
            },
            {
                name: 'MemoryMesh',
                description: 'Knowledge graph server for enhanced context management',
                uses: ['Conversation history', 'Knowledge relationships', 'Context preservation']
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
                name: 'HubSpot',
                description: 'AI-powered marketing automation and customer engagement',
                uses: ['Customer segmentation', 'Automated workflows', 'Engagement tracking']
            },
            {
                name: 'Slack AI',
                description: 'Intelligent message routing and automated responses',
                uses: ['Team collaboration', 'Automated notifications', 'Customer chat integration']
            },
            {
                name: 'Microsoft Teams',
                description: 'AI-powered meeting transcription and collaboration',
                uses: ['Customer meetings', 'Support coordination', 'Team communication']
            },
            {
                name: 'Notion AI',
                description: 'Smart workspace organization and knowledge management',
                uses: ['Support documentation', 'Team knowledge base', 'Process documentation']
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
                name: 'Datadog',
                description: 'Intelligent monitoring and performance management',
                uses: ['System monitoring', 'Performance tracking', 'Alert management']
            },
            {
                name: 'Grafana',
                description: 'AI-powered metrics visualization and anomaly detection',
                uses: ['Real-time dashboards', 'Trend analysis', 'Performance visualization']
            },
            {
                name: 'Axiom',
                description: 'Advanced log analysis and event data processing',
                uses: ['Log analysis', 'Event tracking', 'Performance monitoring']
            },
            {
                name: 'Sentry',
                description: 'Real-time error tracking and monitoring',
                uses: ['Error detection', 'Performance monitoring', 'Issue resolution']
            }
        ]
    },
    {
        category: 'Communication & Channels',
        tools: [
            {
                name: 'Omnichannel Support',
                description: 'Multi-platform support integration',
                uses: ['Email support', 'Chat integration', 'Social media support']
            },
            {
                name: 'Discord Integration',
                description: 'Community management automation and support',
                uses: ['Community support', 'Automated responses', 'User engagement']
            },
            {
                name: 'Telegram Bot',
                description: 'Automated messaging and support automation',
                uses: ['Instant responses', 'Automated updates', 'User notifications']
            },
            {
                name: 'Social Media Integration',
                description: 'Support across social platforms (X/Twitter, etc.)',
                uses: ['Social monitoring', 'Response management', 'Engagement tracking']
            },
            {
                name: 'WeCom Bot',
                description: 'Enterprise messaging and support automation',
                uses: ['Team notifications', 'Customer communication', 'Automated alerts']
            }
        ]
    },
    {
        category: 'Security & Compliance',
        tools: [
            {
                name: 'Auth0',
                description: 'AI-powered authentication and identity management',
                uses: ['Secure access', 'Identity verification', 'User management']
            },
            {
                name: 'Cloudflare AI',
                description: 'Intelligent threat detection and security',
                uses: ['DDoS protection', 'Bot detection', 'Access control']
            },
            {
                name: 'Descope',
                description: 'Advanced user management and audit capabilities',
                uses: ['Access management', 'Audit logging', 'Compliance tracking']
            }
        ]
    }
];
</script>

<template>
    <section data-section="ai-tools" class="space-y-8">
        <h2 class="text-2xl font-bold text-gray-900 dark:text-white mb-6">Available AI Tools</h2>
        <p class="text-gray-600 dark:text-gray-300 mb-8">
            Our platform integrates with industry-leading AI tools to create powerful customer service automation solutions. Here are the key tools available for customer support implementation
             (we are continuously developing additional tools to meet our business partners needs):
        </p>

        <div class="space-y-8">
            <div v-for="(category, index) in tools" :key="category.category" 
                 :data-section="`ai-tools-${['language', 'knowledge', 'platforms', 'analytics', 'channels', 'security'][index]}`"
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
