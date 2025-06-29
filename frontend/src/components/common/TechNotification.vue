<template>
  <div 
    class="tech-notification" 
    :class="[
      `tech-notification-${type}`,
      { 'tech-notification-closing': isClosing }
    ]"
    @click="handleClick"
  >
    <div class="tech-notification-icon">
      <div v-if="type === 'success'" class="icon-success">
        <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
          <path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"></path>
          <polyline points="22 4 12 14.01 9 11.01"></polyline>
        </svg>
      </div>
      <div v-else-if="type === 'error'" class="icon-error">
        <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
          <circle cx="12" cy="12" r="10"></circle>
          <line x1="15" y1="9" x2="9" y2="15"></line>
          <line x1="9" y1="9" x2="15" y2="15"></line>
        </svg>
      </div>
      <div v-else-if="type === 'warning'" class="icon-warning">
        <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
          <path d="M10.29 3.86L1.82 18a2 2 0 0 0 1.71 3h16.94a2 2 0 0 0 1.71-3L13.71 3.86a2 2 0 0 0-3.42 0z"></path>
          <line x1="12" y1="9" x2="12" y2="13"></line>
          <line x1="12" y1="17" x2="12.01" y2="17"></line>
        </svg>
      </div>
      <div v-else class="icon-info">
        <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
          <circle cx="12" cy="12" r="10"></circle>
          <line x1="12" y1="16" x2="12" y2="12"></line>
          <line x1="12" y1="8" x2="12.01" y2="8"></line>
        </svg>
      </div>
    </div>
    <div class="tech-notification-content">
      <div v-if="title" class="tech-notification-title">{{ title }}</div>
      <div class="tech-notification-message">{{ message }}</div>
    </div>
    <div v-if="dismissible" class="tech-notification-close" @click.stop="close">
      <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
        <line x1="18" y1="6" x2="6" y2="18"></line>
        <line x1="6" y1="6" x2="18" y2="18"></line>
      </svg>
    </div>
    <div v-if="autoClose" class="tech-notification-progress">
      <div class="progress-bar" :style="{ animationDuration: `${duration}ms` }"></div>
    </div>
  </div>
</template>

<script>
import { ref } from 'vue';

export default {
  name: 'TechNotification',
  props: {
    id: {
      type: [Number, String],
      required: true
    },
    type: {
      type: String,
      default: 'info',
      validator: (value) => ['info', 'success', 'warning', 'error'].includes(value)
    },
    title: {
      type: String,
      default: ''
    },
    message: {
      type: String,
      required: true
    },
    autoClose: {
      type: Boolean,
      default: true
    },
    duration: {
      type: Number,
      default: 5000
    },
    dismissible: {
      type: Boolean,
      default: true
    },
    onClick: {
      type: Function,
      default: null
    }
  },
  emits: ['close'],
  setup(props, { emit }) {
    const isClosing = ref(false);
    
    // Handle notification click
    const handleClick = () => {
      if (props.onClick) {
        props.onClick(props.id);
      }
    };
    
    // Close notification
    const close = () => {
      isClosing.value = true;
      
      // Wait for animation to complete
      setTimeout(() => {
        emit('close', props.id);
      }, 300);
    };
    
    // Auto close after duration
    if (props.autoClose) {
      setTimeout(() => {
        close();
      }, props.duration);
    }
    
    return {
      isClosing,
      handleClick,
      close
    };
  }
};
</script>

<style scoped>
.tech-notification {
  position: relative;
  display: flex;
  align-items: flex-start;
  width: 100%;
  max-width: 400px;
  margin-bottom: 1rem;
  padding: 1rem;
  background-color: var(--white);
  border-radius: var(--border-radius-md);
  box-shadow: var(--shadow-lg);
  overflow: hidden;
  animation: slide-in 0.3s ease-out forwards;
  cursor: pointer;
  transition: transform 0.3s ease, opacity 0.3s ease, box-shadow 0.3s ease;
}

.tech-notification:hover {
  transform: translateY(-3px);
  box-shadow: var(--shadow-xl);
}

.tech-notification-closing {
  animation: slide-out 0.3s ease-in forwards;
}

.tech-notification-icon {
  flex-shrink: 0;
  width: 24px;
  height: 24px;
  margin-right: 1rem;
  display: flex;
  align-items: center;
  justify-content: center;
}

.tech-notification-content {
  flex-grow: 1;
  padding-right: 1rem;
}

.tech-notification-title {
  font-weight: 600;
  margin-bottom: 0.25rem;
}

.tech-notification-message {
  font-size: 0.875rem;
  line-height: 1.4;
}

.tech-notification-close {
  flex-shrink: 0;
  width: 20px;
  height: 20px;
  opacity: 0.5;
  transition: opacity 0.2s;
  cursor: pointer;
}

.tech-notification-close:hover {
  opacity: 1;
}

.tech-notification-progress {
  position: absolute;
  bottom: 0;
  left: 0;
  width: 100%;
  height: 3px;
  background-color: rgba(0, 0, 0, 0.1);
}

.progress-bar {
  height: 100%;
  width: 100%;
  background-color: currentColor;
  transform-origin: left;
  animation: progress-shrink linear forwards;
}

/* Notification types */
.tech-notification-success {
  border-left: 4px solid var(--success);
  color: var(--success);
}

.tech-notification-error {
  border-left: 4px solid var(--danger);
  color: var(--danger);
}

.tech-notification-warning {
  border-left: 4px solid var(--warning);
  color: var(--warning);
}

.tech-notification-info {
  border-left: 4px solid var(--info);
  color: var(--info);
}

/* Animations */
@keyframes slide-in {
  from {
    transform: translateX(100%);
    opacity: 0;
  }
  to {
    transform: translateX(0);
    opacity: 1;
  }
}

@keyframes slide-out {
  from {
    transform: translateX(0);
    opacity: 1;
  }
  to {
    transform: translateX(100%);
    opacity: 0;
  }
}

@keyframes progress-shrink {
  from {
    transform: scaleX(1);
  }
  to {
    transform: scaleX(0);
  }
}

/* Dark mode adjustments */
:global(.dark-mode) .tech-notification {
  background-color: var(--dark-blue);
  color: var(--white);
}

:global(.dark-mode) .tech-notification-progress {
  background-color: rgba(255, 255, 255, 0.1);
}
</style>