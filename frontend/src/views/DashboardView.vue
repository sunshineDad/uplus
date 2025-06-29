<template>
  <TechLayout title="Dashboard">
    <div class="dashboard">
      <div class="dashboard-header">
        <h1 class="dashboard-title">一键升级-uplus Dashboard</h1>
        <p class="dashboard-subtitle">AI-native software engineering platform</p>
      </div>
      
      <div class="dashboard-stats">
        <div class="stat-card">
          <div class="stat-icon">
            <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
              <path d="M22 19a2 2 0 0 1-2 2H4a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h5l2 3h9a2 2 0 0 1 2 2z"></path>
            </svg>
          </div>
          <div class="stat-content">
            <div class="stat-value">{{ projectCount }}</div>
            <div class="stat-label">Projects</div>
          </div>
        </div>
        
        <div class="stat-card">
          <div class="stat-icon">
            <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
              <path d="M21 11.5a8.38 8.38 0 0 1-.9 3.8 8.5 8.5 0 0 1-7.6 4.7 8.38 8.38 0 0 1-3.8-.9L3 21l1.9-5.7a8.38 8.38 0 0 1-.9-3.8 8.5 8.5 0 0 1 4.7-7.6 8.38 8.38 0 0 1 3.8-.9h.5a8.48 8.48 0 0 1 8 8v.5z"></path>
            </svg>
          </div>
          <div class="stat-content">
            <div class="stat-value">{{ sessionCount }}</div>
            <div class="stat-label">AI-PM Sessions</div>
          </div>
        </div>
        
        <div class="stat-card">
          <div class="stat-icon">
            <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
              <path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"></path>
              <polyline points="14 2 14 8 20 8"></polyline>
              <line x1="16" y1="13" x2="8" y2="13"></line>
              <line x1="16" y1="17" x2="8" y2="17"></line>
              <polyline points="10 9 9 9 8 9"></polyline>
            </svg>
          </div>
          <div class="stat-content">
            <div class="stat-value">{{ rsdCount }}</div>
            <div class="stat-label">RSD Documents</div>
          </div>
        </div>
        
        <div class="stat-card">
          <div class="stat-icon">
            <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
              <polyline points="16 18 22 12 16 6"></polyline>
              <polyline points="8 6 2 12 8 18"></polyline>
            </svg>
          </div>
          <div class="stat-content">
            <div class="stat-value">{{ bitcupCount }}</div>
            <div class="stat-label">BITCUP Models</div>
          </div>
        </div>
      </div>
      
      <div class="dashboard-content">
        <div class="dashboard-section">
          <div class="section-header">
            <h2 class="section-title">Recent Projects</h2>
            <router-link to="/projects" class="section-link">View All</router-link>
          </div>
          
          <div class="section-content">
            <div v-if="loading" class="loading-container">
              <TechLoader message="Loading projects" />
            </div>
            
            <div v-else-if="recentProjects.length === 0" class="empty-state">
              <div class="empty-icon">
                <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                  <path d="M22 19a2 2 0 0 1-2 2H4a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h5l2 3h9a2 2 0 0 1 2 2z"></path>
                </svg>
              </div>
              <h3>No Projects Yet</h3>
              <p>Create your first project to get started</p>
              <router-link to="/projects" class="btn btn-primary">Create Project</router-link>
            </div>
            
            <div v-else class="projects-grid">
              <ProjectCard 
                v-for="project in recentProjects" 
                :key="project.id" 
                :project="project"
                @view-project="viewProject"
                @start-session="startSession"
              />
            </div>
          </div>
        </div>
        
        <div class="dashboard-section">
          <div class="section-header">
            <h2 class="section-title">Platform Overview</h2>
          </div>
          
          <div class="section-content">
            <div class="platform-overview">
              <div class="overview-card">
                <h3 class="overview-title">AI Product Manager</h3>
                <p class="overview-description">
                  Transform vague human desires into precise, executable specifications through Socratic Intelligence.
                </p>
                <router-link to="/ai-pm" class="btn btn-outline-primary">Start Conversation</router-link>
              </div>
              
              <div class="overview-card">
                <h3 class="overview-title">BITCUP Modeling</h3>
                <p class="overview-description">
                  Universal semantic language that expresses "what" not "how" through Declarative Semantics.
                </p>
                <router-link to="/bitcup" class="btn btn-outline-primary">View Models</router-link>
              </div>
              
              <div class="overview-card">
                <h3 class="overview-title">AI Low-Code Platform</h3>
                <p class="overview-description">
                  Materialize BITCUP models into living, breathing systems through Intelligent Materialization.
                </p>
                <button class="btn btn-outline-primary" disabled>Coming Soon</button>
              </div>
              
              <div class="overview-card">
                <h3 class="overview-title">Document Memory</h3>
                <p class="overview-description">
                  Create an immortal, ever-learning organizational brain through Temporal Knowledge Graph.
                </p>
                <button class="btn btn-outline-primary" disabled>Coming Soon</button>
              </div>
            </div>
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
import TechLayout from '@/components/common/TechLayout.vue';
import TechLoader from '@/components/common/TechLoader.vue';
import ProjectCard from '@/components/projects/ProjectCard.vue';

