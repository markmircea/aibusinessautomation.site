<script setup>
import { Link } from '@inertiajs/vue3';
import WebDevelopmentLayout from './WebDevelopmentLayout.vue';

const serviceData = {
    title: 'Mobile Application Development',
    description: 'Custom mobile apps that deliver exceptional user experiences across iOS and Android platforms.',
    focus: 'Building intuitive, high-performance mobile applications that solve real business problems and engage users.',
    keyPoint: 'Extend your digital presence with native and cross-platform mobile apps that provide seamless experiences for your customers.',
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
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 mt-8 space-y-12">
            <!-- Hero Section -->
            <div class="bg-gradient-to-r from-green-500 to-teal-600 rounded-xl shadow-xl p-8 text-white">
                <h1 class="text-3xl font-bold mb-4">{{ serviceData.title }}</h1>
                <p class="text-xl text-green-100 mb-6">{{ serviceData.description }}</p>
                <div class="grid grid-cols-1 md:grid-cols-2 gap-6 mt-8">
                    <div class="bg-white/10 rounded-lg p-6">
                        <h3 class="font-semibold text-lg mb-2">Our Focus</h3>
                        <p>{{ serviceData.focus }}</p>
                    </div>
                    <div class="bg-white/10 rounded-lg p-6">
                        <h3 class="font-semibold text-lg mb-2">Key Benefits</h3>
                        <p>{{ serviceData.keyPoint }}</p>
                    </div>
                </div>
            </div>

            <!-- Service Overview Section -->
            <div id="overview" data-section="overview" class="bg-white dark:bg-gray-800 rounded-xl shadow p-8">
                <h2 class="text-2xl font-bold mb-6 text-gray-800 dark:text-white">Service Overview</h2>
                <p class="text-gray-600 dark:text-gray-300 mb-4">
                    Our mobile application development services provide end-to-end solutions for businesses looking to engage customers through iOS and Android platforms. We create custom mobile apps that are tailored to your specific business needs, ensuring intuitive user experiences and robust functionality.
                </p>
                <p class="text-gray-600 dark:text-gray-300">
                    Whether you need a consumer-facing app or an enterprise solution for internal use, our team delivers scalable, secure, and feature-rich mobile applications that drive engagement and achieve your business objectives.
                </p>
            </div>

            <!-- Key Features Section -->
            <div id="features" data-section="features" class="bg-white dark:bg-gray-800 rounded-xl shadow p-8">
                <h2 class="text-2xl font-bold mb-6 text-gray-800 dark:text-white">Key Features</h2>
                <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
                    <div class="border border-gray-200 dark:border-gray-700 rounded-lg p-6 hover:shadow-md transition-shadow">
                        <h3 class="text-xl font-semibold mb-3 text-gray-800 dark:text-white">Native & Cross-Platform</h3>
                        <p class="text-gray-600 dark:text-gray-300">Development options for both native (iOS/Android) and cross-platform solutions based on your specific requirements.</p>
                    </div>
                    <div class="border border-gray-200 dark:border-gray-700 rounded-lg p-6 hover:shadow-md transition-shadow">
                        <h3 class="text-xl font-semibold mb-3 text-gray-800 dark:text-white">Intuitive UI/UX</h3>
                        <p class="text-gray-600 dark:text-gray-300">User-centered design that follows platform guidelines while providing a unique and engaging experience.</p>
                    </div>
                    <div class="border border-gray-200 dark:border-gray-700 rounded-lg p-6 hover:shadow-md transition-shadow">
                        <h3 class="text-xl font-semibold mb-3 text-gray-800 dark:text-white">Offline Functionality</h3>
                        <p class="text-gray-600 dark:text-gray-300">Capability to work offline with data synchronization when connectivity is restored, ensuring uninterrupted user experience.</p>
                    </div>
                    <div class="border border-gray-200 dark:border-gray-700 rounded-lg p-6 hover:shadow-md transition-shadow">
                        <h3 class="text-xl font-semibold mb-3 text-gray-800 dark:text-white">Push Notifications</h3>
                        <p class="text-gray-600 dark:text-gray-300">Engagement-boosting notifications to keep users informed and drive app usage with timely, relevant messages.</p>
                    </div>
                    <div class="border border-gray-200 dark:border-gray-700 rounded-lg p-6 hover:shadow-md transition-shadow">
                        <h3 class="text-xl font-semibold mb-3 text-gray-800 dark:text-white">API Integration</h3>
                        <p class="text-gray-600 dark:text-gray-300">Seamless connection with your existing systems, third-party services, and data sources for a unified experience.</p>
                    </div>
                    <div class="border border-gray-200 dark:border-gray-700 rounded-lg p-6 hover:shadow-md transition-shadow">
                        <h3 class="text-xl font-semibold mb-3 text-gray-800 dark:text-white">Analytics & Reporting</h3>
                        <p class="text-gray-600 dark:text-gray-300">Built-in analytics to track user behavior, app performance, and key metrics for continuous improvement.</p>
                    </div>
                </div>
            </div>

            <!-- Technologies Section -->
            <div id="technologies" data-section="technologies" class="bg-white dark:bg-gray-800 rounded-xl shadow p-8">
                <h2 class="text-2xl font-bold mb-6 text-gray-800 dark:text-white">Technologies</h2>
                <p class="text-gray-600 dark:text-gray-300 mb-6">
                    We leverage the latest technologies and frameworks to build robust mobile applications:
                </p>
                <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-4">
                    <div class="bg-gray-50 dark:bg-gray-700 p-4 rounded-lg">
                        <h3 class="font-semibold text-gray-800 dark:text-white mb-2">Native iOS</h3>
                        <ul class="list-disc list-inside text-gray-600 dark:text-gray-300 space-y-1">
                            <li>Swift</li>
                            <li>Objective-C</li>
                            <li>SwiftUI</li>
                            <li>UIKit</li>
                            <li>Core Data</li>
                        </ul>
                    </div>
                    <div class="bg-gray-50 dark:bg-gray-700 p-4 rounded-lg">
                        <h3 class="font-semibold text-gray-800 dark:text-white mb-2">Native Android</h3>
                        <ul class="list-disc list-inside text-gray-600 dark:text-gray-300 space-y-1">
                            <li>Kotlin</li>
                            <li>Java</li>
                            <li>Jetpack Compose</li>
                            <li>Android SDK</li>
                            <li>Room Database</li>
                        </ul>
                    </div>
                    <div class="bg-gray-50 dark:bg-gray-700 p-4 rounded-lg">
                        <h3 class="font-semibold text-gray-800 dark:text-white mb-2">Cross-Platform</h3>
                        <ul class="list-disc list-inside text-gray-600 dark:text-gray-300 space-y-1">
                            <li>React Native</li>
                            <li>Flutter</li>
                            <li>Ionic</li>
                            <li>Xamarin</li>
                            <li>Progressive Web Apps</li>
                        </ul>
                    </div>
                    <div class="bg-gray-50 dark:bg-gray-700 p-4 rounded-lg">
                        <h3 class="font-semibold text-gray-800 dark:text-white mb-2">Backend & APIs</h3>
                        <ul class="list-disc list-inside text-gray-600 dark:text-gray-300 space-y-1">
                            <li>Node.js</li>
                            <li>Firebase</li>
                            <li>GraphQL</li>
                            <li>REST APIs</li>
                            <li>AWS Amplify</li>
                        </ul>
                    </div>
                    <div class="bg-gray-50 dark:bg-gray-700 p-4 rounded-lg">
                        <h3 class="font-semibold text-gray-800 dark:text-white mb-2">App Features</h3>
                        <ul class="list-disc list-inside text-gray-600 dark:text-gray-300 space-y-1">
                            <li>Geolocation</li>
                            <li>Push Notifications</li>
                            <li>In-App Purchases</li>
                            <li>Biometric Authentication</li>
                            <li>Offline Storage</li>
                        </ul>
                    </div>
                    <div class="bg-gray-50 dark:bg-gray-700 p-4 rounded-lg">
                        <h3 class="font-semibold text-gray-800 dark:text-white mb-2">DevOps & Testing</h3>
                        <ul class="list-disc list-inside text-gray-600 dark:text-gray-300 space-y-1">
                            <li>CI/CD Pipelines</li>
                            <li>Automated Testing</li>
                            <li>App Store Optimization</li>
                            <li>Beta Testing</li>
                            <li>Analytics Integration</li>
                        </ul>
                    </div>
                </div>
            </div>

            <!-- Development Process Section -->
            <div id="process" data-section="process" class="bg-white dark:bg-gray-800 rounded-xl shadow p-8">
                <h2 class="text-2xl font-bold mb-6 text-gray-800 dark:text-white">Development Process</h2>
                <div class="space-y-6">
                    <div class="flex items-start">
                        <div class="flex-shrink-0 bg-green-500 text-white rounded-full w-10 h-10 flex items-center justify-center font-bold text-lg">1</div>
                        <div class="ml-4">
                            <h3 class="text-xl font-semibold text-gray-800 dark:text-white">Discovery & Planning</h3>
                            <p class="text-gray-600 dark:text-gray-300 mt-2">We begin by understanding your business goals, target audience, and specific requirements to develop a comprehensive mobile app strategy.</p>
                        </div>
                    </div>
                    <div class="flex items-start">
                        <div class="flex-shrink-0 bg-green-500 text-white rounded-full w-10 h-10 flex items-center justify-center font-bold text-lg">2</div>
                        <div class="ml-4">
                            <h3 class="text-xl font-semibold text-gray-800 dark:text-white">UX/UI Design</h3>
                            <p class="text-gray-600 dark:text-gray-300 mt-2">Our designers create wireframes and visual designs that align with platform guidelines while providing an intuitive and engaging user experience.</p>
                        </div>
                    </div>
                    <div class="flex items-start">
                        <div class="flex-shrink-0 bg-green-500 text-white rounded-full w-10 h-10 flex items-center justify-center font-bold text-lg">3</div>
                        <div class="ml-4">
                            <h3 class="text-xl font-semibold text-gray-800 dark:text-white">Architecture Planning</h3>
                            <p class="text-gray-600 dark:text-gray-300 mt-2">We design the technical architecture, selecting the appropriate technologies and frameworks based on your requirements and long-term goals.</p>
                        </div>
                    </div>
                    <div class="flex items-start">
                        <div class="flex-shrink-0 bg-green-500 text-white rounded-full w-10 h-10 flex items-center justify-center font-bold text-lg">4</div>
                        <div class="ml-4">
                            <h3 class="text-xl font-semibold text-gray-800 dark:text-white">Development</h3>
                            <p class="text-gray-600 dark:text-gray-300 mt-2">Our development team builds your mobile application using agile methodologies, with regular sprints and client feedback throughout the process.</p>
                        </div>
                    </div>
                    <div class="flex items-start">
                        <div class="flex-shrink-0 bg-green-500 text-white rounded-full w-10 h-10 flex items-center justify-center font-bold text-lg">5</div>
                        <div class="ml-4">
                            <h3 class="text-xl font-semibold text-gray-800 dark:text-white">Quality Assurance</h3>
                            <p class="text-gray-600 dark:text-gray-300 mt-2">We conduct thorough testing across devices, operating systems, and network conditions to ensure your app functions flawlessly in all scenarios.</p>
                        </div>
                    </div>
                    <div class="flex items-start">
                        <div class="flex-shrink-0 bg-green-500 text-white rounded-full w-10 h-10 flex items-center justify-center font-bold text-lg">6</div>
                        <div class="ml-4">
                            <h3 class="text-xl font-semibold text-gray-800 dark:text-white">Deployment</h3>
                            <p class="text-gray-600 dark:text-gray-300 mt-2">We handle the submission process to app stores, ensuring compliance with guidelines and optimizing for discoverability and downloads.</p>
                        </div>
                    </div>
                    <div class="flex items-start">
                        <div class="flex-shrink-0 bg-green-500 text-white rounded-full w-10 h-10 flex items-center justify-center font-bold text-lg">7</div>
                        <div class="ml-4">
                            <h3 class="text-xl font-semibold text-gray-800 dark:text-white">Post-Launch Support</h3>
                            <p class="text-gray-600 dark:text-gray-300 mt-2">We provide ongoing maintenance, updates, and optimization based on user feedback and analytics to ensure your app remains competitive and effective.</p>
                        </div>
                    </div>
                </div>
            </div>

            <!-- Benefits Section -->
            <div id="benefits" data-section="benefits" class="bg-white dark:bg-gray-800 rounded-xl shadow p-8">
                <h2 class="text-2xl font-bold mb-6 text-gray-800 dark:text-white">Benefits</h2>
                <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
                    <div class="flex">
                        <div class="flex-shrink-0 text-green-500 dark:text-green-400">
                            <svg class="w-6 h-6" fill="currentColor" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg">
                                <path fill-rule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z" clip-rule="evenodd"></path>
                            </svg>
                        </div>
                        <div class="ml-4">
                            <h3 class="text-lg font-semibold text-gray-800 dark:text-white">Enhanced Customer Engagement</h3>
                            <p class="text-gray-600 dark:text-gray-300 mt-1">Mobile apps provide direct access to your customers, allowing for personalized experiences and increased engagement.</p>
                        </div>
                    </div>
                    <div class="flex">
                        <div class="flex-shrink-0 text-green-500 dark:text-green-400">
                            <svg class="w-6 h-6" fill="currentColor" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg">
                                <path fill-rule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z" clip-rule="evenodd"></path>
                            </svg>
                        </div>
                        <div class="ml-4">
                            <h3 class="text-lg font-semibold text-gray-800 dark:text-white">Brand Reinforcement</h3>
                            <p class="text-gray-600 dark:text-gray-300 mt-1">A well-designed mobile app strengthens your brand identity and creates a consistent experience across all customer touchpoints.</p>
                        </div>
                    </div>
                    <div class="flex">
                        <div class="flex-shrink-0 text-green-500 dark:text-green-400">
                            <svg class="w-6 h-6" fill="currentColor" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg">
                                <path fill-rule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z" clip-rule="evenodd"></path>
                            </svg>
                        </div>
                        <div class="ml-4">
                            <h3 class="text-lg font-semibold text-gray-800 dark:text-white">Increased Revenue</h3>
                            <p class="text-gray-600 dark:text-gray-300 mt-1">Mobile apps can create new revenue streams through in-app purchases, subscriptions, or by driving sales through improved customer experience.</p>
                        </div>
                    </div>
                    <div class="flex">
                        <div class="flex-shrink-0 text-green-500 dark:text-green-400">
                            <svg class="w-6 h-6" fill="currentColor" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg">
                                <path fill-rule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z" clip-rule="evenodd"></path>
                            </svg>
                        </div>
                        <div class="ml-4">
                            <h3 class="text-lg font-semibold text-gray-800 dark:text-white">Valuable Customer Insights</h3>
                            <p class="text-gray-600 dark:text-gray-300 mt-1">Mobile apps provide rich data on user behavior and preferences, enabling data-driven business decisions and personalized marketing.</p>
                        </div>
                    </div>
                    <div class="flex">
                        <div class="flex-shrink-0 text-green-500 dark:text-green-400">
                            <svg class="w-6 h-6" fill="currentColor" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg">
                                <path fill-rule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z" clip-rule="evenodd"></path>
                            </svg>
                        </div>
                        <div class="ml-4">
                            <h3 class="text-lg font-semibold text-gray-800 dark:text-white">Competitive Advantage</h3>
                            <p class="text-gray-600 dark:text-gray-300 mt-1">A high-quality mobile app can differentiate your business from competitors and position you as an industry leader.</p>
                        </div>
                    </div>
                    <div class="flex">
                        <div class="flex-shrink-0 text-green-500 dark:text-green-400">
                            <svg class="w-6 h-6" fill="currentColor" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg">
                                <path fill-rule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z" clip-rule="evenodd"></path>
                            </svg>
                        </div>
                        <div class="ml-4">
                            <h3 class="text-lg font-semibold text-gray-800 dark:text-white">Offline Accessibility</h3>
                            <p class="text-gray-600 dark:text-gray-300 mt-1">Mobile apps can function without internet connectivity, providing uninterrupted service to users regardless of their connection status.</p>
                        </div>
                    </div>
                </div>
            </div>

            <!-- Call to Action -->
            <div class="mt-16 text-center">
                <Link :href="route('web-development.ecommerce') + '#contact'" 
                   class="inline-flex items-center px-8 mb-16 py-4 border border-transparent text-lg font-medium rounded-xl text-white bg-green-600 hover:bg-green-700 transition-all duration-300 transform hover:scale-105 hover:shadow-lg">
                    Discuss Your Mobile App Project
                    <svg class="ml-3 -mr-1 w-6 h-6" fill="currentColor" viewBox="0 0 20 20">
                        <path fill-rule="evenodd" d="M10.293 3.293a1 1 0 011.414 0l6 6a1 1 0 010 1.414l-6 6a1 1 0 01-1.414-1.414L14.586 11H3a1 1 0 110-2h11.586l-4.293-4.293a1 1 0 010-1.414z" clip-rule="evenodd" />
                    </svg>
                </Link>
            </div>
        </div>
    </WebDevelopmentLayout>
</template>
