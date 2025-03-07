<script setup>
import { ref, computed } from 'vue';
import { Head, Link, router, usePage } from '@inertiajs/vue3';
import ApplicationMark from '@/Components/ApplicationMark.vue';
import Banner from '@/Components/Banner.vue';
import Dropdown from '@/Components/Dropdown.vue';
import DropdownLink from '@/Components/DropdownLink.vue';
import NavLink from '@/Components/NavLink.vue';
import ResponsiveNavLink from '@/Components/ResponsiveNavLink.vue';
import LazyImage from '@/Components/LazyImage.vue';
import FlashMessage from '@/Components/FlashMessage.vue';
import DynamicSEO from '@/Components/DynamicSEO.vue';
import DarkModeToggle from '@/Components/DarkModeToggle.vue';
import WebDevelopmentDropdown from '@/Components/WebDevelopmentDropdown.vue';
// import SolutionsDropdown from '@/Components/SolutionsDropdown.vue';

defineProps({
    title: String,
});

const showingNavigationDropdown = ref(false);
const showingFullPracticeTestSubmenu = ref(false);

const switchToTeam = (team) => {
    router.put(route('current-team.update'), {
        team_id: team.id,
    }, {
        preserveState: false,
    });
};

const logout = () => {
    router.post(route('logout'));
};

const isAuthenticated = computed(() => usePage().props.auth.user !== null);
const isSubscribed = computed(() => usePage().props.auth.user?.has_paid_subscription ?? false);
const isAdmin = computed(() => {
    const user = usePage().props.auth.user;
    // This is a simple check - in a real app, you'd use a more robust method
    return user && user.email === 'admin@example.com';
});

const currentYear = computed(() => new Date().getFullYear());


</script>

