<script setup>
const logos = [

    {
        name: 'Microsoft',
        image: '/img/logos/microsoft.svg',
        alt: 'Microsoft Logo'
    },
    {
        name: 'Zendesk',
        image: '/img/logos/zendesk.svg',
        alt: 'Zendesk Logo'
    },
    {
        name: 'Cisco',
        image: '/img/logos/cisco.svg',
        alt: 'Cisco Logo'
    },
    {
        name: 'DocuSign',
        image: '/img/logos/docusign.svg',
        alt: 'DocuSign Logo'
    },
    {
        name: 'Wayfair',
        image: '/img/logos/wayfair.svg',
        alt: 'Wayfair Logo'
    }
];
</script>

<template>
    <section class="logo-slider-section py-12 bg-white dark:bg-gray-900">
        <div class="logo-slider-container">
            <div class="logo-track">
                <!-- Use two groups with increased spacing for seamless loop -->
                <div v-for="i in 2" :key="i" class="logo-group">
                    <img v-for="logo in logos" 
                         :key="`${i}-${logo.name}`" 
                         :src="logo.image" 
                         :alt="logo.alt" 
                         class="logo">
                </div>
            </div>
        </div>
    </section>
</template>

<style scoped>
.logo-slider-section {
    width: 100%;
    overflow-x: hidden;
}

.logo-slider-container {
    position: relative;
    padding: 1rem 0;
}

.logo-track {
    display: flex;
    animation: slide 30s linear infinite;
    width: max-content;
}

.logo-group {
    display: flex;
    align-items: center;
    /* Increased spacing between logos */
    gap: clamp(6rem, 12vw, 16rem);
    padding: 0 clamp(3rem, 6vw, 8rem);
}

.logo {
    height: 3.5rem;
    width: auto;
    object-fit: contain;
    filter: grayscale(100%);
    opacity: 0.7;
}

@keyframes slide {
    0% {
        transform: translateX(0);
    }
    100% {
        transform: translateX(-50%); /* Move by 1/2 since we have 2 groups */
    }
}

/* Dark mode styles */
:deep(.dark) .logo {
    filter: grayscale(100%) brightness(0.8) invert(1);
    opacity: 0.6;
}
</style>
