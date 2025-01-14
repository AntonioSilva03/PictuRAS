import { defineStore } from 'pinia';
import axios from 'axios';

const api = import.meta.env.VITE_API_GATEWAY;

export const useImageStore = defineStore('imageStore', {
  state: () => ({
    images: [], // depois vai ser vazia
    selectedImage: null,
  }),
  actions: {
    selectImage(image) {
      this.selectedImage = image;
    },
    async fetchImages(projectId) {
      this.loading = true;
      this.error = null;
      try {
          const response = await axios.get(`${api}/api/projects/images`, {
              params: { projectId: projectId }, // Pass query params
              withCredentials: true // Include credentials if needed (cookies, headers)
          });

          let t = []
          // Iterate through each image element returned by the API
          for (const element of response.data) {
              try {
                  // Fetch the actual image as an ArrayBuffer
                  const response2 = await axios.get(`${api}/api/projects/images/${element.id}`, { 
                      responseType: 'arraybuffer' 
                  });
  
                  // Extract MIME type from response headers
                  const mimeType = response2.headers['content-type'];
  
                  // Create a Blob using the ArrayBuffer and MIME type
                  const blob = new Blob([response2.data], { type: mimeType });
  
                  // Generate an object URL for the image Blob
                  const imageSrc = URL.createObjectURL(blob);
                  
                  // Store the image source URL for later use
                  t.push(imageSrc);
              } catch (error) {
                  console.log("Error fetching image:", error);
              }
          }

          this.images = JSON.parse(JSON.stringify(t));
          
      } catch (error) {
          console.error("Error fetching images:", error);
      } finally {
          this.loading = false;
      }
  }
  
  },
});
