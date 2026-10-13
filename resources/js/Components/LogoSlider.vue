<script setup>
// Every platform below is named somewhere in this site's own content
// (Solutions integration lists, use cases, or the e-commerce services page).
// Deliberately NOT a "clients" row — these are integration targets.
//
// kind: 'glyph'    = square 24x24 mark, needs to render slightly larger
//       'wordmark' = wide lockup, renders smaller so optical weight matches
const platforms = [
  { name: 'Microsoft',   file: 'microsoft',   kind: 'wordmark' },
  { name: 'OpenAI',      file: 'openai',      kind: 'glyph' },
  { name: 'Anthropic',   file: 'anthropic',   kind: 'glyph' },
  { name: 'Google Cloud', file: 'googlecloud', kind: 'glyph' },
  { name: 'Box',         file: 'box',         kind: 'glyph' },
  { name: 'Snowflake',   file: 'snowflake',   kind: 'glyph' },
  { name: 'Grafana',     file: 'grafana',     kind: 'glyph' },
  { name: 'HubSpot',     file: 'hubspot',     kind: 'glyph' },
  { name: 'Zendesk',     file: 'zendesk',     kind: 'wordmark' },
  { name: 'Shopify',     file: 'shopify',     kind: 'glyph' },
  { name: 'WooCommerce', file: 'woocommerce', kind: 'glyph' },
  { name: 'WordPress',   file: 'wordpress',   kind: 'glyph' },
];
</script>

<template>
  <section class="py-14 bg-ink border-y border-line overflow-hidden">
    <p class="text-center text-xs font-semibold uppercase tracking-[0.18em] text-content-subtle mb-9">
      Platforms we integrate with
    </p>

    <div class="logo-marquee relative">
      <!-- Edge fades so logos dissolve rather than clip at the viewport edge -->
      <div class="pointer-events-none absolute inset-y-0 left-0 w-24 z-10 bg-gradient-to-r from-ink to-transparent"></div>
      <div class="pointer-events-none absolute inset-y-0 right-0 w-24 z-10 bg-gradient-to-l from-ink to-transparent"></div>

      <ul class="logo-track">
        <!-- Two identical groups: the track translates -50% for a seamless loop.
             The second group is decorative, so it is hidden from assistive tech. -->
        <template v-for="group in 2" :key="group">
          <li
            v-for="platform in platforms"
            :key="`${group}-${platform.file}`"
            class="logo-item"
            :aria-hidden="group === 2 ? 'true' : undefined"
          >
            <img
              :src="`/img/logos/${platform.file}.svg`"
              :alt="group === 1 ? platform.name : ''"
              :class="platform.kind === 'wordmark' ? 'h-6' : 'h-8'"
              class="w-auto object-contain logo-img"
              loading="lazy"
              decoding="async"
            >
          </li>
        </template>
      </ul>
    </div>
  </section>
</template>

<style scoped>
.logo-track {
  display: flex;
  align-items: center;
  width: max-content;
  animation: logo-scroll 45s linear infinite;
}

.logo-marquee:hover .logo-track {
  animation-play-state: paused;
}

.logo-item {
  display: flex;
  align-items: center;
  justify-content: center;
  flex: 0 0 auto;
  min-width: 132px;
  padding: 0 2rem;
}

/* Normalise every mark to the same flat white so one brand colour
   (HubSpot orange, Grafana orange) cannot dominate the row. */
.logo-img {
  filter: brightness(0) invert(1);
  opacity: 0.55;
  transition: opacity 200ms ease;
}

.logo-item:hover .logo-img {
  opacity: 0.95;
}

@keyframes logo-scroll {
  from { transform: translateX(0); }
  to   { transform: translateX(-50%); }
}

/* No motion: fall back to a static wrapped grid showing one set only. */
@media (prefers-reduced-motion: reduce) {
  .logo-track {
    animation: none;
    flex-wrap: wrap;
    justify-content: center;
    width: 100%;
    row-gap: 1.5rem;
  }

  .logo-item[aria-hidden='true'] {
    display: none;
  }
}
</style>
