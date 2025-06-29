<template>
  <TechLayout title="AI Product Manager">
    <div class="ai-pm-view">
      <div class="ai-pm-header">
        <h1 class="ai-pm-title">AI Product Manager</h1>
        <p class="ai-pm-subtitle">Transform your ideas into precise requirements through intelligent conversation</p>
      </div>
      
      <div class="ai-pm-content">
        <div class="project-selector" v-if="!currentSession">
          <div class="selector-header">
            <h2 class="selector-title">Select a Project</h2>
            <button class="btn btn-primary" @click="showCreateForm = true">
              <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                <line x1="12" y1="5" x2="12" y2="19"></line>
                <line x1="5" y1="12" x2="19" y2="12"></line>
              </svg>
              New Project
            </button>
          </div>
          
          <div v-if="loading" class="loading-container">
            <TechLoader message="Loading projects" />
          </div>
          
          <div v-else-if="projects.length === 0" class="empty-state">
            <div class="empty-icon">
              <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                <path d="M22 19a2 2 0 0 1-2 2H4a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h5l2 3h9a2 2 0 0 1 2 2z"></path>
              </svg>
            </div>
            <h3>No Projects Yet</h3>
            <p>Create your first project to start a conversation with AI-PM</p>
            <button class="btn btn-primary" @click="showCreateForm = true">Create Project</button>
          </div>
          
          <div v-else class="project-list">
            <div 
              v-for="project in projects" 
              :key="project.id" 
              class="project-item"
              @click="selectProject(project)"
            >
              <div class="project-item-content">
                <h3 class="project-item-title">{{ project.name }}</h3>
                <p class="project-item-description">{{ truncateDescription(project.description) }}</p>
                <div class="project-item-status" :class="`status-${project.status.toLowerCase()}`">
                  {{ project.status }}
                </div>
              </div>
              <div class="project-item-action">
                <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                  <polyline points="9 18 15 12 9 6"></polyline>
                </svg>
              </div>
            </div>
          </div>
        </div>
        
        <div class="chat-container" v-else>
          <div class="chat-header-bar">
            <div class="selected-project">
              <div class="project-icon">
                <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                  <path d="M22 19a2 2 0 0 1-2 2H4a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h5l2 3h9a2 2 0 0 1 2 2z"></path>
                </svg>
              </div>
              <div class="project-info">
                <h3 class="project-name">{{ currentProject.name }}</h3>
                <div class="project-status" :class="`status-${currentProject.status.toLowerCase()}`">
                  {{ currentProject.status }}
                </div>
              </div>
            </div>
            <button class="btn btn-outline-secondary" @click="endSession">
              End Session
            </button>
          </div>
          
          <ChatInterface @create-session="createSession" @rsd-generated="handleRsdGenerated" />
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
    
    <!-- RSD Generated Modal -->
    <div v-if="showRsdModal" class="modal-overlay" @click.self="showRsdModal = false">
      <div class="modal-container modal-lg">
        <div class="modal-header">
          <h2 class="modal-title">Requirements Specification Document</h2>
          <button class="modal-close" @click="showRsdModal = false">
            <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
              <line x1="18" y1="6" x2="6" y2="18"></line>
              <line x1="6" y1="6" x2="18" y2="18"></line>
            </svg>
          </button>
        </div>
        <div class="modal-body">
          <div class="rsd-content">
            <div class="rsd-section">
              <h3 class="rsd-section-title">Functional Requirements</h3>
              <div class="rsd-subsection">
                <h4 class="rsd-subsection-title">User Stories</h4>
                <ul class="rsd-list">
                  <li v-for="(story, index) in generatedRsd.functional_requirements?.user_stories" :key="`story-${index}`">
                    {{ story }}
                  </li>
                </ul>
              </div>
              <div class="rsd-subsection">
                <h4 class="rsd-subsection-title">Use Cases</h4>
                <ul class="rsd-list">
                  <li v-for="(useCase, index) in generatedRsd.functional_requirements?.use_cases" :key="`usecase-${index}`">
                    {{ useCase }}
                  </li>
                </ul>
              </div>
              <div class="rsd-subsection">
                <h4 class="rsd-subsection-title">Business Rules</h4>
                <ul class="rsd-list">
                  <li v-for="(rule, index) in generatedRsd.functional_requirements?.business_rules" :key="`rule-${index}`">
                    {{ rule }}
                  </li>
                </ul>
              </div>
            </div>
            
            <div class="rsd-section">
              <h3 class="rsd-section-title">Non-Functional Requirements</h3>
              <div class="rsd-subsection">
                <h4 class="rsd-subsection-title">Performance</h4>
                <ul class="rsd-list">
                  <li v-for="(item, index) in generatedRsd.non_functional_requirements?.performance" :key="`perf-${index}`">
                    {{ item }}
                  </li>
                </ul>
              </div>
              <div class="rsd-subsection">
                <h4 class="rsd-subsection-title">Security</h4>
                <ul class="rsd-list">
                  <li v-for="(item, index) in generatedRsd.non_functional_requirements?.security" :key="`sec-${index}`">
                    {{ item }}
                  </li>
                </ul>
              </div>
              <div class="rsd-subsection">
                <h4 class="rsd-subsection-title">Scalability</h4>
                <ul class="rsd-list">
                  <li v-for="(item, index) in generatedRsd.non_functional_requirements?.scalability" :key="`scale-${index}`">
                    {{ item }}
                  </li>
                </ul>
              </div>
            </div>
            
            <div class="rsd-section">
              <h3 class="rsd-section-title">Constraints</h3>
              <div class="rsd-subsection">
                <h4 class="rsd-subsection-title">Technical</h4>
                <ul class="rsd-list">
                  <li v-for="(item, index) in generatedRsd.constraints?.technical" :key="`tech-${index}`">
                    {{ item }}
                  </li>
                </ul>
              </div>
              <div class="rsd-subsection">
                <h4 class="rsd-subsection-title">Business</h4>
                <ul class="rsd-list">
                  <li v-for="(item, index) in generatedRsd.constraints?.business" :key="`bus-${index}`">
                    {{ item }}
                  </li>
                </ul>
              </div>
              <div class="rsd-subsection">
                <h4 class="rsd-subsection-title">Regulatory</h4>
                <ul class="rsd-list">
                  <li v-for="(item, index) in generatedRsd.constraints?.regulatory" :key="`reg-${index}`">
                    {{ item }}
                  </li>
                </ul>
              </div>
            </div>
            
            <div class="rsd-section">
              <h3 class="rsd-section-title">Success Criteria</h3>
              <div class="rsd-subsection">
                <h4 class="rsd-subsection-title">Metrics</h4>
                <ul class="rsd-list">
                  <li v-for="(item, index) in generatedRsd.success_criteria?.metrics" :key="`metric-${index}`">
                    {{ item }}
                  </li>
                </ul>
              </div>
              <div class="rsd-subsection">
                <h4 class="rsd-subsection-title">Acceptance Tests</h4>
                <ul class="rsd-list">
                  <li v-for="(item, index) in generatedRsd.success_criteria?.acceptance_tests" :key="`test-${index}`">
                    {{ item }}
                  </li>
                </ul>
              </div>
            </div>
          </div>
          
          <div class="rsd-actions">
            <button class="btn btn-primary" @click="downloadRsd">
              <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                <path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"></path>
                <polyline points="7 10 12 15 17 10"></polyline>
                <line x1="12" y1="15" x2="12" y2="3"></line>
              </svg>
              Download RSD
            </button>
            <button class="btn btn-secondary" @click="proceedToBitcup">
              <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                <polyline points="16 18 22 12 16 6"></polyline>
                <polyline points="8 6 2 12 8 18"></polyline>
              </svg>
              Proceed to BITCUP
            </button>
          </div>
        </div>
      </div>
    </div>
  </TechLayout>
