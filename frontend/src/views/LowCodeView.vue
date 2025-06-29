<template>
  <TechLayout title="AI Low-Code Platform">
    <div class="lowcode-view">
      <!-- Revolutionary Low-Code Platform Hero -->
      <div class="lowcode-hero">
        <div class="hero-background">
          <div class="code-particles">
            <div v-for="i in 50" :key="`particle-${i}`" class="code-particle" 
                 :style="{ 
                   left: `${Math.random() * 100}%`, 
                   top: `${Math.random() * 100}%`,
                   animationDelay: `${Math.random() * 5}s`,
                   animationDuration: `${5 + Math.random() * 10}s`
                 }">
              {{ ['<>', '{}', '()', '[]', '//', '/*', '*/', '=>', '&&', '||'][Math.floor(Math.random() * 10)] }}
            </div>
          </div>
          <div class="code-grid">
            <div v-for="i in 20" :key="`grid-${i}`" class="grid-line" 
                 :style="{ transform: `translateY(${i * 5}vh)` }"></div>
          </div>
        </div>
        
        <div class="hero-content">
          <div class="hero-text">
            <div class="hero-badge">
              <span class="badge-text">Intelligent Materialization</span>
              <div class="badge-pulse"></div>
            </div>
            <h1 class="hero-title">
              <span class="title-main">AI Low-Code</span>
              <span class="title-subtitle">Platform</span>
            </h1>
            <p class="hero-description">
              Materialize BITCUP models into <span class="highlight">living, breathing systems</span> 
              through revolutionary understanding-based generation that creates optimal implementations.
            </p>
            
            <div class="generation-pipeline">
              <div class="pipeline-container">
                <div class="pipeline-step" v-motion :initial="{ opacity: 0, x: -50 }" :enter="{ opacity: 1, x: 0, transition: { delay: 100 } }">
                  <div class="step-icon">
                    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                      <path d="M21 16V8a2 2 0 0 0-1-1.73l-7-4a2 2 0 0 0-2 0l-7 4A2 2 0 0 0 3 8v8a2 2 0 0 0 1 1.73l7 4a2 2 0 0 0 2 0l7-4A2 2 0 0 0 21 16z"/>
                    </svg>
                  </div>
                  <div class="step-label">BITCUP Model</div>
                </div>
                <div class="pipeline-arrow">→</div>
                <div class="pipeline-step" v-motion :initial="{ opacity: 0, x: -50 }" :enter="{ opacity: 1, x: 0, transition: { delay: 200 } }">
                  <div class="step-icon">
                    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                      <circle cx="12" cy="12" r="10"/>
                      <path d="M12 16v-4"/>
                      <path d="M12 8h.01"/>
                    </svg>
                  </div>
                  <div class="step-label">Semantic Analysis</div>
                </div>
                <div class="pipeline-arrow">→</div>
                <div class="pipeline-step" v-motion :initial="{ opacity: 0, x: -50 }" :enter="{ opacity: 1, x: 0, transition: { delay: 300 } }">
                  <div class="step-icon">
                    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                      <path d="M12 2l3.09 6.26L22 9.27l-5 4.87 1.18 6.88L12 17.77l-6.18 3.25L7 14.14 2 9.27l6.91-1.01L12 2z"/>
                    </svg>
                  </div>
                  <div class="step-label">Architecture Selection</div>
                </div>
                <div class="pipeline-arrow">→</div>
                <div class="pipeline-step" v-motion :initial="{ opacity: 0, x: -50 }" :enter="{ opacity: 1, x: 0, transition: { delay: 400 } }">
                  <div class="step-icon">
                    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                      <polyline points="16 18 22 12 16 6"/>
                      <polyline points="8 6 2 12 8 18"/>
                    </svg>
                  </div>
                  <div class="step-label">Code Generation</div>
                </div>
                <div class="pipeline-arrow">→</div>
                <div class="pipeline-step" v-motion :initial="{ opacity: 0, x: -50 }" :enter="{ opacity: 1, x: 0, transition: { delay: 500 } }">
                  <div class="step-icon">
                    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                      <path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"/>
                      <polyline points="22 4 12 14.01 9 11.01"/>
                    </svg>
                  </div>
                  <div class="step-label">Deployment</div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
      
      <!-- Revolutionary Low-Code Capabilities -->
      <div class="lowcode-content">
        <div class="capabilities-section">
          <div class="section-header">
            <h2 class="section-title">Revolutionary Capabilities</h2>
            <p class="section-subtitle">Beyond traditional code generation</p>
          </div>
          
          <div class="capabilities-grid">
            <div class="capability-card" v-motion :initial="{ opacity: 0, y: 50 }" :enter="{ opacity: 1, y: 0, transition: { delay: 100 } }">
              <div class="card-background">
                <div class="card-glow"></div>
              </div>
              <div class="card-content">
                <div class="capability-icon">
                  <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                    <path d="M18 10h-4v4h4v-4z"/>
                    <path d="M10 10H6v4h4v-4z"/>
                    <path d="M18 18h-4v4h4v-4z"/>
                    <path d="M10 18H6v4h4v-4z"/>
                  </svg>
                </div>
                <h3 class="capability-title">Understanding-Based Generation</h3>
                <p class="capability-description">
                  Unlike template-based approaches, our system truly understands the semantic intent
                  and generates optimal implementations tailored to your specific needs.
                </p>
              </div>
            </div>
            
            <div class="capability-card" v-motion :initial="{ opacity: 0, y: 50 }" :enter="{ opacity: 1, y: 0, transition: { delay: 200 } }">
              <div class="card-background">
                <div class="card-glow"></div>
              </div>
              <div class="card-content">
                <div class="capability-icon">
                  <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                    <path d="M12 2l3.09 6.26L22 9.27l-5 4.87 1.18 6.88L12 17.77l-6.18 3.25L7 14.14 2 9.27l6.91-1.01L12 2z"/>
                  </svg>
                </div>
                <h3 class="capability-title">Self-Assembling Architectures</h3>
                <p class="capability-description">
                  The system automatically selects and assembles the optimal architecture based on your
                  requirements, creating solutions that would take teams of experts to design.
                </p>
              </div>
            </div>
            
            <div class="capability-card" v-motion :initial="{ opacity: 0, y: 50 }" :enter="{ opacity: 1, y: 0, transition: { delay: 300 } }">
              <div class="card-background">
                <div class="card-glow"></div>
              </div>
              <div class="card-content">
                <div class="capability-icon">
                  <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                    <path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"/>
                    <polyline points="22 4 12 14.01 9 11.01"/>
                  </svg>
                </div>
                <h3 class="capability-title">Zero-Touch Deployment</h3>
                <p class="capability-description">
                  From code generation to production deployment, the entire process is automated with
                  intelligent configuration and optimization at every step.
                </p>
              </div>
            </div>
            
            <div class="capability-card" v-motion :initial="{ opacity: 0, y: 50 }" :enter="{ opacity: 1, y: 0, transition: { delay: 400 } }">
              <div class="card-background">
                <div class="card-glow"></div>
              </div>
              <div class="card-content">
                <div class="capability-icon">
                  <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                    <path d="M21 12.79A9 9 0 1 1 11.21 3 7 7 0 0 0 21 12.79z"/>
                  </svg>
                </div>
                <h3 class="capability-title">Adaptive Learning</h3>
                <p class="capability-description">
                  The system learns from successful patterns and continuously improves its generation
                  capabilities, becoming more intelligent with every project.
                </p>
              </div>
            </div>
          </div>
        </div>
        
        <!-- Output Guarantees Section -->
        <div class="guarantees-section">
          <div class="section-header">
            <h2 class="section-title">Output Guarantees</h2>
            <p class="section-subtitle">What you can expect from every generated system</p>
          </div>
          
          <div class="guarantees-list">
            <div class="guarantee-item" v-motion :initial="{ opacity: 0, x: -50 }" :enter="{ opacity: 1, x: 0, transition: { delay: 100 } }">
              <div class="guarantee-icon">
                <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                  <path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"/>
                  <polyline points="22 4 12 14.01 9 11.01"/>
                </svg>
              </div>
              <div class="guarantee-content">
                <h3 class="guarantee-title">Functional Completeness</h3>
                <p class="guarantee-description">
                  Every requirement in your BITCUP model is fully implemented with no gaps or missing features.
                </p>
              </div>
            </div>
            
            <div class="guarantee-item" v-motion :initial="{ opacity: 0, x: -50 }" :enter="{ opacity: 1, x: 0, transition: { delay: 200 } }">
              <div class="guarantee-icon">
                <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                  <path d="M13 2L3 14h9l-1 8 10-12h-9l1-8z"/>
                </svg>
              </div>
              <div class="guarantee-content">
                <h3 class="guarantee-title">Performance Optimization</h3>
                <p class="guarantee-description">
                  Generated systems are automatically optimized for speed, efficiency, and resource utilization.
                </p>
              </div>
            </div>
            
            <div class="guarantee-item" v-motion :initial="{ opacity: 0, x: -50 }" :enter="{ opacity: 1, x: 0, transition: { delay: 300 } }">
              <div class="guarantee-icon">
                <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                  <rect x="3" y="11" width="18" height="11" rx="2" ry="2"/>
                  <path d="M7 11V7a5 5 0 0 1 10 0v4"/>
                </svg>
              </div>
              <div class="guarantee-content">
                <h3 class="guarantee-title">Security By Design</h3>
                <p class="guarantee-description">
                  Security best practices are built into every layer of the generated system, not added as an afterthought.
                </p>
              </div>
            </div>
            
            <div class="guarantee-item" v-motion :initial="{ opacity: 0, x: -50 }" :enter="{ opacity: 1, x: 0, transition: { delay: 400 } }">
              <div class="guarantee-icon">
                <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                  <path d="M21 16V8a2 2 0 0 0-1-1.73l-7-4a2 2 0 0 0-2 0l-7 4A2 2 0 0 0 3 8v8a2 2 0 0 0 1 1.73l7 4a2 2 0 0 0 2 0l7-4A2 2 0 0 0 21 16z"/>
                  <polyline points="3.27 6.96 12 12.01 20.73 6.96"/>
                  <line x1="12" y1="22.08" x2="12" y2="12"/>
                </svg>
              </div>
              <div class="guarantee-content">
                <h3 class="guarantee-title">Scalability Ready</h3>
                <p class="guarantee-description">
                  All generated systems are cloud-native by default, designed to scale from day one.
                </p>
              </div>
            </div>
          </div>
        </div>
        
        <!-- Coming Soon Notice -->
        <div class="coming-soon-section">
          <div class="coming-soon-container">
            <div class="coming-soon-icon">
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                <circle cx="12" cy="12" r="10"/>
                <path d="M12 6v6l4 2"/>
              </svg>
            </div>
            <div class="coming-soon-content">
              <h2 class="coming-soon-title">Coming in Phase 3</h2>
              <p class="coming-soon-description">
                The AI Low-Code Platform is currently in advanced development. This revolutionary
                system will be available in the next major release, bringing unprecedented capabilities
                to transform your BITCUP models into fully functional systems.
              </p>
              <div class="progress-container">
                <div class="progress-bar">
                  <div class="progress-fill" style="width: 65%"></div>
                </div>
                <div class="progress-label">Development Progress: 65%</div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </TechLayout>
