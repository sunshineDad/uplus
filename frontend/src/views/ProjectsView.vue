<template>
  <TechLayout title="Projects">
    <div class="projects-view">
      <div class="projects-header">
        <h1 class="projects-title">Projects</h1>
        <button class="btn btn-primary" @click="showCreateForm = true">
          <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
            <line x1="12" y1="5" x2="12" y2="19"></line>
            <line x1="5" y1="12" x2="19" y2="12"></line>
          </svg>
          Create Project
        </button>
      </div>
      
      <div class="projects-filters">
        <div class="search-container">
          <input 
            type="text" 
            class="search-input" 
            placeholder="Search projects..." 
            v-model="searchQuery"
          />
          <svg class="search-icon" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
            <circle cx="11" cy="11" r="8"></circle>
            <line x1="21" y1="21" x2="16.65" y2="16.65"></line>
          </svg>
        </div>
        
        <div class="filter-container">
          <select class="filter-select" v-model="statusFilter">
            <option value="ALL">All Statuses</option>
            <option value="ACTIVE">Active</option>
            <option value="PENDING">Pending</option>
            <option value="COMPLETED">Completed</option>
            <option value="ARCHIVED">Archived</option>
          </select>
        </div>
      </div>
      
      <div class="projects-content">
        <div v-if="loading" class="loading-container">
          <TechLoader message="Loading projects" />
        </div>
        
        <div v-else-if="filteredProjects.length === 0" class="empty-state">
          <div class="empty-icon">
            <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
              <path d="M22 19a2 2 0 0 1-2 2H4a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h5l2 3h9a2 2 0 0 1 2 2z"></path>
            </svg>
          </div>
          <h3>{{ searchQuery || statusFilter !== 'ALL' ? 'No matching projects found' : 'No Projects Yet' }}</h3>
          <p>{{ searchQuery || statusFilter !== 'ALL' ? 'Try adjusting your search or filters' : 'Create your first project to get started' }}</p>
          <button v-if="!searchQuery && statusFilter === 'ALL'" class="btn btn-primary" @click="showCreateForm = true">Create Project</button>
          <button v-else class="btn btn-outline-secondary" @click="resetFilters">Reset Filters</button>
        </div>
        
        <div v-else class="projects-grid">
          <ProjectCard 
            v-for="project in filteredProjects" 
            :key="project.id" 
            :project="project"
            @view-project="viewProject"
            @start-session="startSession"
          />
        </div>
      </div>
    </div>
    
    <!-- Create Project Modal -->
    <div v-if="showCreateForm" class="modal-overlay" @click.self="showCreateForm = false">
      <div class="modal-container">
        <div class="modal-header">
          <h2 class="modal-title">Create New Project</h2>
          <button class="modal-close" @click="showCreateForm = false">
            <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
              <line x1="18" y1="6" x2="6" y2="18"></line>
              <line x1="6" y1="6" x2="18" y2="18"></line>
            </svg>
          </button>
        </div>
        <div class="modal-body">
          <ProjectForm 
            :loading="creatingProject" 
            @submit="createProject" 
            @cancel="showCreateForm = false" 
          />
        </div>
      </div>
    </div>
  </TechLayout>
</template>

<script>
import { ref, computed, onMounted, watch } from 'vue';
import { useRouter } from 'vue-router';
import { useProjectStore } from '@/store/projectStore';
import { useSessionStore } from '@/store/sessionStore';
import { useUiStore } from '@/store/uiStore';
import TechLayout from '@/components/common/TechLayout.vue';
import TechLoader from '@/components/common/TechLoader.vue';
import ProjectCard from '@/components/projects/ProjectCard.vue';
import ProjectForm from '@/components/projects/ProjectForm.vue';

