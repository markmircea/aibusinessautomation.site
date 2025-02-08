<template>
    <header ref="headerRef" class="relative overflow-hidden bg-gradient-to-br from-blue-600 to-blue-400 dark:from-blue-600 dark:to-transparent">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-16 sm:py-24">
            <div class="text-center">
                <h1 class="text-4xl sm:text-5xl md:text-6xl font-extrabold text-white mb-6 animate-fade-in-up">
                    <span class="relative z-10 inline-block transition-transform hover:scale-105 duration-300">
                        Criteria Cognitive Aptitude Test (CCAT) & Crossover Psychometric Test
                    </span>
                </h1>

                <!-- Rating Section -->
                <div class="relative z-10 flex justify-center mb-6 animate-fade-in-up">
                    <div class="flex items-center gap-3 bg-white/10 backdrop-blur-sm rounded-full px-6 py-3 shadow-lg hover:bg-white/15 transition-all duration-300">
                        <StarRating :rating="4.7" :readonly="true" size="lg" />
                        <div class="text-lg font-medium text-white/90">
                            4.7
                        </div>
                        <div class="text-sm text-white/70">
                            <span class="px-2 py-1 bg-white/10 rounded-full">
                                <a href="/free-practice-test#reviews" class="text-sm text-white/70 hover:text-white transition-colors"> 26 reviews</a>
                            </span>
                        </div>
                    </div>
                </div>

                <p class="relative z-10 mt-3 max-w-md mx-auto text-xl text-blue-100 sm:text-2xl md:mt-5 md:max-w-3xl animate-fade-in-up">
                    As prior Crossover employees we KNOW what you need to KNOW to get hired. Our CCAT exams are the same types of exams used by CROSSOVER during the hiring process
                    <br><br>Our Questions, Answers and Explanations help you get a leg up on your competition
                </p>
                <p class="relative z-10 mt-3 max-w-md mx-auto text-xl text-blue-100 sm:text-2xl md:mt-5 md:max-w-3xl animate-fade-in-up">
                    Currently serving the latest <strong class="text-orange-300">{{ currentMonthYear }}</strong> version tests!
                </p>
                <div class="mt-10 flex justify-center space-x-4">
                    <Link :href="isSubscribed ? route('full-practice-test-start') : route('free.practice.test')"
                        class="relative z-10 inline-flex items-center px-6 py-3 border border-transparent text-base font-medium rounded-full text-blue-700 bg-white hover:bg-blue-50 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-blue-500 transition-all duration-300 transform hover:scale-105 group">
                        Free Practice
                        <span class="hidden md:inline">&nbsp;Test</span>
                        <svg class="ml-2 -mr-1 w-5 h-5 transition-transform duration-300 group-hover:translate-x-1" fill="currentColor" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg">
                            <path fill-rule="evenodd" d="M10.293 3.293a1 1 0 011.414 0l6 6a1 1 0 010 1.414l-6 6a1 1 0 01-1.414-1.414L14.586 11H3a1 1 0 110-2h11.586l-4.293-4.293a1 1 0 010-1.414z" clip-rule="evenodd"></path>
                        </svg>
                    </Link>
                    <a href="#definition"
                        class="relative z-10 inline-flex items-center px-6 py-3 border border-white text-base font-medium rounded-full text-white hover:bg-white hover:text-blue-600 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-white transition-all duration-300 transform hover:scale-105 group">
                        <div class="hidden md:block">Learn &nbsp;</div> More
                        <svg class="ml-2 -mr-1 w-5 h-5 transition-transform duration-300 group-hover:translate-x-1"
                            fill="currentColor" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg">
                            <path fill-rule="evenodd"
                                d="M10.293 3.293a1 1 0 011.414 0l6 6a1 1 0 010 1.414l-6 6a1 1 0 01-1.414-1.414L14.586 11H3a1 1 0 110-2h11.586l-4.293-4.293a1 1 0 010-1.414z"
                                clip-rule="evenodd"></path>
                        </svg>
                    </a>
                </div>
            </div>
        </div>
        <svg class="absolute bottom-0 w-full h-16 text-gray-50 dark:text-gray-800" preserveAspectRatio="none"
            viewBox="0 0 1440 54">
            <path fill="currentColor" d="M0 54L1440 0v54H0z"></path>
        </svg>
        <div ref="shapeContainer" class="absolute top-0 left-0 w-full h-full overflow-hidden z-0">
            <div v-for="shape in shapes" :key="shape.id" class="shape" :style="getShapeStyle(shape)">
                <template v-if="shape.type === 'triangle'">
                    <svg :width="shape.size" :height="shape.size" viewBox="0 0 100 100">
                        <polygon points="50,15 100,100 0,100" fill="rgba(255,255,255,0.1)" />
                    </svg>
                </template>
                <template v-else-if="shape.type === 'square'">
                    <div
                        :style="{ width: `${shape.size}px`, height: `${shape.size}px`, background: 'rgba(255,255,255,0.1)' }">
                    </div>
                </template>
                <template v-else>
                    <div
                        :style="{ width: `${shape.size}px`, height: `${shape.size}px`, borderRadius: '50%', background: 'rgba(255,255,255,0.1)' }">
                    </div>
                </template>
            </div>
        </div>
    </header>
