<script setup>
import SolutionLayout from './SolutionLayout.vue';
import Hero from '@/Components/CustomerService/Hero.vue';
import CoreCapabilities from '@/Components/CustomerService/CoreCapabilities.vue';
import ImplementationOverview from '@/Components/CustomerService/ImplementationOverview.vue';
import TechnicalIntegration from '@/Components/CustomerService/TechnicalIntegration.vue';
import PerformanceMetrics from '@/Components/CustomerService/PerformanceMetrics.vue';
import AITools from '@/Components/CustomerService/AITools.vue';

const solutionData = {
    title: 'AI-Powered Customer Service Automation',
    description: 'Transform your customer support with AIBrainL.ink, delivering instant, personalized service through intelligent automation that understands, learns, and evolves with your business.',
    focus: 'Seamlessly integrate AI with your knowledge base to provide 24/7 support, reduce response times, and maintain consistent service quality across all channels.',
    keyPoint: 'Achieve 70% reduction in support costs while improving customer satisfaction through intelligent automation that handles routine inquiries and empowers agents to focus on complex issues.',
    sections: [
        { 
            id: 'overview', 
            title: 'Overview' 
        },
        { 
            id: 'capabilities', 
            title: 'Core Capabilities',
            subsections: [
                { id: 'capabilities-automation', title: 'Automation Features' },
                { id: 'capabilities-integration', title: 'Integration Options' },
                { id: 'capabilities-learning', title: 'Learning System' }
            ]
        },
        { 
            id: 'implementation', 
            title: 'Implementation Example',
            subsections: [
                { id: 'implementation-setup', title: 'Initial Setup' },
                { id: 'implementation-workflow', title: 'Workflow Design' },
                { id: 'implementation-deployment', title: 'Deployment Steps' }
            ]
        },
        { 
            id: 'technical', 
            title: 'Technical Details' 
        },
        { 
            id: 'metrics', 
            title: 'Performance Metrics' 
        },
        { 
            id: 'ai-tools', 
            title: 'Available AI Tools',
            subsections: [
                { id: 'ai-tools-language', title: 'Language & Communication' },
                { id: 'ai-tools-knowledge', title: 'Knowledge Integration' },
                { id: 'ai-tools-platforms', title: 'Service Platforms' },
                { id: 'ai-tools-analytics', title: 'Analytics & Monitoring' },
                { id: 'ai-tools-channels', title: 'Communication Channels' },
                { id: 'ai-tools-security', title: 'Security & Compliance' }
            ]
        }
    ]
};
</script>

<template>
    <SolutionLayout v-bind="solutionData">
        <div class="space-y-12">
            <div data-section="overview">
                <Hero />
            </div>

            <div data-section="capabilities">
                <div data-section="capabilities-automation"></div>
                <div data-section="capabilities-integration"></div>
                <div data-section="capabilities-learning"></div>
                <CoreCapabilities />
            </div>

            <div data-section="implementation">
                <div data-section="implementation-setup"></div>
                <div data-section="implementation-workflow"></div>
                <div data-section="implementation-deployment"></div>
                <ImplementationOverview />
            </div>

            <div data-section="technical">
                <TechnicalIntegration />
            </div>

            <div data-section="metrics">
                <PerformanceMetrics />
            </div>

            <div data-section="ai-tools">
                <div data-section="ai-tools-language"></div>
                <div data-section="ai-tools-knowledge"></div>
                <div data-section="ai-tools-platforms"></div>
                <div data-section="ai-tools-analytics"></div>
                <div data-section="ai-tools-channels"></div>
                <div data-section="ai-tools-security"></div>
                <AITools />
            </div>

            <!-- Call to Action -->
            <div class="mt-16 text-center">
                <a href="#contact" 
                   class="inline-flex items-center px-8 py-4 border border-transparent text-lg font-medium rounded-xl text-white bg-blue-600 hover:bg-blue-700 transition-all duration-300 transform hover:scale-105 hover:shadow-lg">
                    Book a Custom Demo
                    <svg class="ml-3 -mr-1 w-6 h-6" fill="currentColor" viewBox="0 0 20 20">
                        <path fill-rule="evenodd" d="M10.293 3.293a1 1 0 011.414 0l6 6a1 1 0 010 1.414l-6 6a1 1 0 01-1.414-1.414L14.586 11H3a1 1 0 110-2h11.586l-4.293-4.293a1 1 0 010-1.414z" clip-rule="evenodd" />
                    </svg>
                </a>
            </div>
        </div>
    </SolutionLayout>
</template>

<style scoped>
.hover-scale {
    transition: transform 0.3s ease-in-out;
}
.hover-scale:hover {
    transform: scale(1.02);
}
</style>
