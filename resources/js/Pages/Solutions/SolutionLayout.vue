<script setup>
import { ref, onMounted, onUnmounted } from 'vue';
import AppLayout from '@/Layouts/AppLayout.vue';
import PageHero from '@/Components/PageHero.vue';
import ContactSection from '@/Components/ContactSection.vue';

// No <Head> here on purpose: DynamicSEO is the single source of truth for
// titles. This layout previously set its own, producing double-suffixed
// titles carrying the stale "AutomateAI" brand.
const props = defineProps({
    title: String,
    description: String,
    focus: String,
    keyPoint: String,
    eyebrow: { type: String, default: 'AI Solutions' },
    sections: {
        type: Array,
        default: () => []
    }
});

const activeSection = ref('');
const expandedSections = ref(new Set());

const updateActiveSection = () => {
    const els = document.querySelectorAll('[data-section]');
    const scrollPosition = window.scrollY + 120;

    for (const section of els) {
        if (section.offsetTop <= scrollPosition &&
            section.offsetTop + section.offsetHeight > scrollPosition) {
            const sectionId = section.getAttribute('data-section');
            activeSection.value = sectionId;
            if (sectionId.includes('-')) {
                expandedSections.value.add(sectionId.split('-')[0]);
            }
            break;
        }
    }
};

const scrollToSection = (sectionId) => {
    const el = document.querySelector(`[data-section="${sectionId}"]`);
    if (el) window.scrollTo({ top: el.offsetTop - 90, behavior: 'smooth' });
};

const toggleSection = (id) => {
    expandedSections.value.has(id) ? expandedSections.value.delete(id) : expandedSections.value.add(id);
};

const isSectionExpanded = (id) => expandedSections.value.has(id);

onMounted(() => {
    window.addEventListener('scroll', updateActiveSection, { passive: true });
    updateActiveSection();
});

onUnmounted(() => window.removeEventListener('scroll', updateActiveSection));
</script>

<template>
    <AppLayout>
        <div class="min-h-screen bg-ink">
            <PageHero
                :eyebrow="eyebrow"
                :title="title"
                :description="description"
                :primary-cta="{ label: 'Get a Quote', href: '#contact' }"
                :secondary-cta="{ label: 'See our work', href: '/portfolio' }"
            />

            <!-- Focus / key benefit, the two facts every solution page carries -->
            <section v-if="focus || keyPoint" class="py-16 bg-ink">
                <div class="max-w-5xl mx-auto px-4 sm:px-6 lg:px-8 grid gap-4 sm:grid-cols-2">
                    <div v-if="focus" class="p-6 rounded-card bg-surface ring-1 ring-inset ring-line">
                        <h2 class="text-xs font-semibold uppercase tracking-[0.12em] text-content-subtle mb-2">Focus</h2>
                        <p class="text-content-muted">{{ focus }}</p>
                    </div>
                    <div v-if="keyPoint" class="p-6 rounded-card bg-surface ring-1 ring-inset ring-line">
                        <h2 class="text-xs font-semibold uppercase tracking-[0.12em] text-content-subtle mb-2">Key benefit</h2>
                        <p class="text-accent-400 font-semibold">{{ keyPoint }}</p>
                    </div>
                </div>
            </section>

            <!-- Page body -->
            <section class="py-16 bg-surface/30 border-y border-line">
                <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
                    <div class="flex gap-10">
                        <!-- On-this-page nav, only for pages that declare sections -->
                        <div v-if="sections.length" class="hidden lg:block w-64 shrink-0 sticky self-start" style="top: 6rem;">
                            <nav class="rounded-card bg-surface ring-1 ring-inset ring-line p-4">
                                <h2 class="text-xs font-semibold uppercase tracking-[0.12em] text-content-subtle mb-3">On this page</h2>
                                <ul class="space-y-1">
                                    <li v-for="section in sections" :key="section.id" class="relative">
                                        <div class="flex items-center">
                                            <button v-if="section.subsections"
                                                    @click="toggleSection(section.id)"
                                                    :aria-label="`Toggle ${section.title} subsections`"
                                                    class="absolute left-0 top-2 w-4 h-4 flex items-center justify-center rounded-control focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-accent-400">
                                                <svg class="w-3 h-3 transition-transform duration-200"
                                                     :class="{ 'rotate-90': isSectionExpanded(section.id) }"
                                                     fill="none" stroke="currentColor" viewBox="0 0 24 24" aria-hidden="true">
                                                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7" />
                                                </svg>
                                            </button>
                                            <button
                                                @click="scrollToSection(section.id)"
                                                class="w-full text-left px-3 py-2 rounded-control text-sm transition-colors duration-200 focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-accent-400"
                                                :class="{
                                                    'pl-7': section.subsections,
                                                    'text-accent-400 bg-accent-500/12 font-medium': activeSection === section.id,
                                                    'text-content-muted hover:text-accent-400 hover:bg-surface-2': activeSection !== section.id
                                                }">
                                                {{ section.title }}
                                            </button>
                                        </div>

                                        <ul v-if="section.subsections && isSectionExpanded(section.id)"
                                            class="mt-1 ml-4 pl-3 border-l border-line space-y-1">
                                            <li v-for="subsection in section.subsections" :key="subsection.id">
                                                <button
                                                    @click="scrollToSection(subsection.id)"
                                                    class="w-full text-left px-3 py-1.5 rounded-control text-sm transition-colors duration-200 focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-accent-400"
                                                    :class="{
                                                        'text-accent-400 bg-accent-500/12 font-medium': activeSection === subsection.id,
                                                        'text-content-subtle hover:text-accent-400 hover:bg-surface-2': activeSection !== subsection.id
                                                    }">
                                                    {{ subsection.title }}
                                                </button>
                                            </li>
                                        </ul>
                                    </li>
                                </ul>
                            </nav>
                        </div>

                        <div class="flex-1 min-w-0">
                            <slot></slot>
                        </div>
                    </div>
                </div>
            </section>

            <!-- Every solution page now ends with its own contact form, so the
                 page's "Get a Quote" #contact anchor actually has a target. -->
            <ContactSection :solution="title" />
        </div>
    </AppLayout>
</template>