</template>

<script>
import TechLayout from '@/components/common/TechLayout.vue';

export default {
  name: 'LowCodeView',
  components: {
    TechLayout
  }
};
</script>

<style scoped>
/* Revolutionary Low-Code Platform Styling */
.lowcode-view {
  min-height: 100vh;
  background: linear-gradient(135deg, #0a0a0a 0%, #1a1a2e 50%, #16213e 100%);
}

/* Hero Section */
.lowcode-hero {
  position: relative;
  min-height: 80vh;
  display: flex;
  align-items: center;
  overflow: hidden;
}

.hero-background {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  z-index: 0;
}

.code-particles {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
}

.code-particle {
  position: absolute;
  font-family: var(--font-mono);
  color: var(--primary-400);
  opacity: 0.3;
  font-size: 1.2rem;
  animation: float-particle linear infinite;
}

@keyframes float-particle {
  0% {
    transform: translate(0, 0);
    opacity: 0;
  }
  10% {
    opacity: 0.3;
  }
  90% {
    opacity: 0.3;
  }
  100% {
    transform: translate(calc(Math.random() * 100px - 50px), calc(Math.random() * 100px - 50px));
    opacity: 0;
  }
}

.code-grid {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
}

.grid-line {
  position: absolute;
  width: 100%;
  height: 1px;
  background: linear-gradient(90deg, transparent 0%, var(--primary-400) 50%, transparent 100%);
  opacity: 0.1;
}

.hero-content {
  position: relative;
  z-index: 1;
  width: 100%;
  max-width: 1200px;
  margin: 0 auto;
  padding: 2rem;
}

.hero-text {
  max-width: 700px;
}

.hero-badge {
  display: inline-flex;
  align-items: center;
  background: rgba(58, 134, 255, 0.1);
  border: 1px solid var(--primary-400);
  border-radius: 20px;
  padding: 0.5rem 1rem;
  margin-bottom: 1.5rem;
  position: relative;
}

.badge-text {
  font-size: 0.9rem;
  font-weight: 600;
  color: var(--primary-400);
  text-transform: uppercase;
  letter-spacing: 1px;
}

.badge-pulse {
  position: absolute;
  top: 50%;
  right: 1rem;
  transform: translateY(-50%);
  width: 8px;
  height: 8px;
  background: var(--primary-400);
  border-radius: 50%;
  animation: pulse 2s infinite;
}

@keyframes pulse {
  0% {
    box-shadow: 0 0 0 0 rgba(58, 134, 255, 0.7);
  }
  70% {
    box-shadow: 0 0 0 10px rgba(58, 134, 255, 0);
  }
  100% {
    box-shadow: 0 0 0 0 rgba(58, 134, 255, 0);
  }
}

.hero-title {
  font-size: 3.5rem;
  font-weight: 800;
  margin-bottom: 1.5rem;
  line-height: 1.1;
  background: linear-gradient(90deg, var(--primary-400), var(--secondary-400));
  -webkit-background-clip: text;
  background-clip: text;
  color: transparent;
}

.title-main {
  display: block;
}

.title-subtitle {
  display: block;
  font-size: 2.5rem;
  opacity: 0.9;
}

.hero-description {
  font-size: 1.2rem;
  line-height: 1.6;
  margin-bottom: 2rem;
  color: var(--text-secondary);
}

.highlight {
  color: var(--accent-400);
  font-weight: 600;
}

/* Generation Pipeline */
.generation-pipeline {
  margin-top: 3rem;
}

.pipeline-container {
  display: flex;
  align-items: center;
  flex-wrap: wrap;
  gap: 1rem;
  background: rgba(0, 0, 0, 0.2);
  border-radius: 12px;
  padding: 1.5rem;
  border: 1px solid rgba(58, 134, 255, 0.2);
}

.pipeline-step {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 0.5rem;
}

.step-icon {
  width: 3rem;
  height: 3rem;
  display: flex;
  align-items: center;
  justify-content: center;
  background: rgba(58, 134, 255, 0.1);
  border-radius: 50%;
  color: var(--primary-400);
}

.step-icon svg {
  width: 1.5rem;
  height: 1.5rem;
}

.step-label {
  font-size: 0.9rem;
  font-weight: 600;
  color: var(--text-secondary);
}

.pipeline-arrow {
  color: var(--primary-400);
  font-size: 1.5rem;
  opacity: 0.7;
}

/* Capabilities Section */
.lowcode-content {
  padding: 4rem 2rem;
  max-width: 1200px;
  margin: 0 auto;
}

.section-header {
  text-align: center;
  margin-bottom: 3rem;
}

.section-title {
  font-size: 2.5rem;
  font-weight: 800;
  margin-bottom: 1rem;
  background: linear-gradient(90deg, var(--primary-400), var(--secondary-400));
  -webkit-background-clip: text;
  background-clip: text;
  color: transparent;
}

.section-subtitle {
  font-size: 1.2rem;
  color: var(--text-secondary);
  max-width: 600px;
  margin: 0 auto;
}

.capabilities-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
  gap: 2rem;
  margin-bottom: 4rem;
}

