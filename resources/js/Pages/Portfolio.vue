<script setup>
import AppLayout from '@/Layouts/AppLayout.vue';
import ProjectCard from '@/Components/ProjectCard.vue';
import Icon from '@/Components/Icon.vue';
import ContactSection from '@/Components/ContactSection.vue';

const projects = [
  {
    name: 'Selenix Web (Laravel)',
    category: 'SaaS Backend / Web App',
    tagline: 'Central SaaS backend for the Selenix browser-automation ecosystem.',
    description: 'Marketing site, user account hub, subscription manager, and API backend for the desktop app — built on Laravel 10/11 with a Filament admin panel, Inertia.js Vue 3 SPA, and PayPal recurring billing across Free / AI Agent / Professional tiers.',
    techStack: ['Laravel 10/11', 'Vue 3 + Inertia', 'Filament 3.3', 'MySQL 8', 'Tailwind CSS', 'Sanctum', 'Google OAuth', 'PayPal'],
    features: [
      'Token-based desktop auth API (/api/desktop/login, /register, /ai-turns)',
      'Tiered subscription billing with PayPal webhooks and AI-turn quotas',
      'Template marketplace with community submission and review workflow',
      'AES-256-CBC encrypted license keys for desktop app distribution',
      'Full Filament admin dashboard for users, content, and subscriptions'
    ],
    status: 'Production',
    icon: 'Server',
    accent: 'blue',
    flagship: true,
    flagshipPart: 'Selenix Tier 1 — Web'
  },
  {
    name: 'AIBrain Webtools (Selenix Desktop)',
    category: 'Desktop App / Automation IDE',
    tagline: 'Electron-based AI browser-automation IDE with 135+ commands and natural-language scripting.',
    description: 'A desktop browser-automation IDE built on Selenium IDE — record, edit, and play back automations, with an AI assistant that turns natural language into automation commands. 25+ package monorepo with code export to Python, Java, C#, JavaScript, and Ruby.',
    techStack: ['Electron 28', 'React 18', 'TypeScript 5', 'Material-UI', 'Selenium WebDriver 4', 'Webpack 5', 'pnpm workspaces'],
    features: [
      'Recorder + playback engine for embedded Chromium automation',
      'AI assistant generates commands from screenshots, HTML, and test state',
      '135+ commands: click, type, scrape, HTTP, email, PowerShell, JS execution',
      'Hourly / daily / weekly / monthly automation scheduler',
      'MCP bridge server on localhost exposing 18 tools for Claude Desktop'
    ],
    status: 'Production',
    icon: 'MonitorSmartphone',
    accent: 'purple',
    flagship: true,
    flagshipPart: 'Selenix Tier 2 — Desktop'
  },
  {
    name: 'Selenix AI Proxy',
    category: 'API / Backend Infrastructure',
    tagline: 'OpenAI-compatible proxy that wraps the Claude Code CLI for team access.',
    description: 'A lightweight TypeScript proxy that exposes a /v1/chat/completions endpoint compatible with any OpenAI client, while running locally-installed Claude Code under the hood. Handles team API key auth, request queuing, and per-key usage tracking.',
    techStack: ['Node.js 18+', 'Express 4', 'TypeScript 5', 'Claude Code CLI', 'Anthropic SDK', 'Nginx Proxy Manager'],
    features: [
      'Drop-in OpenAI-compatible /v1/chat/completions endpoint',
      'sk-team-* API keys with enable/disable and usage tracking',
      'Concurrency-limited request queue (default: 4 concurrent processes)',
      'Base64 image handling via temp file pipeline',
      'HTML admin dashboard for key management and request log inspection'
    ],
    status: 'Production',
    icon: 'Webhook',
    accent: 'green',
    flagship: true,
    flagshipPart: 'Selenix Tier 3 — AI Proxy'
  },
  {
    name: 'Selenix MCP Server',
    category: 'Agentic AI / MCP Integration',
    tagline: 'Claude Desktop integration for browser automation via Model Context Protocol.',
    description: 'A published npm package (@selenix/mcp-server) that bridges Claude Desktop and any MCP-compatible client to the Selenix browser-automation platform. 18+ tools for screenshots, HTML inspection, command execution, and test management — auto-discovered via local bridge config with bearer-token auth.',
    techStack: ['Node.js 18+', 'TypeScript', '@modelcontextprotocol/sdk 1.12+', 'esbuild', 'npm registry'],
    features: [
      'Industry-standard MCP protocol — works with Claude Desktop, Cursor, any MCP client',
      '18+ tools: screenshot, HTML, project metadata, command writes, test runs',
      'Zero-trust local bridge (127.0.0.1) with bearer-token auth',
      'Auto-discovery via ~/.selenix/bridge.json config',
      'Single-file bundle, published on npm and the Glama MCP registry'
    ],
    status: 'Production',
    icon: 'Plug',
    accent: 'indigo'
  },
  {
    name: 'ScorCorect Video Generation',
    category: 'AI Pipeline / Generative Video',
    tagline: 'Hybrid AI + programmatic compositing pipeline for cinematic sports recap videos.',
    description: 'A FastAPI-based video generation service that produces broadcast-quality 10-second match recap videos. Combines LTX-2.3 video diffusion (cached once per template) with PIL/MoviePy programmatic compositing — driving per-video cost to ~$0 after one-time asset generation, versus $30–50K with competing services.',
    techStack: ['Python 3.8+', 'FastAPI', 'LTX-2.3', 'ComfyUI', 'PIL', 'MoviePy 2.x', 'rembg', 'SQLite'],
    features: [
      'Hybrid LTX + programmatic pipeline → ~$0 marginal cost per video',
      'Dynamic goal-aware layouts (handles 0/1/2/3+ goals with smart timing)',
      'Player cutout extraction via deep-learning segmentation',
      'Async job queue with sqlite-backed persistence',
      'Multi-language client examples: curl, Python, JavaScript, Postman'
    ],
    status: 'In Development',
    icon: 'Clapperboard',
    accent: 'orange'
  },
  {
    name: 'Project ADAM',
    category: 'Agentic AI System',
    tagline: 'Community-driven AI that measurably improves from user contributions and votes.',
    description: 'An experimental dual-stack AI platform exploring whether AI quality can be improved through structured community contribution. Python FastAPI backend with a 9-table MySQL schema and ChromaDB vector store, paired with a Laravel + Filament + Inertia/Vue 3 web frontend for participation and admin.',
    techStack: ['Python', 'FastAPI', 'OpenRouter', 'ChromaDB', 'Qdrant', 'Laravel 10', 'Filament', 'Vue 3 + Inertia', 'Docker Compose'],
    features: [
      'Dual-stack architecture: Python backend + PHP frontend (polyglot proof-point)',
      'Vector-database semantic retrieval over user-contributed knowledge',
      'Voting and quality system for crowdsourced curation',
      '9-table relational schema with full referential integrity',
      'Filament admin dashboard for monitoring and management'
    ],
    status: 'In Development',
    icon: 'BrainCircuit',
    accent: 'teal'
  }
];

