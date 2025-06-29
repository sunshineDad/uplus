import { defineStore } from 'pinia';
import { projectsApi } from '@/services/api';

export const useProjectStore = defineStore('project', {
  state: () => ({
    projects: [],
    currentProject: null,
    loading: false,
    error: null,
  }),
  
  getters: {
    getProjectById: (state) => (id) => {
      return state.projects.find(project => project.id === id);
    },
    projectCount: (state) => state.projects.length,
  },
  
  actions: {
    async fetchProjects() {
      this.loading = true;
      this.error = null;
      
      try {
        const data = await projectsApi.getProjects();
        this.projects = data;
      } catch (error) {
        this.error = error.message || 'Failed to fetch projects';
        console.error('Error in fetchProjects:', error);
      } finally {
        this.loading = false;
      }
    },
    
    async createProject(projectData) {
      this.loading = true;
      this.error = null;
      
      try {
        const newProject = await projectsApi.createProject(projectData);
        this.projects.push(newProject);
        this.currentProject = newProject;
        return newProject;
      } catch (error) {
        this.error = error.message || 'Failed to create project';
        console.error('Error in createProject:', error);
        throw error;
      } finally {
        this.loading = false;
      }
    },
    
    setCurrentProject(project) {
      this.currentProject = project;
    },
    
    clearCurrentProject() {
      this.currentProject = null;
    },
  },
});