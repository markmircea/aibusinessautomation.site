<script setup>
import { computed } from 'vue';
// Explicit imports keep this tree-shakeable — importing * from lucide-vue-next
// would pull the entire icon set into the bundle.
import {
  ArrowLeft, ArrowRight, Bot, Boxes, BrainCircuit, ChartColumn, Check, ChevronLeft, ChevronRight,
  Clapperboard, Cpu, ExternalLink, Factory, FileText, Gamepad2, Globe, Image, Languages,
  LayoutTemplate, Mail, Megaphone, MessagesSquare, Monitor, MonitorSmartphone, Plug, Search, Server,
  ShoppingCart, Smartphone, Sparkles, Target, TrendingUp, Users, Wallet, Webhook, Workflow, X,
} from 'lucide-vue-next';

const registry = {
  ArrowLeft, ArrowRight, Bot, Boxes, BrainCircuit, ChartColumn, Check, ChevronLeft, ChevronRight,
  Clapperboard, Cpu, ExternalLink, Factory, FileText, Gamepad2, Globe, Image, Languages,
  LayoutTemplate, Mail, Megaphone, MessagesSquare, Monitor, MonitorSmartphone, Plug, Search, Server,
  ShoppingCart, Smartphone, Sparkles, Target, TrendingUp, Users, Wallet, Webhook, Workflow, X,
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
