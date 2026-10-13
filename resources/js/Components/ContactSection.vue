<script setup>
import { onMounted } from 'vue';
import { useForm } from '@inertiajs/vue3';

// `solution` pre-tags the enquiry with the page it came from (e.g. a specific
// Web Development service). The web-dev-specific copy of this component did the
// same but silently dropped referral_code capture, so it has been removed.
const props = defineProps({
    solution: { type: String, default: '' },
    heading: { type: String, default: 'Tell us about your project' },
});

const form = useForm({
    name: '',
    email: '',
    company: '',
    message: '',
    solution: props.solution,
    tech_stack: '',
    referral_code: ''
});

onMounted(() => {
    const refCode = new URLSearchParams(window.location.search).get('ref');

    if (refCode) {
        form.referral_code = refCode;
    }
});

const handleSubmit = () => {
    form.post(route('contact.submit'), {
        preserveScroll: true,
        preserveState: false,
        onSuccess: () => {
            form.reset();
        }
    });
};
</script>

<template>
    <section id="contact" class="py-20 bg-ink border-t border-line">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
            <div class="text-center mb-16">
                <h2 class="text-3xl sm:text-4xl font-bold tracking-tight text-content mb-4">
                    {{ heading }}
                </h2>
                <p class="max-w-3xl mx-auto text-lg text-content-muted mb-4">
                    Send us the shape of what you need — stack, scope and timeline — and we'll come back with a written quote and a proposed architecture. No obligation.
                </p>
                <div class="flex flex-wrap justify-center gap-5 text-sm text-content-subtle">
                    <div class="flex items-center">
                        <svg class="w-4 h-4 mr-2 text-positive" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7" />
                        </svg>
                        Free project scoping call
                    </div>
                    <div class="flex items-center">
                        <svg class="w-4 h-4 mr-2 text-positive" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7" />
                        </svg>
                        Dedicated Project Manager
                    </div>
                    <div class="flex items-center">
                        <svg class="w-4 h-4 mr-2 text-positive" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7" />
                        </svg>
                        Custom Solution Design
                    </div>
                </div>
            </div>

            <div class="max-w-3xl mx-auto bg-surface rounded-card shadow-e3 ring-1 ring-inset ring-line overflow-hidden">
                <div class="p-8">
                    <form @submit.prevent="handleSubmit" class="space-y-6">
                        <!-- Hidden field for referral code -->
                        <input type="hidden" v-model="form.referral_code">
                        <div class="grid grid-cols-1 gap-6 sm:grid-cols-2">
                            <div>
                                <label for="name" class="block text-sm font-medium text-content-muted">Name</label>
                                <input
                                    type="text"
                                    id="name"
                                    v-model="form.name"
                                    class="mt-1 block w-full rounded-control bg-ink border-line text-content placeholder:text-content-subtle shadow-sm focus:border-accent-500 focus:ring-accent-500 sm:text-sm"
                                >
                                <div v-if="form.errors.name" class="mt-1 text-sm text-danger">{{ form.errors.name }}</div>
                            </div>

                            <div>
                                <label for="email" class="block text-sm font-medium text-content-muted">Email <span class="text-danger">*</span></label>
                                <input
                                    type="email"
                                    id="email"
                                    v-model="form.email"
                                    class="mt-1 block w-full rounded-control bg-ink border-line text-content placeholder:text-content-subtle shadow-sm focus:border-accent-500 focus:ring-accent-500 sm:text-sm"
                                    required
                                >
                                <div v-if="form.errors.email" class="mt-1 text-sm text-danger">{{ form.errors.email }}</div>
                            </div>
                        </div>

                        <div>
                            <label for="company" class="block text-sm font-medium text-content-muted">Company</label>
                            <input
                                type="text"
                                id="company"
                                v-model="form.company"
                                class="mt-1 block w-full rounded-control bg-ink border-line text-content placeholder:text-content-subtle shadow-sm focus:border-accent-500 focus:ring-accent-500 sm:text-sm"
                            >
                            <div v-if="form.errors.company" class="mt-1 text-sm text-danger">{{ form.errors.company }}</div>
                        </div>

                        <div>
                            <label for="tech_stack" class="block text-sm font-medium text-content-muted">Current Tech Stack</label>
                            <p class="text-xs text-content-subtle mb-2">
                                List your current tools and systems that need integration (e.g., Salesforce, SAP, Microsoft 365)
                            </p>
                            <textarea
                                id="tech_stack"
                                v-model="form.tech_stack"
                                rows="2"
                                placeholder="E.g., Salesforce CRM, SAP ERP, Microsoft 365, Custom internal tools..."
                                class="mt-1 block w-full rounded-control bg-ink border-line text-content placeholder:text-content-subtle shadow-sm focus:border-accent-500 focus:ring-accent-500 sm:text-sm"
                            ></textarea>
                            <div v-if="form.errors.tech_stack" class="mt-1 text-sm text-danger">{{ form.errors.tech_stack }}</div>
                        </div>

                        <div>
                            <label for="message" class="block text-sm font-medium text-content-muted">Tell us about your needs <span class="text-danger">*</span></label>
                            <p class="text-xs text-content-subtle mb-2">
                                Share your current challenges, processes you'd like to automate, and any specific requirements. We'll create custom integrations to fit your needs.
                            </p>
                            <textarea
                                id="message"
                                v-model="form.message"
                                rows="4"
                                placeholder="E.g., We're looking to automate our invoice processing system and integrate it with our current ERP. We need custom workflows for approval processes..."
                                class="mt-1 block w-full rounded-control bg-ink border-line text-content placeholder:text-content-subtle shadow-sm focus:border-accent-500 focus:ring-accent-500 sm:text-sm"
                                required
                            ></textarea>
                            <div v-if="form.errors.message" class="mt-1 text-sm text-danger">{{ form.errors.message }}</div>
                        </div>

                        <div class="flex justify-center">
                            <button
                                type="submit"
                                class="inline-flex items-center px-8 py-4 text-base font-semibold rounded-control shadow-e2 text-white bg-accent-500 hover:bg-accent-600 disabled:opacity-60 disabled:cursor-not-allowed focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-accent-400 focus-visible:ring-offset-2 focus-visible:ring-offset-surface transition-colors duration-200 w-full sm:w-auto justify-center"
                                :disabled="form.processing"
                            >
                                <span v-if="form.processing">Sending...</span>
                                <span v-else>Get a Quote</span>
                                <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 ml-2" viewBox="0 0 20 20" fill="currentColor">
                                    <path fill-rule="evenodd" d="M10.293 3.293a1 1 0 011.414 0l6 6a1 1 0 010 1.414l-6 6a1 1 0 01-1.414-1.414L14.586 11H3a1 1 0 110-2h11.586l-4.293-4.293a1 1 0 010-1.414z" clip-rule="evenodd" />
                                </svg>
                            </button>
                        </div>
                    </form>
                </div>
            </div>

            <!-- Contact Information -->
            <div class="mt-16 grid grid-cols-1 gap-8 sm:grid-cols-3">
                <div class="text-center">
                    <div class="flex justify-center items-center mb-4">
                        <div class="p-3 rounded-full bg-accent-500/12 ring-1 ring-inset ring-accent-500/25">
                            <svg class="h-6 w-6 text-accent-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 5a2 2 0 012-2h3.28a1 1 0 01.948.684l1.498 4.493a1 1 0 01-.502 1.21l-2.257 1.13a11.042 11.042 0 005.516 5.516l1.13-2.257a1 1 0 011.21-.502l4.493 1.498a1 1 0 01.684.949V19a2 2 0 01-2 2h-1C9.716 21 3 14.284 3 6V5z" />
                            </svg>
                        </div>
                    </div>
                    <h3 class="text-lg font-semibold text-content">Phone (SMS)</h3>
                    <p class="mt-2 text-base text-content-muted">+1 (248) 387-9399</p>
                </div>

                <div class="text-center">
                    <div class="flex justify-center items-center mb-4">
                        <div class="p-3 rounded-full bg-accent-500/12 ring-1 ring-inset ring-accent-500/25">
                            <svg class="h-6 w-6 text-accent-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 8l7.89 5.26a2 2 0 002.22 0L21 8M5 19h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v10a2 2 0 002 2z" />
                            </svg>
                        </div>
                    </div>
                    <h3 class="text-lg font-semibold text-content">Email</h3>
                    <p class="mt-2 text-base text-content-muted">support@aibrainl.ink</p>
                </div>

                <div class="text-center">
                    <div class="flex justify-center items-center mb-4">
                        <div class="p-3 rounded-full bg-accent-500/12 ring-1 ring-inset ring-accent-500/25">
                            <svg class="h-6 w-6 text-accent-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17.657 16.657L13.414 20.9a1.998 1.998 0 01-2.827 0l-4.244-4.243a8 8 0 1111.314 0z" />
                                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 11a3 3 0 11-6 0 3 3 0 016 0z" />
                            </svg>
                        </div>
                    </div>
                    <h3 class="text-lg font-semibold text-content">Location</h3>
                    <p class="mt-2 text-base text-content-muted">Bucharest, RO</p>

                </div>
            </div>
        </div>
    </section>
</template>

<style scoped>
input, select, textarea {
    @apply placeholder:text-content-subtle;
}
</style>