export default {
  name: 'DashboardView',
  components: {
    TechLayout,
    TechLoader,
    ProjectCard
  },
  setup() {
    const router = useRouter();
    const projectStore = useProjectStore();
    const sessionStore = useSessionStore();
    
    const loading = ref(true);
    const rsdCount = ref(0);
    const bitcupCount = ref(0);
    
    // Computed properties
    const projectCount = computed(() => projectStore.projects.length);
    const sessionCount = computed(() => sessionStore.sessions.length);
    
    const recentProjects = computed(() => {
      return projectStore.projects.slice(0, 3);
    });
    
    // Methods
    const viewProject = (project) => {
      projectStore.setCurrentProject(project);
      router.push(`/projects/${project.id}`);
    };
    
    const startSession = (project) => {
      projectStore.setCurrentProject(project);
      router.push('/ai-pm');
    };
    
    // Fetch data on component mount
    onMounted(async () => {
      try {
        await Promise.all([
          projectStore.fetchProjects(),
          sessionStore.fetchSessions()
        ]);
      } catch (error) {
        console.error('Error fetching dashboard data:', error);
      } finally {
        loading.value = false;
      }
    });
    
    return {
      loading,
      projectCount,
      sessionCount,
      rsdCount,
      bitcupCount,
      recentProjects,
      viewProject,
      startSession
    };
  }
};
</script>

<style scoped>
.dashboard {
  display: flex;
  flex-direction: column;
  gap: 2rem;
}

.dashboard-header {
  text-align: center;
  margin-bottom: 1rem;
}

.dashboard-title {
  font-size: 2.5rem;
  font-weight: 700;
  margin-bottom: 0.5rem;
  background: var(--gradient-primary);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  animation: text-shine 3s linear infinite;
}

.dashboard-subtitle {
  font-size: 1.25rem;
  color: var(--gray-600);
}

.dashboard-stats {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 1.5rem;
}

.stat-card {
  display: flex;
  align-items: center;
  padding: 1.5rem;
  background-color: var(--white);
  border-radius: var(--border-radius-lg);
  box-shadow: var(--shadow-md);
  transition: all var(--transition-normal) var(--transition-timing);
}

.stat-card:hover {
  transform: translateY(-5px);
  box-shadow: var(--shadow-lg);
}

.stat-icon {
  display: flex;
  align-items: center;
  justify-content: center;
  width: 50px;
  height: 50px;
  margin-right: 1rem;
  background-color: var(--primary-light);
  color: var(--white);
  border-radius: var(--border-radius-circle);
}

.stat-icon svg {
  width: 24px;
  height: 24px;
}

.stat-content {
  display: flex;
  flex-direction: column;
}

.stat-value {
  font-size: 2rem;
  font-weight: 700;
  color: var(--gray-900);
}

.stat-label {
  font-size: 0.875rem;
  color: var(--gray-600);
}

.dashboard-content {
  display: flex;
  flex-direction: column;
  gap: 2rem;
}

.dashboard-section {
  display: flex;
  flex-direction: column;
  gap: 1rem;
}

.section-header {
  display: flex;
  align-items: center;
  justify-content: space-between;
}

.section-title {
  font-size: 1.5rem;
  font-weight: 600;
  color: var(--gray-900);
  margin: 0;
}

.section-link {
  font-size: 0.875rem;
  font-weight: 500;
  color: var(--primary);
  text-decoration: none;
}

.section-link:hover {
  text-decoration: underline;
}

.section-content {
  min-height: 200px;
}

.loading-container {
  display: flex;
  align-items: center;
  justify-content: center;
  height: 200px;
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

.platform-overview {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 1.5rem;
}

.overview-card {
  display: flex;
  flex-direction: column;
  padding: 1.5rem;
  background-color: var(--white);
  border-radius: var(--border-radius-lg);
  box-shadow: var(--shadow-md);
  transition: all var(--transition-normal) var(--transition-timing);
}

.overview-card:hover {
  transform: translateY(-5px);
  box-shadow: var(--shadow-lg);
}

.overview-title {
  margin-top: 0;
  margin-bottom: 1rem;
  font-size: 1.25rem;
  font-weight: 600;
  color: var(--gray-900);
}

.overview-description {
  flex: 1;
  margin-bottom: 1.5rem;
  font-size: 0.875rem;
  color: var(--gray-700);
}

/* Dark mode adjustments */
:global(.dark-mode) .dashboard-subtitle {
  color: var(--gray-400);
}

:global(.dark-mode) .stat-card {
  background-color: var(--dark-blue);
}

:global(.dark-mode) .stat-value {
  color: var(--white);
}

:global(.dark-mode) .stat-label {
  color: var(--gray-400);
}

:global(.dark-mode) .section-title {
  color: var(--white);
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

:global(.dark-mode) .overview-card {
  background-color: var(--dark-blue);
}

:global(.dark-mode) .overview-title {
  color: var(--white);
}

:global(.dark-mode) .overview-description {
  color: var(--gray-300);
}

/* Responsive adjustments */
@media (max-width: 1200px) {
  .dashboard-stats {
    grid-template-columns: repeat(2, 1fr);
  }
  
  .platform-overview {
    grid-template-columns: repeat(2, 1fr);
  }
}

@media (max-width: 992px) {
  .projects-grid {
    grid-template-columns: repeat(2, 1fr);
  }
}

@media (max-width: 768px) {
  .dashboard-stats {
    grid-template-columns: 1fr;
  }
  
  .projects-grid {
    grid-template-columns: 1fr;
  }
  
  .platform-overview {
    grid-template-columns: 1fr;
  }
  
  .dashboard-title {
    font-size: 2rem;
  }
  
  .dashboard-subtitle {
    font-size: 1rem;
  }
}
</style>