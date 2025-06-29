<template>
  <TechLayout title="Document Memory Intelligence">
    <div class="memory-view">
      <!-- Revolutionary Memory Intelligence Hero -->
      <div class="memory-hero">
        <div class="hero-background">
          <div class="knowledge-graph">
            <svg class="graph-svg" viewBox="0 0 1000 600" preserveAspectRatio="none">
              <!-- Knowledge Graph Nodes -->
              <g class="graph-nodes">
                <circle class="graph-node" cx="500" cy="300" r="20" />
                <circle class="graph-node" cx="350" cy="200" r="15" />
                <circle class="graph-node" cx="650" cy="200" r="15" />
                <circle class="graph-node" cx="250" cy="350" r="12" />
                <circle class="graph-node" cx="450" cy="450" r="12" />
                <circle class="graph-node" cx="550" cy="450" r="12" />
                <circle class="graph-node" cx="750" cy="350" r="12" />
                <circle class="graph-node" cx="400" cy="150" r="10" />
                <circle class="graph-node" cx="600" cy="150" r="10" />
                <circle class="graph-node" cx="300" cy="250" r="10" />
                <circle class="graph-node" cx="700" cy="250" r="10" />
                <circle class="graph-node" cx="200" cy="400" r="10" />
                <circle class="graph-node" cx="300" cy="450" r="10" />
                <circle class="graph-node" cx="700" cy="450" r="10" />
                <circle class="graph-node" cx="800" cy="400" r="10" />
              </g>
              
              <!-- Knowledge Graph Connections -->
              <g class="graph-connections">
                <path class="graph-connection" d="M500,300 L350,200" />
                <path class="graph-connection" d="M500,300 L650,200" />
                <path class="graph-connection" d="M500,300 L450,450" />
                <path class="graph-connection" d="M500,300 L550,450" />
                <path class="graph-connection" d="M350,200 L250,350" />
                <path class="graph-connection" d="M350,200 L400,150" />
                <path class="graph-connection" d="M350,200 L300,250" />
                <path class="graph-connection" d="M650,200 L750,350" />
                <path class="graph-connection" d="M650,200 L600,150" />
                <path class="graph-connection" d="M650,200 L700,250" />
                <path class="graph-connection" d="M250,350 L200,400" />
                <path class="graph-connection" d="M250,350 L300,450" />
                <path class="graph-connection" d="M750,350 L700,450" />
                <path class="graph-connection" d="M750,350 L800,400" />
                <path class="graph-connection" d="M450,450 L300,450" />
                <path class="graph-connection" d="M550,450 L700,450" />
                <path class="graph-connection" d="M400,150 L600,150" />
              </g>
              
              <!-- Animated Pulses -->
              <g class="graph-pulses">
                <circle class="pulse-circle" cx="500" cy="300" r="5">
                  <animate attributeName="r" from="5" to="30" dur="3s" begin="0s" repeatCount="indefinite" />
                  <animate attributeName="opacity" from="1" to="0" dur="3s" begin="0s" repeatCount="indefinite" />
                </circle>
                <circle class="pulse-circle" cx="350" cy="200" r="5">
                  <animate attributeName="r" from="5" to="20" dur="3s" begin="1s" repeatCount="indefinite" />
                  <animate attributeName="opacity" from="1" to="0" dur="3s" begin="1s" repeatCount="indefinite" />
                </circle>
                <circle class="pulse-circle" cx="650" cy="200" r="5">
                  <animate attributeName="r" from="5" to="20" dur="3s" begin="2s" repeatCount="indefinite" />
                  <animate attributeName="opacity" from="1" to="0" dur="3s" begin="2s" repeatCount="indefinite" />
                </circle>
              </g>
              
              <!-- Data Flow Animations -->
              <g class="data-flows">
                <circle class="data-particle" r="3">
                  <animateMotion path="M500,300 L350,200" dur="2s" begin="0s" repeatCount="indefinite" />
                </circle>
                <circle class="data-particle" r="3">
                  <animateMotion path="M500,300 L650,200" dur="2s" begin="0.5s" repeatCount="indefinite" />
                </circle>
                <circle class="data-particle" r="3">
                  <animateMotion path="M350,200 L250,350" dur="2s" begin="1s" repeatCount="indefinite" />
                </circle>
                <circle class="data-particle" r="3">
                  <animateMotion path="M650,200 L750,350" dur="2s" begin="1.5s" repeatCount="indefinite" />
                </circle>
              </g>
            </svg>
          </div>
          
          <div class="memory-particles">
            <div v-for="i in 30" :key="`particle-${i}`" class="memory-particle" 
                 :style="{ 
                   left: `${Math.random() * 100}%`, 
                   top: `${Math.random() * 100}%`,
                   animationDelay: `${Math.random() * 5}s`,
                   animationDuration: `${5 + Math.random() * 10}s`
                 }">
            </div>
          </div>
        </div>
        
        <div class="hero-content">
          <div class="hero-text">
            <div class="hero-badge">
              <span class="badge-text">Temporal Knowledge Graph</span>
              <div class="badge-pulse"></div>
            </div>
            <h1 class="hero-title">
              <span class="title-main">Memory Intelligence</span>
              <span class="title-subtitle">Organizational Brain</span>
            </h1>
            <p class="hero-description">
              Create an <span class="highlight">immortal, ever-learning organizational brain</span> 
              through revolutionary Temporal Knowledge Graph technology that preserves all decisions
              and their context.
            </p>
            
            <div class="memory-architecture">
              <div class="architecture-container">
                <div class="architecture-step" v-motion :initial="{ opacity: 0, x: -50 }" :enter="{ opacity: 1, x: 0, transition: { delay: 100 } }">
                  <div class="step-icon">
                    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                      <circle cx="12" cy="12" r="10"/>
                      <path d="M12 16v-4"/>
                      <path d="M12 8h.01"/>
                    </svg>
                  </div>
                  <div class="step-label">Events</div>
                </div>
                <div class="architecture-arrow">→</div>
                <div class="architecture-step" v-motion :initial="{ opacity: 0, x: -50 }" :enter="{ opacity: 1, x: 0, transition: { delay: 200 } }">
                  <div class="step-icon">
                    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                      <path d="M21 16V8a2 2 0 0 0-1-1.73l-7-4a2 2 0 0 0-2 0l-7 4A2 2 0 0 0 3 8v8a2 2 0 0 0 1 1.73l7 4a2 2 0 0 0 2 0l7-4A2 2 0 0 0 21 16z"/>
                    </svg>
                  </div>
                  <div class="step-label">Knowledge Graph</div>
                </div>
                <div class="architecture-arrow">→</div>
                <div class="architecture-step" v-motion :initial="{ opacity: 0, x: -50 }" :enter="{ opacity: 1, x: 0, transition: { delay: 300 } }">
                  <div class="step-icon">
                    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                      <path d="M12 2l3.09 6.26L22 9.27l-5 4.87 1.18 6.88L12 17.77l-6.18 3.25L7 14.14 2 9.27l6.91-1.01L12 2z"/>
                    </svg>
                  </div>
                  <div class="step-label">Insights</div>
                </div>
                <div class="architecture-arrow">→</div>
                <div class="architecture-step" v-motion :initial="{ opacity: 0, x: -50 }" :enter="{ opacity: 1, x: 0, transition: { delay: 400 } }">
                  <div class="step-icon">
                    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                      <polyline points="16 18 22 12 16 6"/>
                      <polyline points="8 6 2 12 8 18"/>
                    </svg>
                  </div>
                  <div class="step-label">Recommendations</div>
                </div>
              </div>
              
              <div class="feedback-loop">
                <svg viewBox="0 0 100 20" preserveAspectRatio="none">
                  <path d="M 95,10 C 80,0 20,0 5,10" fill="none" stroke="currentColor" stroke-width="1" />
                  <polygon points="5,10 8,7 8,13" fill="currentColor" />
                </svg>
                <div class="loop-label">Continuous Learning Loop</div>
              </div>
            </div>
          </div>
        </div>
      </div>
      
      <!-- Revolutionary Memory Intelligence Capabilities -->
      <div class="memory-content">
        <div class="capabilities-section">
          <div class="section-header">
            <h2 class="section-title">Key Innovations</h2>
            <p class="section-subtitle">Beyond traditional knowledge management</p>
          </div>
          
          <div class="capabilities-grid">
            <div class="capability-card" v-motion :initial="{ opacity: 0, y: 50 }" :enter="{ opacity: 1, y: 0, transition: { delay: 100 } }">
              <div class="card-background">
                <div class="card-glow"></div>
              </div>
              <div class="card-content">
                <div class="capability-icon">
                  <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                    <path d="M21 16V8a2 2 0 0 0-1-1.73l-7-4a2 2 0 0 0-2 0l-7 4A2 2 0 0 0 3 8v8a2 2 0 0 0 1 1.73l7 4a2 2 0 0 0 2 0l7-4A2 2 0 0 0 21 16z"/>
                  </svg>
                </div>
                <h3 class="capability-title">Active Memory</h3>
                <p class="capability-description">
                  Unlike passive storage systems, our memory intelligence actively understands
                  information, proactively surfaces relevant insights, and identifies patterns
                  before humans notice them.
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
                    <circle cx="12" cy="12" r="10"/>
                    <path d="M12 6v6l4 2"/>
                  </svg>
                </div>
                <h3 class="capability-title">Temporal Reasoning</h3>
                <p class="capability-description">
                  The system understands time-based relationships, tracking how decisions and
                  their contexts evolve over time, enabling you to understand the "why" behind
                  historical choices.
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
                <h3 class="capability-title">Pattern Recognition</h3>
                <p class="capability-description">
                  Advanced algorithms identify recurring patterns across projects and time,
                  recognizing both success patterns to replicate and failure patterns to avoid.
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
                    <path d="M13 2L3 14h9l-1 8 10-12h-9l1-8z"/>
                  </svg>
                </div>
                <h3 class="capability-title">Predictive Warnings</h3>
                <p class="capability-description">
                  The system predicts potential issues before they occur, based on historical
                  patterns and current project trajectories, enabling proactive problem-solving.
                </p>
              </div>
            </div>
          </div>
        </div>
        
        <!-- Intelligence Capabilities Section -->
        <div class="intelligence-section">
          <div class="section-header">
            <h2 class="section-title">Intelligence Capabilities</h2>
            <p class="section-subtitle">How the organizational brain transforms your team</p>
          </div>
          
          <div class="intelligence-list">
            <div class="intelligence-item" v-motion :initial="{ opacity: 0, x: -50 }" :enter="{ opacity: 1, x: 0, transition: { delay: 100 } }">
              <div class="intelligence-icon">
                <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                  <circle cx="12" cy="12" r="10"/>
                  <path d="M12 6v6l4 2"/>
                </svg>
              </div>
              <div class="intelligence-content">
                <h3 class="intelligence-title">Temporal Reasoning</h3>
                <p class="intelligence-description">
                  "Why did we make this decision 6 months ago?" The system preserves the complete
                  context of every decision, including the information available at the time.
                </p>
                <div class="intelligence-example">
                  <div class="example-header">Example Query:</div>
                  <div class="example-query">"What factors influenced our technology stack choice in March?"</div>
                </div>
              </div>
            </div>
            
            <div class="intelligence-item" v-motion :initial="{ opacity: 0, x: -50 }" :enter="{ opacity: 1, x: 0, transition: { delay: 200 } }">
              <div class="intelligence-icon">
                <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                  <path d="M21 16V8a2 2 0 0 0-1-1.73l-7-4a2 2 0 0 0-2 0l-7 4A2 2 0 0 0 3 8v8a2 2 0 0 0 1 1.73l7 4a2 2 0 0 0 2 0l7-4A2 2 0 0 0 21 16z"/>
                  <polyline points="3.27 6.96 12 12.01 20.73 6.96"/>
                  <line x1="12" y1="22.08" x2="12" y2="12"/>
                </svg>
              </div>
              <div class="intelligence-content">
                <h3 class="intelligence-title">Impact Analysis</h3>
                <p class="intelligence-description">
                  "What happens if we change this?" The system models potential ripple effects
                  of changes based on historical dependencies and system understanding.
                </p>
                <div class="intelligence-example">
                  <div class="example-header">Example Query:</div>
                  <div class="example-query">"What systems would be affected if we change our authentication service?"</div>
                </div>
              </div>
            </div>
            
            <div class="intelligence-item" v-motion :initial="{ opacity: 0, x: -50 }" :enter="{ opacity: 1, x: 0, transition: { delay: 300 } }">
              <div class="intelligence-icon">
                <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                  <path d="M12 2l3.09 6.26L22 9.27l-5 4.87 1.18 6.88L12 17.77l-6.18 3.25L7 14.14 2 9.27l6.91-1.01L12 2z"/>
                </svg>
              </div>
              <div class="intelligence-content">
                <h3 class="intelligence-title">Pattern Detection</h3>
                <p class="intelligence-description">
                  "This is similar to a problem we solved before." The system recognizes when current
                  challenges match historical situations, suggesting proven solutions.
                </p>
                <div class="intelligence-example">
                  <div class="example-header">Example Query:</div>
                  <div class="example-query">"Have we solved a similar performance bottleneck before?"</div>
                </div>
              </div>
            </div>
            
            <div class="intelligence-item" v-motion :initial="{ opacity: 0, x: -50 }" :enter="{ opacity: 1, x: 0, transition: { delay: 400 } }">
              <div class="intelligence-icon">
                <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                  <path d="M13 2L3 14h9l-1 8 10-12h-9l1-8z"/>
                </svg>
              </div>
              <div class="intelligence-content">
                <h3 class="intelligence-title">Predictive Warnings</h3>
                <p class="intelligence-description">
                  "This approach failed in 3 previous projects." The system proactively warns about
                  approaches that historically led to problems.
                </p>
                <div class="intelligence-example">
                  <div class="example-header">Example Alert:</div>
                  <div class="example-query">"Warning: Similar architecture choices led to scaling issues in Projects A, B, and C."</div>
                </div>
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
              <h2 class="coming-soon-title">Coming in Phase 4</h2>
              <p class="coming-soon-description">
                The Document Memory Intelligence module is currently in advanced development. This revolutionary
                organizational brain will be available in the next major release, bringing unprecedented
                capabilities to preserve and leverage your team's collective knowledge.
              </p>
              <div class="progress-container">
                <div class="progress-bar">
                  <div class="progress-fill" style="width: 45%"></div>
                </div>
                <div class="progress-label">Development Progress: 45%</div>
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
  name: 'MemoryView',
  components: {
    TechLayout
  }
};
</script>

