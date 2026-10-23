<script setup>
import { ref, onMounted, onUnmounted } from 'vue';
import { Link } from '@inertiajs/vue3';

// Self-contained rather than reusing Dropdown.vue: that component wraps its
// trigger slot in <div @click="open = !open">, so a <Link> inside it would both
// navigate AND toggle. Here the label navigates and only the chevron toggles.
const services = [
    { name: 'E-commerce Platforms', route: 'web-development.ecommerce' },
    { name: 'Presentation Sites', route: 'web-development.presentation' },
    { name: 'Mobile Applications', route: 'web-development.mobile' },
    { name: 'Web Scraping/Automation', route: 'web-development.automation' },
    { name: 'Digital Marketing', route: 'web-development.digital-marketing' },
];

const open = ref(false);
const root = ref(null);

const close = () => { open.value = false; };

const onKeydown = (e) => {
    if (e.key === 'Escape') close();
};

const onClickOutside = (e) => {
    if (open.value && root.value && !root.value.contains(e.target)) close();
};

onMounted(() => {
    document.addEventListener('keydown', onKeydown);
    document.addEventListener('click', onClickOutside);
});

onUnmounted(() => {
    document.removeEventListener('keydown', onKeydown);
    document.removeEventListener('click', onClickOutside);
});
</script>

<template>
    <div ref="root" class="relative inline-flex items-center">
        <Link
            :href="route('web-development.index')"
            class="inline-flex items-center px-1 pt-1 border-b-2 text-sm font-medium leading-5 rounded-control transition duration-150 ease-in-out focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-accent-400 focus-visible:ring-offset-2 focus-visible:ring-offset-ink"
            :class="route().current('web-development.*')
                ? 'border-accent-500 text-content font-semibold'
                : 'border-transparent text-content-muted hover:text-content hover:border-line'"
        >
            Web Development
        </Link>

        <button
            type="button"
            :aria-expanded="open"
            aria-controls="web-development-menu"
            aria-label="Show Web Development services"
            class="ms-1 p-1 rounded-control text-content-muted hover:text-content transition duration-150 ease-in-out focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-accent-400 focus-visible:ring-offset-2 focus-visible:ring-offset-ink"
            @click.stop="open = !open"
        >
            <svg
                class="h-4 w-4 transition-transform duration-200"
                :class="{ 'rotate-180': open }"
                xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"
                stroke-width="1.5" stroke="currentColor" aria-hidden="true"
            >
                <path stroke-linecap="round" stroke-linejoin="round" d="M19.5 8.25l-7.5 7.5-7.5-7.5" />
            </svg>
        </button>

        <transition
            enter-active-class="transition ease-out duration-200"
            enter-from-class="transform opacity-0 scale-95"
            enter-to-class="transform opacity-100 scale-100"
            leave-active-class="transition ease-in duration-75"
            leave-from-class="transform opacity-100 scale-100"
            leave-to-class="transform opacity-0 scale-95"
        >
            <div
                v-show="open"
                id="web-development-menu"
                class="absolute start-0 top-full z-50 mt-3 w-56 rounded-card bg-surface ring-1 ring-inset ring-line shadow-e3 p-2"
                @click="close"
            >
                <Link
                    :href="route('web-development.index')"
                    class="block w-full px-3 py-2 text-sm leading-5 rounded-control font-semibold text-content hover:bg-surface-2 focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-accent-400 transition duration-150 ease-in-out"
                >
                    All Web Development
                </Link>

                <div class="my-1 border-t border-line"></div>

                <Link
                    v-for="service in services"
                    :key="service.route"
                    :href="route(service.route)"
                    class="block w-full px-3 py-2 text-sm leading-5 rounded-control text-content-muted hover:bg-surface-2 hover:text-content focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-accent-400 transition duration-150 ease-in-out"
                >
                    {{ service.name }}
                </Link>
            </div>
        </transition>
    </div>
</template>