</template>

<script setup>
import { ref, onMounted, onUnmounted } from 'vue';
import { Link } from '@inertiajs/vue3';
import StarRating from '@/Components/Stars.vue';

const props = defineProps({
    isSubscribed: Boolean
});

const headerRef = ref(null);
const shapeContainer = ref(null);
const shapes = ref([]);
let shapeId = 0;

const currentMonthYear = ref("");

const createShape = () => {
    const size = Math.random() * 60 + 20;
    shapes.value.push({
        id: shapeId++,
        type: ['circle', 'triangle', 'square'][Math.floor(Math.random() * 3)],
        size,
        top: Math.random() * 100,
        left: Math.random() * 100,
        delay: Math.random() * 5,
        duration: Math.random() * 10 + 10
    });

    if (shapes.value.length > 50) {
        shapes.value.shift();
    }
};

const generateShapes = () => {
    for (let i = 0; i < 20; i++) {
        createShape();
    }
};

const getShapeStyle = (shape) => {
    return {
        position: 'absolute',
        width: `${shape.size}px`,
        height: `${shape.size}px`,
        top: `${shape.top}%`,
        left: `${shape.left}%`,
        animationDelay: `${shape.delay}s`,
        animationDuration: `${shape.duration}s`,
    };
};

const handleScroll = () => {
    const headerBottom = headerRef.value.getBoundingClientRect().bottom;
    if (headerBottom <= 0) {
        createShape();
    }
};

onMounted(() => {
    const monthNames = [
        "January", "February", "March", "April", "May", "June",
        "July", "August", "September", "October", "November", "December"
    ];

    const now = new Date();
    const month = monthNames[now.getMonth()];
    const year = now.getFullYear();

    currentMonthYear.value = `${month.toUpperCase()} ${year}`;

    generateShapes();
    window.addEventListener('scroll', handleScroll);
});

onUnmounted(() => {
    window.removeEventListener('scroll', handleScroll);
});
</script>

<style scoped>
.animate-fade-in-up {
    animation: fadeInUp 0.6s ease-out;
}

@keyframes fadeInUp {
    from {
        opacity: 0;
        transform: translateY(20px);
    }

    to {
        opacity: 1;
        transform: translateY(0);
    }
}

.shape {
    animation: float 20s ease-in-out infinite;
    transition: all 0.3s ease-in-out;
}

.shape:hover {
    opacity: 0.3;
    transform: scale(1.1);
}

@keyframes float {
    0%, 100% {
        transform: translate(0, 0) scale(1);
    }
    25% {
        transform: translate(10px, -15px) scale(1.05);
    }
    50% {
        transform: translate(20px, -30px) scale(1.1);
    }
    75% {
        transform: translate(10px, -45px) scale(1.05);
    }
}

.backdrop-blur-sm {
    backdrop-filter: blur(8px);
    -webkit-backdrop-filter: blur(8px);
}

/* Optional: Add a subtle pulse animation to draw attention to the rating */
@keyframes subtle-pulse {
    0%, 100% {
        transform: scale(1);
    }
    50% {
        transform: scale(1.02);
    }
}

.animate-subtle-pulse {
    animation: subtle-pulse 3s ease-in-out infinite;
}
</style>