<style scoped>
/* Revolutionary Memory Intelligence Styling */
.memory-view {
  min-height: 100vh;
  background: linear-gradient(135deg, #0a0a0a 0%, #1a1a2e 50%, #16213e 100%);
}

/* Hero Section */
.memory-hero {
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

.knowledge-graph {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  opacity: 0.3;
}

.graph-svg {
  width: 100%;
  height: 100%;
}

.graph-node {
  fill: var(--secondary-400);
  opacity: 0.7;
}

.graph-connection {
  stroke: var(--secondary-400);
  stroke-width: 1;
  opacity: 0.3;
}

.pulse-circle {
  fill: var(--secondary-400);
  opacity: 0.7;
}

.data-particle {
  fill: var(--primary-400);
  opacity: 0.8;
}

.memory-particles {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
}

.memory-particle {
  position: absolute;
  width: 5px;
  height: 5px;
  background: radial-gradient(circle, var(--secondary-400) 0%, transparent 70%);
  border-radius: 50%;
  opacity: 0.5;
  animation: float-memory-particle 15s ease-in-out infinite;
}

@keyframes float-memory-particle {
  0%, 100% {
    transform: translate(0, 0) scale(1);
    opacity: 0.5;
  }
  50% {
    transform: translate(30px, -30px) scale(1.5);
    opacity: 0.8;
  }
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
  background: rgba(131, 56, 236, 0.1);
  border: 1px solid var(--secondary-400);
  border-radius: 20px;
  padding: 0.5rem 1rem;
  margin-bottom: 1.5rem;
  position: relative;
}

.badge-text {
  font-size: 0.9rem;
  font-weight: 600;
  color: var(--secondary-400);
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
  background: var(--secondary-400);
  border-radius: 50%;
  animation: pulse 2s infinite;
}

@keyframes pulse {
  0% {
    box-shadow: 0 0 0 0 rgba(131, 56, 236, 0.7);
  }
  70% {
    box-shadow: 0 0 0 10px rgba(131, 56, 236, 0);
  }
  100% {
    box-shadow: 0 0 0 0 rgba(131, 56, 236, 0);
  }
}

.hero-title {
  font-size: 3.5rem;
  font-weight: 800;
  margin-bottom: 1.5rem;
  line-height: 1.1;
  background: linear-gradient(90deg, var(--secondary-400), var(--primary-400));
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

/* Memory Architecture */
.memory-architecture {
  margin-top: 3rem;
}

.architecture-container {
  display: flex;
  align-items: center;
  flex-wrap: wrap;
  gap: 1rem;
  background: rgba(0, 0, 0, 0.2);
  border-radius: 12px;
  padding: 1.5rem;
  border: 1px solid rgba(131, 56, 236, 0.2);
  margin-bottom: 1.5rem;
}

.architecture-step {
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
  background: rgba(131, 56, 236, 0.1);
  border-radius: 50%;
  color: var(--secondary-400);
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

.architecture-arrow {
  color: var(--secondary-400);
  font-size: 1.5rem;
  opacity: 0.7;
}

.feedback-loop {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 0.5rem;
  color: var(--secondary-400);
  opacity: 0.7;
}

.feedback-loop svg {
  width: 100%;
  height: 2rem;
}

.loop-label {
  font-size: 0.9rem;
  font-weight: 600;
}

/* Capabilities Section */
.memory-content {
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
  background: linear-gradient(90deg, var(--secondary-400), var(--primary-400));
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
  border: 1px solid rgba(131, 56, 236, 0.2);
  z-index: 0;
}

.card-glow {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: radial-gradient(circle at 50% 0%, rgba(131, 56, 236, 0.2) 0%, transparent 70%);
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
  background: rgba(131, 56, 236, 0.1);
  border-radius: 50%;
  color: var(--secondary-400);
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

/* Intelligence Section */
.intelligence-section {
  margin-bottom: 4rem;
}

.intelligence-list {
  display: flex;
  flex-direction: column;
  gap: 1.5rem;
}

.intelligence-item {
  display: flex;
  align-items: flex-start;
  gap: 1.5rem;
  background: rgba(0, 0, 0, 0.2);
  border-radius: 12px;
  padding: 1.5rem;
  border: 1px solid rgba(131, 56, 236, 0.2);
}

.intelligence-icon {
  width: 3rem;
  height: 3rem;
  min-width: 3rem;
  display: flex;
  align-items: center;
  justify-content: center;
  background: rgba(131, 56, 236, 0.1);
  border-radius: 50%;
  color: var(--secondary-400);
}

.intelligence-icon svg {
  width: 1.5rem;
  height: 1.5rem;
}

.intelligence-content {
  flex: 1;
}

.intelligence-title {
  font-size: 1.2rem;
  font-weight: 700;
  margin-bottom: 0.5rem;
  color: var(--text-primary);
}

.intelligence-description {
  font-size: 1rem;
  line-height: 1.6;
  color: var(--text-secondary);
  margin-bottom: 1rem;
}

.intelligence-example {
  background: rgba(0, 0, 0, 0.3);
  border-radius: 8px;
  padding: 1rem;
  border-left: 3px solid var(--secondary-400);
}

.example-header {
  font-size: 0.9rem;
  font-weight: 600;
  color: var(--secondary-400);
  margin-bottom: 0.5rem;
}

.example-query {
  font-family: var(--font-mono);
  font-size: 0.9rem;
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
  background: linear-gradient(90deg, var(--secondary-400), var(--primary-400));
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
  
  .architecture-container {
    flex-direction: column;
    align-items: flex-start;
  }
  
  .architecture-step {
    flex-direction: row;
    width: 100%;
  }
  
  .architecture-arrow {
    transform: rotate(90deg);
    margin: 0.5rem 0;
  }
  
  .coming-soon-container {
    flex-direction: column;
    text-align: center;
  }
  
  .intelligence-item {
    flex-direction: column;
    align-items: center;
    text-align: center;
  }
}
</style>