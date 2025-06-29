import { defineStore } from 'pinia';
import { sessionsApi, aiPmApi } from '@/services/api';

export const useSessionStore = defineStore('session', {
  state: () => ({
    sessions: [],
    currentSession: null,
    dialogueHistory: [],
    completenessScore: 0,
    loading: false,
    interacting: false,
    error: null,
  }),
  
  getters: {
    getSessionById: (state) => (id) => {
      return state.sessions.find(session => session.id === id);
    },
    sessionCount: (state) => state.sessions.length,
    isSessionComplete: (state) => state.completenessScore >= 80,
  },
  
  actions: {
    async fetchSessions() {
      this.loading = true;
      this.error = null;
      
      try {
        const data = await sessionsApi.getSessions();
        this.sessions = data;
      } catch (error) {
        this.error = error.message || 'Failed to fetch sessions';
        console.error('Error in fetchSessions:', error);
      } finally {
        this.loading = false;
      }
    },
    
    async createSession(sessionData) {
      this.loading = true;
      this.error = null;
      
      try {
        const newSession = await sessionsApi.createSession(sessionData);
        this.sessions.push(newSession);
        this.currentSession = newSession;
        this.dialogueHistory = [];
        this.completenessScore = 0;
        return newSession;
      } catch (error) {
        this.error = error.message || 'Failed to create session';
        console.error('Error in createSession:', error);
        throw error;
      } finally {
        this.loading = false;
      }
    },
    
    async interactWithAiPm(message) {
      this.interacting = true;
      this.error = null;
      
      try {
        if (!this.currentSession) {
          throw new Error('No active session');
        }
        
        // Add user message to dialogue history
        this.dialogueHistory.push({
          role: 'user',
          content: message,
          timestamp: new Date().toISOString(),
        });
        
        // Send message to AI-PM
        const response = await aiPmApi.interact(message, this.currentSession.id);
        
        // Add AI response to dialogue history
        this.dialogueHistory.push({
          role: 'assistant',
          content: response.response,
          timestamp: new Date().toISOString(),
        });
        
        // Update completeness score
        await this.fetchSessionStatus();
        
        return response;
      } catch (error) {
        this.error = error.message || 'Failed to interact with AI-PM';
        console.error('Error in interactWithAiPm:', error);
        throw error;
      } finally {
        this.interacting = false;
      }
    },
    
    async fetchSessionStatus() {
      if (!this.currentSession) {
        return;
      }
      
      try {
        const status = await aiPmApi.getSessionStatus(this.currentSession.id);
        this.completenessScore = status.completeness_score || 0;
        return status;
      } catch (error) {
        console.error('Error fetching session status:', error);
        throw error;
      }
    },
    
    async generateRsd() {
      this.loading = true;
      this.error = null;
      
      try {
        if (!this.currentSession) {
          throw new Error('No active session');
        }
        
        if (!this.isSessionComplete) {
          throw new Error('Session is not complete enough to generate RSD');
        }
        
        const rsd = await aiPmApi.generateRsd(this.currentSession.id);
        return rsd;
      } catch (error) {
        this.error = error.message || 'Failed to generate RSD';
        console.error('Error in generateRsd:', error);
        throw error;
      } finally {
        this.loading = false;
      }
    },
    
    setCurrentSession(session) {
      this.currentSession = session;
      this.fetchSessionStatus();
    },
    
    clearCurrentSession() {
      this.currentSession = null;
      this.dialogueHistory = [];
      this.completenessScore = 0;
    },
  },
});