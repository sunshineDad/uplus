<template>
  <TechLayout title="RSD Documents">
    <div class="rsd-view">
      <div class="rsd-header">
        <h1 class="rsd-title">Requirements Specification Documents</h1>
        <p class="rsd-subtitle">View and manage your project requirements</p>
      </div>
      
      <div class="coming-soon">
        <div class="coming-soon-icon">
          <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
            <path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"></path>
            <polyline points="14 2 14 8 20 8"></polyline>
            <line x1="16" y1="13" x2="8" y2="13"></line>
            <line x1="16" y1="17" x2="8" y2="17"></line>
            <polyline points="10 9 9 9 8 9"></polyline>
          </svg>
        </div>
        <h2 class="coming-soon-title">RSD Document Management</h2>
        <p class="coming-soon-text">This feature is coming soon in the next phase of development.</p>
        <p class="coming-soon-description">
          The RSD Document Management will allow you to view, edit, and manage all your Requirements Specification Documents in one place.
          You'll be able to track changes, collaborate with team members, and export documents in various formats.
        </p>
        <router-link to="/ai-pm" class="btn btn-primary">
          Go to AI-PM to Generate RSD
        </router-link>
      </div>
    </div>
  </TechLayout>
</template>

<script>
import TechLayout from '@/components/common/TechLayout.vue';

export default {
  name: 'RsdView',
  components: {
    TechLayout
  }
};
</script>

<style scoped>
.rsd-view {
  display: flex;
  flex-direction: column;
  gap: 2rem;
}

.rsd-header {
  text-align: center;
  margin-bottom: 1rem;
}

.rsd-title {
  font-size: 2.5rem;
  font-weight: 700;
  margin-bottom: 0.5rem;
  background: var(--gradient-primary);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  animation: text-shine 3s linear infinite;
}

.rsd-subtitle {
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
  background-color: var(--primary-light);
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
  max-width: 600px;
  margin-bottom: 2rem;
  color: var(--gray-600);
}

/* Dark mode adjustments */
:global(.dark-mode) .rsd-subtitle {
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

/* Responsive adjustments */
@media (max-width: 768px) {
  .rsd-title {
    font-size: 2rem;
  }
  
  .rsd-subtitle {
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
}
</style>