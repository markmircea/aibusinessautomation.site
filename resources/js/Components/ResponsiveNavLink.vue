<script setup>
import { computed } from 'vue';
import { Link } from '@inertiajs/vue3';

const props = defineProps({
    active: Boolean,
    href: String,
    as: String,
    textWhite: Boolean,
});

const classes = computed(() => {
    if (props.textWhite) {
        return props.active
            ? 'block w-full ps-3 pe-4 py-2 border-l-4 border-accent-500 text-start text-base font-medium text-white bg-surface-2 focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-accent-400 transition duration-150 ease-in-out'
            : 'block w-full ps-3 pe-4 py-2 border-l-4 border-transparent text-start text-base font-medium text-white hover:text-white hover:bg-surface-2 hover:border-line focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-accent-400 transition duration-150 ease-in-out';
    }
    
    return props.active
        ? 'block w-full ps-3 pe-4 py-2 border-l-4 border-accent-500 text-start text-base font-medium text-content bg-surface-2 focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-accent-400 transition duration-150 ease-in-out'
        : 'block w-full ps-3 pe-4 py-2 border-l-4 border-transparent text-start text-base font-medium text-content-muted hover:text-content hover:bg-surface-2 hover:border-line focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-accent-400 transition duration-150 ease-in-out';
});
</script>

<template>
    <div>
        <button v-if="as == 'button'" :class="classes" class="w-full text-start">
            <slot />
        </button>

        <Link v-else :href="href" :class="classes">
            <slot name="icon"></slot>

            <slot />
        </Link>
    </div>
</template>
