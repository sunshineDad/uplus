<template>
  <TechLayout title="BITCUP Models">
    <div class="bitcup-view">
      <!-- Revolutionary BITCUP Hero with Semantic Visualization -->
      <div class="bitcup-hero">
        <div class="hero-background">
          <div class="semantic-grid">
            <div class="grid-line" v-for="i in 20" :key="`h-${i}`" :style="{ top: `${i * 5}%` }"></div>
            <div class="grid-line vertical" v-for="i in 20" :key="`v-${i}`" :style="{ left: `${i * 5}%` }"></div>
          </div>
          <div class="semantic-nodes">
            <div class="semantic-node entity" :style="{ top: '20%', left: '15%' }">
              <div class="node-core"></div>
              <div class="node-label">Entity</div>
            </div>
            <div class="semantic-node behavior" :style="{ top: '30%', left: '45%' }">
              <div class="node-core"></div>
              <div class="node-label">Behavior</div>
            </div>
            <div class="semantic-node rule" :style="{ top: '50%', left: '25%' }">
              <div class="node-core"></div>
              <div class="node-label">Rule</div>
            </div>
            <div class="semantic-node flow" :style="{ top: '40%', left: '70%' }">
              <div class="node-core"></div>
              <div class="node-label">Flow</div>
            </div>
            <div class="semantic-node event" :style="{ top: '65%', left: '55%' }">
              <div class="node-core"></div>
              <div class="node-label">Event</div>
            </div>
            <div class="semantic-node view" :style="{ top: '70%', left: '80%' }">
              <div class="node-core"></div>
              <div class="node-label">View</div>
            </div>
          </div>
          <div class="semantic-connections">
            <svg class="connection-svg" viewBox="0 0 100 100" preserveAspectRatio="none">
              <path d="M15,20 Q30,35 45,30" stroke="url(#connectionGradient)" stroke-width="0.2" fill="none" opacity="0.6"/>
              <path d="M45,30 Q35,45 25,50" stroke="url(#connectionGradient)" stroke-width="0.2" fill="none" opacity="0.6"/>
              <path d="M45,30 Q57,35 70,40" stroke="url(#connectionGradient)" stroke-width="0.2" fill="none" opacity="0.6"/>
              <path d="M25,50 Q40,57 55,65" stroke="url(#connectionGradient)" stroke-width="0.2" fill="none" opacity="0.6"/>
              <path d="M70,40 Q75,55 80,70" stroke="url(#connectionGradient)" stroke-width="0.2" fill="none" opacity="0.6"/>
              <defs>
                <linearGradient id="connectionGradient" x1="0%" y1="0%" x2="100%" y2="0%">
                  <stop offset="0%" style="stop-color:#3a86ff;stop-opacity:0.8" />
                  <stop offset="100%" style="stop-color:#8338ec;stop-opacity:0.8" />
                </linearGradient>
              </defs>
            </svg>
          </div>
        </div>
        
        <div class="hero-content">
          <div class="hero-text">
            <div class="hero-badge">
              <span class="badge-text">Declarative Semantics</span>
              <div class="badge-pulse"></div>
            </div>
            <h1 class="hero-title">
              <span class="title-main">BITCUP</span>
              <span class="title-subtitle">Modeling Language</span>
            </h1>
            <p class="hero-description">
              Universal semantic language expressing <span class="highlight">"what" not "how"</span> 
              through revolutionary declarative semantics that bridge human intent and machine understanding.
            </p>
            
            <div class="bitcup-formula">
              <div class="formula-container">
                <div class="formula-part">
                  <span class="formula-letter">B</span>
                  <span class="formula-word">Business</span>
                </div>
                <div class="formula-operator">+</div>
                <div class="formula-part">
                  <span class="formula-letter">I</span>
                  <span class="formula-word">Intent</span>
                </div>
                <div class="formula-operator">+</div>
                <div class="formula-part">
                  <span class="formula-letter">T</span>
                  <span class="formula-word">Technology</span>
                </div>
                <div class="formula-operator">+</div>
                <div class="formula-part">
                  <span class="formula-letter">C</span>
                  <span class="formula-word">Constraints</span>
                </div>
                <div class="formula-operator">+</div>
                <div class="formula-part">
                  <span class="formula-letter">U</span>
                  <span class="formula-word">User</span>
                </div>
                <div class="formula-operator">+</div>
                <div class="formula-part">
                  <span class="formula-letter">P</span>
                  <span class="formula-word">Process</span>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
      
      <!-- Revolutionary BITCUP Capabilities Preview -->
      <div class="bitcup-content">
        <div class="capabilities-section">
          <div class="section-header">
            <h2 class="section-title">Core Constructs</h2>
            <p class="section-subtitle">Building blocks of semantic understanding</p>
          </div>
          
          <div class="constructs-grid">
            <div class="construct-card entity-card" v-motion :initial="{ opacity: 0, y: 50 }" :enter="{ opacity: 1, y: 0, transition: { delay: 100 } }">
              <div class="card-background">
                <div class="card-glow entity-glow"></div>
              </div>
              <div class="card-content">
                <div class="construct-icon">
                  <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                    <rect x="3" y="3" width="18" height="18" rx="2" ry="2"/>
                    <line x1="3" y1="9" x2="21" y2="9"/>
                    <line x1="9" y1="21" x2="9" y2="9"/>
                  </svg>
                </div>
                <h3 class="construct-title">Entities</h3>
                <p class="construct-description">Define what exists in your system - the fundamental building blocks of your domain</p>
                <div class="construct-example">
                  <code>Entity User { name, email, role }</code>
                </div>
              </div>
            </div>
            
            <div class="construct-card behavior-card" v-motion :initial="{ opacity: 0, y: 50 }" :enter="{ opacity: 1, y: 0, transition: { delay: 200 } }">
              <div class="card-background">
                <div class="card-glow behavior-glow"></div>
              </div>
              <div class="card-content">
                <div class="construct-icon">
                  <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                    <circle cx="12" cy="12" r="10"/>
                    <path d="M9.09 9a3 3 0 0 1 5.83 1c0 2-3 3-3 3"/>
                    <line x1="12" y1="17" x2="12.01" y2="17"/>
                  </svg>
                </div>
                <h3 class="construct-title">Behaviors</h3>
                <p class="construct-description">Define what your system does - the actions and operations that create value</p>
                <div class="construct-example">
                  <code>Behavior CreateTask { input, validation, output }</code>
                </div>
              </div>
            </div>
            
            <div class="construct-card rule-card" v-motion :initial="{ opacity: 0, y: 50 }" :enter="{ opacity: 1, y: 0, transition: { delay: 300 } }">
              <div class="card-background">
                <div class="card-glow rule-glow"></div>
              </div>
              <div class="card-content">
                <div class="construct-icon">
                  <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                    <path d="M12 2l3.09 6.26L22 9.27l-5 4.87 1.18 6.88L12 17.77l-6.18 3.25L7 14.14 2 9.27l6.91-1.01L12 2z"/>
                  </svg>
                </div>
                <h3 class="construct-title">Rules</h3>
                <p class="construct-description">Define constraints and validations - the business logic that governs behavior</p>
                <div class="construct-example">
                  <code>Rule ValidEmail { pattern: email_regex }</code>
                </div>
              </div>
            </div>
            
            <div class="construct-card flow-card" v-motion :initial="{ opacity: 0, y: 50 }" :enter="{ opacity: 1, y: 0, transition: { delay: 400 } }">
              <div class="card-background">
                <div class="card-glow flow-glow"></div>
              </div>
              <div class="card-content">
                <div class="construct-icon">
                  <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                    <path d="M21 16V8a2 2 0 0 0-1-1.73l-7-4a2 2 0 0 0-2 0l-7 4A2 2 0 0 0 3 8v8a2 2 0 0 0 1 1.73l7 4a2 2 0 0 0 2 0l7-4A2 2 0 0 0 21 16z"/>
                    <polyline points="3.27 6.96 12 12.01 20.73 6.96"/>
                    <line x1="12" y1="22.08" x2="12" y2="12"/>
                  </svg>
                </div>
                <h3 class="construct-title">Flows</h3>
                <p class="construct-description">Define how things connect - the pathways that link entities and behaviors</p>
                <div class="construct-example">
                  <code>Flow UserRegistration { steps, conditions }</code>
                </div>
              </div>
            </div>
            
            <div class="construct-card event-card" v-motion :initial="{ opacity: 0, y: 50 }" :enter="{ opacity: 1, y: 0, transition: { delay: 500 } }">
              <div class="card-background">
                <div class="card-glow event-glow"></div>
              </div>
              <div class="card-content">
                <div class="construct-icon">
                  <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                    <circle cx="12" cy="12" r="3"/>
                    <path d="M12 1v6m0 6v6"/>
                    <path d="M21 12h-6m-6 0H3"/>
                  </svg>
                </div>
                <h3 class="construct-title">Events</h3>
                <p class="construct-description">Define what triggers actions - the signals that initiate behaviors and flows</p>
                <div class="construct-example">
                  <code>Event UserLogin { timestamp, context }</code>
                </div>
              </div>
            </div>
            
            <div class="construct-card view-card" v-motion :initial="{ opacity: 0, y: 50 }" :enter="{ opacity: 1, y: 0, transition: { delay: 600 } }">
              <div class="card-background">
                <div class="card-glow view-glow"></div>
              </div>
              <div class="card-content">
                <div class="construct-icon">
                  <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                    <path d="M1 12s4-8 11-8 11 8 11 8-4 8-11 8-11-8-11-8z"/>
                    <circle cx="12" cy="12" r="3"/>
                  </svg>
                </div>
                <h3 class="construct-title">Views</h3>
                <p class="construct-description">Define how users interact - the interfaces that present and collect information</p>
                <div class="construct-example">
                  <code>View TaskDashboard { layout, components }</code>
                </div>
              </div>
            </div>
          </div>
        </div>
        
        <!-- Revolutionary Preview Section -->
        <div class="preview-section">
          <div class="preview-container">
            <div class="preview-header">
              <h2 class="preview-title">
                <span class="title-icon">
                  <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                    <path d="M12 2l3.09 6.26L22 9.27l-5 4.87 1.18 6.88L12 17.77l-6.18 3.25L7 14.14 2 9.27l6.91-1.01L12 2z"/>
                  </svg>
                </span>
                Revolutionary Capabilities
              </h2>
              <p class="preview-subtitle">Experience the future of semantic modeling</p>
            </div>
            
            <div class="capabilities-showcase">
              <div class="capability-item">
                <div class="capability-icon">
                  <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                    <path d="M21 16V8a2 2 0 0 0-1-1.73l-7-4a2 2 0 0 0-2 0l-7 4A2 2 0 0 0 3 8v8a2 2 0 0 0 1 1.73l7 4a2 2 0 0 0 2 0l7-4A2 2 0 0 0 21 16z"/>
                  </svg>
                </div>
                <div class="capability-content">
                  <h3 class="capability-title">Bidirectional Transformation</h3>
                  <p class="capability-description">Generate BITCUP from requirements and requirements from BITCUP with perfect semantic equivalence</p>
                </div>
              </div>
              
              <div class="capability-item">
                <div class="capability-icon">
                  <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                    <circle cx="12" cy="12" r="10"/>
                    <path d="M12 6v6l4 2"/>
                  </svg>
                </div>
                <div class="capability-content">
                  <h3 class="capability-title">Real-time Validation</h3>
                  <p class="capability-description">Instant semantic validation ensures your models are always consistent and executable</p>
                </div>
              </div>
              
              <div class="capability-item">
                <div class="capability-icon">
                  <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                    <path d="M12 2l3.09 6.26L22 9.27l-5 4.87 1.18 6.88L12 17.77l-6.18 3.25L7 14.14 2 9.27l6.91-1.01L12 2z"/>
                  </svg>
                </div>
                <div class="capability-content">
                  <h3 class="capability-title">Universal Expressiveness</h3>
                  <p class="capability-description">Every conceivable software system can be expressed in BITCUP with mathematical precision</p>
                </div>
              </div>
            </div>
            
            <div class="coming-soon-notice">
              <div class="notice-content">
                <div class="notice-icon">
                  <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                    <circle cx="12" cy="12" r="10"/>
                    <path d="M12 6v6l4 2"/>
                  </svg>
                </div>
                <div class="notice-text">
                  <h3 class="notice-title">Coming in Phase 4</h3>
                  <p class="notice-description">
                    The BITCUP Modeling Language is currently in advanced development. 
                    This revolutionary semantic modeling system will be available in the next major release.
                  </p>
                </div>
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
  name: 'BitcupView',
  components: {
    TechLayout
  }
};
</script>