<template>
    <div class="min-h-screen bg-gray-100 dark:bg-gray-900">
        <DynamicSEO />

        <Head :title="title" />

        <Banner />
        <FlashMessage />

        <div class="min-h-screen bg-gray-100 dark:bg-gray-900">
            <nav class="bg-white dark:bg-gray-800 border-b border-gray-100 dark:border-gray-700">
                <!-- Primary Navigation Menu -->
                <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
                    <div class="flex justify-between h-16">
                        <div class="flex">
                            <!-- Logo -->
                            <div class="shrink-0 flex items-center">
                                <Link :href="route('welcome')">
                                    <div class="text-2xl font-bold">
                                        <span class="text-blue-600 dark:text-blue-400">AI</span>
                                        <span class="text-gray-900 dark:text-white">Brain</span>
                                        <span class="text-blue-600 dark:text-blue-400">L.ink</span>
                                    </div>
                                </Link>
                            </div>

                            <!-- Navigation Links -->
                            <div class="hidden space-x-8 sm:-my-px sm:ms-10 sm:flex">
                                <NavLink :href="route('welcome')" :active="route().current('welcome')">
                                    AI Automation
                                </NavLink>
                                <NavLink :href="route('solutions.customer-service')" :active="route().current('solutions.customer-service')">
                                    Use Case
                                </NavLink>
                        
                                <NavLink :href="route('solutions.ai-integrations')" :active="route().current('solutions.ai-integrations')">
                                    AI & Integrations
                                </NavLink>
                                <WebDevelopmentDropdown />
                                <NavLink href="#benefits" :active="false">
                                    How it works
                                </NavLink>
                            </div>
                        </div>

                        <div class="hidden sm:flex sm:items-center sm:ms-6">
                            <!-- Authentication Links -->
                            <template v-if="!isAuthenticated">
                                <NavLink :href="route('login')" :active="route().current('login')">
                                    Log in
                                </NavLink>
                                <NavLink :href="route('register')" :active="route().current('register')">
                                    Sign up
                                </NavLink>
                                <NavLink href="/#contact" :active="false" class="get-quote-btn">
                                    Get A Quote
                                </NavLink>
                            </template>

                            <template v-else>
                                <!-- Get A Quote button for authenticated users -->
                                <NavLink href="/#contact" :active="false" class="get-quote-btn mr-3">
                                    Get A Quote
                                </NavLink>
                                
                                <!-- Settings Dropdown -->
                                <div class="ms-3 relative">
                                    <Dropdown align="right" width="48">
                                        <template #trigger>
                                            <button v-if="$page.props.jetstream.managesProfilePhotos"
                                                class="flex text-sm border-2 border-transparent rounded-full focus:outline-none focus:border-gray-300 transition">
                                                <LazyImage class="h-8 w-8 rounded-full object-cover"
                                                    :src="$page.props.auth.user.profile_photo_url"
                                                    :alt="$page.props.auth.user.name" width="32" height="32" />
                                            </button>

                                            <span v-else class="inline-flex rounded-md">
                                                <button type="button"
                                                    class="inline-flex items-center px-3 py-2 border border-transparent text-sm leading-4 font-medium rounded-md text-gray-500 dark:text-gray-400 bg-white dark:bg-gray-800 hover:text-gray-700 dark:hover:text-gray-300 focus:outline-none focus:bg-gray-50 dark:focus:bg-gray-700 active:bg-gray-50 dark:active:bg-gray-700 transition ease-in-out duration-150">
                                                    {{ $page.props.auth.user.name }}

                                                    <svg class="ms-2 -me-0.5 h-4 w-4" xmlns="http://www.w3.org/2000/svg"
                                                        fill="none" viewBox="0 0 24 24" stroke-width="1.5"
                                                        stroke="currentColor">
                                                        <path stroke-linecap="round" stroke-linejoin="round"
                                                            d="M19.5 8.25l-7.5 7.5-7.5-7.5" />
                                                    </svg>
                                                </button>
                                            </span>
                                        </template>

                                        <template #content>
                                            <!-- Account Management -->
                                            <div class="block px-4 py-2 text-xs text-gray-400">
                                                Manage Account
                                            </div>

                                            <DropdownLink :href="route('profile.show')">
                                                Profile
                                            </DropdownLink>

                                            <DropdownLink v-if="$page.props.jetstream.hasApiFeatures"
                                                :href="route('api-tokens.index')">
                                                API Tokens
                                            </DropdownLink>

                                            <!-- Admin Dashboard Link (for admins only) -->
                                            <DropdownLink v-if="isAdmin" :href="route('admin.dashboard')">
                                                Admin Dashboard
                                            </DropdownLink>

                                            <!-- Referrals Link -->
                                            <DropdownLink :href="route('referrals.index')">
                                                My Referrals
                                            </DropdownLink>

                                            <!-- Upgrade Account Button
                                            <DropdownLink v-if="!isSubscribed" :href="route('upgrade.account')">
                                                Upgrade Account
                                            </DropdownLink> -->

                                            <div class="border-t border-gray-200 dark:border-gray-600" />

                                            <!-- Authentication -->
                                            <form @submit.prevent="logout">
                                                <DropdownLink as="button">
                                                    Log Out
                                                </DropdownLink>
                                            </form>
                                        </template>
                                    </Dropdown>
                                </div>
                            </template>
                        </div>

                        <!-- Hamburger -->
                        <div class="-me-2 flex items-center sm:hidden">
                            <button
                                class="inline-flex items-center justify-center p-2 rounded-md text-gray-400 dark:text-gray-500 hover:text-gray-500 dark:hover:text-gray-400 hover:bg-gray-100 dark:hover:bg-gray-900 focus:outline-none focus:bg-gray-100 dark:focus:bg-gray-900 focus:text-gray-500 dark:focus:text-gray-400 transition duration-150 ease-in-out"
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
                        <div class="border-t border-gray-200 dark:border-gray-600 my-2"></div>
                        <div class="px-4 py-2 text-xs text-gray-400">Use Case</div>
                        <ResponsiveNavLink :href="route('solutions.customer-service')" :active="route().current('solutions.customer-service')">
                            Customer Service
                        </ResponsiveNavLink>
                        <div class="border-t border-gray-200 dark:border-gray-600 my-2"></div>
                        <!-- <ResponsiveNavLink :href="route('solutions.desktop-automation')" :active="route().current('solutions.desktop-automation')">
                            AI Desktop Automation
                        </ResponsiveNavLink> -->
                        <ResponsiveNavLink :href="route('solutions.ai-integrations')" :active="route().current('solutions.ai-integrations')">
                            AI Integrations
                        </ResponsiveNavLink>
                        <div class="border-t border-gray-200 dark:border-gray-600 my-2"></div>
                        <div class="px-4 py-2 text-xs text-gray-400">Web Development</div>
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
                        <ResponsiveNavLink href="#benefits">
                            How it works
                        </ResponsiveNavLink>
                    </div>

                    <!-- Responsive Settings Options -->
                    <div class="pt-4 pb-1 border-t border-gray-200 dark:border-gray-600">
                        <template v-if="!isAuthenticated">
                            <ResponsiveNavLink :href="route('login')" :active="route().current('login')">
                                Log in
                            </ResponsiveNavLink>
                            <ResponsiveNavLink :href="route('register')" :active="route().current('register')">
                                Sign up
                            </ResponsiveNavLink>
<ResponsiveNavLink href="/#contact" class="get-quote-responsive-btn" :textWhite="true">
    Get A Quote
