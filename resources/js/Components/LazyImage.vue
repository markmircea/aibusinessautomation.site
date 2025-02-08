<script setup>
import { ref, onMounted } from 'vue';

const props = defineProps({
  src: {
    type: String,
    required: true
  },
  alt: {
    type: String,
    default: ''
  },
  width: {
    type: [Number, String],
    required: true
  },
  height: {
    type: [Number, String],
    required: true
  }
});

const isLoaded = ref(false);
const imgRef = ref(null);

onMounted(() => {
  const observer = new IntersectionObserver((entries) => {
    if (entries[0].isIntersecting) {
      imgRef.value.src = props.src;
      observer.disconnect();
    }
  });

  observer.observe(imgRef.value);
});

const onLoad = () => {
  isLoaded.value = true;
};
</script>

<template>
  <img
    ref="imgRef"
    :data-src="src"
    :alt="alt"
    :width="width"
    :height="height"
    :class="{ 'opacity-0': !isLoaded, 'opacity-100': isLoaded }"
    class="transition-opacity duration-300 rounded-lg shadow-md mx-auto mb-4"
    @load="onLoad"
  />
</template>
