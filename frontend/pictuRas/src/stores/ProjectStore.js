import { defineStore } from 'pinia';
import axios from 'axios';

const api = import.meta.env.VITE_API_GATEWAY;

export const useProjectStore = defineStore('projectStore', {
  state: () => ({
    projects: [],
    selectedProject: null,
  }),
  actions: {
    selectProject(project) {
      this.selectedProject = project;
    },
    async fetchProject(projectId) {
      try {
        const response = await axios.get(`${api}/api/projects/${projectId}`, {
          withCredentials: true,
        });
        this.projects = response.data;
      } catch (error) {
        console.error('Error fetching projects:', error);
      }
    },
    async fetchProjects() {
      try {
        const response = await axios.get(`${api}/api/projects`, {
          withCredentials: true,
        });
        this.projects = response.data;
      } catch (error) {
        console.error('Error fetching projects:', error);
      }
    },
    async generateSessionProject() {
      try {
        const tempProject = {
          name: "Undefined",
          owner: ""
        };

        await this.fetchProjects();

        if (this.projects.length === 0) {
          const response = await axios.post(
            `${api}/api/projects`,
            tempProject,
            { withCredentials: true }
          );

          const newProject = response.data;
          this.selectedProject = newProject;
          this.projects.push(newProject);
        } else {
          this.selectedProject = this.projects[0];
          console.log('Existing project selected:', this.selectedProject);
        }
      } catch (error) {
        console.error('Error generating session project:', error);
      }
    },
    async saveProject(tools) {
      if (!this.selectedProject) {
        console.error('No project selected to save.');
        return;
      }

      try {
        // Filter and format tools
        const activeToolsInOrder = tools.filter(tool => tool.active);
        const activeToolsInOrderWrapper = activeToolsInOrder.map(({ active, position, ...rest }) => rest);

        // Assign tools to the selected project
        this.selectedProject.tools = activeToolsInOrderWrapper;

        // Create a deep copy of the project for the API request
        const tempProject = JSON.parse(JSON.stringify(this.selectedProject));

        // Make the API request to save the project
        const response = await axios.put(
          `${api}/api/projects`,
          tempProject,
          { withCredentials: true }
        );

        console.log('Project saved successfully:', response.data);
      } catch (error) {
        console.error('Error saving project:', error);
      }
    },
    printStore() {
      console.log(this.selectedProject)
    },
    getId(){
      return this.selectedProject ? this.selectedProject.id : "";
    },
    getTools(){
      return this.selectedProject ? this.selectedProject.tools : [];
    },
    async createProject(projectData) {
      const api = import.meta.env.VITE_API_GATEWAY;
    
      try {
        // Envia os dados ao backend
        const response = await axios.post(`${api}/api/projects`, projectData, {
          withCredentials: true, 
        });
    
        const newProject = response.data;
    
        // Atualiza os estados locais
        this.projects.push(newProject);
        this.selectedProject = newProject;
    
        console.log('Project created successfully:', newProject);
        return newProject; // Retorna o projeto criado
      } catch (error) {
        console.error('Error creating project:', error.message);
        throw error;
      }
  },

  async deleteProject(projectId) {
      const api = import.meta.env.VITE_API_GATEWAY;

      try {
        // Faz uma requisição DELETE para o API Gateway
        await axios.delete(`${api}/api/projects/${projectId}`, {
          withCredentials: true, // Inclui credenciais de autenticação
        });

        // Remove o projeto da lista local
        this.projects = this.projects.filter((project) => project.id !== projectId);

        console.log(`Project ${projectId} deleted successfully.`);
      } catch (error) {
        console.error('Error deleting project:', error);
        throw error;
      }
    }, 
    
  },
});
