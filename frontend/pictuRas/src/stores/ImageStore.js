import { defineStore } from 'pinia';
import JSZip from 'jszip';
import axios from 'axios';

const api = import.meta.env.VITE_API_GATEWAY;

export const useImageStore = defineStore('imageStore', {
  state: () => ({
    images: [], // depois vai ser vazia
    bytes:[],
    old:[],
    ids:[],
    selectedImage: null,
    previewMode:false,
    onProcess:false,
  }),
  actions: {
    selectImage(image) {
      this.selectedImage = image;
    },
    async fetchImages(projectId) {
      this.loading = true;
      this.error = null;
      try {
        this.image = [];
        this.ids = [];
        this.selectedImage = null;
        const response = await axios.get(`${api}/api/projects/images`, {
          params: { projectId: projectId }, // Pass query params
          withCredentials: true // Include credentials if needed (cookies, headers)
        });
        this.ids = response.data.map((element) => element.id);
        let imageUrls = [];
        let imageBlobs = [];
        
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
    
            // Store the image source URL and blob
            imageUrls.push(imageSrc);
            imageBlobs.push(blob);
          } catch (error) {
            console.log("Error fetching image:", error);
          }
        }
    
        // Update the store state
        this.images = imageUrls; // URLs for displaying images
        this.bytes = imageBlobs; // Blobs for downloading images
      } catch (error) {
        console.error("Error fetching images:", error);
      } finally {
        this.loading = false;
      }
    },
    async downloadAllImagesAsZip(projectId) {
      if (this.bytes.length === 0) {
        console.error("No images available for download.");
        return;
      }
    
      const zip = new JSZip(); // Create a new ZIP file instance
    
      // Add each blob to the ZIP
      for (let i = 0; i < this.bytes.length; i++) {
        const blob = this.bytes[i];
        zip.file(`image-${i + 1}.jpg`, blob); // Add the blob as a file
      }
    
      try {
        // Generate the ZIP file asynchronously
        const zipBlob = await zip.generateAsync({ type: 'blob' });
    
        // Create a temporary object URL for the ZIP blob
        const url = URL.createObjectURL(zipBlob);
    
        // Create a temporary <a> element
        const a = document.createElement('a');
        a.href = url;
        a.download = `${projectId}-images.zip`; // Name of the downloaded ZIP file
        document.body.appendChild(a);
        a.click(); // Trigger the download
    
        // Cleanup
        document.body.removeChild(a); // Remove the anchor element
        URL.revokeObjectURL(url); // Revoke the object URL to free up memory
      } catch (error) {
        console.error("Error creating ZIP file:", error);
      }
    },
    clear(){
      this.images = [];
      this.bytes= [];
      this.ids=[];
      this.selectedImage = null;
    },enterProcessMode(){
      this.onProcess = true;
      this.old = this.bytes;
    },leaveProvessMode(cancel){
        if (!cancel){
          this.onProcess = false;
        }else{
          // todo
          this.onProcess = false;
        }
        console.log(this.onProcess)
    },async updateList(images){
      console.log(images)
      let imageUrls = [];
      let imageBlobs = [];
      let imagesIds = [];
      try {

        for (const element of images) {
          try {
    
            // Extract MIME type from response headers
            // Create a Blob using the ArrayBuffer and MIME type
            const blob = new Blob([element.data], { type: 'image/png' });
            // Generate an object URL for the image Blob
            const imageSrc = URL.createObjectURL(blob);
    
            // Store the image source URL and blob
            imageUrls.push(imageSrc);
            imageBlobs.push(blob);
            imagesIds.push(element.id)
          } catch (error) {
            console.log("Error fetching image:", error);
          }
        }
        this.images = imageUrls; // URLs for displaying images
        this.bytes = imageBlobs; // Blobs for downloading images
        this.ids = imagesIds;
      } catch (error) {
        console.log("Error fetching image:", error);
      }

    },async deleteImages(projectId,imageIds){
          // Send delete request to the API
          try{
          console.log(`${api}/api/projects/images`);
          const response = await axios.delete(`${api}/api/projects/images`, {
            params: { projectId: projectId, images:imageIds }, // Pass query params
            withCredentials: true // Include credentials if needed (cookies, headers)
          });
          
          await this.fetchImages(projectId);
          console.log("here")
      }catch(e){
        console.log(e)
      }
    }
  },
});
