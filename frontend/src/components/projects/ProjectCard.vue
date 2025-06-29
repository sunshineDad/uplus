<template>
  <div class="project-card" :class="{ 'project-card-dark': isDarkMode }" @click="handleClick">
    <div class="project-card-header">
      <h3 class="project-title">{{ project.name }}</h3>
      <div class="project-status" :class="`status-${project.status.toLowerCase()}`">
        {{ project.status }}
      </div>
    </div>
    
    <div class="project-card-body">
      <p class="project-description">{{ truncateDescription(project.description) }}</p>
    </div>
    
    <div class="project-card-footer">
      <div class="project-meta">
        <div class="project-created">
          <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
            <circle cx="12" cy="12" r="10"></circle>
            <polyline points="12 6 12 12 16 14"></polyline>
          </svg>
          <span>{{ formatDate(project.created_at) }}</span>
        </div>
      </div>
      
      <div class="project-actions">
        <button class="action-button" @click.stop="$emit('view-project', project)">
          <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
            <path d="M1 12s4-8 11-8 11 8 11 8-4 8-11 8-11-8-11-8z"></path>
            <circle cx="12" cy="12" r="3"></circle>
          </svg>
        </button>
        
        <button class="action-button" @click.stop="$emit('start-session', project)">
          <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
            <path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"></path>
          </svg>
        </button>
      </div>
    </div>
    
    <div class="project-card-glow"></div>
  </div>
</template>

<script>
import { computed } from 'vue';
import { useUiStore } from '@/store/uiStore';

export default {
  name: 'ProjectCard',
  props: {
    project: {
      type: Object,
      required: true
    }
  },
  emits: ['view-project', 'start-session'],
  setup(props, { emit }) {
    const uiStore = useUiStore();
    
    // Computed properties
    const isDarkMode = computed(() => uiStore.darkMode);
    
    // Methods
    const truncateDescription = (description) => {
      if (!description) return 'No description provided';
      return description.length > 120 ? description.substring(0, 120) + '...' : description;
    };
    
    const formatDate = (dateString) => {
      if (!dateString) return '';
      
      const date = new Date(dateString);
      return date.toLocaleDateString(undefined, {
        year: 'numeric',
        month: 'short',
        day: 'numeric'
      });
    };
    
    const handleClick = () => {
      emit('view-project', props.project);
    };
    
    return {
      isDarkMode,
      truncateDescription,
      formatDate,
      handleClick
    };
  }
};
</script>

<style scoped>
.project-card {
  position: relative;
  display: flex;
  flex-direction: column;
  height: 100%;
  background-color: var(--white);
  border-radius: var(--border-radius-lg);
  box-shadow: var(--shadow-md);
  overflow: hidden;
  transition: all var(--transition-normal) var(--transition-timing);
  cursor: pointer;
  z-index: 1;
}

.project-card:hover {
  transform: translateY(-5px);
  box-shadow: var(--shadow-lg);
}

.project-card:hover .project-card-glow {
  opacity: 1;
}

.project-card-dark {
  background-color: var(--dark-blue);
  box-shadow: 0 4px 20px rgba(0, 0, 0, 0.3);
}

.project-card-header {
  display: flex;
  align-items: flex-start;
  justify-content: space-between;
  padding: 1.5rem;
  border-bottom: 1px solid var(--gray-200);
}

.project-card-dark .project-card-header {
  border-bottom: 1px solid var(--gray-800);
}

.project-title {
  margin: 0;
  font-size: 1.25rem;
  font-weight: 600;
  color: var(--gray-900);
}

.project-card-dark .project-title {
  color: var(--white);
}

.project-status {
  padding: 0.25rem 0.75rem;
  font-size: 0.75rem;
  font-weight: 600;
  text-transform: uppercase;
  border-radius: var(--border-radius-pill);
}

.status-active {
  background-color: var(--success);
  color: var(--white);
}

.status-pending {
  background-color: var(--warning);
  color: var(--gray-900);
}

.status-completed {
  background-color: var(--info);
  color: var(--white);
}

.status-archived {
  background-color: var(--gray-500);
  color: var(--white);
}

.project-card-body {
  flex: 1;
  padding: 1.5rem;
}

.project-description {
  margin: 0;
  font-size: 0.875rem;
  line-height: 1.5;
  color: var(--gray-700);
}

.project-card-dark .project-description {
  color: var(--gray-300);
}

.project-card-footer {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 1rem 1.5rem;
  background-color: var(--gray-100);
  border-top: 1px solid var(--gray-200);
}

.project-card-dark .project-card-footer {
  background-color: var(--dark-purple);
  border-top: 1px solid var(--gray-800);
}

.project-meta {
  display: flex;
  align-items: center;
}

.project-created {
  display: flex;
  align-items: center;
  font-size: 0.75rem;
  color: var(--gray-600);
}

.project-card-dark .project-created {
  color: var(--gray-400);
}

.project-created svg {
  width: 14px;
  height: 14px;
  margin-right: 0.25rem;
}

.project-actions {
  display: flex;
  align-items: center;
  gap: 0.5rem;
}

.action-button {
  display: flex;
  align-items: center;
  justify-content: center;
  width: 32px;
  height: 32px;
  background-color: var(--white);
  color: var(--gray-700);
  border: 1px solid var(--gray-300);
  border-radius: var(--border-radius-circle);
  cursor: pointer;
  transition: all var(--transition-normal) var(--transition-timing);
}

.action-button:hover {
  background-color: var(--primary);
  color: var(--white);
  border-color: var(--primary);
}

.project-card-dark .action-button {
  background-color: var(--gray-800);
  color: var(--gray-300);
  border-color: var(--gray-700);
}

.project-card-dark .action-button:hover {
  background-color: var(--primary);
  color: var(--white);
  border-color: var(--primary);
}

.action-button svg {
  width: 16px;
  height: 16px;
}

.project-card-glow {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: linear-gradient(45deg, 
    rgba(58, 134, 255, 0.1) 0%, 
    rgba(131, 56, 236, 0.1) 50%, 
    rgba(255, 0, 110, 0.1) 100%);
  opacity: 0;
  transition: opacity var(--transition-normal) var(--transition-timing);
  z-index: -1;
}

.project-card-dark .project-card-glow {
  background: linear-gradient(45deg, 
    rgba(58, 134, 255, 0.2) 0%, 
    rgba(131, 56, 236, 0.2) 50%, 
    rgba(255, 0, 110, 0.2) 100%);
}
</style>