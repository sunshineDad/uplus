<template>
  <TechLayout title="Dashboard">
    <div class="dashboard">
      <!-- Hero Section with Premium Design -->
      <div class="dashboard-hero">
        <div class="hero-background">
          <div class="hero-gradient"></div>
          <div class="hero-particles"></div>
        </div>
        <div class="hero-content">
          <div class="hero-badge">
            <span class="badge-text">AI-Native Platform</span>
            <div class="badge-glow"></div>
          </div>
          <h1 class="hero-title">
            <span class="title-main">一键升级</span>
            <span class="title-accent">uplus</span>
          </h1>
          <p class="hero-subtitle">
            Transform your 3-5 person team into a 50+ capability organization
          </p>
          <div class="hero-stats">
            <div class="stat-item">
              <div class="stat-number">{{ projectCount }}</div>
              <div class="stat-label">Active Projects</div>
            </div>
            <div class="stat-divider"></div>
            <div class="stat-item">
              <div class="stat-number">{{ sessionCount }}</div>
              <div class="stat-label">AI Sessions</div>
            </div>
            <div class="stat-divider"></div>
            <div class="stat-item">
              <div class="stat-number">{{ rsdCount }}</div>
              <div class="stat-label">RSD Generated</div>
            </div>
          </div>
        </div>
      </div>
      
      <!-- Premium Capability Cards -->
      <div class="capability-grid">
        <div class="capability-card ai-pm-card" @click="navigateToAIPM">
          <div class="card-background">
            <div class="card-gradient"></div>
            <div class="card-pattern"></div>
          </div>
          <div class="card-content">
            <div class="card-icon">
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                <path d="M21 11.5a8.38 8.38 0 0 1-.9 3.8 8.5 8.5 0 0 1-7.6 4.7 8.38 8.38 0 0 1-3.8-.9L3 21l1.9-5.7a8.38 8.38 0 0 1-.9-3.8 8.5 8.5 0 0 1 4.7-7.6 8.38 8.38 0 0 1 3.8-.9h.5a8.48 8.48 0 0 1 8 8v.5z"></path>
              </svg>
            </div>
            <div class="card-header">
              <h3 class="card-title">AI Product Manager</h3>
              <div class="card-status active">Active</div>
            </div>
            <p class="card-description">
              Transform vague human desires into precise, executable specifications through Socratic Intelligence
            </p>
            <div class="card-metrics">
              <div class="metric">
                <span class="metric-value">{{ sessionCount }}</span>
                <span class="metric-label">Sessions</span>
              </div>
              <div class="metric">
                <span class="metric-value">95%</span>
                <span class="metric-label">Accuracy</span>
              </div>
            </div>
            <div class="card-action">
              <span>Start Conversation</span>
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                <path d="m9 18 6-6-6-6"/>
              </svg>
            </div>
          </div>
        </div>

        <div class="capability-card bitcup-card" @click="navigateToBITCUP">
          <div class="card-background">
            <div class="card-gradient"></div>
            <div class="card-pattern"></div>
          </div>
          <div class="card-content">
            <div class="card-icon">
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                <polyline points="16 18 22 12 16 6"></polyline>
                <polyline points="8 6 2 12 8 18"></polyline>
              </svg>
            </div>
            <div class="card-header">
              <h3 class="card-title">BITCUP Modeling</h3>
              <div class="card-status beta">Beta</div>
            </div>
            <p class="card-description">
              Universal semantic language expressing "what" not "how" through Declarative Semantics
            </p>
            <div class="card-metrics">
              <div class="metric">
                <span class="metric-value">{{ bitcupCount }}</span>
                <span class="metric-label">Models</span>
              </div>
              <div class="metric">
                <span class="metric-value">100%</span>
                <span class="metric-label">Semantic</span>
              </div>
            </div>
            <div class="card-action">
              <span>View Models</span>
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                <path d="m9 18 6-6-6-6"/>
              </svg>
            </div>
          </div>
        </div>

        <div class="capability-card lowcode-card">
          <div class="card-background">
            <div class="card-gradient"></div>
            <div class="card-pattern"></div>
          </div>
          <div class="card-content">
            <div class="card-icon">
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                <rect x="3" y="3" width="18" height="18" rx="2" ry="2"/>
                <rect x="7" y="7" width="3" height="9"/>
                <rect x="14" y="7" width="3" height="5"/>
              </svg>
            </div>
            <div class="card-header">
              <h3 class="card-title">AI Low-Code Platform</h3>
              <div class="card-status coming-soon">Coming Soon</div>
            </div>
            <p class="card-description">
              Materialize BITCUP models into living systems through Intelligent Materialization
            </p>
            <div class="card-metrics">
              <div class="metric">
                <span class="metric-value">∞</span>
                <span class="metric-label">Potential</span>
              </div>
              <div class="metric">
                <span class="metric-value">AI</span>
                <span class="metric-label">Powered</span>
              </div>
            </div>
            <div class="card-action disabled">
              <span>Coming Soon</span>
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                <circle cx="12" cy="12" r="10"/>
                <polyline points="12,6 12,12 16,14"/>
              </svg>
            </div>
          </div>
        </div>

        <div class="capability-card memory-card">
          <div class="card-background">
            <div class="card-gradient"></div>
            <div class="card-pattern"></div>
          </div>
          <div class="card-content">
            <div class="card-icon">
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                <path d="M9 19c-5 0-8-3-8-8s3-8 8-8 8 3 8 8-3 8-8 8"/>
                <path d="M15 11c0-3-3-6-6-6"/>
              </svg>
            </div>
            <div class="card-header">
              <h3 class="card-title">Memory Intelligence</h3>
              <div class="card-status coming-soon">Coming Soon</div>
            </div>
            <p class="card-description">
              Create an immortal, ever-learning organizational brain through Temporal Knowledge Graph
            </p>
            <div class="card-metrics">
              <div class="metric">
                <span class="metric-value">∞</span>
                <span class="metric-label">Memory</span>
              </div>
              <div class="metric">
                <span class="metric-value">∞</span>
                <span class="metric-label">Learning</span>
              </div>
            </div>
            <div class="card-action disabled">
              <span>Coming Soon</span>
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                <circle cx="12" cy="12" r="10"/>
                <polyline points="12,6 12,12 16,14"/>
              </svg>
            </div>
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
    
    const navigateToAIPM = () => {
      router.push('/ai-pm');
    };
    
    const navigateToBITCUP = () => {
      router.push('/bitcup');
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
      startSession,
      navigateToAIPM,
      navigateToBITCUP
    };
  }
};
</script>

