import { defineStore } from 'pinia';

export const useUiStore = defineStore('ui', {
  state: () => ({
    darkMode: false,
    sidebarOpen: true,
    notifications: [],
    currentView: 'dashboard',
  }),
  
  getters: {
    isDarkMode: (state) => state.darkMode,
    isSidebarOpen: (state) => state.sidebarOpen,
  },
  
  actions: {
    toggleDarkMode() {
      this.darkMode = !this.darkMode;
      
      // Apply dark mode to document
      if (this.darkMode) {
        document.documentElement.classList.add('dark-mode');
      } else {
        document.documentElement.classList.remove('dark-mode');
      }
      
      // Save preference to localStorage
      localStorage.setItem('darkMode', this.darkMode);
    },
    
    toggleSidebar() {
      this.sidebarOpen = !this.sidebarOpen;
    },
    
    setCurrentView(view) {
      this.currentView = view;
    },
    
    addNotification(notification) {
      // Add a unique ID and timestamp
      const newNotification = {
        id: Date.now(),
        timestamp: new Date().toISOString(),
        read: false,
        ...notification,
      };
      
      this.notifications.push(newNotification);
      
      // Auto-remove after timeout if dismissible
      if (notification.dismissible !== false) {
        setTimeout(() => {
          this.removeNotification(newNotification.id);
        }, notification.timeout || 5000);
      }
      
      return newNotification.id;
    },
    
    removeNotification(id) {
      const index = this.notifications.findIndex(n => n.id === id);
      if (index !== -1) {
        this.notifications.splice(index, 1);
      }
    },
    
    markNotificationAsRead(id) {
      const notification = this.notifications.find(n => n.id === id);
      if (notification) {
        notification.read = true;
      }
    },
    
    clearAllNotifications() {
      this.notifications = [];
    },
    
    initializeFromLocalStorage() {
      // Load dark mode preference
      const darkMode = localStorage.getItem('darkMode');
      if (darkMode !== null) {
        this.darkMode = darkMode === 'true';
        
        // Apply dark mode to document
        if (this.darkMode) {
          document.documentElement.classList.add('dark-mode');
        }
      }
    },
  },
});