import axios from 'axios';

// Create axios instance with base URL
const api = axios.create({
  baseURL: 'http://localhost:12000/api/v1',
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

export const bitcupApi = {
  // Generate BITCUP model from RSD
  generateModel: async (rsdId) => {
    try {
      const response = await api.post('/bitcup/generate-model', {
        rsd_id: rsdId,
      });
      return response.data;
    } catch (error) {
      console.error('Error generating BITCUP model:', error);
      throw error;
    }
  },
  
  // Generate RSD from BITCUP model (bidirectional transformation)
  generateRsd: async (bitcupId) => {
    try {
      const response = await api.post('/bitcup/generate-rsd', {
        bitcup_id: bitcupId,
      });
      return response.data;
    } catch (error) {
      console.error('Error generating RSD from BITCUP:', error);
      throw error;
    }
  },
  
  // Get all BITCUP models for a project
  getProjectModels: async (projectId) => {
    try {
      const response = await api.get(`/bitcup/models/${projectId}`);
      return response.data;
    } catch (error) {
      console.error('Error fetching BITCUP models:', error);
      throw error;
    }
  },
  
  // Get a specific BITCUP model
  getModel: async (modelId) => {
    try {
      const response = await api.get(`/bitcup/model/${modelId}`);
      return response.data;
    } catch (error) {
      console.error('Error fetching BITCUP model:', error);
      throw error;
    }
  },
};

export const lowcodeApi = {
  // Generate code from BITCUP model
  generateCode: async (bitcupId, techStack = null) => {
    try {
      const response = await api.post('/lowcode/generate-code', {
        bitcup_id: bitcupId,
        tech_stack: techStack,
      });
      return response.data;
    } catch (error) {
      console.error('Error generating code:', error);
      throw error;
    }
  },
  
  // Generate application preview
  generatePreview: async (codeId) => {
    try {
      const response = await api.post('/lowcode/preview', {
        code_id: codeId,
      });
      return response.data;
    } catch (error) {
      console.error('Error generating preview:', error);
      throw error;
    }
  },
  
  // Deploy application
  deployApplication: async (codeId, environment = 'development') => {
    try {
      const response = await api.post('/lowcode/deploy', {
        code_id: codeId,
        environment,
      });
      return response.data;
    } catch (error) {
      console.error('Error deploying application:', error);
      throw error;
    }
  },
  
  // Get available technology stacks
  getTechStacks: async () => {
    try {
      const response = await api.get('/lowcode/tech-stacks');
      return response.data;
    } catch (error) {
      console.error('Error fetching tech stacks:', error);
      throw error;
    }
  },
  
  // Get generated code by ID
  getGeneratedCode: async (codeId) => {
    try {
      const response = await api.get(`/lowcode/code/${codeId}`);
      return response.data;
    } catch (error) {
      console.error('Error fetching generated code:', error);
      throw error;
    }
  },
  
  // Get all generated code for a BITCUP model
  getCodesByBitcup: async (bitcupId) => {
    try {
      const response = await api.get(`/lowcode/codes/${bitcupId}`);
      return response.data;
    } catch (error) {
      console.error('Error fetching generated codes:', error);
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