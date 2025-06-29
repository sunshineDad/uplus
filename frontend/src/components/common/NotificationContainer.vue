<template>
  <div class="notification-container" :class="position">
    <TechNotification
      v-for="notification in notifications"
      :key="notification.id"
      :id="notification.id"
      :type="notification.type"
      :title="notification.title"
      :message="notification.message"
      :auto-close="notification.dismissible !== false"
      :duration="notification.timeout || 5000"
      :dismissible="notification.dismissible !== false"
      :onClick="notification.onClick"
      @close="removeNotification"
    />
  </div>
</template>

<script>
import { computed } from 'vue';
import { useUiStore } from '@/store/uiStore';
import TechNotification from './TechNotification.vue';

export default {
  name: 'NotificationContainer',
  components: {
    TechNotification
  },
  props: {
    position: {
      type: String,
      default: 'top-right',
      validator: (value) => [
        'top-right',
        'top-left',
        'bottom-right',
        'bottom-left',
        'top-center',
        'bottom-center'
      ].includes(value)
    }
  },
  setup() {
    const uiStore = useUiStore();
    
    // Get notifications from store
    const notifications = computed(() => uiStore.notifications);
    
    // Remove notification
    const removeNotification = (id) => {
      uiStore.removeNotification(id);
    };
    
    return {
      notifications,
      removeNotification
    };
  }
};
</script>

<style scoped>
.notification-container {
  position: fixed;
  z-index: var(--z-index-tooltip);
  display: flex;
  flex-direction: column;
  gap: 0.5rem;
  max-width: 400px;
  max-height: 100vh;
  overflow-y: auto;
  padding: 1rem;
  pointer-events: none;
}

.notification-container > :deep(*) {
  pointer-events: auto;
}

/* Positions */
.top-right {
  top: 0;
  right: 0;
}

.top-left {
  top: 0;
  left: 0;
}

.bottom-right {
  bottom: 0;
  right: 0;
}

.bottom-left {
  bottom: 0;
  left: 0;
}

.top-center {
  top: 0;
  left: 50%;
  transform: translateX(-50%);
}

.bottom-center {
  bottom: 0;
  left: 50%;
  transform: translateX(-50%);
}
</style>