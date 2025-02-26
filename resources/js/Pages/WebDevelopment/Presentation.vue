<script setup>
import { Link } from '@inertiajs/vue3';
import WebDevelopmentLayout from './WebDevelopmentLayout.vue';

const serviceData = {
    title: 'Presentation Website Development',
    description: 'Professional, engaging websites that showcase your brand, products, and services with impact.',
    focus: 'Creating visually stunning, user-friendly websites that effectively communicate your brand message and drive conversions.',
    keyPoint: 'Stand out from the competition with a custom-designed website that reflects your unique brand identity and engages your target audience.',
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
            <div class="bg-gradient-to-r from-indigo-600 to-purple-700 rounded-xl shadow-xl p-8 text-white">
                <h1 class="text-3xl font-bold mb-4">{{ serviceData.title }}</h1>
                <p class="text-xl text-indigo-100 mb-6">{{ serviceData.description }}</p>
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
                    Our presentation website development services focus on creating compelling online presences that effectively showcase your business, products, and services. We design and develop websites that not only look great but also deliver results by engaging visitors and converting them into customers.
                </p>
                <p class="text-gray-600 dark:text-gray-300">
                    Whether you need a simple brochure site or a complex corporate website with multiple sections and features, our team delivers custom solutions tailored to your specific business goals and target audience.
                </p>
            </div>

            <!-- Key Features Section -->
            <div id="features" data-section="features" class="bg-white dark:bg-gray-800 rounded-xl shadow p-8">
                <h2 class="text-2xl font-bold mb-6 text-gray-800 dark:text-white">Key Features</h2>
                <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
                    <div class="border border-gray-200 dark:border-gray-700 rounded-lg p-6 hover:shadow-md transition-shadow">
                        <h3 class="text-xl font-semibold mb-3 text-gray-800 dark:text-white">Custom Design</h3>
                        <p class="text-gray-600 dark:text-gray-300">Unique, brand-aligned designs that stand out from template-based websites and reflect your company's identity.</p>
                    </div>
                    <div class="border border-gray-200 dark:border-gray-700 rounded-lg p-6 hover:shadow-md transition-shadow">
                        <h3 class="text-xl font-semibold mb-3 text-gray-800 dark:text-white">Responsive Layout</h3>
                        <p class="text-gray-600 dark:text-gray-300">Mobile-optimized websites that provide an excellent user experience across all devices and screen sizes.</p>
                    </div>
                    <div class="border border-gray-200 dark:border-gray-700 rounded-lg p-6 hover:shadow-md transition-shadow">
                        <h3 class="text-xl font-semibold mb-3 text-gray-800 dark:text-white">SEO Optimization</h3>
                        <p class="text-gray-600 dark:text-gray-300">Built-in search engine optimization to improve visibility and drive organic traffic to your website.</p>
                    </div>
                    <div class="border border-gray-200 dark:border-gray-700 rounded-lg p-6 hover:shadow-md transition-shadow">
                        <h3 class="text-xl font-semibold mb-3 text-gray-800 dark:text-white">Fast Loading Speed</h3>
                        <p class="text-gray-600 dark:text-gray-300">Performance-optimized code and assets to ensure quick page loading times and better user experience.</p>
                    </div>
                    <div class="border border-gray-200 dark:border-gray-700 rounded-lg p-6 hover:shadow-md transition-shadow">
                        <h3 class="text-xl font-semibold mb-3 text-gray-800 dark:text-white">Content Management</h3>
                        <p class="text-gray-600 dark:text-gray-300">User-friendly CMS integration allowing you to easily update content without technical knowledge.</p>
                    </div>
                    <div class="border border-gray-200 dark:border-gray-700 rounded-lg p-6 hover:shadow-md transition-shadow">
                        <h3 class="text-xl font-semibold mb-3 text-gray-800 dark:text-white">Contact & Lead Generation</h3>
                        <p class="text-gray-600 dark:text-gray-300">Integrated contact forms, call-to-action elements, and lead capture mechanisms to convert visitors into leads.</p>
                    </div>
                </div>
            </div>

            <!-- Technologies Section -->
            <div id="technologies" data-section="technologies" class="bg-white dark:bg-gray-800 rounded-xl shadow p-8">
                <h2 class="text-2xl font-bold mb-6 text-gray-800 dark:text-white">Technologies</h2>
                <p class="text-gray-600 dark:text-gray-300 mb-6">
                    We use modern technologies and frameworks to build fast, secure, and maintainable websites:
                </p>
                <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-4">
                    <div class="bg-gray-50 dark:bg-gray-700 p-4 rounded-lg">
                        <h3 class="font-semibold text-gray-800 dark:text-white mb-2">Frontend</h3>
                        <ul class="list-disc list-inside text-gray-600 dark:text-gray-300 space-y-1">
                            <li>HTML5/CSS3</li>
                            <li>JavaScript/TypeScript</li>
                            <li>React.js</li>
                            <li>Vue.js</li>
                            <li>Next.js</li>
                        </ul>
                    </div>
                    <div class="bg-gray-50 dark:bg-gray-700 p-4 rounded-lg">
                        <h3 class="font-semibold text-gray-800 dark:text-white mb-2">CSS Frameworks</h3>
                        <ul class="list-disc list-inside text-gray-600 dark:text-gray-300 space-y-1">
                            <li>Tailwind CSS</li>
                            <li>Bootstrap</li>
                            <li>SASS/SCSS</li>
                            <li>CSS Modules</li>
                            <li>Styled Components</li>
                        </ul>
                    </div>
                    <div class="bg-gray-50 dark:bg-gray-700 p-4 rounded-lg">
                        <h3 class="font-semibold text-gray-800 dark:text-white mb-2">Backend & CMS</h3>
                        <ul class="list-disc list-inside text-gray-600 dark:text-gray-300 space-y-1">
                            <li>WordPress</li>
                            <li>Laravel</li>
                            <li>Node.js</li>
                            <li>Headless CMS (Strapi, Contentful)</li>
                            <li>Static Site Generators</li>
                        </ul>
                    </div>
                    <div class="bg-gray-50 dark:bg-gray-700 p-4 rounded-lg">
                        <h3 class="font-semibold text-gray-800 dark:text-white mb-2">Performance</h3>
                        <ul class="list-disc list-inside text-gray-600 dark:text-gray-300 space-y-1">
                            <li>Lazy Loading</li>
                            <li>Code Splitting</li>
                            <li>Image Optimization</li>
                            <li>Caching Strategies</li>
                            <li>CDN Integration</li>
                        </ul>
                    </div>
                    <div class="bg-gray-50 dark:bg-gray-700 p-4 rounded-lg">
                        <h3 class="font-semibold text-gray-800 dark:text-white mb-2">Analytics & Marketing</h3>
                        <ul class="list-disc list-inside text-gray-600 dark:text-gray-300 space-y-1">
                            <li>Google Analytics</li>
                            <li>Google Tag Manager</li>
                            <li>Facebook Pixel</li>
                            <li>Mailchimp Integration</li>
                            <li>HubSpot Integration</li>
                        </ul>
                    </div>
                    <div class="bg-gray-50 dark:bg-gray-700 p-4 rounded-lg">
                        <h3 class="font-semibold text-gray-800 dark:text-white mb-2">Hosting & Infrastructure</h3>
                        <ul class="list-disc list-inside text-gray-600 dark:text-gray-300 space-y-1">
                            <li>AWS</li>
                            <li>Netlify</li>
                            <li>Vercel</li>
                            <li>Digital Ocean</li>
                            <li>Cloudflare</li>
                        </ul>
                    </div>
                </div>
            </div>

            <!-- Development Process Section -->
            <div id="process" data-section="process" class="bg-white dark:bg-gray-800 rounded-xl shadow p-8">
                <h2 class="text-2xl font-bold mb-6 text-gray-800 dark:text-white">Development Process</h2>
                <div class="space-y-6">
                    <div class="flex items-start">
                        <div class="flex-shrink-0 bg-indigo-600 text-white rounded-full w-10 h-10 flex items-center justify-center font-bold text-lg">1</div>
                        <div class="ml-4">
                            <h3 class="text-xl font-semibold text-gray-800 dark:text-white">Discovery & Strategy</h3>
                            <p class="text-gray-600 dark:text-gray-300 mt-2">We begin by understanding your business, target audience, goals, and requirements to develop a comprehensive website strategy.</p>
                        </div>
                    </div>
                    <div class="flex items-start">
                        <div class="flex-shrink-0 bg-indigo-600 text-white rounded-full w-10 h-10 flex items-center justify-center font-bold text-lg">2</div>
                        <div class="ml-4">
                            <h3 class="text-xl font-semibold text-gray-800 dark:text-white">Wireframing & Design</h3>
                            <p class="text-gray-600 dark:text-gray-300 mt-2">Our designers create wireframes and visual designs that align with your brand identity and provide an optimal user experience.</p>
                        </div>
                    </div>
                    <div class="flex items-start">
                        <div class="flex-shrink-0 bg-indigo-600 text-white rounded-full w-10 h-10 flex items-center justify-center font-bold text-lg">3</div>
                        <div class="ml-4">
                            <h3 class="text-xl font-semibold text-gray-800 dark:text-white">Content Planning</h3>
                            <p class="text-gray-600 dark:text-gray-300 mt-2">We help you plan and organize your content to effectively communicate your message and drive user engagement.</p>
                        </div>
                    </div>
                    <div class="flex items-start">
                        <div class="flex-shrink-0 bg-indigo-600 text-white rounded-full w-10 h-10 flex items-center justify-center font-bold text-lg">4</div>
                        <div class="ml-4">
                            <h3 class="text-xl font-semibold text-gray-800 dark:text-white">Development</h3>
                            <p class="text-gray-600 dark:text-gray-300 mt-2">Our development team builds your website using modern technologies, ensuring it's responsive, fast, and SEO-friendly.</p>
                        </div>
                    </div>
                    <div class="flex items-start">
                        <div class="flex-shrink-0 bg-indigo-600 text-white rounded-full w-10 h-10 flex items-center justify-center font-bold text-lg">5</div>
                        <div class="ml-4">
                            <h3 class="text-xl font-semibold text-gray-800 dark:text-white">Testing & Quality Assurance</h3>
                            <p class="text-gray-600 dark:text-gray-300 mt-2">We thoroughly test your website across devices and browsers to ensure it functions flawlessly and provides a consistent experience.</p>
                        </div>
                    </div>
                    <div class="flex items-start">
                        <div class="flex-shrink-0 bg-indigo-600 text-white rounded-full w-10 h-10 flex items-center justify-center font-bold text-lg">6</div>
                        <div class="ml-4">
                            <h3 class="text-xl font-semibold text-gray-800 dark:text-white">Launch & Training</h3>
                            <p class="text-gray-600 dark:text-gray-300 mt-2">We deploy your website and provide training on how to manage and update content through the CMS.</p>
                        </div>
                    </div>
                    <div class="flex items-start">
                        <div class="flex-shrink-0 bg-indigo-600 text-white rounded-full w-10 h-10 flex items-center justify-center font-bold text-lg">7</div>
                        <div class="ml-4">
                            <h3 class="text-xl font-semibold text-gray-800 dark:text-white">Ongoing Support & Optimization</h3>
                            <p class="text-gray-600 dark:text-gray-300 mt-2">We provide continued support, maintenance, and data-driven optimization to ensure your website remains effective and up-to-date.</p>
                        </div>
                    </div>
                </div>
            </div>

            <!-- Benefits Section -->
            <div id="benefits" data-section="benefits" class="bg-white dark:bg-gray-800 rounded-xl shadow p-8">
                <h2 class="text-2xl font-bold mb-6 text-gray-800 dark:text-white">Benefits</h2>
                <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
                    <div class="flex">
                        <div class="flex-shrink-0 text-indigo-600 dark:text-indigo-400">
                            <svg class="w-6 h-6" fill="currentColor" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg">
                                <path fill-rule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z" clip-rule="evenodd"></path>
                            </svg>
                        </div>
                        <div class="ml-4">
                            <h3 class="text-lg font-semibold text-gray-800 dark:text-white">Professional Brand Image</h3>
                            <p class="text-gray-600 dark:text-gray-300 mt-1">A well-designed website enhances your credibility and establishes trust with potential customers.</p>
                        </div>
                    </div>
                    <div class="flex">
                        <div class="flex-shrink-0 text-indigo-600 dark:text-indigo-400">
                            <svg class="w-6 h-6" fill="currentColor" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg">
                                <path fill-rule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z" clip-rule="evenodd"></path>
                            </svg>
                        </div>
                        <div class="ml-4">
                            <h3 class="text-lg font-semibold text-gray-800 dark:text-white">Increased Visibility</h3>
                            <p class="text-gray-600 dark:text-gray-300 mt-1">SEO-optimized websites rank higher in search results, driving more organic traffic to your business.</p>
                        </div>
                    </div>
                    <div class="flex">
                        <div class="flex-shrink-0 text-indigo-600 dark:text-indigo-400">
                            <svg class="w-6 h-6" fill="currentColor" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg">
                                <path fill-rule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z" clip-rule="evenodd"></path>
                            </svg>
                        </div>
                        <div class="ml-4">
                            <h3 class="text-lg font-semibold text-gray-800 dark:text-white">Better User Experience</h3>
                            <p class="text-gray-600 dark:text-gray-300 mt-1">Intuitive navigation and responsive design create a positive experience that keeps visitors engaged.</p>
                        </div>
                    </div>
                    <div class="flex">
                        <div class="flex-shrink-0 text-indigo-600 dark:text-indigo-400">
                            <svg class="w-6 h-6" fill="currentColor" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg">
                                <path fill-rule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z" clip-rule="evenodd"></path>
                            </svg>
                        </div>
                        <div class="ml-4">
                            <h3 class="text-lg font-semibold text-gray-800 dark:text-white">Lead Generation</h3>
                            <p class="text-gray-600 dark:text-gray-300 mt-1">Strategic calls-to-action and contact forms convert website visitors into potential customers and sales.</p>
                        </div>
                    </div>
                    <div class="flex">
                        <div class="flex-shrink-0 text-indigo-600 dark:text-indigo-400">
                            <svg class="w-6 h-6" fill="currentColor" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg">
                                <path fill-rule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z" clip-rule="evenodd"></path>
                            </svg>
                        </div>
                        <div class="ml-4">
                            <h3 class="text-lg font-semibold text-gray-800 dark:text-white">24/7 Availability</h3>
                            <p class="text-gray-600 dark:text-gray-300 mt-1">Your website works around the clock, providing information and generating leads even outside business hours.</p>
                        </div>
                    </div>
                    <div class="flex">
                        <div class="flex-shrink-0 text-indigo-600 dark:text-indigo-400">
                            <svg class="w-6 h-6" fill="currentColor" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg">
                                <path fill-rule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z" clip-rule="evenodd"></path>
                            </svg>
                        </div>
                        <div class="ml-4">
                            <h3 class="text-lg font-semibold text-gray-800 dark:text-white">Measurable Results</h3>
                            <p class="text-gray-600 dark:text-gray-300 mt-1">Analytics integration provides valuable insights into visitor behavior, allowing for data-driven improvements.</p>
                        </div>
                    </div>
                </div>
            </div>

            <!-- Call to Action -->
            <div class="mt-16 text-center">
                <Link href="/#contact" 
                   class="inline-flex items-center px-8 py-4 border border-transparent text-lg font-medium rounded-xl text-white bg-indigo-600 hover:bg-indigo-700 transition-all duration-300 transform hover:scale-105 hover:shadow-lg">
                    Discuss Your Website Project
                    <svg class="ml-3 -mr-1 w-6 h-6" fill="currentColor" viewBox="0 0 20 20">
                        <path fill-rule="evenodd" d="M10.293 3.293a1 1 0 011.414 0l6 6a1 1 0 010 1.414l-6 6a1 1 0 01-1.414-1.414L14.586 11H3a1 1 0 110-2h11.586l-4.293-4.293a1 1 0 010-1.414z" clip-rule="evenodd" />
                    </svg>
                </Link>
            </div>
        </div>
    </WebDevelopmentLayout>
</template>
