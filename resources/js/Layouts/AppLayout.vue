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
import SolutionsDropdown from '@/Components/SolutionsDropdown.vue';

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
                                    Home
                                </NavLink>
                                <SolutionsDropdown />
                                <NavLink :href="route('solutions.desktop-automation')" :active="route().current('solutions.desktop-automation')">
                                    AI Desktop Automation
                                </NavLink>
                                <NavLink :href="route('solutions.ai-integrations')" :active="route().current('solutions.ai-integrations')">
                                    What we offer
                                </NavLink>
                                <NavLink href="#benefits" :active="false">
                                    How it works
                                </NavLink>
                                <NavLink href="#contact" :active="false">
                                    Contact
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
                            </template>

                            <template v-else>
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

                                            <!-- Upgrade Account Button -->
                                            <DropdownLink v-if="!isSubscribed" :href="route('upgrade.account')">
                                                Upgrade Account
                                            </DropdownLink>

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
                        <ResponsiveNavLink :href="route('dashboard')" :active="route().current('dashboard')">
                            Home
                        </ResponsiveNavLink>
                        <div class="border-t border-gray-200 dark:border-gray-600 my-2"></div>
                        <div class="px-4 py-2 text-xs text-gray-400">Business Solutions</div>
                        <ResponsiveNavLink :href="route('solutions.document-processing')" :active="route().current('solutions.document-processing')">
                            Document Processing
                        </ResponsiveNavLink>
                        <ResponsiveNavLink :href="route('solutions.customer-service')" :active="route().current('solutions.customer-service')">
                            Customer Service
                        </ResponsiveNavLink>
                        <ResponsiveNavLink :href="route('solutions.financial-operations')" :active="route().current('solutions.financial-operations')">
                            Financial Operations
                        </ResponsiveNavLink>
                        <ResponsiveNavLink :href="route('solutions.hr-recruitment')" :active="route().current('solutions.hr-recruitment')">
                            HR & Recruitment
                        </ResponsiveNavLink>
                        <ResponsiveNavLink :href="route('solutions.sales-marketing')" :active="route().current('solutions.sales-marketing')">
                            Sales & Marketing
                        </ResponsiveNavLink>
                        <ResponsiveNavLink :href="route('solutions.supply-chain')" :active="route().current('solutions.supply-chain')">
                            Supply Chain
                        </ResponsiveNavLink>
                        <div class="border-t border-gray-200 dark:border-gray-600 my-2"></div>
                        <ResponsiveNavLink :href="route('solutions.desktop-automation')" :active="route().current('solutions.desktop-automation')">
                            AI Desktop Automation
                        </ResponsiveNavLink>
                        <ResponsiveNavLink :href="route('solutions.ai-integrations')" :active="route().current('solutions.ai-integrations')">
                            AI Integrations
                        </ResponsiveNavLink>
                        <ResponsiveNavLink href="#benefits">
                            Benefits
                        </ResponsiveNavLink>
                        <ResponsiveNavLink href="#contact">
                            Contact
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
                        </template>

                        <template v-else>
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

                                <!-- Responsive Upgrade Account Button -->
                                <ResponsiveNavLink v-if="!isSubscribed" :href="route('upgrade.account')"
                                    :active="route().current('upgrade.account')">
                                    Upgrade Account
                                </ResponsiveNavLink>

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
        <p class="mb-2">Payment Secured by</p>
        <div class="flex justify-center items-center space-x-8">
          <!-- PayPal SVG -->
          <svg xmlns="http://www.w3.org/2000/svg" width="96" height="80" viewBox="0 0 124 33">
            <circle cx="24" cy="24" r="20" fill="#0070BA"/>
            <path d="M32.3305 18.0977C32.3082 18.24 32.2828 18.3856 32.2542 18.5351C31.2704 23.5861 27.9046 25.331 23.606 25.331H21.4173C20.8916 25.331 20.4486 25.7127 20.3667 26.2313L19.2461 33.3381L18.9288 35.3527C18.8755 35.693 19.1379 36 19.4815 36H23.3634C23.8231 36 24.2136 35.666 24.286 35.2127L24.3241 35.0154L25.055 30.3772L25.1019 30.1227C25.1735 29.6678 25.5648 29.3338 26.0245 29.3338H26.6051C30.3661 29.3338 33.3103 27.8068 34.1708 23.388C34.5303 21.5421 34.3442 20.0008 33.393 18.9168C33.1051 18.59 32.748 18.3188 32.3305 18.0977Z" fill="white" fill-opacity="0.6"/>
            <path d="M31.3009 17.6871C31.1506 17.6434 30.9955 17.6036 30.8364 17.5678C30.6766 17.5328 30.5127 17.5018 30.3441 17.4748C29.754 17.3793 29.1074 17.334 28.4147 17.334H22.5676C22.4237 17.334 22.2869 17.3666 22.1644 17.4254C21.8948 17.5551 21.6944 17.8104 21.6459 18.1229L20.402 26.0013L20.3662 26.2311C20.4481 25.7126 20.8911 25.3308 21.4168 25.3308H23.6055C27.9041 25.3308 31.2699 23.5851 32.2537 18.5349C32.2831 18.3854 32.3078 18.2398 32.33 18.0975C32.0811 17.9655 31.8115 17.8525 31.5212 17.7563C31.4496 17.7324 31.3757 17.7094 31.3009 17.6871Z" fill="white" fill-opacity="0.8"/>
            <path d="M21.6461 18.1231C21.6946 17.8105 21.895 17.5552 22.1646 17.4264C22.2879 17.3675 22.4239 17.3349 22.5678 17.3349H28.4149C29.1077 17.3349 29.7542 17.3803 30.3444 17.4757C30.513 17.5027 30.6768 17.5338 30.8367 17.5687C30.9957 17.6045 31.1508 17.6443 31.3011 17.688C31.3759 17.7103 31.4498 17.7334 31.5222 17.7564C31.8125 17.8527 32.0821 17.9664 32.331 18.0976C32.6237 16.231 32.3287 14.9601 31.3194 13.8093C30.2068 12.5424 28.1986 12 25.629 12H18.169C17.6441 12 17.1963 12.3817 17.1152 12.9011L14.0079 32.5969C13.9467 32.9866 14.2473 33.3381 14.6402 33.3381H19.2458L20.4022 26.0014L21.6461 18.1231Z" fill="white"/>
          </svg>
          <!-- Visa SVG -->
          <svg xmlns="http://www.w3.org/2000/svg" width="96" height="60" viewBox="0 0 1000 324">
            <path d="m293.2 348.73l33.359-195.76h53.358l-33.384 195.76h-53.333zm246.11-191.54c-10.569-3.966-27.135-8.222-47.821-8.222-52.726 0-89.863 26.551-90.181 64.604-0.297 28.129 26.515 43.822 46.754 53.185 20.771 9.598 27.752 15.716 27.652 24.283-0.133 13.123-16.586 19.115-31.924 19.115-21.355 0-32.701-2.967-50.225-10.273l-6.878-3.111-7.487 43.822c12.463 5.467 35.508 10.199 59.438 10.445 56.09 0 92.502-26.248 92.916-66.885 0.199-22.27-14.016-39.215-44.801-53.188-18.65-9.056-30.072-15.099-29.951-24.269 0-8.137 9.668-16.838 30.56-16.838 17.446-0.271 30.088 3.534 39.936 7.5l4.781 2.259 7.231-42.427m137.31-4.223h-41.23c-12.772 0-22.332 3.486-27.94 16.234l-79.245 179.4h56.031s9.159-24.121 11.231-29.418c6.123 0 60.555 0.084 68.336 0.084 1.596 6.854 6.492 29.334 6.492 29.334h49.512l-43.187-195.64zm-65.417 126.41c4.414-11.279 21.26-54.724 21.26-54.724-0.314 0.521 4.381-11.334 7.074-18.684l3.606 16.878s10.217 46.729 12.353 56.527h-44.293v3e-3zm-363.3-126.41l-52.239 133.5-5.565-27.129c-9.726-31.274-40.025-65.157-73.898-82.12l47.767 171.2 56.455-0.063 84.004-195.39-56.524-1e-3" fill="#0E4595"/>
            <path d="m146.92 152.96h-86.041l-0.682 4.073c66.939 16.204 111.23 55.363 129.62 102.42l-18.709-89.96c-3.229-12.396-12.597-16.096-24.186-16.528" fill="#F2AE14"/>
          </svg>
          <!-- Mastercard SVG -->
          <svg xmlns="http://www.w3.org/2000/svg" width="56" height="50" viewBox="0 0 130 69.9">
            <path d="M48.37 15.14h34.66v56.61H48.37z" fill="#ff5f00"/>
            <path d="M51.94 43.45a35.94 35.94 0 0113.75-28.3 36 36 0 100 56.61 35.94 35.94 0 01-13.75-28.31z" fill="#eb001b"/>
            <path d="M120.5 65.76V64.6h.5v-.24h-1.19v.24h.47v1.16zm2.31 0v-1.4h-.36l-.42 1-.42-1h-.36v1.4h.26V64.7l.39.93h.27l.39-.93v1.06z" fill="#f79e1b"/>
            <path d="M123.94 43.45a36 36 0 01-58.25 28.3 36 36 0 000-56.61 36 36 0 0158.25 28.3z" fill="#f79e1b"/>
          </svg>
        </div>
      </div>
      <div>
        © {{ currentYear }}
        <a href="mailto:support@aibrainl.ink" class="hover:text-gray-700 dark:hover:text-gray-300" target="_blank" rel="noopener noreferrer">
          support@aibrainl.ink
        </a>
      </div>
    </div>
  </footer>


            <!-- Dark Mode Toggle -->
            <DarkModeToggle />
        </div>
    </div>
</template>

<style scoped>


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
