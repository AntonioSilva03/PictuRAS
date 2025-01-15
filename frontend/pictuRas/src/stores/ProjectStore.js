import { defineStore } from 'pinia';
import axios from 'axios';
import { useEditingToolStore } from '../stores/EditingTool'

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
          withCredentials: true, // Ensure credentials are sent with the request
        });
        this.projects = response.data;
      } catch (error) {
        console.error('Error fetching projects:', error);
      }
    },
    async fetchProjects() {
        try {
          const response = await axios.get(`${api}/api/projects`, {
            withCredentials: true, // Ensure credentials are sent with the request
          });
          this.projects = response.data;
          console.log(response.data)
        } catch (error) {
          console.error('Error fetching projects:', error);
        }
      },

    async generateSessionProject() {
        try {
          // Send a request to the server to create a session-based project
          const tempProject = {
            name: "Undefined", // Default name
            owner: ""          // Will be replaced by the server
          };
          // vou ter id + data + tools vazias
          await this.fetchProjects();

          if(this.projects.length === 0){
            const response = await axios.post(
              `${api}/api/projects`, 
              tempProject, // No need to stringify; Axios automatically sets JSON headers
              { withCredentials: true } // Ensure the session cookie is sent with the request
            );
            
            const newProject = response.data;
            this.selectedProject = newProject; // Set the new project as the selected project
            this.projects.push(newProject);   // Add it to the project list
        
            console.log('New session-based project generated:', newProject);
        }else{
          this.selectProject = this.projects[0];
        }
        } catch (error) {
          console.error('Error generating session project:', error);
        }
    }, 
      async updateProject(){
          console.log(tools.tools)
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