export default {
  name: 'ProjectsView',
  components: {
    TechLayout,
    TechLoader,
    ProjectCard,
    ProjectForm
  },
  setup() {
    const router = useRouter();
    const projectStore = useProjectStore();
    const sessionStore = useSessionStore();
    const uiStore = useUiStore();
    
    const loading = ref(true);
    const showCreateForm = ref(false);
    const creatingProject = ref(false);
    const searchQuery = ref('');
    const statusFilter = ref('ALL');
    
    // Computed properties
    const filteredProjects = computed(() => {
      let filtered = projectStore.projects;
      
      // Apply search filter
      if (searchQuery.value) {
        const query = searchQuery.value.toLowerCase();
        filtered = filtered.filter(project => 
          project.name.toLowerCase().includes(query) || 
          (project.description && project.description.toLowerCase().includes(query))
        );
      }
      
      // Apply status filter
      if (statusFilter.value !== 'ALL') {
        filtered = filtered.filter(project => project.status === statusFilter.value);
      }
      
      return filtered;
    });
    
    // Methods
    const viewProject = (project) => {
      projectStore.setCurrentProject(project);
      router.push(`/projects/${project.id}`);
    };
    
    const startSession = async (project) => {
      try {
        loading.value = true;
        
        // Create a new session for the project
        const sessionData = {
          project_id: project.id
        };
        
        const newSession = await sessionStore.createSession(sessionData);
        
        // Navigate to AI-PM view
        router.push('/ai-pm');
        
        uiStore.addNotification({
          type: 'success',
          title: 'Session Created',
          message: `New session started for project "${project.name}"`
        });
      } catch (error) {
        uiStore.addNotification({
          type: 'error',
          title: 'Error',
          message: error.message || 'Failed to create session'
        });
      } finally {
        loading.value = false;
      }
    };
    
    const createProject = async (projectData) => {
      creatingProject.value = true;
      
      try {
        const newProject = await projectStore.createProject(projectData);
        
        showCreateForm.value = false;
        
        uiStore.addNotification({
          type: 'success',
          title: 'Project Created',
          message: `Project "${newProject.name}" has been created successfully`
        });
      } catch (error) {
        uiStore.addNotification({
          type: 'error',
          title: 'Error',
          message: error.message || 'Failed to create project'
        });
      } finally {
        creatingProject.value = false;
      }
    };
    
    const resetFilters = () => {
      searchQuery.value = '';
      statusFilter.value = 'ALL';
    };
    
    // Fetch projects on component mount
    onMounted(async () => {
      try {
        await projectStore.fetchProjects();
      } catch (error) {
        uiStore.addNotification({
          type: 'error',
          title: 'Error',
          message: error.message || 'Failed to fetch projects'
        });
      } finally {
        loading.value = false;
      }
    });
    
    // Watch for store changes
    watch(() => projectStore.projects, () => {
      loading.value = false;
    });
    
    return {
      loading,
      showCreateForm,
      creatingProject,
      searchQuery,
      statusFilter,
      filteredProjects,
      viewProject,
      startSession,
      createProject,
      resetFilters
    };
  }
};
</script>

<style scoped>
.projects-view {
  display: flex;
  flex-direction: column;
  gap: 1.5rem;
}

.projects-header {
  display: flex;
  align-items: center;
  justify-content: space-between;
}

.projects-title {
  font-size: 2rem;
  font-weight: 700;
  margin: 0;
  color: var(--gray-900);
}

.projects-header .btn svg {
  width: 18px;
  height: 18px;
  margin-right: 0.5rem;
}

.projects-filters {
  display: flex;
  gap: 1rem;
}

.search-container {
  position: relative;
  flex: 1;
}

.search-input {
  width: 100%;
  padding: 0.75rem 1rem 0.75rem 2.5rem;
  font-size: 1rem;
  color: var(--gray-800);
  background-color: var(--white);
  border: 1px solid var(--gray-300);
  border-radius: var(--border-radius-md);
  transition: all var(--transition-normal) var(--transition-timing);
}

.search-input:focus {
  border-color: var(--primary);
  box-shadow: 0 0 0 3px rgba(58, 134, 255, 0.2);
  outline: none;
}

.search-icon {
  position: absolute;
  top: 50%;
  left: 0.75rem;
  transform: translateY(-50%);
  width: 18px;
  height: 18px;
  color: var(--gray-500);
}

.filter-container {
  width: 200px;
}

.filter-select {
  width: 100%;
  padding: 0.75rem 1rem;
  font-size: 1rem;
  color: var(--gray-800);
  background-color: var(--white);
  border: 1px solid var(--gray-300);
  border-radius: var(--border-radius-md);
  transition: all var(--transition-normal) var(--transition-timing);
  appearance: none;
  background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24' fill='none' stroke='%236c757d' stroke-width='2' stroke-linecap='round' stroke-linejoin='round'%3E%3Cpolyline points='6 9 12 15 18 9'%3E%3C/polyline%3E%3C/svg%3E");
  background-repeat: no-repeat;
  background-position: right 0.75rem center;
  background-size: 16px;
}

.filter-select:focus {
  border-color: var(--primary);
  box-shadow: 0 0 0 3px rgba(58, 134, 255, 0.2);
  outline: none;
}

