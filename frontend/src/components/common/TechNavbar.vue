<template>
  <nav class="tech-navbar" :class="{ 'tech-navbar-dark': isDarkMode }">
    <div class="tech-navbar-brand">
      <router-link to="/" class="tech-navbar-logo">
        <div class="logo-container">
          <span class="logo-text">一键升级</span>
          <span class="logo-text-secondary">uplus</span>
        </div>
      </router-link>
    </div>
    
    <div class="tech-navbar-content">
      <div class="tech-navbar-title" v-if="title">
        {{ title }}
      </div>
    </div>
    
    <div class="tech-navbar-actions">
      <button class="tech-navbar-button" @click="toggleDarkMode">
        <svg v-if="isDarkMode" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
          <circle cx="12" cy="12" r="5"></circle>
          <line x1="12" y1="1" x2="12" y2="3"></line>
          <line x1="12" y1="21" x2="12" y2="23"></line>
          <line x1="4.22" y1="4.22" x2="5.64" y2="5.64"></line>
          <line x1="18.36" y1="18.36" x2="19.78" y2="19.78"></line>
          <line x1="1" y1="12" x2="3" y2="12"></line>
          <line x1="21" y1="12" x2="23" y2="12"></line>
          <line x1="4.22" y1="19.78" x2="5.64" y2="18.36"></line>
          <line x1="18.36" y1="5.64" x2="19.78" y2="4.22"></line>
        </svg>
        <svg v-else xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
          <path d="M21 12.79A9 9 0 1 1 11.21 3 7 7 0 0 0 21 12.79z"></path>
        </svg>
      </button>
      
      <button class="tech-navbar-button" @click="toggleSidebar">
        <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
          <line x1="3" y1="12" x2="21" y2="12"></line>
          <line x1="3" y1="6" x2="21" y2="6"></line>
          <line x1="3" y1="18" x2="21" y2="18"></line>
        </svg>
      </button>
    </div>
  </nav>
</template>

<script>
import { computed } from 'vue';
import { useUiStore } from '@/store/uiStore';

export default {
  name: 'TechNavbar',
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
    
    // Methods
    const toggleDarkMode = () => {
      uiStore.toggleDarkMode();
    };
    
    const toggleSidebar = () => {
      uiStore.toggleSidebar();
    };
    
    return {
      isDarkMode,
      toggleDarkMode,
      toggleSidebar
    };
  }
};
</script>

<style scoped>
.tech-navbar {
  display: flex;
  align-items: center;
  justify-content: space-between;
  height: 70px;
  padding: 0 1.5rem;
  background-color: var(--white);
  border-bottom: 1px solid var(--gray-200);
  box-shadow: var(--shadow-sm);
  z-index: var(--z-index-fixed);
}

.tech-navbar-dark {
  background-color: var(--dark-blue);
  border-bottom: 1px solid var(--gray-800);
}

.tech-navbar-brand {
  display: flex;
  align-items: center;
}

.tech-navbar-logo {
  display: flex;
  align-items: center;
  text-decoration: none;
}

.logo-container {
  display: flex;
  flex-direction: column;
  align-items: flex-start;
}

.logo-text {
  font-size: 1.25rem;
  font-weight: 700;
  color: var(--primary);
  line-height: 1.2;
}

.logo-text-secondary {
  font-size: 1rem;
  font-weight: 600;
  color: var(--secondary);
  line-height: 1;
}

.tech-navbar-content {
  flex: 1;
  display: flex;
  align-items: center;
  justify-content: center;
}

.tech-navbar-title {
  font-size: 1.25rem;
  font-weight: 600;
  color: var(--gray-800);
}

.tech-navbar-dark .tech-navbar-title {
  color: var(--white);
}

.tech-navbar-actions {
  display: flex;
  align-items: center;
  gap: 0.75rem;
}

.tech-navbar-button {
  display: flex;
  align-items: center;
  justify-content: center;
  width: 40px;
  height: 40px;
  border: none;
  border-radius: var(--border-radius-circle);
  background-color: var(--gray-100);
  color: var(--gray-700);
  cursor: pointer;
  transition: all var(--transition-normal) var(--transition-timing);
}

.tech-navbar-button:hover {
  background-color: var(--gray-200);
  color: var(--gray-900);
}

.tech-navbar-dark .tech-navbar-button {
  background-color: var(--gray-800);
  color: var(--gray-300);
}

.tech-navbar-dark .tech-navbar-button:hover {
  background-color: var(--gray-700);
  color: var(--white);
}

.tech-navbar-button svg {
  width: 20px;
  height: 20px;
}

@media (max-width: 768px) {
  .tech-navbar {
    padding: 0 1rem;
  }
  
  .tech-navbar-title {
    font-size: 1rem;
  }
}
</style>