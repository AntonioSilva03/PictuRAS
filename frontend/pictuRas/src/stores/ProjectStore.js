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

          const projectsResponse = await this.fetchProjects();

          if(!projectsResponse){
            const response = await axios.post(
              `${api}/api/projects`, 
              tempProject, // No need to stringify; Axios automatically sets JSON headers
              { withCredentials: true } // Ensure the session cookie is sent with the request
            );
            
            const newProject = response.data;
            this.selectedProject = newProject; // Set the new project as the selected project
            this.projects.push(newProject);   // Add it to the project list
        
            console.log('New session-based project generated:', newProject);
        }
        } catch (error) {
          console.error('Error generating session project:', error);
        }
      },      
  },
});