const capabilities = [
  { icon: 'Globe', label: 'E-commerce & Web Apps' },
  { icon: 'Smartphone', label: 'Mobile Apps' },
  { icon: 'Monitor', label: 'Desktop Apps' },
  { icon: 'Webhook', label: 'APIs & Backends' },
  { icon: 'Workflow', label: 'Automations' },
  { icon: 'BrainCircuit', label: 'Agentic AI Systems' },
];

const stats = [
  { value: '10+', label: 'Years building production software' },
  { value: '2,500+', label: 'Subscribers across shipped products' },
  { value: '6', label: 'Active flagship projects' },
  { value: '15+', label: 'Languages, frameworks, and platforms' }
];
</script>

<template>
  <AppLayout>

    <div class="min-h-screen bg-ink">
      <!-- Hero -->
      <section class="relative overflow-hidden bg-ink py-24 border-b border-line">
        <div class="absolute inset-0 hero-mesh" aria-hidden="true"></div>
        <div class="absolute inset-0 bg-grid-pattern opacity-[0.07]" aria-hidden="true"></div>
        <div class="relative max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 text-center">
          <span class="inline-block px-3 py-1 rounded-full border border-line bg-surface text-accent-400 text-xs font-semibold uppercase tracking-[0.14em] mb-6">
            Portfolio
          </span>
          <h1 class="text-4xl sm:text-5xl md:text-6xl font-extrabold tracking-tight text-content mb-6">
            What we've built —
            <span class="block text-accent-400">across the full stack</span>
          </h1>
          <p class="mx-auto max-w-3xl text-lg sm:text-xl text-content-muted mb-10">
            E-commerce web apps, mobile and desktop apps, APIs, automation pipelines, agentic AI systems, MCP servers — every project below is real, production-grade work shipped by the same team that will build yours.
          </p>

          <div class="grid grid-cols-2 md:grid-cols-4 gap-6 max-w-4xl mx-auto">
            <div v-for="stat in stats" :key="stat.label" class="text-center">
              <div class="text-3xl font-bold text-content">{{ stat.value }}</div>
              <div class="text-sm text-content-subtle mt-1">{{ stat.label }}</div>
            </div>
          </div>
        </div>
      </section>

      <!-- Flagship callout -->
      <section class="py-16 bg-ink">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div class="bg-surface rounded-card shadow-e3 ring-1 ring-inset ring-line overflow-hidden">
            <div class="grid md:grid-cols-3 gap-0">
              <div class="md:col-span-1 bg-gradient-to-br from-brand-700 to-accent-600 p-8 text-white">
                <div class="text-xs font-semibold uppercase tracking-[0.14em] text-white/70 mb-2">Flagship Platform</div>
                <h2 class="text-3xl font-bold mb-4">Selenix</h2>
                <p class="text-white/85 mb-6">
                  An AI-powered browser-automation platform. Three independently shipped components — SaaS backend, Electron desktop IDE, and AI proxy — work together to deliver natural-language browser automation to 2,500+ subscribers.
                </p>
                <a href="https://selenix.io" target="_blank" rel="noopener noreferrer"
                   class="inline-flex items-center px-4 py-2 bg-white/10 hover:bg-white/20 border border-white/25 rounded-control text-sm font-semibold transition-colors focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-white/60">
                  Visit selenix.io
                  <svg class="h-4 w-4 ml-1" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M14 5l7 7m0 0l-7 7m7-7H3" />
                  </svg>
                </a>
              </div>
              <div class="md:col-span-2 p-8 grid sm:grid-cols-3 gap-6">
                <div>
                  <div class="text-xs font-semibold uppercase tracking-[0.14em] text-accent-400 mb-2">Tier 1</div>
                  <h3 class="font-bold text-content mb-1">SelenixWeb</h3>
                  <p class="text-sm text-content-subtle">Laravel SaaS backend, billing, marketplace, admin.</p>
                </div>
                <div>
                  <div class="text-xs font-semibold uppercase tracking-[0.14em] text-accent-400 mb-2">Tier 2</div>
                  <h3 class="font-bold text-content mb-1">Desktop IDE</h3>
                  <p class="text-sm text-content-subtle">Electron + React automation IDE with AI assistant.</p>
                </div>
                <div>
                  <div class="text-xs font-semibold uppercase tracking-[0.14em] text-accent-400 mb-2">Tier 3</div>
                  <h3 class="font-bold text-content mb-1">AI Proxy</h3>
                  <p class="text-sm text-content-subtle">OpenAI-compatible Claude Code CLI wrapper.</p>
                </div>
              </div>
            </div>
          </div>
        </div>
      </section>

      <!-- Projects grid -->
      <section class="py-16 bg-surface/30 border-y border-line">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div class="text-center mb-12">
            <h2 class="text-3xl sm:text-4xl font-bold tracking-tight text-content mb-4">
              Selected Projects
            </h2>
            <p class="max-w-3xl mx-auto text-lg text-content-muted">
              From flagship SaaS platforms to research-grade AI pipelines, each card below links to the technical work behind it.
            </p>
          </div>

          <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
            <ProjectCard
              v-for="(project, idx) in projects"
              :key="project.name"
              v-bind="project"
              :animation-delay="`${idx * 0.1}s`"
            />
          </div>
        </div>
      </section>

      <!-- Capabilities band -->
      <section class="py-16 bg-ink">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div class="text-center mb-10">
            <h2 class="text-2xl sm:text-3xl font-bold tracking-tight text-content mb-3">
              What we can build for you
            </h2>
            <p class="max-w-3xl mx-auto text-content-muted">
              The portfolio above demonstrates capabilities across every category we offer.
            </p>
          </div>
          <div class="grid grid-cols-2 md:grid-cols-3 lg:grid-cols-6 gap-4">
            <div
              v-for="capability in capabilities"
              :key="capability.label"
              class="flex flex-col items-center gap-3 p-5 rounded-card bg-surface ring-1 ring-inset ring-line transition-colors duration-200 hover:ring-accent-500/40"
            >
              <Icon :name="capability.icon" class="h-6 w-6 text-accent-400" />
              <span class="text-sm font-semibold text-content text-center">{{ capability.label }}</span>
            </div>
          </div>
        </div>
      </section>

      <ContactSection />
    </div>
  </AppLayout>
</template>

<style scoped>
.hero-mesh {
  background:
    radial-gradient(60% 55% at 50% 0%, rgba(91, 108, 255, 0.24) 0%, transparent 70%),
    radial-gradient(45% 45% at 15% 20%, rgba(47, 75, 196, 0.20) 0%, transparent 70%);
}

.bg-grid-pattern {
  background-image: radial-gradient(circle, #ffffff 1px, transparent 1px);
  background-size: 32px 32px;
}
</style>
