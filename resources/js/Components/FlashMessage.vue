<script setup>
import { ref, onMounted, computed } from 'vue';
import { usePage } from '@inertiajs/vue3';

const show = ref(false);
const message = ref('');
const type = ref('');

const classes = computed(() => {
    return {
        'bg-green-500 text-white': type.value === 'success',
        'bg-red-500 text-white': type.value === 'error',
        'bg-blue-500 text-white': type.value === 'info'
    };
});

const dismiss = () => {
    show.value = false;
};

import { watch } from 'vue';

const page = usePage();

watch(() => page.props.flash, (flash) => {
    if (flash?.success) {
        message.value = flash.success;
        type.value = 'success';
        show.value = true;
    } else if (flash?.error) {
        message.value = flash.error;
        type.value = 'error';
        show.value = true;
    } else if (flash?.message) {
        message.value = flash.message;
        type.value = 'info';
        show.value = true;
    }

    if (show.value) {
        setTimeout(() => {
            show.value = false;
        }, 5000);
    }
}, { immediate: true, deep: true });
</script>

<template>
    <Transition
        enter-active-class="transform ease-out duration-300 transition"
        enter-from-class="translate-y-2 opacity-0 sm:translate-y-0 sm:translate-x-2"
        enter-to-class="translate-y-0 opacity-100 sm:translate-x-0"
        leave-active-class="transition ease-in duration-200"
        leave-from-class="opacity-100"
        leave-to-class="opacity-0"
    >
        <div
            v-if="show"
            :class="classes"
            class="fixed bottom-4 left-1/2 transform -translate-x-1/2 z-50 p-4 rounded-md shadow-md pointer-events-auto max-w-sm w-full"
        >
            <div class="flex items-center">
                <div class="flex-grow text-center">{{ message }}</div>
                <button @click="dismiss" class="ml-4 text-white hover:text-gray-200 focus:outline-none">
                    <svg class="h-5 w-5" viewBox="0 0 20 20" fill="currentColor">
                        <path fill-rule="evenodd" d="M4.293 4.293a1 1 0 011.414 0L10 8.586l4.293-4.293a1 1 0 111.414 1.414L11.414 10l4.293 4.293a1 1 0 01-1.414 1.414L10 11.414l-4.293 4.293a1 1 0 01-1.414-1.414L8.586 10 4.293 5.707a1 1 0 010-1.414z" clip-rule="evenodd" />
                    </svg>
                </button>
            </div>
        </div>
    </Transition>
</template>