.capability-card {
  position: relative;
  border-radius: 12px;
  overflow: hidden;
  height: 100%;
  min-height: 250px;
}

.card-background {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: rgba(0, 0, 0, 0.2);
  border: 1px solid rgba(58, 134, 255, 0.2);
  z-index: 0;
}

.card-glow {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: radial-gradient(circle at 50% 0%, rgba(58, 134, 255, 0.2) 0%, transparent 70%);
}

.card-content {
  position: relative;
  z-index: 1;
  padding: 2rem;
  height: 100%;
  display: flex;
  flex-direction: column;
  gap: 1rem;
}

.capability-icon {
  width: 3rem;
  height: 3rem;
  display: flex;
  align-items: center;
  justify-content: center;
  background: rgba(58, 134, 255, 0.1);
  border-radius: 50%;
  color: var(--primary-400);
}

.capability-icon svg {
  width: 1.5rem;
  height: 1.5rem;
}

.capability-title {
  font-size: 1.3rem;
  font-weight: 700;
  color: var(--text-primary);
}

.capability-description {
  font-size: 1rem;
  line-height: 1.6;
  color: var(--text-secondary);
}

/* Guarantees Section */
.guarantees-section {
  margin-bottom: 4rem;
}

.guarantees-list {
  display: flex;
  flex-direction: column;
  gap: 1.5rem;
}

