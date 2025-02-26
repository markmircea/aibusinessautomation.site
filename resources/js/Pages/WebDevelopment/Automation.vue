<script setup>
import { Link } from '@inertiajs/vue3';
import WebDevelopmentLayout from './WebDevelopmentLayout.vue';

const serviceData = {
    title: 'Web Scraping & Automation',
    description: 'Custom web scraping solutions and automation tools that streamline processes and extract valuable data.',
    focus: 'Building efficient, reliable systems that automate repetitive tasks and gather actionable insights from web data.',
    keyPoint: 'Save time, reduce errors, and gain competitive intelligence with tailored web scraping and automation solutions.',
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
            <div class="bg-gradient-to-r from-purple-600 to-pink-600 rounded-xl shadow-xl p-8 text-white">
                <h1 class="text-3xl font-bold mb-4">{{ serviceData.title }}</h1>
                <p class="text-xl text-purple-100 mb-6">{{ serviceData.description }}</p>
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
                    Our web scraping and automation services provide powerful solutions for businesses looking to extract valuable data from websites and automate repetitive tasks. We develop custom tools that can gather, process, and analyze information from various online sources, helping you make data-driven decisions and streamline operations.
                </p>
                <p class="text-gray-600 dark:text-gray-300">
                    Whether you need competitive intelligence, price monitoring, content aggregation, or workflow automation, our team delivers reliable, scalable solutions that comply with legal and ethical standards while providing the data and efficiency you need.
                </p>
            </div>

            <!-- Key Features Section -->
            <div id="features" data-section="features" class="bg-white dark:bg-gray-800 rounded-xl shadow p-8">
                <h2 class="text-2xl font-bold mb-6 text-gray-800 dark:text-white">Key Features</h2>
                <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
                    <div class="border border-gray-200 dark:border-gray-700 rounded-lg p-6 hover:shadow-md transition-shadow">
                        <h3 class="text-xl font-semibold mb-3 text-gray-800 dark:text-white">Custom Data Extraction</h3>
                        <p class="text-gray-600 dark:text-gray-300">Tailored scraping solutions that target specific websites and extract exactly the data you need in your preferred format.</p>
                    </div>
                    <div class="border border-gray-200 dark:border-gray-700 rounded-lg p-6 hover:shadow-md transition-shadow">
                        <h3 class="text-xl font-semibold mb-3 text-gray-800 dark:text-white">Scheduled Automation</h3>
                        <p class="text-gray-600 dark:text-gray-300">Automated processes that run on your preferred schedule, ensuring you always have the most up-to-date information.</p>
                    </div>
                    <div class="border border-gray-200 dark:border-gray-700 rounded-lg p-6 hover:shadow-md transition-shadow">
                        <h3 class="text-xl font-semibold mb-3 text-gray-800 dark:text-white">Data Processing & Analysis</h3>
                        <p class="text-gray-600 dark:text-gray-300">Advanced data cleaning, transformation, and analysis capabilities to convert raw data into actionable insights.</p>
                    </div>
                    <div class="border border-gray-200 dark:border-gray-700 rounded-lg p-6 hover:shadow-md transition-shadow">
                        <h3 class="text-xl font-semibold mb-3 text-gray-800 dark:text-white">API Integration</h3>
                        <p class="text-gray-600 dark:text-gray-300">Seamless connection with your existing systems and third-party services to enhance functionality and data flow.</p>
                    </div>
                    <div class="border border-gray-200 dark:border-gray-700 rounded-lg p-6 hover:shadow-md transition-shadow">
                        <h3 class="text-xl font-semibold mb-3 text-gray-800 dark:text-white">Monitoring & Alerts</h3>
                        <p class="text-gray-600 dark:text-gray-300">Real-time monitoring of data changes with customizable alerts for important updates or threshold breaches.</p>
                    </div>
                    <div class="border border-gray-200 dark:border-gray-700 rounded-lg p-6 hover:shadow-md transition-shadow">
                        <h3 class="text-xl font-semibold mb-3 text-gray-800 dark:text-white">Scalable Infrastructure</h3>
                        <p class="text-gray-600 dark:text-gray-300">Cloud-based solutions that can scale with your needs, handling everything from small data sets to large-scale operations.</p>
                    </div>
                </div>
            </div>

            <!-- Technologies Section -->
            <div id="technologies" data-section="technologies" class="bg-white dark:bg-gray-800 rounded-xl shadow p-8">
                <h2 class="text-2xl font-bold mb-6 text-gray-800 dark:text-white">Technologies</h2>
                <p class="text-gray-600 dark:text-gray-300 mb-6">
                    We leverage the latest technologies and frameworks to build powerful web scraping and automation solutions:
                </p>
                <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-4">
                    <div class="bg-gray-50 dark:bg-gray-700 p-4 rounded-lg">
                        <h3 class="font-semibold text-gray-800 dark:text-white mb-2">Scraping Technologies</h3>
                        <ul class="list-disc list-inside text-gray-600 dark:text-gray-300 space-y-1">
                            <li>Python (BeautifulSoup, Scrapy)</li>
                            <li>Puppeteer</li>
                            <li>Selenium</li>
                            <li>Cheerio</li>
                            <li>Playwright</li>
                        </ul>
                    </div>
                    <div class="bg-gray-50 dark:bg-gray-700 p-4 rounded-lg">
                        <h3 class="font-semibold text-gray-800 dark:text-white mb-2">Automation Tools</h3>
                        <ul class="list-disc list-inside text-gray-600 dark:text-gray-300 space-y-1">
                            <li>Node.js</li>
                            <li>Python</li>
                            <li>Zapier</li>
                            <li>Make (Integromat)</li>
                            <li>Power Automate</li>
                        </ul>
                    </div>
                    <div class="bg-gray-50 dark:bg-gray-700 p-4 rounded-lg">
                        <h3 class="font-semibold text-gray-800 dark:text-white mb-2">Data Processing</h3>
                        <ul class="list-disc list-inside text-gray-600 dark:text-gray-300 space-y-1">
                            <li>Pandas</li>
                            <li>NumPy</li>
                            <li>SQL</li>
                            <li>MongoDB</li>
                            <li>Elasticsearch</li>
                        </ul>
                    </div>
                    <div class="bg-gray-50 dark:bg-gray-700 p-4 rounded-lg">
                        <h3 class="font-semibold text-gray-800 dark:text-white mb-2">APIs & Integration</h3>
                        <ul class="list-disc list-inside text-gray-600 dark:text-gray-300 space-y-1">
                            <li>RESTful APIs</li>
                            <li>GraphQL</li>
                            <li>Webhooks</li>
                            <li>OAuth</li>
                            <li>JSON/XML Processing</li>
                        </ul>
                    </div>
                    <div class="bg-gray-50 dark:bg-gray-700 p-4 rounded-lg">
                        <h3 class="font-semibold text-gray-800 dark:text-white mb-2">Infrastructure</h3>
                        <ul class="list-disc list-inside text-gray-600 dark:text-gray-300 space-y-1">
                            <li>AWS</li>
                            <li>Google Cloud</li>
                            <li>Docker</li>
                            <li>Kubernetes</li>
                            <li>Serverless Functions</li>
                        </ul>
                    </div>
                    <div class="bg-gray-50 dark:bg-gray-700 p-4 rounded-lg">
                        <h3 class="font-semibold text-gray-800 dark:text-white mb-2">Monitoring & Scheduling</h3>
                        <ul class="list-disc list-inside text-gray-600 dark:text-gray-300 space-y-1">
                            <li>Cron Jobs</li>
                            <li>Airflow</li>
                            <li>Prometheus</li>
                            <li>Grafana</li>
                            <li>Sentry</li>
                        </ul>
                    </div>
                </div>
            </div>

            <!-- Development Process Section -->
            <div id="process" data-section="process" class="bg-white dark:bg-gray-800 rounded-xl shadow p-8">
                <h2 class="text-2xl font-bold mb-6 text-gray-800 dark:text-white">Development Process</h2>
                <div class="space-y-6">
                    <div class="flex items-start">
                        <div class="flex-shrink-0 bg-purple-600 text-white rounded-full w-10 h-10 flex items-center justify-center font-bold text-lg">1</div>
                        <div class="ml-4">
                            <h3 class="text-xl font-semibold text-gray-800 dark:text-white">Requirements Analysis</h3>
                            <p class="text-gray-600 dark:text-gray-300 mt-2">We begin by understanding your data needs, target websites, and automation goals to develop a comprehensive strategy.</p>
                        </div>
                    </div>
                    <div class="flex items-start">
                        <div class="flex-shrink-0 bg-purple-600 text-white rounded-full w-10 h-10 flex items-center justify-center font-bold text-lg">2</div>
                        <div class="ml-4">
                            <h3 class="text-xl font-semibold text-gray-800 dark:text-white">Website Analysis</h3>
                            <p class="text-gray-600 dark:text-gray-300 mt-2">Our team analyzes the target websites' structure, data patterns, and anti-scraping measures to develop an effective extraction approach.</p>
                        </div>
                    </div>
                    <div class="flex items-start">
                        <div class="flex-shrink-0 bg-purple-600 text-white rounded-full w-10 h-10 flex items-center justify-center font-bold text-lg">3</div>
                        <div class="ml-4">
                            <h3 class="text-xl font-semibold text-gray-800 dark:text-white">Solution Design</h3>
                            <p class="text-gray-600 dark:text-gray-300 mt-2">We design a custom solution architecture, selecting the appropriate technologies and frameworks based on your specific requirements.</p>
                        </div>
                    </div>
                    <div class="flex items-start">
                        <div class="flex-shrink-0 bg-purple-600 text-white rounded-full w-10 h-10 flex items-center justify-center font-bold text-lg">4</div>
                        <div class="ml-4">
                            <h3 class="text-xl font-semibold text-gray-800 dark:text-white">Development</h3>
                            <p class="text-gray-600 dark:text-gray-300 mt-2">Our development team builds your scraping and automation solution, implementing data extraction, processing, and integration components.</p>
                        </div>
                    </div>
                    <div class="flex items-start">
                        <div class="flex-shrink-0 bg-purple-600 text-white rounded-full w-10 h-10 flex items-center justify-center font-bold text-lg">5</div>
                        <div class="ml-4">
                            <h3 class="text-xl font-semibold text-gray-800 dark:text-white">Testing & Optimization</h3>
                            <p class="text-gray-600 dark:text-gray-300 mt-2">We thoroughly test the solution for accuracy, reliability, and performance, optimizing for efficiency and resilience against website changes.</p>
                        </div>
                    </div>
                    <div class="flex items-start">
                        <div class="flex-shrink-0 bg-purple-600 text-white rounded-full w-10 h-10 flex items-center justify-center font-bold text-lg">6</div>
                        <div class="ml-4">
                            <h3 class="text-xl font-semibold text-gray-800 dark:text-white">Deployment</h3>
                            <p class="text-gray-600 dark:text-gray-300 mt-2">We deploy your solution to the appropriate infrastructure, setting up scheduling, monitoring, and alert systems as needed.</p>
                        </div>
                    </div>
                    <div class="flex items-start">
                        <div class="flex-shrink-0 bg-purple-600 text-white rounded-full w-10 h-10 flex items-center justify-center font-bold text-lg">7</div>
                        <div class="ml-4">
                            <h3 class="text-xl font-semibold text-gray-800 dark:text-white">Maintenance & Support</h3>
                            <p class="text-gray-600 dark:text-gray-300 mt-2">We provide ongoing maintenance and support to ensure your solution continues to function effectively as websites change and your needs evolve.</p>
                        </div>
                    </div>
                </div>
            </div>

            <!-- Benefits Section -->
            <div id="benefits" data-section="benefits" class="bg-white dark:bg-gray-800 rounded-xl shadow p-8">
                <h2 class="text-2xl font-bold mb-6 text-gray-800 dark:text-white">Benefits</h2>
                <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
                    <div class="flex">
                        <div class="flex-shrink-0 text-purple-600 dark:text-purple-400">
                            <svg class="w-6 h-6" fill="currentColor" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg">
                                <path fill-rule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z" clip-rule="evenodd"></path>
                            </svg>
                        </div>
                        <div class="ml-4">
                            <h3 class="text-lg font-semibold text-gray-800 dark:text-white">Time & Cost Savings</h3>
                            <p class="text-gray-600 dark:text-gray-300 mt-1">Automate manual data collection and repetitive tasks, freeing up your team to focus on higher-value activities.</p>
                        </div>
                    </div>
                    <div class="flex">
                        <div class="flex-shrink-0 text-purple-600 dark:text-purple-400">
                            <svg class="w-6 h-6" fill="currentColor" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg">
                                <path fill-rule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z" clip-rule="evenodd"></path>
                            </svg>
                        </div>
                        <div class="ml-4">
                            <h3 class="text-lg font-semibold text-gray-800 dark:text-white">Competitive Intelligence</h3>
                            <p class="text-gray-600 dark:text-gray-300 mt-1">Gain valuable insights into competitor pricing, products, and strategies to inform your business decisions.</p>
                        </div>
                    </div>
                    <div class="flex">
                        <div class="flex-shrink-0 text-purple-600 dark:text-purple-400">
                            <svg class="w-6 h-6" fill="currentColor" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg">
                                <path fill-rule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z" clip-rule="evenodd"></path>
                            </svg>
                        </div>
                        <div class="ml-4">
                            <h3 class="text-lg font-semibold text-gray-800 dark:text-white">Data Accuracy</h3>
                            <p class="text-gray-600 dark:text-gray-300 mt-1">Eliminate human error in data collection and processing, ensuring consistent, reliable information.</p>
                        </div>
                    </div>
                    <div class="flex">
                        <div class="flex-shrink-0 text-purple-600 dark:text-purple-400">
                            <svg class="w-6 h-6" fill="currentColor" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg">
                                <path fill-rule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z" clip-rule="evenodd"></path>
                            </svg>
                        </div>
                        <div class="ml-4">
                            <h3 class="text-lg font-semibold text-gray-800 dark:text-white">Scalability</h3>
                            <p class="text-gray-600 dark:text-gray-300 mt-1">Easily scale your data collection and automation processes as your business grows and needs evolve.</p>
                        </div>
                    </div>
                    <div class="flex">
                        <div class="flex-shrink-0 text-purple-600 dark:text-purple-400">
                            <svg class="w-6 h-6" fill="currentColor" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg">
                                <path fill-rule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z" clip-rule="evenodd"></path>
                            </svg>
                        </div>
                        <div class="ml-4">
                            <h3 class="text-lg font-semibold text-gray-800 dark:text-white">Real-time Insights</h3>
                            <p class="text-gray-600 dark:text-gray-300 mt-1">Access up-to-date information and receive alerts about important changes, enabling faster decision-making.</p>
                        </div>
                    </div>
                    <div class="flex">
                        <div class="flex-shrink-0 text-purple-600 dark:text-purple-400">
                            <svg class="w-6 h-6" fill="currentColor" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg">
                                <path fill-rule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z" clip-rule="evenodd"></path>
                            </svg>
                        </div>
                        <div class="ml-4">
                            <h3 class="text-lg font-semibold text-gray-800 dark:text-white">Process Optimization</h3>
                            <p class="text-gray-600 dark:text-gray-300 mt-1">Identify inefficiencies and bottlenecks in your workflows through automation and data analysis.</p>
                        </div>
                    </div>
                </div>
            </div>

            <!-- Call to Action -->
            <div class="mt-16 text-center">
                <Link :href="route('web-development.ecommerce') + '#contact'" 
                   class="inline-flex items-center px-8 mb-16 py-4 border border-transparent text-lg font-medium rounded-xl text-white bg-purple-600 hover:bg-purple-700 transition-all duration-300 transform hover:scale-105 hover:shadow-lg">
                    Discuss Your Automation Project
                    <svg class="ml-3 -mr-1 w-6 h-6" fill="currentColor" viewBox="0 0 20 20">
                        <path fill-rule="evenodd" d="M10.293 3.293a1 1 0 011.414 0l6 6a1 1 0 010 1.414l-6 6a1 1 0 01-1.414-1.414L14.586 11H3a1 1 0 110-2h11.586l-4.293-4.293a1 1 0 010-1.414z" clip-rule="evenodd" />
                    </svg>
                </Link>
            </div>
        </div>
    </WebDevelopmentLayout>
</template>