<style scoped>
/* Revolutionary BITCUP Interface Styling */
.bitcup-view {
  min-height: 100vh;
  background: linear-gradient(135deg, #0a0a0a 0%, #1a1a2e 50%, #16213e 100%);
  position: relative;
  overflow: hidden;
}

/* BITCUP Hero with Semantic Visualization */
.bitcup-hero {
  position: relative;
  padding: 4rem 0 6rem;
  margin-bottom: 4rem;
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

/* Semantic Grid Animation */
.semantic-grid {
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  opacity: 0.1;
}

.grid-line {
  position: absolute;
  background: linear-gradient(90deg, transparent 0%, #3a86ff 50%, transparent 100%);
  height: 1px;
  width: 100%;
  animation: grid-pulse 4s infinite ease-in-out;
}

.grid-line.vertical {
  background: linear-gradient(0deg, transparent 0%, #8338ec 50%, transparent 100%);
  width: 1px;
  height: 100%;
  top: 0;
  left: 0;
}

@keyframes grid-pulse {
  0%, 100% { opacity: 0.1; }
  50% { opacity: 0.3; }
}

/* Semantic Nodes */
.semantic-nodes {
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  z-index: 2;
}

.semantic-node {
  position: absolute;
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 0.5rem;
  animation: node-float 6s infinite ease-in-out;
}

.semantic-node.entity { animation-delay: 0s; }
.semantic-node.behavior { animation-delay: 1s; }
.semantic-node.rule { animation-delay: 2s; }
.semantic-node.flow { animation-delay: 3s; }
.semantic-node.event { animation-delay: 4s; }
.semantic-node.view { animation-delay: 5s; }

@keyframes node-float {
  0%, 100% { transform: translateY(0) scale(1); }
  50% { transform: translateY(-10px) scale(1.1); }
}

.node-core {
  width: 12px;
  height: 12px;
  border-radius: 50%;
  background: radial-gradient(circle, #3a86ff 0%, #8338ec 100%);
  box-shadow: 0 0 20px rgba(58, 134, 255, 0.6);
  animation: node-pulse 2s infinite ease-in-out;
}

@keyframes node-pulse {
  0%, 100% { 
    transform: scale(1); 
    box-shadow: 0 0 20px rgba(58, 134, 255, 0.6);
  }
  50% { 
    transform: scale(1.3); 
    box-shadow: 0 0 30px rgba(58, 134, 255, 0.8);
  }
}

.node-label {
  font-size: 0.75rem;
  font-weight: 600;
  color: rgba(255, 255, 255, 0.8);
  text-transform: uppercase;
  letter-spacing: 0.1em;
  text-align: center;
}

/* Semantic Connections */
.semantic-connections {
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  z-index: 1;
}

.connection-svg {
  width: 100%;
  height: 100%;
  position: absolute;
  top: 0;
  left: 0;
}

.connection-svg path {
  animation: connection-flow 3s infinite ease-in-out;
}

@keyframes connection-flow {
  0%, 100% { stroke-dasharray: 0, 100; }
  50% { stroke-dasharray: 50, 50; }
}

/* Hero Content */
.hero-content {
  position: relative;
  z-index: 3;
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 2rem;
  text-align: center;
}

.hero-text {
  max-width: 800px;
  margin: 0 auto;
}

.hero-badge {
  position: relative;
  display: inline-flex;
  align-items: center;
  padding: 0.75rem 2rem;
  background: rgba(255, 255, 255, 0.05);
  border: 1px solid rgba(255, 255, 255, 0.1);
  border-radius: 50px;
  backdrop-filter: blur(10px);
  margin-bottom: 2rem;
  overflow: hidden;
}

.badge-text {
  font-size: 0.875rem;
  font-weight: 600;
  color: var(--white);
  text-transform: uppercase;
  letter-spacing: 0.1em;
  position: relative;
  z-index: 2;
}

.badge-pulse {
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: linear-gradient(90deg, transparent, rgba(58, 134, 255, 0.2), transparent);
  animation: badge-pulse 3s infinite ease-in-out;
}

@keyframes badge-pulse {
  0%, 100% { transform: translateX(-100%); }
  50% { transform: translateX(100%); }
}

.hero-title {
  margin-bottom: 2rem;
}

.title-main {
  display: block;
  font-size: 4rem;
  font-weight: 900;
  background: linear-gradient(135deg, #3a86ff 0%, #8338ec 100%);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
  line-height: 1;
  margin-bottom: 0.5rem;
  letter-spacing: -0.02em;
}

.title-subtitle {
  display: block;
  font-size: 1.75rem;
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

/* BITCUP Formula */
.bitcup-formula {
  margin-top: 3rem;
}

.formula-container {
  display: flex;
  align-items: center;
  justify-content: center;
  flex-wrap: wrap;
  gap: 1rem;
  padding: 2rem;
  background: rgba(255, 255, 255, 0.03);
  border: 1px solid rgba(255, 255, 255, 0.1);
  border-radius: 1rem;
  backdrop-filter: blur(20px);
}

.formula-part {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 0.5rem;
  padding: 1rem;
  background: rgba(255, 255, 255, 0.05);
  border-radius: 0.75rem;
  transition: all 0.3s ease;
}

.formula-part:hover {
  background: rgba(255, 255, 255, 0.1);
  transform: translateY(-2px);
}

.formula-letter {
  font-size: 2rem;
  font-weight: 800;
  color: #3a86ff;
  text-shadow: 0 0 20px rgba(58, 134, 255, 0.5);
}

.formula-word {
  font-size: 0.875rem;
  font-weight: 600;
  color: rgba(255, 255, 255, 0.8);
  text-transform: uppercase;
  letter-spacing: 0.1em;
}

.formula-operator {
  font-size: 1.5rem;
  font-weight: 600;
  color: rgba(255, 255, 255, 0.6);
}

/* BITCUP Content */
.bitcup-content {
  position: relative;
  z-index: 2;
  padding: 0 2rem 4rem;
}

/* Capabilities Section */
.capabilities-section {
  max-width: 1400px;
  margin: 0 auto 6rem;
}

.section-header {
  text-align: center;
  margin-bottom: 4rem;
}

.section-title {
  font-size: 3rem;
  font-weight: 700;
  color: var(--white);
  margin-bottom: 1rem;
}

.section-subtitle {
  font-size: 1.25rem;
  color: rgba(255, 255, 255, 0.7);
}

/* Constructs Grid */
.constructs-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(350px, 1fr));
  gap: 2rem;
}

.construct-card {
  position: relative;
  height: 300px;
  border-radius: 1.5rem;
  overflow: hidden;
  transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
}

.construct-card:hover {
  transform: translateY(-8px) scale(1.02);
}

.card-background {
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

.construct-card:hover .card-background {
  background: linear-gradient(135deg, 
    rgba(255, 255, 255, 0.1) 0%, 
    rgba(255, 255, 255, 0.05) 100%);
  border-color: rgba(255, 255, 255, 0.2);
}

.card-glow {
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  opacity: 0;
  transition: opacity 0.4s ease;
}

.construct-card:hover .card-glow {
  opacity: 1;
}

.entity-glow {
  background: radial-gradient(circle at 50% 50%, rgba(58, 134, 255, 0.1) 0%, transparent 70%);
}

.behavior-glow {
  background: radial-gradient(circle at 50% 50%, rgba(131, 56, 236, 0.1) 0%, transparent 70%);
}

.rule-glow {
  background: radial-gradient(circle at 50% 50%, rgba(255, 0, 110, 0.1) 0%, transparent 70%);
}

.flow-glow {
  background: radial-gradient(circle at 50% 50%, rgba(255, 190, 11, 0.1) 0%, transparent 70%);
}

.event-glow {
  background: radial-gradient(circle at 50% 50%, rgba(6, 214, 160, 0.1) 0%, transparent 70%);
}

.view-glow {
  background: radial-gradient(circle at 50% 50%, rgba(255, 95, 109, 0.1) 0%, transparent 70%);
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

.construct-icon {
  width: 60px;
  height: 60px;
  padding: 1rem;
  background: rgba(255, 255, 255, 0.1);
  border-radius: 1rem;
  display: flex;
  align-items: center;
  justify-content: center;
  margin-bottom: 1.5rem;
  transition: all 0.3s ease;
}

.construct-icon svg {
  width: 28px;
  height: 28px;
  stroke: #3a86ff;
}

.construct-card:hover .construct-icon {
  background: rgba(255, 255, 255, 0.2);
  transform: scale(1.1);
}

.construct-title {
  font-size: 1.5rem;
  font-weight: 700;
  margin-bottom: 1rem;
  line-height: 1.3;
}

.construct-description {
  font-size: 1rem;
  line-height: 1.5;
  color: rgba(255, 255, 255, 0.7);
  margin-bottom: 1.5rem;
  flex: 1;
}

.construct-example {
  padding: 1rem;
  background: rgba(0, 0, 0, 0.3);
  border-radius: 0.5rem;
  border-left: 3px solid #3a86ff;
}

.construct-example code {
  font-family: 'JetBrains Mono', 'Fira Code', monospace;
  font-size: 0.875rem;
  color: #6ea8ff;
  font-weight: 500;
}

/* Preview Section */
.preview-section {
  max-width: 1200px;
  margin: 0 auto;
}

.preview-container {
  background: rgba(255, 255, 255, 0.03);
  border: 1px solid rgba(255, 255, 255, 0.1);
  border-radius: 2rem;
  backdrop-filter: blur(20px);
  overflow: hidden;
}

.preview-header {
  text-align: center;
  padding: 3rem 2rem 2rem;
  border-bottom: 1px solid rgba(255, 255, 255, 0.1);
}

.preview-title {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 1rem;
  font-size: 2.5rem;
  font-weight: 700;
  color: var(--white);
  margin-bottom: 1rem;
}

.title-icon {
  width: 40px;
  height: 40px;
  padding: 0.5rem;
  background: linear-gradient(135deg, rgba(58, 134, 255, 0.2) 0%, rgba(131, 56, 236, 0.2) 100%);
  border-radius: 0.75rem;
  display: flex;
  align-items: center;
  justify-content: center;
}

.title-icon svg {
  width: 24px;
  height: 24px;
  stroke: #3a86ff;
}

.preview-subtitle {
  font-size: 1.25rem;
  color: rgba(255, 255, 255, 0.7);
}

/* Capabilities Showcase */
.capabilities-showcase {
  padding: 3rem 2rem;
  display: flex;
  flex-direction: column;
  gap: 2rem;
}

.capability-item {
  display: flex;
  align-items: flex-start;
  gap: 2rem;
  padding: 2rem;
  background: rgba(255, 255, 255, 0.03);
  border-radius: 1rem;
  transition: all 0.3s ease;
}

.capability-item:hover {
  background: rgba(255, 255, 255, 0.05);
  transform: translateX(10px);
}

.capability-icon {
  width: 60px;
  height: 60px;
  padding: 1rem;
  background: linear-gradient(135deg, rgba(58, 134, 255, 0.2) 0%, rgba(131, 56, 236, 0.2) 100%);
  border-radius: 1rem;
  display: flex;
  align-items: center;
  justify-content: center;
  flex-shrink: 0;
}

.capability-icon svg {
  width: 28px;
  height: 28px;
  stroke: #3a86ff;
}

.capability-content {
  flex: 1;
}

.capability-title {
  font-size: 1.5rem;
  font-weight: 700;
  color: var(--white);
  margin-bottom: 0.75rem;
}

.capability-description {
  font-size: 1.1rem;
  line-height: 1.6;
  color: rgba(255, 255, 255, 0.7);
}

/* Coming Soon Notice */
.coming-soon-notice {
  padding: 3rem 2rem;
  border-top: 1px solid rgba(255, 255, 255, 0.1);
}

.notice-content {
  display: flex;
  align-items: center;
  gap: 2rem;
  max-width: 800px;
  margin: 0 auto;
}

.notice-icon {
  width: 80px;
  height: 80px;
  padding: 1.5rem;
  background: linear-gradient(135deg, rgba(255, 190, 11, 0.2) 0%, rgba(255, 95, 109, 0.2) 100%);
  border-radius: 1.5rem;
  display: flex;
  align-items: center;
  justify-content: center;
  flex-shrink: 0;
}

.notice-icon svg {
  width: 40px;
  height: 40px;
  stroke: #ffbe0b;
}

.notice-text {
  flex: 1;
}

.notice-title {
  font-size: 1.75rem;
  font-weight: 700;
  color: var(--white);
  margin-bottom: 1rem;
}

.notice-description {
  font-size: 1.1rem;
  line-height: 1.6;
  color: rgba(255, 255, 255, 0.7);
}

/* Responsive Design */
@media (max-width: 1024px) {
  .title-main {
    font-size: 3rem;
  }
  
  .formula-container {
    flex-direction: column;
    gap: 0.5rem;
  }
  
  .formula-part {
    flex-direction: row;
    gap: 1rem;
  }
  
  .constructs-grid {
    grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
  }
  
  .capability-item {
    flex-direction: column;
    text-align: center;
  }
  
  .notice-content {
    flex-direction: column;
    text-align: center;
  }
}

@media (max-width: 768px) {
  .bitcup-hero {
    padding: 3rem 0 4rem;
  }
  
  .hero-content {
    padding: 0 1rem;
  }
  
  .title-main {
    font-size: 2.5rem;
  }
  
  .title-subtitle {
    font-size: 1.5rem;
  }
  
  .section-title {
    font-size: 2rem;
  }
  
  .constructs-grid {
    grid-template-columns: 1fr;
    gap: 1.5rem;
  }
  
  .construct-card {
    height: 280px;
  }
  
  .preview-header {
    padding: 2rem 1rem 1.5rem;
  }
  
  .preview-title {
    font-size: 2rem;
    flex-direction: column;
  }
  
  .capabilities-showcase {
    padding: 2rem 1rem;
  }
}

@media (max-width: 480px) {
  .bitcup-content {
    padding: 0 1rem 2rem;
  }
  
  .title-main {
    font-size: 2rem;
  }
  
  .formula-container {
    padding: 1rem;
  }
  
  .formula-part {
    padding: 0.75rem;
  }
  
  .construct-card {
    height: 260px;
  }
  
  .card-content {
    padding: 1.5rem;
  }
  
  .construct-icon {
    width: 50px;
    height: 50px;
  }
}
</style>