.guarantee-item {
  display: flex;
  align-items: flex-start;
  gap: 1.5rem;
  background: rgba(0, 0, 0, 0.2);
  border-radius: 12px;
  padding: 1.5rem;
  border: 1px solid rgba(58, 134, 255, 0.2);
}

.guarantee-icon {
  width: 3rem;
  height: 3rem;
  min-width: 3rem;
  display: flex;
  align-items: center;
  justify-content: center;
  background: rgba(58, 134, 255, 0.1);
  border-radius: 50%;
  color: var(--primary-400);
}

.guarantee-icon svg {
  width: 1.5rem;
  height: 1.5rem;
}

.guarantee-content {
  flex: 1;
}

.guarantee-title {
  font-size: 1.2rem;
  font-weight: 700;
  margin-bottom: 0.5rem;
  color: var(--text-primary);
}

.guarantee-description {
  font-size: 1rem;
  line-height: 1.6;
  color: var(--text-secondary);
}

/* Coming Soon Section */
.coming-soon-section {
  margin-top: 4rem;
}

.coming-soon-container {
  display: flex;
  align-items: center;
  gap: 2rem;
  background: rgba(0, 0, 0, 0.3);
  border-radius: 12px;
  padding: 2rem;
  border: 1px solid rgba(131, 56, 236, 0.3);
}

