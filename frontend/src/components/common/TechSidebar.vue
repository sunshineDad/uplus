<template>
  <aside class="tech-sidebar" :class="{ 'tech-sidebar-collapsed': !isOpen, 'tech-sidebar-dark': isDarkMode }">
    <div class="tech-sidebar-header">
      <div class="tech-sidebar-brand" v-if="isOpen">
        <router-link to="/" class="tech-sidebar-logo">
          <span class="logo-text">一键升级</span>
          <span class="logo-text-secondary">uplus</span>
        </router-link>
      </div>
      <button class="tech-sidebar-toggle" @click="toggleSidebar">
        <svg v-if="isOpen" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
          <polyline points="15 18 9 12 15 6"></polyline>
        </svg>
        <svg v-else xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
          <polyline points="9 18 15 12 9 6"></polyline>
        </svg>
      </button>
    </div>
    
    <div class="tech-sidebar-content">
      <nav class="tech-sidebar-nav">
        <router-link 
          v-for="item in navItems" 
          :key="item.path" 
          :to="item.path" 
          class="tech-sidebar-nav-item"
          :class="{ 'active': currentRoute === item.path }"
        >
          <div class="nav-item-icon" v-html="item.icon"></div>
          <span class="nav-item-text" v-if="isOpen">{{ item.title }}</span>
        </router-link>
      </nav>
    </div>
    
    <div class="tech-sidebar-footer" v-if="isOpen">
      <div class="tech-sidebar-footer-content">
        <div class="tech-sidebar-footer-title">一键升级-uplus</div>
        <div class="tech-sidebar-footer-subtitle">v1.0.0</div>
      </div>
    </div>
  </aside>
</template>

<script>
import { computed, ref } from 'vue';
import { useRoute } from 'vue-router';
import { useUiStore } from '@/store/uiStore';

// Define navigation icons as template strings
const DASHBOARD_ICON = `
  <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
    <rect x="3" y="3" width="7" height="7"></rect>
    <rect x="14" y="3" width="7" height="7"></rect>
    <rect x="14" y="14" width="7" height="7"></rect>
    <rect x="3" y="14" width="7" height="7"></rect>
  </svg>
`;

const PROJECTS_ICON = `
  <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
    <path d="M22 19a2 2 0 0 1-2 2H4a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h5l2 3h9a2 2 0 0 1 2 2z"></path>
  </svg>
`;

const AI_PM_ICON = `
  <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
    <path d="M21 11.5a8.38 8.38 0 0 1-.9 3.8 8.5 8.5 0 0 1-7.6 4.7 8.38 8.38 0 0 1-3.8-.9L3 21l1.9-5.7a8.38 8.38 0 0 1-.9-3.8 8.5 8.5 0 0 1 4.7-7.6 8.38 8.38 0 0 1 3.8-.9h.5a8.48 8.48 0 0 1 8 8v.5z"></path>
  </svg>
`;

const RSD_ICON = `
  <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
    <path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"></path>
    <polyline points="14 2 14 8 20 8"></polyline>
    <line x1="16" y1="13" x2="8" y2="13"></line>
    <line x1="16" y1="17" x2="8" y2="17"></line>
    <polyline points="10 9 9 9 8 9"></polyline>
  </svg>
`;

const BITCUP_ICON = `
  <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
    <polyline points="16 18 22 12 16 6"></polyline>
    <polyline points="8 6 2 12 8 18"></polyline>
  </svg>
`;

const LOWCODE_ICON = `
  <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
    <rect x="3" y="3" width="18" height="18" rx="2" ry="2"></rect>
    <line x1="3" y1="9" x2="21" y2="9"></line>
    <line x1="9" y1="21" x2="9" y2="9"></line>
  </svg>
`;

const MEMORY_ICON = `
  <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
    <circle cx="12" cy="12" r="10"></circle>
    <path d="M12 6v6l4 2"></path>
  </svg>
`;

export default {
  name: 'TechSidebar',
  setup() {
    const route = useRoute();
    const uiStore = useUiStore();
    
    // Computed properties
    const isOpen = computed(() => uiStore.sidebarOpen);
    const isDarkMode = computed(() => uiStore.darkMode);
    const currentRoute = computed(() => route.path);
    
    // Navigation items
    const navItems = ref([
      {
        title: 'Dashboard',
        path: '/',
        icon: DASHBOARD_ICON
      },
      {
        title: 'Projects',
        path: '/projects',
        icon: PROJECTS_ICON
      },
      {
        title: 'AI-PM',
        path: '/ai-pm',
        icon: AI_PM_ICON
      },
      {
        title: 'RSD Documents',
        path: '/rsd',
        icon: RSD_ICON
      },
      {
        title: 'BITCUP Models',
        path: '/bitcup',
        icon: BITCUP_ICON
      },
      {
        title: 'Low-Code Platform',
        path: '/lowcode',
        icon: LOWCODE_ICON
      },
      {
        title: 'Memory Intelligence',
        path: '/memory',
        icon: MEMORY_ICON
      }
    ]);
    
    // Methods
    const toggleSidebar = () => {
      uiStore.toggleSidebar();
    };
    
    return {
      isOpen,
      isDarkMode,
      currentRoute,
      navItems,
      toggleSidebar
    };
  }
};
</script>

