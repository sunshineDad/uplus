import axios from 'axios';

// Create axios instance with base URL
const api = axios.create({
  baseURL: '/api/v1',
  headers: {
    'Content-Type': 'application/json',
    'Accept': 'application/json',
  },
});

// API endpoints
export const projectsApi = {
  // Get all projects
  getProjects: async () => {
    try {
      const response = await api.get('/projects/');
      return response.data;
    } catch (error) {
      console.error('Error fetching projects:', error);
      throw error;
    }
  },
  
  // Create a new project
  createProject: async (projectData) => {
    try {
      const response = await api.post('/projects/', projectData);
      return response.data;
    } catch (error) {
      console.error('Error creating project:', error);
      throw error;
    }
  },
};

export const sessionsApi = {
  // Get all sessions
  getSessions: async () => {
    try {
      const response = await api.get('/sessions/');
      return response.data;
    } catch (error) {
      console.error('Error fetching sessions:', error);
      throw error;
    }
  },
  
  // Create a new session
  createSession: async (sessionData) => {
    try {
      const response = await api.post('/sessions/', sessionData);
      return response.data;
    } catch (error) {
      console.error('Error creating session:', error);
      throw error;
    }
  },
};

export const aiPmApi = {
  // Interact with AI-PM
  interact: async (message, sessionId) => {
    try {
      const response = await api.post('/ai-pm/interact', {
        message,
        session_id: sessionId,
      });
      return response.data;
    } catch (error) {
      console.error('Error interacting with AI-PM:', error);
      throw error;
    }
  },
  
  // Get session status
  getSessionStatus: async (sessionId) => {
    try {
      const response = await api.get(`/ai-pm/session/${sessionId}/status`);
      return response.data;
    } catch (error) {
      console.error('Error fetching session status:', error);
      throw error;
    }
  },
  
  // Generate RSD document
  generateRsd: async (sessionId) => {
    try {
      const response = await api.post('/ai-pm/generate-rsd', {
        session_id: sessionId,
      });
      return response.data;
    } catch (error) {
      console.error('Error generating RSD:', error);
      throw error;
    }
  },
};

// Interceptors for handling errors globally
api.interceptors.response.use(
  (response) => response,
  (error) => {
    // Handle global errors here
    if (error.response) {
      // Server responded with an error status
      console.error('API Error:', error.response.data);
    } else if (error.request) {
      // Request was made but no response received
      console.error('Network Error:', error.request);
    } else {
      // Something else happened
      console.error('Error:', error.message);
    }
    return Promise.reject(error);
  }
);

export default api;