<style scoped>
.dashboard {
  display: flex;
  flex-direction: column;
  gap: 3rem;
  min-height: 100vh;
}

/* Premium Hero Section */
.dashboard-hero {
  position: relative;
  padding: 4rem 0 6rem;
  overflow: hidden;
  border-radius: 2rem;
  margin-bottom: 2rem;
}

.hero-background {
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  z-index: 1;
}

.hero-gradient {
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: linear-gradient(
    135deg,
    rgba(58, 134, 255, 0.1) 0%,
    rgba(131, 56, 236, 0.1) 50%,
    rgba(255, 0, 110, 0.1) 100%
  );
  backdrop-filter: blur(20px);
  border: 1px solid rgba(255, 255, 255, 0.1);
}

.hero-particles {
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background-image: 
    radial-gradient(circle at 20% 20%, rgba(58, 134, 255, 0.3) 0%, transparent 50%),
    radial-gradient(circle at 80% 80%, rgba(131, 56, 236, 0.3) 0%, transparent 50%),
    radial-gradient(circle at 40% 60%, rgba(255, 0, 110, 0.2) 0%, transparent 50%);
  animation: float 6s ease-in-out infinite;
}

@keyframes float {
  0%, 100% { transform: translateY(0px) rotate(0deg); }
  50% { transform: translateY(-20px) rotate(180deg); }
}

.hero-content {
  position: relative;
  z-index: 2;
  text-align: center;
  max-width: 800px;
  margin: 0 auto;
  padding: 0 2rem;
}

