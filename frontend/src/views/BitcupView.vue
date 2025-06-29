<template>
  <TechLayout title="BITCUP Models">
    <div class="bitcup-view">
      <div class="bitcup-header">
        <h1 class="bitcup-title">BITCUP Modeling Language</h1>
        <p class="bitcup-subtitle">Universal semantic language that expresses "what" not "how"</p>
      </div>
      
      <div class="coming-soon">
        <div class="coming-soon-icon">
          <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
            <polyline points="16 18 22 12 16 6"></polyline>
            <polyline points="8 6 2 12 8 18"></polyline>
          </svg>
        </div>
        <h2 class="coming-soon-title">BITCUP Modeling</h2>
        <p class="coming-soon-text">This feature is coming soon in the next phase of development.</p>
        <p class="coming-soon-description">
          BITCUP = Business + Intent + Technology + Constraints + User + Process
          <br><br>
          The BITCUP Modeling Language will allow you to create and manage semantic models that describe your software systems in business terms, not technical implementation details. These models will be used to automatically generate code and documentation.
        </p>
        <div class="bitcup-features">
          <div class="feature-card">
            <div class="feature-icon">
              <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                <rect x="3" y="3" width="18" height="18" rx="2" ry="2"></rect>
                <line x1="3" y1="9" x2="21" y2="9"></line>
                <line x1="9" y1="21" x2="9" y2="9"></line>
              </svg>
            </div>
            <h3 class="feature-title">Entities</h3>
            <p class="feature-description">Define what exists in your system</p>
          </div>
          
          <div class="feature-card">
            <div class="feature-icon">
              <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                <circle cx="12" cy="12" r="10"></circle>
                <path d="M9.09 9a3 3 0 0 1 5.83 1c0 2-3 3-3 3"></path>
                <line x1="12" y1="17" x2="12.01" y2="17"></line>
              </svg>
            </div>
            <h3 class="feature-title">Behaviors</h3>
            <p class="feature-description">Define what your system does</p>
          </div>
          
          <div class="feature-card">
            <div class="feature-icon">
              <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                <path d="M22 12h-4l-3 9L9 3l-3 9H2"></path>
              </svg>
            </div>
            <h3 class="feature-title">Flows</h3>
            <p class="feature-description">Define how things connect</p>
          </div>
          
          <div class="feature-card">
            <div class="feature-icon">
              <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                <path d="M18 13v6a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h6"></path>
                <polyline points="15 3 21 3 21 9"></polyline>
                <line x1="10" y1="14" x2="21" y2="3"></line>
              </svg>
            </div>
            <h3 class="feature-title">Events</h3>
            <p class="feature-description">Define what triggers actions</p>
          </div>
        </div>
        
        <router-link to="/ai-pm" class="btn btn-primary">
          Go to AI-PM to Generate Requirements
        </router-link>
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
.bitcup-view {
  display: flex;
  flex-direction: column;
  gap: 2rem;
}

.bitcup-header {
  text-align: center;
  margin-bottom: 1rem;
}

.bitcup-title {
  font-size: 2.5rem;
  font-weight: 700;
  margin-bottom: 0.5rem;
  background: var(--gradient-secondary);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  animation: text-shine 3s linear infinite;
}

.bitcup-subtitle {
  font-size: 1.25rem;
  color: var(--gray-600);
}

.coming-soon {
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

.coming-soon-icon {
  display: flex;
  align-items: center;
  justify-content: center;
  width: 100px;
  height: 100px;
  margin-bottom: 1.5rem;
  background-color: var(--secondary-light);
  color: var(--white);
  border-radius: var(--border-radius-circle);
}

.coming-soon-icon svg {
  width: 50px;
  height: 50px;
}

.coming-soon-title {
  margin-bottom: 1rem;
  font-size: 2rem;
  color: var(--gray-900);
}

.coming-soon-text {
  margin-bottom: 1.5rem;
  font-size: 1.25rem;
  color: var(--gray-700);
}

.coming-soon-description {
  max-width: 800px;
  margin-bottom: 2rem;
  color: var(--gray-600);
}

.bitcup-features {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 1.5rem;
  margin-bottom: 2rem;
  width: 100%;
  max-width: 1000px;
}

.feature-card {
  display: flex;
  flex-direction: column;
  align-items: center;
  padding: 1.5rem;
  background-color: var(--gray-100);
  border-radius: var(--border-radius-lg);
  transition: all var(--transition-normal) var(--transition-timing);
}

.feature-card:hover {
  transform: translateY(-5px);
  box-shadow: var(--shadow-md);
}

.feature-icon {
  display: flex;
  align-items: center;
  justify-content: center;
  width: 60px;
  height: 60px;
  margin-bottom: 1rem;
  background-color: var(--secondary);
  color: var(--white);
  border-radius: var(--border-radius-circle);
}

.feature-icon svg {
  width: 30px;
  height: 30px;
}

.feature-title {
  margin-bottom: 0.5rem;
  font-size: 1.25rem;
  font-weight: 600;
  color: var(--gray-900);
}

.feature-description {
  font-size: 0.875rem;
  color: var(--gray-600);
  text-align: center;
}

/* Dark mode adjustments */
:global(.dark-mode) .bitcup-subtitle {
  color: var(--gray-400);
}

:global(.dark-mode) .coming-soon {
  background-color: var(--dark-blue);
}

:global(.dark-mode) .coming-soon-title {
  color: var(--white);
}

:global(.dark-mode) .coming-soon-text {
  color: var(--gray-300);
}

:global(.dark-mode) .coming-soon-description {
  color: var(--gray-400);
}

:global(.dark-mode) .feature-card {
  background-color: var(--dark-purple);
}

:global(.dark-mode) .feature-title {
  color: var(--white);
}

:global(.dark-mode) .feature-description {
  color: var(--gray-400);
}

/* Responsive adjustments */
@media (max-width: 992px) {
  .bitcup-features {
    grid-template-columns: repeat(2, 1fr);
  }
}

@media (max-width: 768px) {
  .bitcup-title {
    font-size: 2rem;
  }
  
  .bitcup-subtitle {
    font-size: 1rem;
  }
  
  .coming-soon {
    padding: 2rem 1rem;
  }
  
  .coming-soon-title {
    font-size: 1.5rem;
  }
  
  .coming-soon-text {
    font-size: 1rem;
  }
  
  .bitcup-features {
    grid-template-columns: 1fr;
  }
}
</style>