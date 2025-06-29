<template>
  <TechLayout title="AI Product Manager">
    <div class="ai-pm-view">
      <!-- Revolutionary AI-PM Header with Dynamic Intelligence Indicators -->
      <div class="ai-pm-hero">
        <div class="hero-background">
          <div class="neural-network">
            <div class="neural-node" v-for="i in 12" :key="i" :style="{ animationDelay: `${i * 0.2}s` }"></div>
          </div>
          <div class="intelligence-waves"></div>
        </div>
        
        <div class="hero-content">
          <div class="ai-avatar">
            <div class="avatar-core">
              <div class="avatar-pulse"></div>
              <div class="avatar-brain">
                <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                  <path d="M9.5 2A2.5 2.5 0 0 1 12 4.5v15a2.5 2.5 0 0 1-4.96.44 2.5 2.5 0 0 1-2.96-3.08 3 3 0 0 1-.34-5.58 2.5 2.5 0 0 1 1.32-4.24 2.5 2.5 0 0 1 1.98-3A2.5 2.5 0 0 1 9.5 2Z"/>
                  <path d="M14.5 2A2.5 2.5 0 0 0 12 4.5v15a2.5 2.5 0 0 0 4.96.44 2.5 2.5 0 0 0 2.96-3.08 3 3 0 0 0 .34-5.58 2.5 2.5 0 0 0-1.32-4.24 2.5 2.5 0 0 0-1.98-3A2.5 2.5 0 0 0 14.5 2Z"/>
                </svg>
              </div>
            </div>
            <div class="avatar-status" :class="{ active: currentSession }">
              <div class="status-indicator"></div>
              <span>{{ currentSession ? 'Active Session' : 'Ready to Assist' }}</span>
            </div>
          </div>
          
          <div class="hero-text">
            <h1 class="hero-title">
              <span class="title-line">AI Product Manager</span>
              <span class="title-subtitle">Socratic Intelligence Engine</span>
            </h1>
            <p class="hero-description">
              Transform vague human desires into precise, executable specifications through 
              <span class="highlight">revolutionary conversational intelligence</span>
            </p>
            
            <div class="intelligence-metrics" v-if="currentSession">
              <div class="metric">
                <div class="metric-value">{{ sessionProgress }}%</div>
                <div class="metric-label">Requirement Clarity</div>
              </div>
              <div class="metric">
                <div class="metric-value">{{ messageCount }}</div>
                <div class="metric-label">Interactions</div>
              </div>
              <div class="metric">
                <div class="metric-value">{{ intelligenceLevel }}</div>
                <div class="metric-label">AI Confidence</div>
              </div>
            </div>
          </div>
        </div>
      </div>
      
      <div class="ai-pm-content">
        <!-- Revolutionary Project Selector with Holographic Design -->
        <div class="project-selector" v-if="!currentSession">
          <div class="selector-container">
            <div class="selector-header">
              <div class="header-content">
                <h2 class="selector-title">
                  <span class="title-icon">
                    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                      <path d="M22 19a2 2 0 0 1-2 2H4a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h5l2 3h9a2 2 0 0 1 2 2z"/>
                    </svg>
                  </span>
                  Initialize AI-PM Session
                </h2>
                <p class="selector-subtitle">Select a project to begin intelligent requirement gathering</p>
              </div>
              <button class="create-project-btn" @click="showCreateForm = true">
                <div class="btn-background"></div>
                <div class="btn-content">
                  <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                    <circle cx="12" cy="12" r="10"/>
                    <line x1="12" y1="8" x2="12" y2="16"/>
                    <line x1="8" y1="12" x2="16" y2="12"/>
                  </svg>
                  <span>Create Project</span>
                </div>
                <div class="btn-glow"></div>
              </button>
            </div>
          
            <div v-if="loading" class="loading-container">
              <div class="ai-loading">
                <div class="loading-brain">
                  <div class="brain-pulse"></div>
                  <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                    <path d="M9.5 2A2.5 2.5 0 0 1 12 4.5v15a2.5 2.5 0 0 1-4.96.44 2.5 2.5 0 0 1-2.96-3.08 3 3 0 0 1-.34-5.58 2.5 2.5 0 0 1 1.32-4.24 2.5 2.5 0 0 1 1.98-3A2.5 2.5 0 0 1 9.5 2Z"/>
                    <path d="M14.5 2A2.5 2.5 0 0 0 12 4.5v15a2.5 2.5 0 0 0 4.96.44 2.5 2.5 0 0 0 2.96-3.08 3 3 0 0 0 .34-5.58 2.5 2.5 0 0 0-1.32-4.24 2.5 2.5 0 0 0-1.98-3A2.5 2.5 0 0 0 14.5 2Z"/>
                  </svg>
                </div>
                <div class="loading-text">
                  <span>Initializing AI Intelligence</span>
                  <div class="loading-dots">
                    <span></span><span></span><span></span>
                  </div>
                </div>
              </div>
            </div>
            
            <div v-else-if="projects.length === 0" class="empty-state">
              <div class="empty-background">
                <div class="empty-particles"></div>
              </div>
              <div class="empty-content">
                <div class="empty-icon">
                  <div class="icon-glow"></div>
                  <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                    <path d="M22 19a2 2 0 0 1-2 2H4a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h5l2 3h9a2 2 0 0 1 2 2z"/>
                    <path d="M12 11v6"/>
                    <path d="M12 7h.01"/>
                  </svg>
                </div>
                <h3 class="empty-title">Ready to Begin Your Journey</h3>
                <p class="empty-description">
                  Create your first project and experience the power of AI-driven requirement gathering.
                  Our Socratic Intelligence Engine will transform your ideas into precise specifications.
                </p>
                <button class="empty-action-btn" @click="showCreateForm = true">
                  <div class="btn-shimmer"></div>
                  <span>Create Your First Project</span>
                  <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                    <path d="M5 12h14"/>
                    <path d="M12 5l7 7-7 7"/>
                  </svg>
                </button>
              </div>
            </div>
            
            <div v-else class="project-grid">
              <div 
                v-for="project in projects" 
                :key="project.id" 
                class="project-card"
                @click="selectProject(project)"
                v-motion
                :initial="{ opacity: 0, y: 50 }"
                :enter="{ opacity: 1, y: 0, transition: { delay: projects.indexOf(project) * 100 } }"
              >
                <div class="card-background">
                  <div class="card-gradient"></div>
                  <div class="card-pattern"></div>
                </div>
                
                <div class="card-content">
                  <div class="card-header">
                    <div class="project-icon">
                      <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                        <path d="M22 19a2 2 0 0 1-2 2H4a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h5l2 3h9a2 2 0 0 1 2 2z"/>
                      </svg>
                    </div>
                    <div class="project-status" :class="`status-${project.status.toLowerCase()}`">
                      <div class="status-dot"></div>
                      <span>{{ project.status }}</span>
                    </div>
                  </div>
                  
                  <div class="card-body">
                    <h3 class="project-title">{{ project.name }}</h3>
                    <p class="project-description">{{ truncateDescription(project.description) }}</p>
                  </div>
                  
                  <div class="card-footer">
                    <div class="project-meta">
                      <span class="meta-item">
                        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                          <circle cx="12" cy="12" r="3"/>
                          <path d="M12 1v6m0 6v6"/>
                        </svg>
                        AI-Ready
                      </span>
                    </div>
                    <div class="card-action">
                      <span>Start Session</span>
                      <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                        <path d="M5 12h14"/>
                        <path d="M12 5l7 7-7 7"/>
                      </svg>
                    </div>
                  </div>
                </div>
                
                <div class="card-hover-effect"></div>
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
    
    // AI Intelligence Metrics
    const sessionProgress = computed(() => {
      if (!currentSession.value) return 0;
      return Math.min(100, (currentSession.value.completeness_score || 0) * 100);
    });
    
    const messageCount = computed(() => {
      if (!currentSession.value?.dialogue_history) return 0;
      return currentSession.value.dialogue_history.length;
    });
    
    const intelligenceLevel = computed(() => {
      const progress = sessionProgress.value;
      if (progress >= 80) return 'Expert';
      if (progress >= 60) return 'Advanced';
      if (progress >= 40) return 'Intermediate';
      if (progress >= 20) return 'Learning';
      return 'Initializing';
    });
    
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
      sessionProgress,
      messageCount,
      intelligenceLevel,
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
/* Revolutionary AI-PM Interface Styling */
.ai-pm-view {
  min-height: 100vh;
  background: linear-gradient(135deg, #0a0a0a 0%, #1a1a2e 50%, #16213e 100%);
  position: relative;
  overflow: hidden;
}

/* AI-PM Hero Section with Neural Network Animation */
.ai-pm-hero {
  position: relative;
  padding: 4rem 0 6rem;
  margin-bottom: 3rem;
  overflow: hidden;
}

.hero-background {
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  z-index: 1;
}

.neural-network {
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  opacity: 0.3;
}

.neural-node {
  position: absolute;
  width: 4px;
  height: 4px;
  background: radial-gradient(circle, #3a86ff 0%, transparent 70%);
  border-radius: 50%;
  animation: neural-pulse 3s infinite ease-in-out;
}

.neural-node:nth-child(1) { top: 20%; left: 10%; }
.neural-node:nth-child(2) { top: 30%; left: 25%; }
.neural-node:nth-child(3) { top: 15%; left: 40%; }
.neural-node:nth-child(4) { top: 35%; left: 55%; }
.neural-node:nth-child(5) { top: 25%; left: 70%; }
.neural-node:nth-child(6) { top: 40%; left: 85%; }
.neural-node:nth-child(7) { top: 60%; left: 15%; }
.neural-node:nth-child(8) { top: 70%; left: 30%; }
.neural-node:nth-child(9) { top: 65%; left: 45%; }
.neural-node:nth-child(10) { top: 75%; left: 60%; }
.neural-node:nth-child(11) { top: 55%; left: 75%; }
.neural-node:nth-child(12) { top: 80%; left: 90%; }

@keyframes neural-pulse {
  0%, 100% { 
    opacity: 0.3; 
    transform: scale(1); 
    box-shadow: 0 0 0 0 rgba(58, 134, 255, 0.7);
  }
  50% { 
    opacity: 1; 
    transform: scale(1.5); 
    box-shadow: 0 0 0 10px rgba(58, 134, 255, 0);
  }
}

.intelligence-waves {
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: 
    radial-gradient(ellipse at 20% 30%, rgba(58, 134, 255, 0.1) 0%, transparent 50%),
    radial-gradient(ellipse at 80% 70%, rgba(131, 56, 236, 0.1) 0%, transparent 50%),
    radial-gradient(ellipse at 50% 50%, rgba(255, 0, 110, 0.05) 0%, transparent 50%);
  animation: intelligence-flow 8s infinite ease-in-out;
}

@keyframes intelligence-flow {
  0%, 100% { transform: translateX(0) translateY(0) scale(1); }
  33% { transform: translateX(20px) translateY(-10px) scale(1.1); }
  66% { transform: translateX(-15px) translateY(15px) scale(0.9); }
}

.hero-content {
  position: relative;
  z-index: 2;
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 4rem;
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 2rem;
}

/* AI Avatar with Sophisticated Animation */
.ai-avatar {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 1.5rem;
}

.avatar-core {
  position: relative;
  width: 120px;
  height: 120px;
  display: flex;
  align-items: center;
  justify-content: center;
}

.avatar-pulse {
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  border-radius: 50%;
  background: radial-gradient(circle, rgba(58, 134, 255, 0.2) 0%, transparent 70%);
  animation: avatar-pulse 2s infinite ease-in-out;
}

@keyframes avatar-pulse {
  0%, 100% { transform: scale(1); opacity: 0.7; }
  50% { transform: scale(1.2); opacity: 0.3; }
}

.avatar-brain {
  position: relative;
  z-index: 2;
  width: 80px;
  height: 80px;
  padding: 1.5rem;
  background: linear-gradient(135deg, rgba(58, 134, 255, 0.2) 0%, rgba(131, 56, 236, 0.2) 100%);
  border: 2px solid rgba(255, 255, 255, 0.1);
  border-radius: 50%;
  backdrop-filter: blur(20px);
  display: flex;
  align-items: center;
  justify-content: center;
  transition: all 0.3s ease;
}

.avatar-brain svg {
  width: 40px;
  height: 40px;
  stroke: #3a86ff;
  filter: drop-shadow(0 0 10px rgba(58, 134, 255, 0.5));
}

.avatar-status {
  display: flex;
  align-items: center;
  gap: 0.75rem;
  padding: 0.75rem 1.5rem;
  background: rgba(255, 255, 255, 0.05);
  border: 1px solid rgba(255, 255, 255, 0.1);
  border-radius: 50px;
  backdrop-filter: blur(10px);
  transition: all 0.3s ease;
}

.avatar-status.active {
  background: rgba(6, 214, 160, 0.1);
  border-color: rgba(6, 214, 160, 0.3);
}

.status-indicator {
  width: 8px;
  height: 8px;
  border-radius: 50%;
  background: #6c757d;
  transition: all 0.3s ease;
}

.avatar-status.active .status-indicator {
  background: #06d6a0;
  box-shadow: 0 0 10px rgba(6, 214, 160, 0.5);
  animation: status-pulse 2s infinite;
}

@keyframes status-pulse {
  0%, 100% { opacity: 1; }
  50% { opacity: 0.5; }
}

.avatar-status span {
  font-size: 0.875rem;
  font-weight: 600;
  color: var(--white);
  text-transform: uppercase;
  letter-spacing: 0.05em;
}

/* Hero Text with Premium Typography */
.hero-text {
  flex: 1;
  max-width: 600px;
}

.hero-title {
  margin-bottom: 2rem;
}

.title-line {
  display: block;
  font-size: 3.5rem;
  font-weight: 800;
  background: linear-gradient(135deg, #3a86ff 0%, #8338ec 100%);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
  line-height: 1.1;
  margin-bottom: 0.5rem;
}

.title-subtitle {
  display: block;
  font-size: 1.5rem;
  font-weight: 400;
  color: rgba(255, 255, 255, 0.7);
  font-style: italic;
}

.hero-description {
  font-size: 1.25rem;
  line-height: 1.6;
  color: rgba(255, 255, 255, 0.8);
  margin-bottom: 3rem;
}

.highlight {
  background: linear-gradient(135deg, #ff006e 0%, #ffbe0b 100%);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
  font-weight: 600;
}

/* Intelligence Metrics Display */
.intelligence-metrics {
  display: flex;
  gap: 2rem;
  padding: 2rem;
  background: rgba(255, 255, 255, 0.05);
  border: 1px solid rgba(255, 255, 255, 0.1);
  border-radius: 1rem;
  backdrop-filter: blur(20px);
}

.metric {
  text-align: center;
}

.metric-value {
  font-size: 2rem;
  font-weight: 700;
  color: var(--white);
  margin-bottom: 0.5rem;
  display: block;
}

.metric-label {
  font-size: 0.875rem;
  color: rgba(255, 255, 255, 0.6);
  text-transform: uppercase;
  letter-spacing: 0.1em;
}

/* Project Selector with Holographic Design */
.ai-pm-content {
  position: relative;
  z-index: 2;
  padding: 0 2rem 4rem;
}

.project-selector {
  max-width: 1200px;
  margin: 0 auto;
}

.selector-container {
  background: rgba(255, 255, 255, 0.03);
  border: 1px solid rgba(255, 255, 255, 0.1);
  border-radius: 2rem;
  backdrop-filter: blur(20px);
  overflow: hidden;
}

.selector-header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 3rem;
  border-bottom: 1px solid rgba(255, 255, 255, 0.1);
}

.header-content {
  flex: 1;
}

.selector-title {
  display: flex;
  align-items: center;
  gap: 1rem;
  font-size: 2rem;
  font-weight: 700;
  color: var(--white);
  margin-bottom: 0.75rem;
}

.title-icon {
  width: 32px;
  height: 32px;
  padding: 0.5rem;
  background: linear-gradient(135deg, rgba(58, 134, 255, 0.2) 0%, rgba(131, 56, 236, 0.2) 100%);
  border-radius: 0.5rem;
  display: flex;
  align-items: center;
  justify-content: center;
}

.title-icon svg {
  width: 20px;
  height: 20px;
  stroke: #3a86ff;
}

.selector-subtitle {
  font-size: 1.1rem;
  color: rgba(255, 255, 255, 0.7);
  margin: 0;
}

/* Premium Create Project Button */
.create-project-btn {
  position: relative;
  padding: 1rem 2rem;
  background: transparent;
  border: none;
  border-radius: 1rem;
  cursor: pointer;
  overflow: hidden;
  transition: all 0.3s ease;
}

.btn-background {
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: linear-gradient(135deg, rgba(58, 134, 255, 0.2) 0%, rgba(131, 56, 236, 0.2) 100%);
  border: 1px solid rgba(255, 255, 255, 0.2);
  border-radius: 1rem;
  backdrop-filter: blur(10px);
  transition: all 0.3s ease;
}

.btn-content {
  position: relative;
  z-index: 2;
  display: flex;
  align-items: center;
  gap: 0.75rem;
  color: var(--white);
  font-weight: 600;
}

.btn-content svg {
  width: 20px;
  height: 20px;
  stroke: currentColor;
}

.btn-glow {
  position: absolute;
  top: 0;
  left: -100%;
  width: 100%;
  height: 100%;
  background: linear-gradient(90deg, transparent, rgba(255, 255, 255, 0.2), transparent);
  transition: left 0.5s ease;
}

.create-project-btn:hover .btn-background {
  background: linear-gradient(135deg, rgba(58, 134, 255, 0.3) 0%, rgba(131, 56, 236, 0.3) 100%);
  border-color: rgba(255, 255, 255, 0.3);
}

.create-project-btn:hover .btn-glow {
  left: 100%;
}

.create-project-btn:hover {
  transform: translateY(-2px);
}

/* AI Loading Animation */
.loading-container {
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 6rem 2rem;
}

.ai-loading {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 2rem;
}

.loading-brain {
  position: relative;
  width: 80px;
  height: 80px;
  display: flex;
  align-items: center;
  justify-content: center;
}

.brain-pulse {
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  border-radius: 50%;
  background: radial-gradient(circle, rgba(58, 134, 255, 0.3) 0%, transparent 70%);
  animation: brain-pulse 1.5s infinite ease-in-out;
}

@keyframes brain-pulse {
  0%, 100% { transform: scale(1); opacity: 0.7; }
  50% { transform: scale(1.3); opacity: 0.3; }
}

.loading-brain svg {
  width: 40px;
  height: 40px;
  stroke: #3a86ff;
  filter: drop-shadow(0 0 10px rgba(58, 134, 255, 0.5));
  animation: brain-rotate 3s linear infinite;
}

@keyframes brain-rotate {
  from { transform: rotate(0deg); }
  to { transform: rotate(360deg); }
}

.loading-text {
  text-align: center;
  color: var(--white);
}

.loading-text span {
  font-size: 1.25rem;
  font-weight: 600;
  display: block;
  margin-bottom: 1rem;
}

.loading-dots {
  display: flex;
  gap: 0.5rem;
  justify-content: center;
}

.loading-dots span {
  width: 8px;
  height: 8px;
  background: #3a86ff;
  border-radius: 50%;
  animation: loading-dot 1.4s infinite ease-in-out;
}

.loading-dots span:nth-child(1) { animation-delay: -0.32s; }
.loading-dots span:nth-child(2) { animation-delay: -0.16s; }
.loading-dots span:nth-child(3) { animation-delay: 0s; }

@keyframes loading-dot {
  0%, 80%, 100% { transform: scale(0); }
  40% { transform: scale(1); }
}

/* Revolutionary Empty State */
.empty-state {
  position: relative;
  padding: 6rem 2rem;
  text-align: center;
  overflow: hidden;
}

.empty-background {
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  z-index: 1;
}

.empty-particles {
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background-image: 
    radial-gradient(circle at 25% 25%, rgba(58, 134, 255, 0.1) 0%, transparent 50%),
    radial-gradient(circle at 75% 75%, rgba(131, 56, 236, 0.1) 0%, transparent 50%);
  animation: particles-float 6s infinite ease-in-out;
}

@keyframes particles-float {
  0%, 100% { transform: translateY(0) rotate(0deg); }
  50% { transform: translateY(-20px) rotate(180deg); }
}

.empty-content {
  position: relative;
  z-index: 2;
  max-width: 500px;
  margin: 0 auto;
}

.empty-icon {
  position: relative;
  width: 120px;
  height: 120px;
  margin: 0 auto 2rem;
  display: flex;
  align-items: center;
  justify-content: center;
}

.icon-glow {
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  border-radius: 50%;
  background: radial-gradient(circle, rgba(58, 134, 255, 0.2) 0%, transparent 70%);
  animation: icon-glow 3s infinite ease-in-out;
}

@keyframes icon-glow {
  0%, 100% { transform: scale(1); opacity: 0.5; }
  50% { transform: scale(1.2); opacity: 0.8; }
}

.empty-icon svg {
  position: relative;
  z-index: 2;
  width: 60px;
  height: 60px;
  stroke: #3a86ff;
  filter: drop-shadow(0 0 20px rgba(58, 134, 255, 0.5));
}

.empty-title {
  font-size: 2rem;
  font-weight: 700;
  color: var(--white);
  margin-bottom: 1rem;
}

.empty-description {
  font-size: 1.1rem;
  line-height: 1.6;
  color: rgba(255, 255, 255, 0.7);
  margin-bottom: 3rem;
}

/* Premium Action Button */
.empty-action-btn {
  position: relative;
  display: inline-flex;
  align-items: center;
  gap: 1rem;
  padding: 1.25rem 2.5rem;
  background: linear-gradient(135deg, #3a86ff 0%, #8338ec 100%);
  border: none;
  border-radius: 1rem;
  color: var(--white);
  font-size: 1.1rem;
  font-weight: 600;
  cursor: pointer;
  overflow: hidden;
  transition: all 0.3s ease;
  box-shadow: 0 10px 30px rgba(58, 134, 255, 0.3);
}

.btn-shimmer {
  position: absolute;
  top: 0;
  left: -100%;
  width: 100%;
  height: 100%;
  background: linear-gradient(90deg, transparent, rgba(255, 255, 255, 0.3), transparent);
  transition: left 0.6s ease;
}

.empty-action-btn:hover .btn-shimmer {
  left: 100%;
}

.empty-action-btn:hover {
  transform: translateY(-3px);
  box-shadow: 0 15px 40px rgba(58, 134, 255, 0.4);
}

.empty-action-btn svg {
  width: 20px;
  height: 20px;
  stroke: currentColor;
}

/* Premium Project Grid */
.project-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(350px, 1fr));
  gap: 2rem;
  padding: 3rem;
}

.project-card {
  position: relative;
  height: 280px;
  border-radius: 1.5rem;
  overflow: hidden;
  cursor: pointer;
  transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
}

.project-card:hover {
  transform: translateY(-8px) scale(1.02);
}

.card-background {
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  z-index: 1;
}

.card-gradient {
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: linear-gradient(135deg, 
    rgba(255, 255, 255, 0.05) 0%, 
    rgba(255, 255, 255, 0.02) 100%);
  border: 1px solid rgba(255, 255, 255, 0.1);
  backdrop-filter: blur(20px);
  transition: all 0.4s ease;
}

.project-card:hover .card-gradient {
  background: linear-gradient(135deg, 
    rgba(255, 255, 255, 0.1) 0%, 
    rgba(255, 255, 255, 0.05) 100%);
  border-color: rgba(255, 255, 255, 0.2);
}

.card-pattern {
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background-image: 
    radial-gradient(circle at 20% 20%, rgba(58, 134, 255, 0.1) 0%, transparent 50%),
    radial-gradient(circle at 80% 80%, rgba(131, 56, 236, 0.1) 0%, transparent 50%);
  opacity: 0;
  transition: opacity 0.4s ease;
}

.project-card:hover .card-pattern {
  opacity: 1;
}

.card-content {
  position: relative;
  z-index: 2;
  padding: 2rem;
  height: 100%;
  display: flex;
  flex-direction: column;
  color: var(--white);
}

.card-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 1.5rem;
}

.project-icon {
  width: 48px;
  height: 48px;
  padding: 0.75rem;
  background: rgba(255, 255, 255, 0.1);
  border-radius: 0.75rem;
  display: flex;
  align-items: center;
  justify-content: center;
  transition: all 0.3s ease;
}

.project-icon svg {
  width: 24px;
  height: 24px;
  stroke: #3a86ff;
}

.project-card:hover .project-icon {
  background: rgba(255, 255, 255, 0.2);
  transform: scale(1.1);
}

.project-status {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  padding: 0.5rem 1rem;
  border-radius: 50px;
  font-size: 0.75rem;
  font-weight: 600;
  text-transform: uppercase;
  letter-spacing: 0.05em;
}

.status-dot {
  width: 6px;
  height: 6px;
  border-radius: 50%;
}

.project-status.status-active {
  background: rgba(6, 214, 160, 0.2);
  color: #06d6a0;
  border: 1px solid rgba(6, 214, 160, 0.3);
}

.project-status.status-active .status-dot {
  background: #06d6a0;
  box-shadow: 0 0 8px rgba(6, 214, 160, 0.5);
}

.project-status.status-planning {
  background: rgba(255, 190, 11, 0.2);
  color: #ffbe0b;
  border: 1px solid rgba(255, 190, 11, 0.3);
}

.project-status.status-planning .status-dot {
  background: #ffbe0b;
}

.card-body {
  flex: 1;
  margin-bottom: 1.5rem;
}

.project-title {
  font-size: 1.5rem;
  font-weight: 700;
  margin-bottom: 0.75rem;
  line-height: 1.3;
}

.project-description {
  font-size: 0.95rem;
  line-height: 1.5;
  color: rgba(255, 255, 255, 0.7);
}

.card-footer {
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.project-meta {
  display: flex;
  gap: 1rem;
}

.meta-item {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  font-size: 0.75rem;
  color: rgba(255, 255, 255, 0.6);
  text-transform: uppercase;
  letter-spacing: 0.05em;
}

.meta-item svg {
  width: 14px;
  height: 14px;
  stroke: currentColor;
}

.card-action {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  font-size: 0.875rem;
  font-weight: 600;
  color: #3a86ff;
  transition: all 0.3s ease;
}

.card-action svg {
  width: 16px;
  height: 16px;
  stroke: currentColor;
  transition: transform 0.3s ease;
}

.project-card:hover .card-action {
  color: #6ea8ff;
}

.project-card:hover .card-action svg {
  transform: translateX(4px);
}

.card-hover-effect {
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: linear-gradient(135deg, rgba(58, 134, 255, 0.1) 0%, rgba(131, 56, 236, 0.1) 100%);
  opacity: 0;
  transition: opacity 0.4s ease;
  z-index: 1;
}

.project-card:hover .card-hover-effect {
  opacity: 1;
}

/* Responsive Design */
@media (max-width: 1024px) {
  .hero-content {
    flex-direction: column;
    gap: 3rem;
    text-align: center;
  }
  
  .title-line {
    font-size: 3rem;
  }
  
  .intelligence-metrics {
    flex-direction: column;
    gap: 1rem;
  }
  
  .selector-header {
    flex-direction: column;
    gap: 2rem;
    align-items: stretch;
  }
  
  .project-grid {
    grid-template-columns: 1fr;
    padding: 2rem;
  }
}

@media (max-width: 768px) {
  .ai-pm-hero {
    padding: 3rem 0 4rem;
  }
  
  .hero-content {
    padding: 0 1rem;
  }
  
  .title-line {
    font-size: 2.5rem;
  }
  
  .title-subtitle {
    font-size: 1.25rem;
  }
  
  .hero-description {
    font-size: 1.1rem;
  }
  
  .selector-header {
    padding: 2rem;
  }
  
  .selector-title {
    font-size: 1.5rem;
  }
  
  .project-grid {
    padding: 1.5rem;
  }
  
  .project-card {
    height: 250px;
  }
}

@media (max-width: 480px) {
  .ai-pm-content {
    padding: 0 1rem 2rem;
  }
  
  .title-line {
    font-size: 2rem;
  }
  
  .avatar-core {
    width: 100px;
    height: 100px;
  }
  
  .avatar-brain {
    width: 70px;
    height: 70px;
  }
  
  .avatar-brain svg {
    width: 32px;
    height: 32px;
  }
  
  .selector-header {
    padding: 1.5rem;
  }
  
  .project-grid {
    grid-template-columns: 1fr;
    gap: 1.5rem;
    padding: 1rem;
  }
}
</style>
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