<script setup>
import { ref, computed } from 'vue';
import { Head, Link } from '@inertiajs/vue3';
import ApplicationMark from '@/Components/ApplicationMark.vue';
import Banner from '@/Components/Banner.vue';
import NavLink from '@/Components/NavLink.vue';
import ResponsiveNavLink from '@/Components/ResponsiveNavLink.vue';
import FlashMessage from '@/Components/FlashMessage.vue';
import DynamicSEO from '@/Components/DynamicSEO.vue';
import WebDevelopmentDropdown from '@/Components/WebDevelopmentDropdown.vue';

defineProps({
    title: String,
});

const showingNavigationDropdown = ref(false);

const currentYear = computed(() => new Date().getFullYear());


</script>

<template>
    <div class="min-h-screen bg-ink">
        <DynamicSEO />

        <Head :title="title" />

        <Banner />
        <FlashMessage />

        <div class="min-h-screen bg-ink">
            <nav class="sticky top-0 z-40 bg-ink/85 backdrop-blur-md border-b border-line">
                <!-- Primary Navigation Menu -->
                <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
                    <div class="flex justify-between h-16">
                        <div class="flex">
                            <!-- Logo -->
                            <div class="shrink-0 flex items-center">
                                <Link :href="route('welcome')">
                                    <div class="text-2xl font-bold">
                                        <span class="text-accent-400">AI</span>
                                        <span class="text-content">Brain</span>
                                        <span class="text-accent-400">L.ink</span>
                                    </div>
                                </Link>
                            </div>

                            <!-- Navigation Links -->
                            <div class="hidden space-x-8 sm:-my-px sm:ms-10 sm:flex">
                                <NavLink :href="route('welcome')" :active="route().current('welcome')">
                                    AI Automation
                                </NavLink>
                                <NavLink :href="route('portfolio')" :active="route().current('portfolio')">
                                    Portfolio
                                </NavLink>
                                <NavLink :href="route('solutions.customer-service')" :active="route().current('solutions.customer-service')">
                                    Use Case
                                </NavLink>

                                <NavLink :href="route('solutions.ai-integrations')" :active="route().current('solutions.ai-integrations')">
                                    AI & Integrations
                                </NavLink>
                                <WebDevelopmentDropdown />
                                <NavLink href="/#benefits" :active="false">
                                    How it works
                                </NavLink>
                            </div>
                        </div>

                        <div class="hidden sm:flex sm:items-center sm:ms-6">
                            <NavLink href="/#contact" :active="false" class="get-quote-btn">
                                Get a Quote
                            </NavLink>
                        </div>

                        <!-- Hamburger -->
                        <div class="-me-2 flex items-center sm:hidden">
                            <button
                                class="inline-flex items-center justify-center p-2 rounded-control text-content-muted hover:text-content hover:bg-surface-2 focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-accent-400 focus-visible:ring-offset-2 focus-visible:ring-offset-ink transition duration-150 ease-in-out"
                                @click="showingNavigationDropdown = !showingNavigationDropdown">
                                <svg class="h-6 w-6" stroke="currentColor" fill="none" viewBox="0 0 24 24">
                                    <path
                                        :class="{ 'hidden': showingNavigationDropdown, 'inline-flex': !showingNavigationDropdown }"
                                        stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                                        d="M4 6h16M4 12h16M4 18h16" />
                                    <path
                                        :class="{ 'hidden': !showingNavigationDropdown, 'inline-flex': showingNavigationDropdown }"
                                        stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                                        d="M6 18L18 6M6 6l12 12" />
                                </svg>
                            </button>
                        </div>
                    </div>
                </div>

                <!-- Responsive Navigation Menu -->
                <div :class="{ 'block': showingNavigationDropdown, 'hidden': !showingNavigationDropdown }"
                    class="sm:hidden">
                    <div class="pt-2 pb-3 space-y-1">
                        <ResponsiveNavLink :href="route('welcome')" :active="route().current('welcome')">
                            AI Automation
                        </ResponsiveNavLink>
                        <ResponsiveNavLink :href="route('portfolio')" :active="route().current('portfolio')">
                            Portfolio
                        </ResponsiveNavLink>
                        <div class="border-t border-line my-2"></div>
                        <div class="px-4 py-2 text-xs text-content-subtle">Use Case</div>
                        <ResponsiveNavLink :href="route('solutions.customer-service')" :active="route().current('solutions.customer-service')">
                            Customer Service
                        </ResponsiveNavLink>
                        <div class="border-t border-line my-2"></div>
                        <!-- <ResponsiveNavLink :href="route('solutions.desktop-automation')" :active="route().current('solutions.desktop-automation')">
                            AI Desktop Automation
                        </ResponsiveNavLink> -->
                        <ResponsiveNavLink :href="route('solutions.ai-integrations')" :active="route().current('solutions.ai-integrations')">
                            AI Integrations
                        </ResponsiveNavLink>
                        <div class="border-t border-line my-2"></div>
                        <div class="px-4 py-2 text-xs text-content-subtle">Web Development</div>
                        <ResponsiveNavLink :href="route('web-development.index')" :active="route().current('web-development.index')">
                            All Web Development
                        </ResponsiveNavLink>
                        <ResponsiveNavLink :href="route('web-development.ecommerce')" :active="route().current('web-development.ecommerce')">
                            E-commerce Platforms
                        </ResponsiveNavLink>
                        <ResponsiveNavLink :href="route('web-development.presentation')" :active="route().current('web-development.presentation')">
                            Presentation Sites
                        </ResponsiveNavLink>
                        <ResponsiveNavLink :href="route('web-development.mobile')" :active="route().current('web-development.mobile')">
                            Mobile Applications
                        </ResponsiveNavLink>
                        <ResponsiveNavLink :href="route('web-development.automation')" :active="route().current('web-development.automation')">
                            Web Scraping/Automation
                        </ResponsiveNavLink>
                        <ResponsiveNavLink href="/#benefits">
                            How it works
                        </ResponsiveNavLink>
                    </div>

                    <!-- Responsive Settings Options -->
                    <div class="pt-4 pb-1 border-t border-line">
                        <ResponsiveNavLink href="/#contact" class="get-quote-responsive-btn" :textWhite="true">
                            Get a Quote
                        </ResponsiveNavLink>
                    </div>
                </div>
            </nav>

            <!-- Page Heading -->
            <header v-if="$slots.header" class="bg-surface border-b border-line">
                <div class="max-w-7xl mx-auto py-6 px-4 sm:px-6 lg:px-8">
                    <slot name="header" />
                </div>
            </header>

            <!-- Page Content -->
            <main class="flex-grow">
                <slot />
            </main>

           <!-- Footer -->
  <footer class="bg-ink border-t border-line py-8">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 text-center text-sm text-content-subtle">
      <div class="flex flex-col items-center mb-4">
        <p class="mb-2">MarkIT S.R.L. -|- Fiscal Code: 50900467 -|- EU Tax ID: ROONRC.J2024042186003         </p>
        <div class="flex justify-center items-center space-x-8">
         
        </div>
      </div>
      <div>
       
        <a href="mailto:support@aibrainl.ink" class="hover:text-content transition-colors">
          support@aibrainl.ink
        </a>
        <span class="mx-2 text-line">·</span>
        <Link :href="route('privacy-policy')" class="hover:text-content transition-colors">Privacy</Link>
        <span class="mx-2 text-line">·</span>
        <Link :href="route('terms-of-service')" class="hover:text-content transition-colors">Terms</Link>
        <span class="mx-2 text-line">·</span>
        © {{ currentYear }}
      </div>
    </div>
  </footer>


        </div>
    </div>
</template>

<style scoped>
.get-quote-btn {
    @apply bg-accent-500 text-white px-4 py-2 rounded-control font-semibold shadow-e1 hover:bg-accent-600 transition-colors duration-200;
    margin-top: -2px;
    margin-bottom: -2px;
    margin-left: 10px;
}

.get-quote-responsive-btn {
    @apply bg-accent-500 text-white font-semibold hover:bg-accent-600 rounded-control shadow-e1;
    margin-left: 0.75rem;
    margin-right: 0.75rem;
    width: calc(100% - 1.5rem) !important;
}

.min-h-screen {
    display: flex;
    flex-direction: column;
}

main {
    flex: 1 0 auto;
}

footer {
    flex-shrink: 0;
}
footer svg {
  transition: transform 0.3s ease;
}

footer svg:hover {
  transform: scale(1.1);
}
</style>
