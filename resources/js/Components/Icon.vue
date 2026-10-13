<script setup>
import { computed } from 'vue';
// Explicit imports keep this tree-shakeable — importing * from lucide-vue-next
// would pull the entire icon set into the bundle.
import {
  ArrowRight, Bot, BrainCircuit, Check, Clapperboard, CreditCard, Factory, FileText, Globe,
  LayoutTemplate, MessagesSquare, Monitor, MonitorSmartphone, Plug, Server,
  ReceiptText, ShoppingCart, Smartphone, Sparkles, TrendingUp, Users, Wallet, Webhook,
  Workflow,
} from 'lucide-vue-next';

const registry = {
  ArrowRight, Bot, BrainCircuit, Check, Clapperboard, CreditCard, Factory, FileText, Globe,
  LayoutTemplate, MessagesSquare, Monitor, MonitorSmartphone, Plug, Server,
  ReceiptText, ShoppingCart, Smartphone, Sparkles, TrendingUp, Users, Wallet, Webhook,
  Workflow,
};

const props = defineProps({
  name: { type: String, required: true },
  strokeWidth: { type: Number, default: 1.75 },
});

const component = computed(() => registry[props.name] ?? Sparkles);
</script>

<template>
  <component :is="component" :stroke-width="strokeWidth" aria-hidden="true" />
</template>
