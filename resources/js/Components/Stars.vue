<script setup>
import { ref, computed } from 'vue';

const props = defineProps({
    rating: {
        type: Number,
        default: 0
    },
    readonly: {
        type: Boolean,
        default: false
    },
    size: {
        type: String,
        default: 'md',
        validator: (value) => ['sm', 'md', 'lg'].includes(value)
    }
});

const emit = defineEmits(['update:rating']);

// Generate a unique ID for this instance of the rating component
const instanceId = ref(`star-rating-${Math.random().toString(36).substr(2, 9)}`);

const currentRating = computed({
    get: () => props.rating,
    set: (value) => emit('update:rating', value)
});

const stars = [1, 2, 3, 4, 5];

const starSize = computed(() => {
    const sizes = {
        sm: 'w-4 h-4',
        md: 'w-6 h-6',
        lg: 'w-8 h-8'
    };
    return sizes[props.size];
});

const isHovered = ref(false);
const hoveredRating = ref(0);

const handleMouseEnter = (star) => {
    if (props.readonly) return;
    isHovered.value = true;
    hoveredRating.value = star;
};

const handleMouseLeave = () => {
    isHovered.value = false;
    hoveredRating.value = 0;
};

const displayRating = computed(() => {
    return isHovered.value ? hoveredRating.value : currentRating.value;
});

const getStarFill = (starNumber) => {
    const rating = displayRating.value;
    if (starNumber <= Math.floor(rating)) return 100;
    if (starNumber > Math.ceil(rating)) return 0;

    // Handle partial stars
    const decimal = rating % 1;
    return decimal * 100;
};

const getStarClasses = (star) => {
    return [
        starSize.value,
        'transition-colors duration-200',
        {
            'text-yellow-400': star <= Math.ceil(displayRating.value),
            'text-gray-300 dark:text-gray-600': star > Math.ceil(displayRating.value)
        }
    ];
};

// Generate unique gradient ID for each star
const getGradientId = (star) => `${instanceId.value}-star-fill-${star}`;
</script>

<template>
    <div class="flex items-center space-x-1">
        <button
            v-for="star in stars"
            :key="star"
            type="button"
            class="focus:outline-none transition-transform duration-200 ease-in-out transform hover:scale-110"
            :class="{
                'cursor-pointer': !readonly,
                'cursor-default': readonly
            }"
            @click="!readonly && (currentRating = star)"
            @mouseenter="handleMouseEnter(star)"
            @mouseleave="handleMouseLeave"
        >
            <svg
                :class="getStarClasses(star)"
                xmlns="http://www.w3.org/2000/svg"
                viewBox="0 0 20 20"
            >
                <defs>
                    <linearGradient :id="getGradientId(star)">
                        <stop offset="0%" stop-color="currentColor"/>
                        <stop :offset="getStarFill(star) + '%'" stop-color="currentColor"/>
                        <stop :offset="getStarFill(star) + '%'" stop-color="#CBD5E0"/>
                        <stop offset="100%" stop-color="#CBD5E0"/>
                    </linearGradient>
                </defs>
                <path
                    :fill="`url(#${getGradientId(star)})`"
                    d="M9.049 2.927c.3-.921 1.603-.921 1.902 0l1.07 3.292a1 1 0 00.95.69h3.462c.969 0 1.371 1.24.588 1.81l-2.8 2.034a1 1 0 00-.364 1.118l1.07 3.292c.3.921-.755 1.688-1.54 1.118l-2.8-2.034a1 1 0 00-1.175 0l-2.8 2.034c-.784.57-1.838-.197-1.539-1.118l1.07-3.292a1 1 0 00-.364-1.118L2.98 8.72c-.783-.57-.38-1.81.588-1.81h3.461a1 1 0 00.951-.69l1.07-3.292z"
                />
            </svg>
        </button>
    </div>
</template>