.coming-soon-icon {
  width: 5rem;
  height: 5rem;
  min-width: 5rem;
  display: flex;
  align-items: center;
  justify-content: center;
  background: rgba(131, 56, 236, 0.1);
  border-radius: 50%;
  color: var(--secondary-400);
}

.coming-soon-icon svg {
  width: 2.5rem;
  height: 2.5rem;
}

.coming-soon-content {
  flex: 1;
}

.coming-soon-title {
  font-size: 1.8rem;
  font-weight: 700;
  margin-bottom: 1rem;
  color: var(--secondary-400);
}

.coming-soon-description {
  font-size: 1.1rem;
  line-height: 1.6;
  color: var(--text-secondary);
  margin-bottom: 1.5rem;
}

.progress-container {
  margin-top: 1.5rem;
}

.progress-bar {
  height: 8px;
  background: rgba(255, 255, 255, 0.1);
  border-radius: 4px;
  overflow: hidden;
  margin-bottom: 0.5rem;
}

.progress-fill {
  height: 100%;
  background: linear-gradient(90deg, var(--primary-400), var(--secondary-400));
  border-radius: 4px;
}

.progress-label {
  font-size: 0.9rem;
  color: var(--text-secondary);
  font-weight: 600;
}

/* Responsive Adjustments */
@media (max-width: 768px) {
  .hero-title {
    font-size: 2.5rem;
  }
  
  .title-subtitle {
    font-size: 2rem;
  }
  
  .pipeline-container {
    flex-direction: column;
    align-items: flex-start;
  }
  
  .pipeline-step {
    flex-direction: row;
    width: 100%;
  }
  
  .pipeline-arrow {
    transform: rotate(90deg);
    margin: 0.5rem 0;
  }
  
  .coming-soon-container {
    flex-direction: column;
    text-align: center;
  }
  
  .guarantee-item {
    flex-direction: column;
    align-items: center;
    text-align: center;
  }
}
</style>