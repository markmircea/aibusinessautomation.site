<script setup>
const metrics = {
    response: [
        { label: 'Accuracy', value: '95%+' },
        { label: 'Relevance', value: '90%+' },
        { label: 'Source Attribution', value: '100%' }
    ],
    system: [
        { label: 'Response Time', value: '<1s' },
        { label: 'Uptime', value: '99.9%' },
        { label: 'Scalability', value: '∞' }
    ],
    business: [
        { label: 'Cost Reduction', value: '70%' },
        { label: 'Availability', value: '24/7' },
        { label: 'CSAT Improvement', value: '90%' }
    ]
};
</script>

<template>
    <div class="bg-surface shadow-sm rounded-card overflow-hidden transform hover:shadow-lg transition-all duration-300">
        <div class="p-6">
            <h3 class="text-xl font-semibold text-content mb-4">Performance Metrics</h3>
            <p class="text-content-muted mb-6">
                Example metrics from similar implementations:
            </p>
            <div class="grid grid-cols-1 md:grid-cols-3 gap-6">
                <!-- Response Quality -->
                <div class="metric-card group bg-surface-2/60 rounded-card p-6 hover:bg-accent-500/12">
                    <div class="flex items-center mb-4">
                        <svg class="h-8 w-8 text-accent-400 mr-3 transform group-hover:scale-110 transition-transform duration-300" 
                             fill="none" stroke="currentColor" viewBox="0 0 24 24">
                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" 
                                  d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z" />
                        </svg>
                        <h5 class="font-medium text-content text-lg">Response Quality</h5>
                    </div>
                    <ul class="space-y-3">
                        <li v-for="(item, index) in metrics.response" :key="index">
                            <div class="flex justify-between items-baseline">
                                <span class="text-content-muted">{{ item.label }}</span>
                                <span class="metric-value">{{ item.value }}</span>
                            </div>
                            <div class="mt-1 h-1 w-full bg-surface-2 rounded">
                                <div class="metric-bar h-1 bg-accent-500 rounded-full transition-all duration-1000 ease-out"
                                     :style="{ width: item.value.replace('+', '').replace('%', '') + '%' }"></div>
                            </div>
                        </li>
                    </ul>
                </div>

                <!-- System Performance -->
                <div class="metric-card group bg-surface-2/60 rounded-card p-6 hover:bg-accent-500/12">
                    <div class="flex items-center mb-4">
                        <svg class="h-8 w-8 text-accent-400 mr-3 transform group-hover:scale-110 transition-transform duration-300" 
                             fill="none" stroke="currentColor" viewBox="0 0 24 24">
                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" 
                                  d="M13 10V3L4 14h7v7l9-11h-7z" />
                        </svg>
                        <h5 class="font-medium text-content text-lg">System Performance</h5>
                    </div>
                    <ul class="space-y-3">
                        <li v-for="(item, index) in metrics.system" :key="index">
                            <div class="flex justify-between items-baseline">
                                <span class="text-content-muted">{{ item.label }}</span>
                                <span class="metric-value">{{ item.value }}</span>
                            </div>
                            <div v-if="item.value.includes('%')" class="mt-1 h-1 w-full bg-surface-2 rounded">
                                <div class="metric-bar h-1 bg-accent-500 rounded-full transition-all duration-1000 ease-out"
                                     :style="{ width: item.value.replace('%', '') + '%' }"></div>
                            </div>
                        </li>
                    </ul>
                </div>

                <!-- Business Impact -->
                <div class="metric-card group bg-surface-2/60 rounded-card p-6 hover:bg-accent-500/12">
                    <div class="flex items-center mb-4">
                        <svg class="h-8 w-8 text-accent-400 mr-3 transform group-hover:scale-110 transition-transform duration-300" 
                             fill="none" stroke="currentColor" viewBox="0 0 24 24">
                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" 
                                  d="M9 19v-6a2 2 0 00-2-2H5a2 2 0 00-2 2v6a2 2 0 002 2h2a2 2 0 002-2zm0 0V9a2 2 0 012-2h2a2 2 0 012 2v10m-6 0a2 2 0 002 2h2a2 2 0 002-2m0 0V5a2 2 0 012-2h2a2 2 0 012 2v14a2 2 0 01-2 2h-2a2 2 0 01-2-2z" />
                        </svg>
                        <h5 class="font-medium text-content text-lg">Business Impact</h5>
                    </div>
                    <ul class="space-y-3">
                        <li v-for="(item, index) in metrics.business" :key="index">
                            <div class="flex justify-between items-baseline">
                                <span class="text-content-muted">{{ item.label }}</span>
                                <span class="metric-value">{{ item.value }}</span>
                            </div>
                            <div v-if="item.value.includes('%')" class="mt-1 h-1 w-full bg-surface-2 rounded">
                                <div class="metric-bar h-1 bg-accent-500 rounded-full transition-all duration-1000 ease-out"
                                     :style="{ width: item.value.replace('%', '') + '%' }"></div>
                            </div>
                        </li>
                    </ul>
                </div>
            </div>
        </div>
    </div>
</template>

<style scoped>
.metric-card {
    transition: all 0.3s ease-in-out;
}

.metric-card:hover {
    transform: translateY(-4px);
}

.metric-value {
    @apply text-2xl font-bold text-accent-400;
    transition: all 0.3s ease-in-out;
}

.metric-card:hover .metric-value {
    transform: scale(1.1);
}

.metric-bar {
    transition: width 1.5s ease-in-out;
}
</style>
