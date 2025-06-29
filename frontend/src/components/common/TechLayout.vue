<template>
  <div class="tech-layout" :class="{ 'tech-layout-dark': isDarkMode }">
    <TechSidebar />
    
    <div class="tech-layout-main">
      <TechNavbar :title="title" />
      
      <main class="tech-layout-content">
        <slot></slot>
      </main>
    </div>
    
    <NotificationContainer position="top-right" />
  </div>
</template>

<script>
import { computed, onMounted } from 'vue';
import { useUiStore } from '@/store/uiStore';
import TechNavbar from './TechNavbar.vue';
import TechSidebar from './TechSidebar.vue';
import NotificationContainer from './NotificationContainer.vue';

export default {
  name: 'TechLayout',
  components: {
    TechNavbar,
    TechSidebar,
    NotificationContainer
  },
  props: {
    title: {
      type: String,
      default: ''
    }
  },
  setup() {
    const uiStore = useUiStore();
    
    // Computed properties
    const isDarkMode = computed(() => uiStore.darkMode);
    
    // Initialize UI settings from localStorage
    onMounted(() => {
      uiStore.initializeFromLocalStorage();
    });
    
    return {
      isDarkMode
    };
  }
};
</script>

<style scoped>
.tech-layout {
  display: grid;
  grid-template-columns: auto 1fr;
  grid-template-rows: 1fr;
  height: 100vh;
  width: 100%;
  overflow: hidden;
  background-color: var(--gray-100);
}

.tech-layout-dark {
  background-color: var(--dark);
}

.tech-layout-main {
  display: flex;
  flex-direction: column;
  height: 100vh;
  overflow: hidden;
}

.tech-layout-content {
  flex: 1;
  padding: 1.5rem;
  overflow-y: auto;
}

@media (max-width: 768px) {
  .tech-layout-content {
    padding: 1rem;
  }
}
</style>