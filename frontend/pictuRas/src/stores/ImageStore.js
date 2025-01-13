import { defineStore } from 'pinia';
import axios from 'axios';

export const useImageStore = defineStore('imageStore', {
  state: () => ({
    images: [
      'https://placehold.co/800x800',
      'https://placehold.co/400x400',
      'https://placehold.co/800x800',
      'https://placehold.co/400x400',
      'https://placehold.co/800x800',
      'https://placehold.co/400x400',
      'https://placehold.co/800x800',
      'https://placehold.co/400x400',
      'https://placehold.co/1000x1200',
      'https://placehold.co/1800x1200'
    ], // depois vai ser vazia
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
          this.images = response.data;
        } catch (err) {
          this.error = `Failed to fetch images for project ID: ${projectId}`;
          console.error(err);
        } finally {
          this.loading = false;
        }
      },
  },
});