</ResponsiveNavLink>
                        </template>

                        <template v-else>
                            <!-- Get A Quote button for authenticated users in mobile -->
                            <ResponsiveNavLink href="/#contact" class="get-quote-responsive-btn" :textWhite="true">
                                Get A Quote
                            </ResponsiveNavLink>
                            
                            <div class="flex items-center px-4">
                                <div v-if="$page.props.jetstream.managesProfilePhotos" class="shrink-0 me-3">
                                    <LazyImage class="h-10 w-10 rounded-full object-cover"
                                        :src="$page.props.auth.user.profile_photo_url" :alt="$page.props.auth.user.name"
                                        width="40" height="40" />
                                </div>

                                <div>
                                    <div class="font-medium text-base text-gray-800 dark:text-gray-200">
                                        {{ $page.props.auth.user.name }}
                                    </div>
                                    <div class="font-medium text-sm text-gray-500">
                                        {{ $page.props.auth.user.email }}
                                    </div>
                                </div>
                            </div>

                            <div class="mt-3 space-y-1">
                                <ResponsiveNavLink :href="route('profile.show')"
                                    :active="route().current('profile.show')">
                                    Profile
                                </ResponsiveNavLink>

                                <ResponsiveNavLink v-if="$page.props.jetstream.hasApiFeatures"
                                    :href="route('api-tokens.index')" :active="route().current('api-tokens.index')">
                                    API Tokens
                                </ResponsiveNavLink>

                                <!-- Responsive Admin Dashboard Link (for admins only) -->
                                <ResponsiveNavLink v-if="isAdmin" :href="route('admin.dashboard')"
                                    :active="route().current('admin.dashboard')">
                                    Admin Dashboard
                                </ResponsiveNavLink>

                                <!-- Responsive Referrals Link -->
                                <ResponsiveNavLink :href="route('referrals.index')"
                                    :active="route().current('referrals.index')">
                                    My Referrals
                                </ResponsiveNavLink>

                                <!-- Responsive Upgrade Account Button
                                <ResponsiveNavLink v-if="!isSubscribed" :href="route('upgrade.account')"
                                    :active="route().current('upgrade.account')">
                                    Upgrade Account
                                </ResponsiveNavLink> -->

                                <!-- Authentication -->
                                <form method="POST" @submit.prevent="logout">
                                    <ResponsiveNavLink as="button">
                                        Log Out
                                    </ResponsiveNavLink>
                                </form>
                            </div>
                        </template>
                    </div>
                </div>
            </nav>

            <!-- Page Heading -->
            <header v-if="$slots.header" class="bg-white dark:bg-gray-800 shadow">
                <div class="max-w-7xl mx-auto py-6 px-4 sm:px-6 lg:px-8">
                    <slot name="header" />
                </div>
            </header>

            <!-- Page Content -->
            <main class="flex-grow">
                <slot />
            </main>

           <!-- Footer -->
  <footer class="bg-white dark:bg-gray-800 border-t border-gray-100 dark:border-gray-700 py-4">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 text-center text-sm text-gray-500 dark:text-gray-400">
      <div class="flex flex-col items-center mb-4">
        <p class="mb-2">MarkIT S.R.L. -|- Fiscal Code: 50900467 -|- EU Tax ID: ROONRC.J2024042186003         </p>
        <div class="flex justify-center items-center space-x-8">
         
        </div>
      </div>
      <div>
       
        <a href="mailto:support@aibrainl.ink" class="hover:text-gray-700 dark:hover:text-gray-300" target="_blank" rel="noopener noreferrer">
          support@aibrainl.ink
        </a>© {{ currentYear }}
      </div>
    </div>
  </footer>


            <!-- Dark Mode Toggle -->
            <DarkModeToggle />
        </div>
    </div>
</template>

<style scoped>
.get-quote-btn {
    @apply bg-blue-500 dark:bg-blue-600 text-white dark:text-white px-3 py-1 rounded-md font-medium shadow-sm hover:bg-blue-600 dark:hover:bg-blue-700 transition-all duration-200 ease-in-out transform hover:scale-105;
    margin-top: -2px;
    margin-bottom: -2px;
    margin-left: 10px;
}

.get-quote-responsive-btn {
    @apply bg-blue-500 dark:bg-blue-600 text-white dark:text-white font-medium hover:bg-blue-600 dark:hover:bg-blue-700 rounded-md shadow-sm;
    margin-left: 0.75rem;
    margin-right: 0.75rem;
    width: calc(100% - 1.5rem) !important;
}

.nav-icon {
    display: inline-flex;
    align-items: center;
    justify-content: center;
    width: 24px;
    height: 24px;
    margin-right: 8px;
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
