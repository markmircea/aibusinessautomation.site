<script setup>
import { Link } from '@inertiajs/vue3';
import WebDevelopmentLayout from './WebDevelopmentLayout.vue';
import WebDevContactSection from '@/Components/WebDevelopment/ContactSection.vue';

const serviceData = {
    title: 'E-commerce Platform Development',
    description: 'Custom e-commerce solutions that drive sales, enhance customer experience, and scale with your business needs.',
    focus: 'Building robust, secure, and user-friendly online stores with seamless payment processing and inventory management.',
    keyPoint: 'Increase conversion rates and customer satisfaction with tailored e-commerce platforms designed for your specific business requirements.',
    sections: [
        {
            id: 'overview',
            title: 'Service Overview'
        },
        {
            id: 'features',
            title: 'Key Features'
        },
        {
            id: 'technologies',
            title: 'Technologies'
        },
        {
            id: 'process',
            title: 'Development Process'
        },
        {
            id: 'benefits',
            title: 'Benefits'
        }
    ]
};
</script>

<template>
    <WebDevelopmentLayout v-bind="serviceData">
        <!-- Hero Section -->
        <div class="relative overflow-hidden animated-bg">
            <!-- Animated background elements -->
            <div class="absolute inset-0">
                <div class="absolute inset-0 bg-grid-pattern opacity-10"></div>
                <div class="absolute inset-0 bg-gradient-radial from-blue-500/30 to-transparent"></div>
            </div>

            <div class="relative max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-24 sm:py-32">
                <div class="text-center">
                    <h1 class="hero-text text-4xl sm:text-5xl md:text-6xl font-extrabold text-white mb-6">
                        {{ serviceData.title }}
                        <span class="block text-blue-400">That Drives Business Growth</span>
                    </h1>

                    <p class="hero-text mx-auto max-w-2xl text-xl sm:text-2xl text-blue-100 mb-6">
                        {{ serviceData.description }}
                    </p>

                    <p class="hero-text mx-auto max-w-2xl text-lg text-blue-200 mb-6">
                        {{ serviceData.focus }}
                    </p>

                    <div class="hero-text mx-auto max-w-3xl text-center mb-10">
                        <p class="text-lg text-blue-200 mb-4">
                            Powerful e-commerce solutions built with industry-leading technologies:
                        </p>
                        <div class="flex flex-wrap justify-center gap-4 text-sm">
                            <span class="px-3 py-1 bg-blue-900/30 rounded-full text-blue-100">Shopify</span>
                            <span class="px-3 py-1 bg-blue-900/30 rounded-full text-blue-100">WooCommerce</span>
                            <span class="px-3 py-1 bg-blue-900/30 rounded-full text-blue-100">Magento</span>
                            <span class="px-3 py-1 bg-blue-900/30 rounded-full text-blue-100">BigCommerce</span>
                            <span class="px-3 py-1 bg-blue-900/30 rounded-full text-blue-100">Laravel</span>
                            <span class="px-3 py-1 bg-green-900/30 rounded-full text-green-100">+ Custom
                                Solutions</span>
                        </div>
                    </div>

                    <div class="hero-text flex flex-wrap justify-center gap-4">
                        <a href="#overview"
                            class="inline-flex items-center px-6 py-3 border border-transparent text-base font-medium rounded-md text-white bg-blue-600 hover:bg-blue-700 transition-colors duration-200">
                            Explore Features
                            <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 ml-2" viewBox="0 0 20 20"
                                fill="currentColor">
                                <path fill-rule="evenodd"
                                    d="M16.707 10.293a1 1 0 010 1.414l-6 6a1 1 0 01-1.414 0l-6-6a1 1 0 111.414-1.414L9 14.586V3a1 1 0 012 0v11.586l4.293-4.293a1 1 0 011.414 0z"
                                    clip-rule="evenodd" />
                            </svg>
                        </a>
                        <a href="#contact"
                            class="inline-flex items-center px-6 py-3 border border-blue-400 text-base font-medium rounded-md text-blue-100 hover:bg-blue-800/50 transition-colors duration-200">
                            Contact Us
                        </a>
                        <a href="#contact"
                            class="inline-flex items-center px-6 py-3 border border-transparent text-base font-medium rounded-md text-white bg-green-600 hover:bg-green-700 transition-colors duration-200">
                            Request a Quote
                            <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 ml-2" viewBox="0 0 20 20"
                                fill="currentColor">
                                <path d="M10 12a2 2 0 100-4 2 2 0 000 4z" />
                                <path fill-rule="evenodd"
                                    d="M.458 10C1.732 5.943 5.522 3 10 3s8.268 2.943 9.542 7c-1.274 4.057-5.064 7-9.542 7S1.732 14.057.458 10zM14 10a4 4 0 11-8 0 4 4 0 018 0z"
                                    clip-rule="evenodd" />
                            </svg>
                        </a>
                    </div>

                    <!-- Stats -->
                    <div class="hero-text mt-16 grid grid-cols-2 gap-8 md:grid-cols-4">
                        <div class="text-center transform hover:scale-105 transition-transform duration-300">
                            <div class="text-3xl font-bold text-white">24/7</div>
                            <div class="text-sm text-blue-200">Customer Support</div>
                        </div>
                        <div class="text-center transform hover:scale-105 transition-transform duration-300">
                            <div class="text-3xl font-bold text-white">100%</div>
                            <div class="text-sm text-blue-200">Secure Transactions</div>
                        </div>
                        <div class="text-center transform hover:scale-105 transition-transform duration-300">
                            <div class="text-3xl font-bold text-white">+40%</div>
                            <div class="text-sm text-blue-200">Conversion Rate</div>
                        </div>
                        <div class="text-center transform hover:scale-105 transition-transform duration-300">
                            <div class="text-3xl font-bold text-white">99.9%</div>
                            <div class="text-sm text-blue-200">Uptime Guarantee</div>
                        </div>
                    </div>
                </div>
            </div>
        </div>

        <!-- Main Content -->
        <div class="bg-white dark:bg-gray-900 py-16">
            <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
                <!-- Service Overview Section -->
                <div id="overview" data-section="overview"
                    class="content-section bg-white dark:bg-gray-800 rounded-xl shadow-xl p-8 mb-16">
                    <h2 class="text-2xl font-bold mb-6 text-gray-800 dark:text-white">Service Overview</h2>
                    <p class="text-gray-600 dark:text-gray-300 mb-4">
                        Our e-commerce development services provide end-to-end solutions for businesses looking to
                        establish or enhance their online retail presence. We create custom e-commerce platforms that
                        are tailored to your specific business needs, ensuring a seamless shopping experience for your
                        customers and efficient management tools for your team.
                    </p>
                    <p class="text-gray-600 dark:text-gray-300">
                        Whether you're launching a new online store or upgrading an existing one, our team delivers
                        scalable, secure, and feature-rich e-commerce solutions that drive conversions and growth.
                    </p>
                </div>

                <!-- Key Features Section with Icons -->
                <div id="features" data-section="features"
                    class="content-section bg-white dark:bg-gray-800 rounded-xl shadow-xl p-8 mb-16">
                    <div class="text-center mb-10">
                        <h2 class="text-3xl font-bold mb-6 text-gray-800 dark:text-white">Key Features</h2>
                        <p class="max-w-3xl mx-auto text-lg text-gray-600 dark:text-gray-300">
                            Our e-commerce platforms come packed with powerful features designed to maximize sales and
                            streamline operations.
                        </p>
                    </div>

                    <div class="grid grid-cols-1 md:grid-cols-3 gap-8">
                        <div
                            class="bg-gray-50 dark:bg-gray-700 rounded-xl p-6 hover:shadow-lg transition-all duration-300 transform hover:scale-105 hover:bg-blue-50 dark:hover:bg-blue-900/20">
                            <div
                                class="w-16 h-16 bg-blue-100 dark:bg-blue-800 rounded-lg flex items-center justify-center mb-4 mx-auto">
                                <svg class="w-8 h-8 text-blue-600 dark:text-blue-300" fill="none" stroke="currentColor"
                                    viewBox="0 0 24 24">
                                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                                        d="M12 18h.01M8 21h8a2 2 0 002-2V5a2 2 0 00-2-2H8a2 2 0 00-2 2v14a2 2 0 002 2z" />
                                </svg>
                            </div>
                            <h3 class="text-xl font-semibold mb-3 text-gray-800 dark:text-white text-center">Responsive
                                Design</h3>
                            <p class="text-gray-600 dark:text-gray-300 text-center">Mobile-optimized shopping
                                experiences that look great on any device, ensuring you never lose a sale due to poor
                                usability.</p>
                        </div>

                        <div
                            class="bg-gray-50 dark:bg-gray-700 rounded-xl p-6 hover:shadow-lg transition-all duration-300 transform hover:scale-105 hover:bg-blue-50 dark:hover:bg-blue-900/20">
                            <div
                                class="w-16 h-16 bg-green-100 dark:bg-green-800 rounded-lg flex items-center justify-center mb-4 mx-auto">
                                <svg class="w-8 h-8 text-green-600 dark:text-green-300" fill="none"
                                    stroke="currentColor" viewBox="0 0 24 24">
                                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                                        d="M9 12l2 2 4-4m5.618-4.016A11.955 11.955 0 0112 2.944a11.955 11.955 0 01-8.618 3.04A12.02 12.02 0 003 9c0 5.591 3.824 10.29 9 11.622 5.176-1.332 9-6.03 9-11.622 0-1.042-.133-2.052-.382-3.016z" />
                                </svg>
                            </div>
                            <h3 class="text-xl font-semibold mb-3 text-gray-800 dark:text-white text-center">Secure
                                Payments</h3>
                            <p class="text-gray-600 dark:text-gray-300 text-center">Integration with multiple payment
                                gateways and robust security measures to protect customer data and transactions.</p>
                        </div>

                        <div
                            class="bg-gray-50 dark:bg-gray-700 rounded-xl p-6 hover:shadow-lg transition-all duration-300 transform hover:scale-105 hover:bg-blue-50 dark:hover:bg-blue-900/20">
                            <div
                                class="w-16 h-16 bg-purple-100 dark:bg-purple-800 rounded-lg flex items-center justify-center mb-4 mx-auto">
                                <svg class="w-8 h-8 text-purple-600 dark:text-purple-300" fill="none"
                                    stroke="currentColor" viewBox="0 0 24 24">
                                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                                        d="M20 7l-8-4-8 4m16 0l-8 4m8-4v10l-8 4m0-10L4 7m8 4v10M4 7v10l8 4" />
                                </svg>
                            </div>
                            <h3 class="text-xl font-semibold mb-3 text-gray-800 dark:text-white text-center">Inventory
                                Management</h3>
                            <p class="text-gray-600 dark:text-gray-300 text-center">Automated stock tracking, low-stock
                                alerts, and multi-warehouse support to streamline your inventory operations.</p>
                        </div>

                        <div
                            class="bg-gray-50 dark:bg-gray-700 rounded-xl p-6 hover:shadow-lg transition-all duration-300 transform hover:scale-105 hover:bg-blue-50 dark:hover:bg-blue-900/20">
                            <div
                                class="w-16 h-16 bg-yellow-100 dark:bg-yellow-800 rounded-lg flex items-center justify-center mb-4 mx-auto">
                                <svg class="w-8 h-8 text-yellow-600 dark:text-yellow-300" fill="none"
                                    stroke="currentColor" viewBox="0 0 24 24">
                                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                                        d="M17 20h5v-2a3 3 0 00-5.356-1.857M17 20H7m10 0v-2c0-.656-.126-1.283-.356-1.857M7 20H2v-2a3 3 0 015.356-1.857M7 20v-2c0-.656.126-1.283.356-1.857m0 0a5.002 5.002 0 019.288 0M15 7a3 3 0 11-6 0 3 3 0 016 0zm6 3a2 2 0 11-4 0 2 2 0 014 0zM7 10a2 2 0 11-4 0 2 2 0 014 0z" />
                                </svg>
                            </div>
                            <h3 class="text-xl font-semibold mb-3 text-gray-800 dark:text-white text-center">Customer
                                Accounts</h3>
                            <p class="text-gray-600 dark:text-gray-300 text-center">User-friendly account management,
                                order history, wishlist functionality, and personalized shopping experiences.</p>
                        </div>

                        <div
                            class="bg-gray-50 dark:bg-gray-700 rounded-xl p-6 hover:shadow-lg transition-all duration-300 transform hover:scale-105 hover:bg-blue-50 dark:hover:bg-blue-900/20">
                            <div
                                class="w-16 h-16 bg-red-100 dark:bg-red-800 rounded-lg flex items-center justify-center mb-4 mx-auto">
                                <svg class="w-8 h-8 text-red-600 dark:text-red-300" fill="none" stroke="currentColor"
                                    viewBox="0 0 24 24">
                                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                                        d="M11 3.055A9.001 9.001 0 1020.945 13H11V3.055z" />
                                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                                        d="M20.488 9H15V3.512A9.025 9.025 0 0120.488 9z" />
                                </svg>
                            </div>
                            <h3 class="text-xl font-semibold mb-3 text-gray-800 dark:text-white text-center">Marketing
                                Tools</h3>
                            <p class="text-gray-600 dark:text-gray-300 text-center">Built-in SEO optimization, discount
                                systems, email marketing integration, and analytics to drive traffic and sales.</p>
                        </div>

                        <div
                            class="bg-gray-50 dark:bg-gray-700 rounded-xl p-6 hover:shadow-lg transition-all duration-300 transform hover:scale-105 hover:bg-blue-50 dark:hover:bg-blue-900/20">
                            <div
                                class="w-16 h-16 bg-indigo-100 dark:bg-indigo-800 rounded-lg flex items-center justify-center mb-4 mx-auto">
                                <svg class="w-8 h-8 text-indigo-600 dark:text-indigo-300" fill="none"
                                    stroke="currentColor" viewBox="0 0 24 24">
                                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                                        d="M9 19v-6a2 2 0 00-2-2H5a2 2 0 00-2 2v6a2 2 0 002 2h2a2 2 0 002-2zm0 0V9a2 2 0 012-2h2a2 2 0 012 2v10m-6 0a2 2 0 002 2h2a2 2 0 002-2m0 0V5a2 2 0 012-2h2a2 2 0 012 2v14a2 2 0 01-2 2h-2a2 2 0 01-2-2z" />
                                </svg>
                            </div>
                            <h3 class="text-xl font-semibold mb-3 text-gray-800 dark:text-white text-center">Admin
                                Dashboard</h3>
                            <p class="text-gray-600 dark:text-gray-300 text-center">Comprehensive control panel for
                                managing products, orders, customers, and generating reports on store performance.</p>
                        </div>
                    </div>
                </div>

                <!-- Technologies Section -->
                <div id="technologies" data-section="technologies"
                    class="content-section bg-white dark:bg-gray-800 rounded-xl shadow-xl p-8 mb-16">
                    <h2 class="text-2xl font-bold mb-6 text-gray-800 dark:text-white">Technologies</h2>
                    <p class="text-gray-600 dark:text-gray-300 mb-6">
                        We leverage the latest technologies and platforms to build robust e-commerce solutions:
                    </p>
                    <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-4">
                        <div class="bg-gray-50 dark:bg-gray-700 p-4 rounded-lg">
                            <h3 class="font-semibold text-gray-800 dark:text-white mb-2">Platforms</h3>
                            <ul class="list-disc list-inside text-gray-600 dark:text-gray-300 space-y-1">
                                <li>Shopify</li>
                                <li>WooCommerce</li>
                                <li>Magento</li>
                                <li>BigCommerce</li>
                                <li>Custom Solutions</li>
                            </ul>
                        </div>
                        <div class="bg-gray-50 dark:bg-gray-700 p-4 rounded-lg">
                            <h3 class="font-semibold text-gray-800 dark:text-white mb-2">Frontend</h3>
                            <ul class="list-disc list-inside text-gray-600 dark:text-gray-300 space-y-1">
                                <li>React.js</li>
                                <li>Vue.js</li>
                                <li>Next.js</li>
                                <li>Tailwind CSS</li>
                                <li>Bootstrap</li>
                            </ul>
                        </div>
                        <div class="bg-gray-50 dark:bg-gray-700 p-4 rounded-lg">
                            <h3 class="font-semibold text-gray-800 dark:text-white mb-2">Backend</h3>
                            <ul class="list-disc list-inside text-gray-600 dark:text-gray-300 space-y-1">
                                <li>PHP/Laravel</li>
                                <li>Node.js</li>
                                <li>Python/Django</li>
                                <li>Ruby on Rails</li>
                                <li>GraphQL</li>
                            </ul>
                        </div>
                        <div class="bg-gray-50 dark:bg-gray-700 p-4 rounded-lg">
                            <h3 class="font-semibold text-gray-800 dark:text-white mb-2">Payment Gateways</h3>
                            <ul class="list-disc list-inside text-gray-600 dark:text-gray-300 space-y-1">
                                <li>Stripe</li>
                                <li>PayPal</li>
                                <li>Square</li>
                                <li>Braintree</li>
                                <li>Authorize.net</li>
                            </ul>
                        </div>
                        <div class="bg-gray-50 dark:bg-gray-700 p-4 rounded-lg">
                            <h3 class="font-semibold text-gray-800 dark:text-white mb-2">Integrations</h3>
                            <ul class="list-disc list-inside text-gray-600 dark:text-gray-300 space-y-1">
                                <li>Shipping APIs</li>
                                <li>CRM Systems</li>
                                <li>ERP Solutions</li>
                                <li>Marketing Tools</li>
                                <li>Analytics Platforms</li>
                            </ul>
                        </div>
                        <div class="bg-gray-50 dark:bg-gray-700 p-4 rounded-lg">
                            <h3 class="font-semibold text-gray-800 dark:text-white mb-2">Hosting & Infrastructure</h3>
                            <ul class="list-disc list-inside text-gray-600 dark:text-gray-300 space-y-1">
                                <li>AWS</li>
                                <li>Google Cloud</li>
                                <li>Microsoft Azure</li>
                                <li>Cloudflare</li>
                                <li>Docker/Kubernetes</li>
                            </ul>
                        </div>
                    </div>
                </div>

                <!-- Development Process Section with Timeline -->
                <div id="benefits" data-section="process"
                    class="content-section bg-white dark:bg-gray-800 rounded-xl shadow-xl p-8 mb-16">
                    <div class="text-center mb-10">
                        <h2 class="text-3xl font-bold mb-6 text-gray-800 dark:text-white">Development Process</h2>
                        <p class="max-w-3xl mx-auto text-lg text-gray-600 dark:text-gray-300">
                            Our proven development methodology ensures a smooth journey from concept to launch.
                        </p>
                    </div>

                    <!-- Process Timeline -->
                    <div class="mt-12">
                        <div class="relative">
                            <!-- Timeline Line -->
                            <div
                                class="absolute left-1/2 transform -translate-x-1/2 h-full w-1 bg-blue-200 dark:bg-blue-800">
                            </div>

                            <!-- Timeline Items -->
                            <div class="space-y-12">
                                <div class="flex items-center justify-center">
                                    <div class="w-1/2 pr-8 text-right">
                                        <h4 class="text-lg font-semibold text-blue-600 dark:text-blue-400">Discovery &
                                            Planning</h4>
                                        <p class="text-gray-600 dark:text-gray-400">Understanding your business goals
                                            and requirements</p>
                                    </div>
                                    <div class="w-4 h-4 bg-blue-500 rounded-full"></div>
                                    <div class="w-1/2 pl-8"></div>
                                </div>

                                <div class="flex items-center justify-center">
                                    <div class="w-1/2 pr-8"></div>
                                    <div class="w-4 h-4 bg-blue-500 rounded-full"></div>
                                    <div class="w-1/2 pl-8">
                                        <h4 class="text-lg font-semibold text-blue-600 dark:text-blue-400">UX/UI Design
                                        </h4>
                                        <p class="text-gray-600 dark:text-gray-400">Creating intuitive,
                                            conversion-focused interfaces</p>
                                    </div>
                                </div>

                                <div class="flex items-center justify-center">
                                    <div class="w-1/2 pr-8 text-right">
                                        <h4 class="text-lg font-semibold text-blue-600 dark:text-blue-400">Development
                                        </h4>
                                        <p class="text-gray-600 dark:text-gray-400">Building your e-commerce platform
                                            with the right technologies</p>
                                    </div>
                                    <div class="w-4 h-4 bg-blue-500 rounded-full"></div>
                                    <div class="w-1/2 pl-8"></div>
                                </div>

                                <div class="flex items-center justify-center">
                                    <div class="w-1/2 pr-8"></div>
                                    <div class="w-4 h-4 bg-blue-500 rounded-full"></div>
                                    <div class="w-1/2 pl-8">
                                        <h4 class="text-lg font-semibold text-blue-600 dark:text-blue-400">Testing & QA
                                        </h4>
                                        <p class="text-gray-600 dark:text-gray-400">Ensuring flawless functionality
                                            across devices</p>
                                    </div>
                                </div>

                                <div class="flex items-center justify-center">
                                    <div class="w-1/2 pr-8 text-right">
                                        <h4 class="text-lg font-semibold text-blue-600 dark:text-blue-400">Launch &
                                            Training</h4>
                                        <p class="text-gray-600 dark:text-gray-400">Deploying your store and training
                                            your team</p>
                                    </div>
                                    <div class="w-4 h-4 bg-blue-500 rounded-full"></div>
                                    <div class="w-1/2 pl-8"></div>
                                </div>

                                <div class="flex items-center justify-center">
                                    <div class="w-1/2 pr-8"></div>
                                    <div class="w-4 h-4 bg-blue-500 rounded-full"></div>
                                    <div class="w-1/2 pl-8">
                                        <h4 class="text-lg font-semibold text-blue-600 dark:text-blue-400">Ongoing
                                            Support</h4>
                                        <p class="text-gray-600 dark:text-gray-400">Continuous optimization and
                                            technical support</p>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>

                <!-- Benefits Section -->
                <div id="process" data-section="benefits"
                    class="content-section bg-white dark:bg-gray-800 rounded-xl shadow-xl p-8">
                    <h2 class="text-2xl font-bold mb-6 text-gray-800 dark:text-white">Benefits</h2>
                    <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
                        <div class="flex">
                            <div class="flex-shrink-0 text-blue-600 dark:text-blue-400">
                                <svg class="w-6 h-6" fill="currentColor" viewBox="0 0 20 20"
                                    xmlns="http://www.w3.org/2000/svg">
                                    <path fill-rule="evenodd"
                                        d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z"
                                        clip-rule="evenodd"></path>
                                </svg>
                            </div>
                            <div class="ml-4">
                                <h3 class="text-lg font-semibold text-gray-800 dark:text-white">Increased Sales</h3>
                                <p class="text-gray-600 dark:text-gray-300 mt-1">Optimized user experience and checkout
                                    process leads to higher conversion rates and increased average order value.</p>
                            </div>
                        </div>
                        <div class="flex">
                            <div class="flex-shrink-0 text-blue-600 dark:text-blue-400">
                                <svg class="w-6 h-6" fill="currentColor" viewBox="0 0 20 20"
                                    xmlns="http://www.w3.org/2000/svg">
                                    <path fill-rule="evenodd"
                                        d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z"
                                        clip-rule="evenodd"></path>
                                </svg>
                            </div>
                            <div class="ml-4">
                                <h3 class="text-lg font-semibold text-gray-800 dark:text-white">Scalability</h3>
                                <p class="text-gray-600 dark:text-gray-300 mt-1">Our solutions grow with your business,
                                    handling increased traffic, products, and orders without performance issues.</p>
                            </div>
                        </div>
                        <div class="flex">
                            <div class="flex-shrink-0 text-blue-600 dark:text-blue-400">
                                <svg class="w-6 h-6" fill="currentColor" viewBox="0 0 20 20"
                                    xmlns="http://www.w3.org/2000/svg">
                                    <path fill-rule="evenodd"
                                        d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z"
                                        clip-rule="evenodd"></path>
                                </svg>
                            </div>
                            <div class="ml-4">
                                <h3 class="text-lg font-semibold text-gray-800 dark:text-white">Enhanced Customer
                                    Experience</h3>
                                <p class="text-gray-600 dark:text-gray-300 mt-1">Intuitive navigation, personalized
                                    recommendations, and streamlined checkout create a superior shopping experience.</p>
                            </div>
                        </div>
                        <div class="flex">
                            <div class="flex-shrink-0 text-blue-600 dark:text-blue-400">
                                <svg class="w-6 h-6" fill="currentColor" viewBox="0 0 20 20"
                                    xmlns="http://www.w3.org/2000/svg">
                                    <path fill-rule="evenodd"
                                        d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z"
                                        clip-rule="evenodd"></path>
                                </svg>
                            </div>
                            <div class="ml-4">
                                <h3 class="text-lg font-semibold text-gray-800 dark:text-white">Operational Efficiency
                                </h3>
                                <p class="text-gray-600 dark:text-gray-300 mt-1">Automated inventory management, order
                                    processing, and customer communications reduce manual work and errors.</p>
                            </div>
                        </div>
                        <div class="flex">
                            <div class="flex-shrink-0 text-blue-600 dark:text-blue-400">
                                <svg class="w-6 h-6" fill="currentColor" viewBox="0 0 20 20"
                                    xmlns="http://www.w3.org/2000/svg">
                                    <path fill-rule="evenodd"
                                        d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z"
                                        clip-rule="evenodd"></path>
                                </svg>
                            </div>
                            <div class="ml-4">
                                <h3 class="text-lg font-semibold text-gray-800 dark:text-white">Competitive Advantage
                                </h3>
                                <p class="text-gray-600 dark:text-gray-300 mt-1">Stand out from competitors with a
                                    professional, feature-rich online store that delivers exceptional shopping
                                    experiences.</p>
                            </div>
                        </div>
                    </div>
                </div>

                <!-- Call to Action -->
                <div class="content-section mt-16 text-center py-8">
                    <div class="bg-gradient-to-r from-blue-600 to-indigo-700 rounded-xl shadow-xl p-12 text-white">
                        <h2 class="text-3xl font-bold mb-6">Ready to Launch Your E-commerce Platform?</h2>
                        <p class="text-xl text-blue-100 mb-8 max-w-3xl mx-auto">
                            Get in touch with our team to discuss your e-commerce project and discover how we can help
                            you create a successful online store.
                        </p>
                        <Link :href="route('web-development.ecommerce') + '#contact'" 
                            class="inline-flex items-center px-8 py-4 border border-transparent text-lg font-medium rounded-xl text-white bg-blue-500 hover:bg-blue-400 transition-all duration-300 transform hover:scale-105 hover:shadow-lg">
                            Discuss Your E-commerce Project
                            <svg class="ml-3 -mr-1 w-6 h-6" fill="currentColor" viewBox="0 0 20 20">
                                <path fill-rule="evenodd"
                                    d="M10.293 3.293a1 1 0 011.414 0l6 6a1 1 0 010 1.414l-6 6a1 1 0 01-1.414-1.414L14.586 11H3a1 1 0 110-2h11.586l-4.293-4.293a1 1 0 010-1.414z"
                                    clip-rule="evenodd" />
                            </svg>
                        </Link>
                    </div>
                </div>
            </div>
        </div>

        <!-- Contact Section -->
        <WebDevContactSection />
    </WebDevelopmentLayout>
</template>

<style scoped>
.bg-grid-pattern {
    background-image: radial-gradient(circle, #ffffff 1px, transparent 1px);
    background-size: 30px 30px;
    animation: pulse 8s ease-in-out infinite;
}

.bg-gradient-radial {
    background: radial-gradient(circle at center, var(--tw-gradient-from), var(--tw-gradient-to));
    animation: breathe 15s ease-in-out infinite;
}

@keyframes pulse {

    0%,
    100% {
        opacity: 0.1;
    }

    50% {
        opacity: 0.25;
    }
}

@keyframes breathe {

    0%,
    100% {
        transform: scale(1);
    }

    50% {
        transform: scale(1.05);
    }
}

.animated-bg {
    background: linear-gradient(135deg, #1e3a8a, #1e40af, #1e3a8a);
    background-size: 400% 400%;
    animation: gradient 15s ease infinite;
}

.dark .animated-bg {
    background: linear-gradient(135deg, #111827, #1f2937, #111827);
    background-size: 400% 400%;
    animation: gradient 15s ease infinite;
}

@keyframes gradient {
    0% {
        background-position: 0% 50%;
    }

    50% {
        background-position: 100% 50%;
    }

    100% {
        background-position: 0% 50%;
    }
}
</style>