</template>

<script>
import { ref, computed, onMounted } from 'vue';
import { useRouter } from 'vue-router';
import { useProjectStore } from '@/store/projectStore';
import { useSessionStore } from '@/store/sessionStore';
import { useUiStore } from '@/store/uiStore';
import TechLayout from '@/components/common/TechLayout.vue';
import TechLoader from '@/components/common/TechLoader.vue';
import ChatInterface from '@/components/ai-pm/ChatInterface.vue';
import ProjectForm from '@/components/projects/ProjectForm.vue';

export default {
  name: 'AiPmView',
  components: {
    TechLayout,
    TechLoader,
    ChatInterface,
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
    const showRsdModal = ref(false);
    const generatedRsd = ref({});
    
    // Computed properties
    const projects = computed(() => projectStore.projects);
    const currentProject = computed(() => projectStore.currentProject);
    const currentSession = computed(() => sessionStore.currentSession);
    
    // Methods
    const truncateDescription = (description) => {
      if (!description) return 'No description provided';
      return description.length > 100 ? description.substring(0, 100) + '...' : description;
    };
    
    const selectProject = async (project) => {
      try {
        loading.value = true;
        
        // Set current project
        projectStore.setCurrentProject(project);
        
        // Create a new session for the project
        const sessionData = {
          project_id: project.id
        };
        
        await sessionStore.createSession(sessionData);
        
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
        
        // Select the newly created project
        await selectProject(newProject);
        
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
    
    const createSession = async () => {
      if (!currentProject.value) {
        uiStore.addNotification({
          type: 'warning',
          title: 'No Project Selected',
          message: 'Please select a project first'
        });
        return;
      }
      
      try {
        loading.value = true;
        
        // Create a new session for the current project
        const sessionData = {
          project_id: currentProject.value.id
        };
        
        await sessionStore.createSession(sessionData);
        
        uiStore.addNotification({
          type: 'success',
          title: 'Session Created',
          message: `New session started for project "${currentProject.value.name}"`
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
    
    const endSession = () => {
      sessionStore.clearCurrentSession();
    };
    
    const handleRsdGenerated = (rsd) => {
      generatedRsd.value = rsd;
      showRsdModal.value = true;
    };
    
    const downloadRsd = () => {
      // Create a JSON blob and download it
      const rsdJson = JSON.stringify(generatedRsd.value, null, 2);
      const blob = new Blob([rsdJson], { type: 'application/json' });
      const url = URL.createObjectURL(blob);
      
      const a = document.createElement('a');
      a.href = url;
      a.download = `rsd_${currentProject.value.name.replace(/\s+/g, '_').toLowerCase()}.json`;
      document.body.appendChild(a);
      a.click();
      document.body.removeChild(a);
      URL.revokeObjectURL(url);
    };
    
    const proceedToBitcup = () => {
      showRsdModal.value = false;
      router.push('/bitcup');
    };
    
    // Fetch data on component mount
    onMounted(async () => {
      try {
        await projectStore.fetchProjects();
        
        // Check if there's already a current session
        if (sessionStore.currentSession) {
          // Make sure the current project is set
          const sessionProject = projects.value.find(p => p.id === sessionStore.currentSession.project_id);
          if (sessionProject) {
            projectStore.setCurrentProject(sessionProject);
          }
        }
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
    
    return {
      loading,
      showCreateForm,
      creatingProject,
      showRsdModal,
      generatedRsd,
      projects,
      currentProject,
      currentSession,
      truncateDescription,
      selectProject,
      createProject,
      createSession,
      endSession,
      handleRsdGenerated,
      downloadRsd,
      proceedToBitcup
    };
  }
};
</script>

<style scoped>
.ai-pm-view {
  display: flex;
  flex-direction: column;
  gap: 1.5rem;
}

.ai-pm-header {
  text-align: center;
  margin-bottom: 1rem;
}

.ai-pm-title {
  font-size: 2.5rem;
  font-weight: 700;
  margin-bottom: 0.5rem;
  background: var(--gradient-primary);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  animation: text-shine 3s linear infinite;
}

.ai-pm-subtitle {
  font-size: 1.25rem;
  color: var(--gray-600);
}

.ai-pm-content {
  flex: 1;
  display: flex;
  flex-direction: column;
  min-height: 600px;
}

.project-selector {
  display: flex;
  flex-direction: column;
  gap: 1.5rem;
  background-color: var(--white);
  border-radius: var(--border-radius-lg);
  box-shadow: var(--shadow-md);
  padding: 1.5rem;
}

.selector-header {
  display: flex;
  align-items: center;
  justify-content: space-between;
}

.selector-title {
  font-size: 1.5rem;
  font-weight: 600;
  margin: 0;
  color: var(--gray-900);
}

.selector-header .btn svg {
  width: 18px;
  height: 18px;
  margin-right: 0.5rem;
}

.loading-container {
  display: flex;
  align-items: center;
  justify-content: center;
  height: 300px;
}

.empty-state {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  padding: 3rem;
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

.project-list {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 1rem;
}

.project-item {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 1.5rem;
  background-color: var(--gray-100);
  border-radius: var(--border-radius-lg);
  cursor: pointer;
  transition: all var(--transition-normal) var(--transition-timing);
}

.project-item:hover {
  background-color: var(--gray-200);
  transform: translateY(-3px);
}

.project-item-content {
  flex: 1;
}

.project-item-title {
  margin: 0 0 0.5rem 0;
  font-size: 1.25rem;
  font-weight: 600;
  color: var(--gray-900);
}

.project-item-description {
  margin: 0 0 0.75rem 0;
  font-size: 0.875rem;
  color: var(--gray-700);
}

.project-item-status {
  display: inline-block;
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

.project-item-action {
  display: flex;
  align-items: center;
  justify-content: center;
  width: 40px;
  height: 40px;
  color: var(--gray-600);
}

.project-item-action svg {
  width: 24px;
  height: 24px;
}

.chat-container {
  display: flex;
  flex-direction: column;
  height: 600px;
  background-color: var(--white);
  border-radius: var(--border-radius-lg);
  box-shadow: var(--shadow-md);
  overflow: hidden;
}

.chat-header-bar {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 1rem 1.5rem;
  background-color: var(--gray-100);
  border-bottom: 1px solid var(--gray-200);
}

.selected-project {
  display: flex;
  align-items: center;
}

.project-icon {
  display: flex;
  align-items: center;
  justify-content: center;
  width: 40px;
  height: 40px;
  margin-right: 1rem;
  background-color: var(--primary);
  color: var(--white);
  border-radius: var(--border-radius-circle);
}

.project-icon svg {
  width: 20px;
  height: 20px;
}

.project-info {
  display: flex;
  flex-direction: column;
}

.project-name {
  margin: 0;
  font-size: 1.125rem;
  font-weight: 600;
  color: var(--gray-900);
}

.project-status {
  display: inline-block;
  padding: 0.125rem 0.5rem;
  font-size: 0.75rem;
  font-weight: 600;
  text-transform: uppercase;
  border-radius: var(--border-radius-pill);
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
  max-height: 90vh;
  background-color: var(--white);
  border-radius: var(--border-radius-lg);
  box-shadow: var(--shadow-xl);
  overflow: hidden;
  z-index: var(--z-index-modal);
  animation: modal-slide-in 0.3s ease-out forwards;
  display: flex;
  flex-direction: column;
}

.modal-lg {
  max-width: 800px;
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
  overflow-y: auto;
  flex: 1;
}

/* RSD styles */
.rsd-content {
  display: flex;
  flex-direction: column;
  gap: 2rem;
}

.rsd-section {
  display: flex;
  flex-direction: column;
  gap: 1rem;
}

.rsd-section-title {
  margin: 0;
  font-size: 1.5rem;
  font-weight: 600;
  color: var(--gray-900);
  padding-bottom: 0.5rem;
  border-bottom: 2px solid var(--primary);
}

.rsd-subsection {
  margin-left: 1rem;
}

.rsd-subsection-title {
  margin: 0 0 0.75rem 0;
  font-size: 1.25rem;
  font-weight: 500;
  color: var(--gray-800);
}

.rsd-list {
  margin: 0;
  padding-left: 1.5rem;
}

.rsd-list li {
  margin-bottom: 0.5rem;
  color: var(--gray-700);
}

.rsd-actions {
  display: flex;
  justify-content: flex-end;
  gap: 1rem;
  margin-top: 2rem;
  padding-top: 1.5rem;
  border-top: 1px solid var(--gray-200);
}

.rsd-actions .btn svg {
  width: 18px;
  height: 18px;
  margin-right: 0.5rem;
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
:global(.dark-mode) .ai-pm-subtitle {
  color: var(--gray-400);
}

:global(.dark-mode) .project-selector {
  background-color: var(--dark-blue);
}

:global(.dark-mode) .selector-title {
  color: var(--white);
}

:global(.dark-mode) .project-item {
  background-color: var(--dark-purple);
}

:global(.dark-mode) .project-item:hover {
  background-color: var(--gray-800);
}

:global(.dark-mode) .project-item-title {
  color: var(--white);
}

:global(.dark-mode) .project-item-description {
  color: var(--gray-300);
}

:global(.dark-mode) .project-item-action {
  color: var(--gray-400);
}

:global(.dark-mode) .chat-container {
  background-color: var(--dark-blue);
}

:global(.dark-mode) .chat-header-bar {
  background-color: var(--dark-purple);
  border-bottom: 1px solid var(--gray-800);
}

:global(.dark-mode) .project-name {
  color: var(--white);
}

:global(.dark-mode) .empty-state {
  background-color: transparent;
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

:global(.dark-mode) .rsd-section-title {
  color: var(--white);
}

:global(.dark-mode) .rsd-subsection-title {
  color: var(--gray-200);
}

:global(.dark-mode) .rsd-list li {
  color: var(--gray-300);
}

:global(.dark-mode) .rsd-actions {
  border-top: 1px solid var(--gray-800);
}

/* Responsive adjustments */
@media (max-width: 992px) {
  .project-list {
    grid-template-columns: 1fr;
  }
  
  .chat-container {
    height: 500px;
  }
}

@media (max-width: 768px) {
  .ai-pm-title {
    font-size: 2rem;
  }
  
  .ai-pm-subtitle {
    font-size: 1rem;
  }
  
  .selector-header {
    flex-direction: column;
    align-items: flex-start;
    gap: 1rem;
  }
  
  .chat-header-bar {
    flex-direction: column;
    align-items: flex-start;
    gap: 1rem;
  }
  
  .modal-container {
    width: 90%;
  }
}
</style>