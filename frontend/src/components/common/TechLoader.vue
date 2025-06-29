<template>
  <div class="tech-loader-container" :class="{ 'fullscreen': fullscreen }">
    <div class="tech-loader-content">
      <div class="tech-loader-spinner">
        <div class="spinner-ring"></div>
        <div class="spinner-ring"></div>
        <div class="spinner-ring"></div>
        <div class="spinner-core"></div>
      </div>
      <div v-if="message" class="tech-loader-message">
        <span class="message-text">{{ message }}</span>
        <span v-if="showDots" class="loading-dots">
          <span class="dot"></span>
          <span class="dot"></span>
          <span class="dot"></span>
        </span>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'TechLoader',
  props: {
    message: {
      type: String,
      default: 'Loading'
    },
    fullscreen: {
      type: Boolean,
      default: false
    },
    showDots: {
      type: Boolean,
      default: true
    }
  }
};
</script>

<style scoped>
.tech-loader-container {
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 2rem;
}

.tech-loader-container.fullscreen {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(0, 0, 0, 0.7);
  backdrop-filter: blur(5px);
  z-index: 9999;
}

.tech-loader-content {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
}

.tech-loader-spinner {
  position: relative;
  width: 80px;
  height: 80px;
  margin-bottom: 1.5rem;
}

.spinner-ring {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  border: 3px solid transparent;
  border-radius: 50%;
}

.spinner-ring:nth-child(1) {
  border-top-color: var(--primary);
  animation: spin 1.5s linear infinite;
}

.spinner-ring:nth-child(2) {
  border-right-color: var(--secondary);
  animation: spin 2s linear infinite reverse;
}

.spinner-ring:nth-child(3) {
  border-bottom-color: var(--accent);
  animation: spin 2.5s linear infinite;
}

.spinner-core {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  width: 40%;
  height: 40%;
  background: var(--gradient-primary);
  border-radius: 50%;
  box-shadow: 0 0 15px var(--primary);
  animation: pulse 2s ease-in-out infinite;
}

.tech-loader-message {
  font-family: var(--font-family-mono);
  font-size: 1rem;
  color: var(--white);
  text-align: center;
  display: flex;
  align-items: center;
}

.loading-dots {
  display: inline-flex;
  margin-left: 0.5rem;
}

.dot {
  width: 6px;
  height: 6px;
  margin: 0 2px;
  border-radius: 50%;
  background-color: var(--primary);
  animation: dot-pulse 1.5s infinite ease-in-out;
}

.dot:nth-child(2) {
  animation-delay: 0.5s;
  background-color: var(--secondary);
}

.dot:nth-child(3) {
  animation-delay: 1s;
  background-color: var(--accent);
}

@keyframes spin {
  0% {
    transform: rotate(0deg);
  }
  100% {
    transform: rotate(360deg);
  }
}

@keyframes pulse {
  0%, 100% {
    transform: translate(-50%, -50%) scale(1);
    opacity: 0.8;
  }
  50% {
    transform: translate(-50%, -50%) scale(1.2);
    opacity: 1;
  }
}

@keyframes dot-pulse {
  0%, 100% {
    transform: scale(1);
    opacity: 0.7;
  }
  50% {
    transform: scale(1.5);
    opacity: 1;
  }
}

/* Dark mode adjustments */
:global(.dark-mode) .tech-loader-message {
  color: var(--white);
}
</style>