.hero-badge {
  position: relative;
  display: inline-block;
  margin-bottom: 2rem;
  padding: 0.75rem 2rem;
  background: rgba(255, 255, 255, 0.1);
  border: 1px solid rgba(255, 255, 255, 0.2);
  border-radius: 50px;
  backdrop-filter: blur(10px);
  overflow: hidden;
}

.badge-text {
  position: relative;
  z-index: 2;
  font-size: 0.875rem;
  font-weight: 600;
  color: var(--white);
  text-transform: uppercase;
  letter-spacing: 0.1em;
}

.badge-glow {
  position: absolute;
  top: 0;
  left: -100%;
  width: 100%;
  height: 100%;
  background: linear-gradient(90deg, transparent, rgba(255, 255, 255, 0.3), transparent);
  animation: badge-shine 3s infinite;
}

@keyframes badge-shine {
  0% { left: -100%; }
  100% { left: 100%; }
}

.hero-title {
  font-size: 4rem;
  font-weight: 800;
  margin-bottom: 1.5rem;
  line-height: 1.1;
}

.title-main {
  display: block;
  background: linear-gradient(135deg, #3a86ff 0%, #8338ec 100%);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
  margin-bottom: 0.5rem;
}

.title-accent {
  display: block;
  background: linear-gradient(135deg, #ff006e 0%, #ffbe0b 100%);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
  font-size: 3rem;
}

.hero-subtitle {
  font-size: 1.5rem;
  font-weight: 400;
  color: rgba(255, 255, 255, 0.8);
  margin-bottom: 3rem;
  line-height: 1.6;
}

.hero-stats {
  display: flex;
  justify-content: center;
  align-items: center;
  gap: 2rem;
  margin-top: 3rem;
}

.stat-item {
  text-align: center;
}

.stat-number {
  font-size: 2.5rem;
  font-weight: 700;
  color: var(--white);
  margin-bottom: 0.5rem;
}

.stat-label {
  font-size: 0.875rem;
  color: rgba(255, 255, 255, 0.7);
  text-transform: uppercase;
  letter-spacing: 0.1em;
}

.stat-divider {
  width: 1px;
  height: 3rem;
  background: linear-gradient(to bottom, transparent, rgba(255, 255, 255, 0.3), transparent);
}

/* Premium Capability Cards */
.capability-grid {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 2rem;
  margin-bottom: 3rem;
}

.capability-card {
  position: relative;
  height: 400px;
  border-radius: 1.5rem;
  overflow: hidden;
  cursor: pointer;
  transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
  transform-style: preserve-3d;
}

.capability-card:hover {
  transform: translateY(-8px) scale(1.02);
  box-shadow: 0 25px 50px rgba(0, 0, 0, 0.3);
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
  backdrop-filter: blur(20px);
  border: 1px solid rgba(255, 255, 255, 0.1);
  transition: all 0.4s ease;
}

.ai-pm-card .card-gradient {
  background: linear-gradient(135deg, 
    rgba(58, 134, 255, 0.15) 0%, 
    rgba(131, 56, 236, 0.15) 100%);
}

.bitcup-card .card-gradient {
  background: linear-gradient(135deg, 
    rgba(131, 56, 236, 0.15) 0%, 
    rgba(255, 0, 110, 0.15) 100%);
}

.lowcode-card .card-gradient {
  background: linear-gradient(135deg, 
    rgba(255, 0, 110, 0.15) 0%, 
    rgba(255, 190, 11, 0.15) 100%);
}

.memory-card .card-gradient {
  background: linear-gradient(135deg, 
    rgba(6, 214, 160, 0.15) 0%, 
    rgba(17, 138, 178, 0.15) 100%);
}

.card-pattern {
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background-image: 
    radial-gradient(circle at 20% 20%, rgba(255, 255, 255, 0.1) 0%, transparent 50%),
    radial-gradient(circle at 80% 80%, rgba(255, 255, 255, 0.05) 0%, transparent 50%);
  opacity: 0;
  transition: opacity 0.4s ease;
}

.capability-card:hover .card-pattern {
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

.card-icon {
  width: 60px;
  height: 60px;
  margin-bottom: 1.5rem;
  padding: 1rem;
  border-radius: 1rem;
  background: rgba(255, 255, 255, 0.1);
  backdrop-filter: blur(10px);
  display: flex;
  align-items: center;
  justify-content: center;
  transition: all 0.3s ease;
}

.card-icon svg {
  width: 28px;
  height: 28px;
  stroke: currentColor;
}

.capability-card:hover .card-icon {
  transform: scale(1.1);
  background: rgba(255, 255, 255, 0.2);
}

.card-header {
  display: flex;
  justify-content: space-between;
  align-items: flex-start;
  margin-bottom: 1rem;
}

.card-title {
  font-size: 1.5rem;
  font-weight: 700;
  margin: 0;
  line-height: 1.3;
}

.card-status {
  padding: 0.25rem 0.75rem;
  border-radius: 50px;
  font-size: 0.75rem;
  font-weight: 600;
  text-transform: uppercase;
  letter-spacing: 0.05em;
}

.card-status.active {
  background: rgba(6, 214, 160, 0.2);
  color: #06d6a0;
  border: 1px solid rgba(6, 214, 160, 0.3);
}

.card-status.beta {
  background: rgba(255, 190, 11, 0.2);
  color: #ffbe0b;
  border: 1px solid rgba(255, 190, 11, 0.3);
}

.card-status.coming-soon {
  background: rgba(255, 255, 255, 0.1);
  color: rgba(255, 255, 255, 0.7);
  border: 1px solid rgba(255, 255, 255, 0.2);
}

.card-description {
  font-size: 1rem;
  line-height: 1.6;
  color: rgba(255, 255, 255, 0.8);
  margin-bottom: 2rem;
  flex: 1;
}

.card-metrics {
  display: flex;
  gap: 2rem;
  margin-bottom: 2rem;
}

.metric {
  display: flex;
  flex-direction: column;
  align-items: center;
  text-align: center;
}

.metric-value {
  font-size: 1.5rem;
  font-weight: 700;
  color: var(--white);
  margin-bottom: 0.25rem;
}

.metric-label {
  font-size: 0.75rem;
  color: rgba(255, 255, 255, 0.6);
  text-transform: uppercase;
  letter-spacing: 0.1em;
}

.card-action {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 1rem 1.5rem;
  background: rgba(255, 255, 255, 0.1);
  border-radius: 0.75rem;
  border: 1px solid rgba(255, 255, 255, 0.2);
  transition: all 0.3s ease;
  margin-top: auto;
}

.card-action:not(.disabled):hover {
  background: rgba(255, 255, 255, 0.2);
  transform: translateX(4px);
}

.card-action.disabled {
  opacity: 0.5;
  cursor: not-allowed;
}

.card-action span {
  font-weight: 600;
  font-size: 0.875rem;
}

.card-action svg {
  width: 16px;
  height: 16px;
  transition: transform 0.3s ease;
}

.card-action:not(.disabled):hover svg {
  transform: translateX(4px);
}

/* Projects Section */
.dashboard-content {
  display: flex;
  flex-direction: column;
  gap: 3rem;
}

.dashboard-section {
  position: relative;
  padding: 2rem;
  background: rgba(255, 255, 255, 0.05);
  border-radius: 1.5rem;
  border: 1px solid rgba(255, 255, 255, 0.1);
  backdrop-filter: blur(20px);
}

.section-header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  margin-bottom: 2rem;
}

.section-title {
  font-size: 2rem;
  font-weight: 700;
  color: var(--white);
  margin: 0;
}

.section-link {
  padding: 0.75rem 1.5rem;
  background: rgba(255, 255, 255, 0.1);
  border: 1px solid rgba(255, 255, 255, 0.2);
  border-radius: 0.75rem;
  color: var(--white);
  text-decoration: none;
  font-weight: 600;
  transition: all 0.3s ease;
}

.section-link:hover {
  background: rgba(255, 255, 255, 0.2);
  transform: translateY(-2px);
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
  padding: 4rem;
  text-align: center;
  color: var(--white);
}

.empty-icon {
  display: flex;
  align-items: center;
  justify-content: center;
  width: 80px;
  height: 80px;
  margin-bottom: 2rem;
  background: rgba(255, 255, 255, 0.1);
  border-radius: 50%;
  backdrop-filter: blur(10px);
}

.empty-icon svg {
  width: 40px;
  height: 40px;
  stroke: currentColor;
}

.empty-state h3 {
  margin-bottom: 1rem;
  font-size: 1.5rem;
  font-weight: 700;
}

.empty-state p {
  margin-bottom: 2rem;
  color: rgba(255, 255, 255, 0.7);
  font-size: 1.1rem;
}

.projects-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
  gap: 2rem;
}

/* Responsive Design */
@media (max-width: 1400px) {
  .capability-grid {
    grid-template-columns: repeat(2, 1fr);
  }
}

@media (max-width: 1024px) {
  .hero-title {
    font-size: 3rem;
  }
  
  .title-accent {
    font-size: 2.5rem;
  }
  
  .hero-subtitle {
    font-size: 1.25rem;
  }
  
  .hero-stats {
    flex-direction: column;
    gap: 1.5rem;
  }
  
  .stat-divider {
    display: none;
  }
  
  .capability-grid {
    grid-template-columns: 1fr;
    gap: 1.5rem;
  }
  
  .capability-card {
    height: 350px;
  }
}

@media (max-width: 768px) {
  .dashboard {
    gap: 2rem;
  }
  
  .dashboard-hero {
    padding: 3rem 0 4rem;
    margin-bottom: 1rem;
  }
  
  .hero-content {
    padding: 0 1rem;
  }
  
  .hero-title {
    font-size: 2.5rem;
  }
  
  .title-accent {
    font-size: 2rem;
  }
  
  .hero-subtitle {
    font-size: 1.1rem;
    margin-bottom: 2rem;
  }
  
  .hero-stats {
    gap: 1rem;
  }
  
  .stat-number {
    font-size: 2rem;
  }
  
  .capability-card {
    height: 320px;
  }
  
  .card-content {
    padding: 1.5rem;
  }
  
  .card-title {
    font-size: 1.25rem;
  }
  
  .card-description {
    font-size: 0.9rem;
    margin-bottom: 1.5rem;
  }
  
  .card-metrics {
    gap: 1.5rem;
    margin-bottom: 1.5rem;
  }
  
  .dashboard-section {
    padding: 1.5rem;
  }
  
  .section-title {
    font-size: 1.5rem;
  }
  
  .projects-grid {
    grid-template-columns: 1fr;
    gap: 1.5rem;
  }
}

@media (max-width: 480px) {
  .hero-title {
    font-size: 2rem;
  }
  
  .title-accent {
    font-size: 1.75rem;
  }
  
  .hero-subtitle {
    font-size: 1rem;
  }
  
  .capability-card {
    height: 300px;
  }
  
  .card-content {
    padding: 1.25rem;
  }
  
  .card-icon {
    width: 50px;
    height: 50px;
    margin-bottom: 1rem;
  }
  
  .card-icon svg {
    width: 24px;
    height: 24px;
  }
  
  .card-title {
    font-size: 1.1rem;
  }
  
  .card-description {
    font-size: 0.85rem;
  }
  
  .metric-value {
    font-size: 1.25rem;
  }
  
  .dashboard-section {
    padding: 1rem;
  }
}

/* Animation Enhancements */
@keyframes pulse {
  0%, 100% { opacity: 1; }
  50% { opacity: 0.7; }
}

.loading-container {
  animation: pulse 2s infinite;
}

/* Smooth scroll behavior */
html {
  scroll-behavior: smooth;
}

/* Focus states for accessibility */
.capability-card:focus,
.section-link:focus,
.card-action:focus {
  outline: 2px solid rgba(58, 134, 255, 0.5);
  outline-offset: 2px;
}
</style>