import { defineStore } from 'pinia';
import axios from 'axios';

export const useImageStore = defineStore('imageStore', {
  state: () => ({
    images: [
      'https://via.placeholder.com/150/FF0000/FFFFFF?text=1',
      'https://via.placeholder.com/150/00FF00/FFFFFF?text=2',
      'https://via.placeholder.com/150/0000FF/FFFFFF?text=3',
      'https://via.placeholder.com/150/FFFF00/FFFFFF?text=4',
      'https://via.placeholder.com/150/FFFF00/FFFFFF?text=5',
      'https://via.placeholder.com/150/FFFF00/FFFFFF?text=6',
      'https://via.placeholder.com/150/FFFF00/FFFFFF?text=7',
      'https://via.placeholder.com/150/FFFF00/FFFFFF?text=8',
      'https://placehold.co/1000x1200',
      'https://placehold.co/1800x1200'
    ], // depois vai ser vazia
    multiSelectedImages:[], // ainda fazer algo com isto
    selectedImage: null,
  }),
  actions: {
    selectImage(image) {
      console.log(image)
      this.selectedImage = image;
    },
    async fetchImages(projectId) {
        this.loading = true;
        this.error = null;
  
        try {
          const response = await axios.get(`https://api.example.com/projects/${projectId}/images`);
          this.images = response.data; // Assume the API returns an array of images for the project
        } catch (err) {
          this.error = `Failed to fetch images for project ID: ${projectId}`;
          console.error(err);
        } finally {
          this.loading = false;
        }
      },
  },
});
