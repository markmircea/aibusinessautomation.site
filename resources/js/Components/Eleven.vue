<template>
    <div id="elevenlabs-widget"></div>
</template>

<script setup>
import { onMounted, onUnmounted } from 'vue';

onMounted(() => {
    const widget = document.createElement('elevenlabs-convai');
    widget.setAttribute('agent-id', '86X1xJWAjz9vdTJfQC9h'); // Replace with your actual agent ID
    
    const script = document.createElement('script');
    script.src = 'https://elevenlabs.io/convai-widget/index.js';
    script.async = true;
    script.type = 'text/javascript';
    
    const container = document.getElementById('elevenlabs-widget');
    container.appendChild(widget);
    document.body.appendChild(script);
});

onUnmounted(() => {
    const script = document.querySelector('script[src="https://elevenlabs.io/convai-widget/index.js"]');
    if (script) {
        script.remove();
    }
});
</script>

<style>
#elevenlabs-widget {
    position: fixed;
    bottom: 20px;
    right: 20px;
    z-index: 1000;
}
</style>