.projects-content {
  min-height: 400px;
}

.loading-container {
  display: flex;
  align-items: center;
  justify-content: center;
  height: 400px;
}

.empty-state {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  padding: 3rem;
  background-color: var(--white);
  border-radius: var(--border-radius-lg);
  box-shadow: var(--shadow-md);
  text-align: center;
}

.empty-icon {
  display: flex;
  align-items: center;
  justify-content: center;
  width: 60px;
  height: 60px;
  margin-bottom: 1rem;
  background-color: var(--gray-200);
  color: var(--gray-600);
  border-radius: var(--border-radius-circle);
}

.empty-icon svg {
  width: 30px;
  height: 30px;
}

.empty-state h3 {
  margin-bottom: 0.5rem;
  font-size: 1.25rem;
  color: var(--gray-800);
}

.empty-state p {
  margin-bottom: 1.5rem;
  color: var(--gray-600);
}

.projects-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 1.5rem;
}

/* Modal styles */
.modal-overlay {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(0, 0, 0, 0.5);
  backdrop-filter: blur(5px);
  display: flex;
  align-items: center;
  justify-content: center;
  z-index: var(--z-index-modal-backdrop);
}

.modal-container {
  width: 100%;
  max-width: 600px;
  background-color: var(--white);
  border-radius: var(--border-radius-lg);
  box-shadow: var(--shadow-xl);
  overflow: hidden;
  z-index: var(--z-index-modal);
  animation: modal-slide-in 0.3s ease-out forwards;
}

.modal-header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 1.5rem;
  border-bottom: 1px solid var(--gray-200);
}

.modal-title {
  margin: 0;
  font-size: 1.5rem;
  font-weight: 600;
  color: var(--gray-900);
}

.modal-close {
  display: flex;
  align-items: center;
  justify-content: center;
  width: 36px;
  height: 36px;
  background-color: var(--gray-100);
  color: var(--gray-700);
  border: none;
  border-radius: var(--border-radius-circle);
  cursor: pointer;
  transition: all var(--transition-normal) var(--transition-timing);
}

.modal-close:hover {
  background-color: var(--gray-200);
  color: var(--gray-900);
}

.modal-close svg {
  width: 20px;
  height: 20px;
}

.modal-body {
  padding: 1.5rem;
}

@keyframes modal-slide-in {
  from {
    transform: translateY(50px);
    opacity: 0;
  }
  to {
    transform: translateY(0);
    opacity: 1;
  }
}

/* Dark mode adjustments */
:global(.dark-mode) .projects-title {
  color: var(--white);
}

:global(.dark-mode) .search-input {
  color: var(--gray-200);
  background-color: var(--dark-blue);
  border-color: var(--gray-700);
}

:global(.dark-mode) .filter-select {
  color: var(--gray-200);
  background-color: var(--dark-blue);
  border-color: var(--gray-700);
  background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24' fill='none' stroke='%23adb5bd' stroke-width='2' stroke-linecap='round' stroke-linejoin='round'%3E%3Cpolyline points='6 9 12 15 18 9'%3E%3C/polyline%3E%3C/svg%3E");
}

:global(.dark-mode) .empty-state {
  background-color: var(--dark-blue);
}

:global(.dark-mode) .empty-icon {
  background-color: var(--gray-800);
  color: var(--gray-400);
}

:global(.dark-mode) .empty-state h3 {
  color: var(--white);
}

:global(.dark-mode) .empty-state p {
  color: var(--gray-400);
}

:global(.dark-mode) .modal-container {
  background-color: var(--dark-blue);
}

:global(.dark-mode) .modal-header {
  border-bottom: 1px solid var(--gray-800);
}

:global(.dark-mode) .modal-title {
  color: var(--white);
}

:global(.dark-mode) .modal-close {
  background-color: var(--gray-800);
  color: var(--gray-300);
}

:global(.dark-mode) .modal-close:hover {
  background-color: var(--gray-700);
  color: var(--white);
}

/* Responsive adjustments */
@media (max-width: 992px) {
  .projects-grid {
    grid-template-columns: repeat(2, 1fr);
  }
}

@media (max-width: 768px) {
  .projects-header {
    flex-direction: column;
    align-items: flex-start;
    gap: 1rem;
  }
  
  .projects-filters {
    flex-direction: column;
    width: 100%;
  }
  
  .filter-container {
    width: 100%;
  }
  
  .projects-grid {
    grid-template-columns: 1fr;
  }
  
  .modal-container {
    width: 90%;
  }
}
</style>