<style scoped>
.tech-sidebar {
  display: flex;
  flex-direction: column;
  width: 250px;
  height: 100%;
  background-color: var(--white);
  border-right: 1px solid var(--gray-200);
  transition: width var(--transition-normal) var(--transition-timing);
  overflow: hidden;
}

.tech-sidebar-collapsed {
  width: 70px;
}

.tech-sidebar-dark {
  background-color: var(--dark-purple);
  border-right: 1px solid var(--gray-800);
}

.tech-sidebar-header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  height: 70px;
  padding: 0 1rem;
  border-bottom: 1px solid var(--gray-200);
}

.tech-sidebar-dark .tech-sidebar-header {
  border-bottom: 1px solid var(--gray-800);
}

.tech-sidebar-brand {
  display: flex;
  align-items: center;
}

.tech-sidebar-logo {
  display: flex;
  flex-direction: column;
  text-decoration: none;
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

.tech-sidebar-toggle {
  display: flex;
  align-items: center;
  justify-content: center;
  width: 30px;
  height: 30px;
  border: none;
  border-radius: var(--border-radius-circle);
  background-color: var(--gray-100);
  color: var(--gray-700);
  cursor: pointer;
  transition: all var(--transition-normal) var(--transition-timing);
}

.tech-sidebar-toggle:hover {
  background-color: var(--gray-200);
  color: var(--gray-900);
}

.tech-sidebar-dark .tech-sidebar-toggle {
  background-color: var(--gray-800);
  color: var(--gray-300);
}

.tech-sidebar-dark .tech-sidebar-toggle:hover {
  background-color: var(--gray-700);
  color: var(--white);
}

.tech-sidebar-toggle svg {
  width: 18px;
  height: 18px;
}

.tech-sidebar-content {
  flex: 1;
  overflow-y: auto;
  padding: 1rem 0;
}

.tech-sidebar-nav {
  display: flex;
  flex-direction: column;
  gap: 0.5rem;
}

.tech-sidebar-nav-item {
  display: flex;
  align-items: center;
  padding: 0.75rem 1rem;
  color: var(--gray-700);
  text-decoration: none;
  border-radius: var(--border-radius-md);
  transition: all var(--transition-normal) var(--transition-timing);
}

.tech-sidebar-nav-item:hover {
  background-color: var(--gray-100);
  color: var(--gray-900);
}

.tech-sidebar-nav-item.active {
  background-color: var(--primary-light);
  color: var(--white);
}

.tech-sidebar-dark .tech-sidebar-nav-item {
  color: var(--gray-300);
}

.tech-sidebar-dark .tech-sidebar-nav-item:hover {
  background-color: var(--gray-800);
  color: var(--white);
}

.tech-sidebar-dark .tech-sidebar-nav-item.active {
  background-color: var(--primary-dark);
  color: var(--white);
}

.nav-item-icon {
  display: flex;
  align-items: center;
  justify-content: center;
  width: 24px;
  height: 24px;
  margin-right: 0.75rem;
}

.tech-sidebar-collapsed .nav-item-icon {
  margin-right: 0;
}

.nav-item-icon svg {
  width: 20px;
  height: 20px;
}

.tech-sidebar-footer {
  padding: 1rem;
  border-top: 1px solid var(--gray-200);
}

.tech-sidebar-dark .tech-sidebar-footer {
  border-top: 1px solid var(--gray-800);
}

.tech-sidebar-footer-content {
  display: flex;
  flex-direction: column;
  align-items: center;
}

.tech-sidebar-footer-title {
  font-size: 0.875rem;
  font-weight: 600;
  color: var(--gray-700);
}

.tech-sidebar-dark .tech-sidebar-footer-title {
  color: var(--gray-300);
}

.tech-sidebar-footer-subtitle {
  font-size: 0.75rem;
  color: var(--gray-500);
}

.tech-sidebar-dark .tech-sidebar-footer-subtitle {
  color: var(--gray-500);
}

@media (max-width: 992px) {
  .tech-sidebar {
    position: fixed;
    top: 0;
    left: 0;
    z-index: var(--z-index-fixed);
    height: 100vh;
    transform: translateX(0);
    box-shadow: var(--shadow-lg);
  }
  
  .tech-sidebar-collapsed {
    transform: translateX(-100%);
    width: 250px;
  }
}
</style>