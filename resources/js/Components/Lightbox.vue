<script setup>
import { computed, nextTick, onBeforeUnmount, ref, watch } from 'vue';
import Icon from '@/Components/Icon.vue';

// Keyboard-accessible image viewer. `index` is the position in `images`, or
// null while closed; the parent owns that state through v-model:index.
const props = defineProps({
  images: { type: Array, default: () => [] },
  index: { type: Number, default: null },
});

const emit = defineEmits(['update:index']);

const current = computed(() => (props.index === null ? null : props.images[props.index] ?? null));
const closeButton = ref(null);
const dialog = ref(null);

let open = false;
let lastFocused = null;

function close() {
  emit('update:index', null);
}

function step(delta) {
  if (props.images.length < 2) return;
  emit('update:index', (props.index + delta + props.images.length) % props.images.length);
}

function onKeydown(event) {
  if (event.key === 'Escape') {
    close();
    return;
  }
  if (event.key === 'ArrowLeft') {
    step(-1);
    return;
  }
  if (event.key === 'ArrowRight') {
    step(1);
    return;
  }
  if (event.key === 'Tab') {
    // Focus trap: Tab keeps cycling through the dialog's own buttons.
    const buttons = [...(dialog.value?.querySelectorAll('[data-lightbox-button]') ?? [])];
    if (!buttons.length) return;
    const first = buttons[0];
    const last = buttons[buttons.length - 1];
    const active = document.activeElement;
    if (!buttons.includes(active)) {
      event.preventDefault();
      first.focus();
    } else if (event.shiftKey && active === first) {
      event.preventDefault();
      last.focus();
    } else if (!event.shiftKey && active === last) {
      event.preventDefault();
      first.focus();
    }
  }
}

function unlock() {
  if (!open) return;
  open = false;
  document.removeEventListener('keydown', onKeydown);
  document.documentElement.style.overflow = '';
  if (lastFocused && typeof lastFocused.focus === 'function') lastFocused.focus();
  lastFocused = null;
}

watch(
  () => props.index,
  (value) => {
    if (value === null || !props.images.length) {
      unlock();
      return;
    }
    if (!open) {
      open = true;
      lastFocused = document.activeElement;
      document.documentElement.style.overflow = 'hidden';
      document.addEventListener('keydown', onKeydown);
      // Focus moves into the dialog once, on open; stepping between images leaves it where the user put it.
      nextTick(() => closeButton.value?.focus());
    }
  }
);

onBeforeUnmount(unlock);
</script>

<template>
  <Teleport to="body">
    <div
      v-if="index !== null && current"
      ref="dialog"
      class="fixed inset-0 z-50 flex flex-col items-center justify-center bg-ink/95 backdrop-blur-sm p-4 sm:p-10"
      role="dialog"
      aria-modal="true"
      aria-label="Image viewer"
      @click.self="close"
    >
      <img
        :src="`${current.src}.webp`"
        :alt="current.alt"
        :width="current.width"
        :height="current.height"
        class="max-h-[78vh] max-w-full rounded-card ring-1 ring-line shadow-e3 object-contain"
      >

      <p class="mt-4 max-w-3xl text-center text-sm text-content-muted" aria-live="polite">
        <template v-if="current.caption">{{ current.caption }} · </template>{{ index + 1 }} / {{ images.length }}
      </p>

      <button
        ref="closeButton"
        type="button"
        data-lightbox-button
        aria-label="Close"
        class="absolute top-4 right-4 rounded-full bg-surface/90 p-3 text-content ring-1 ring-line hover:bg-surface-2 focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-accent-400"
        @click="close"
      >
        <Icon name="X" class="h-5 w-5" />
      </button>

      <button
        v-if="images.length > 1"
        type="button"
        data-lightbox-button
        aria-label="Previous image"
        class="absolute left-4 top-1/2 -translate-y-1/2 rounded-full bg-surface/90 p-3 text-content ring-1 ring-line hover:bg-surface-2 focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-accent-400"
        @click="step(-1)"
      >
        <Icon name="ChevronLeft" class="h-6 w-6" />
      </button>

      <button
        v-if="images.length > 1"
        type="button"
        data-lightbox-button
        aria-label="Next image"
        class="absolute right-4 top-1/2 -translate-y-1/2 rounded-full bg-surface/90 p-3 text-content ring-1 ring-line hover:bg-surface-2 focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-accent-400"
        @click="step(1)"
      >
        <Icon name="ChevronRight" class="h-6 w-6" />
      </button>
    </div>
  </Teleport>
</template>
