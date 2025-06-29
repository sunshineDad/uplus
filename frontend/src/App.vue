<script setup>
import { onMounted } from 'vue';
import { useUiStore } from './store/uiStore';
import TechBackground from './components/common/TechBackground.vue';

const uiStore = useUiStore();

// Initialize UI settings from localStorage on app mount
onMounted(() => {
  uiStore.initializeFromLocalStorage();
});
</script>

<template>
  <div id="app">
    <TechBackground />
    <router-view v-slot="{ Component }">
      <transition name="fade" mode="out-in">
        <component :is="Component" />
      </transition>
    </router-view>
  </div>
</template>

<style>
/* Import fonts */
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=Manrope:wght@400;500;600;700&family=JetBrains+Mono:wght@400;500&display=swap');

/* Global transitions */
.fade-enter-active,
.fade-leave-active {
  transition: opacity 0.3s ease;
}

.fade-enter-from,
.fade-leave-to {
  opacity: 0;
}
</style>
