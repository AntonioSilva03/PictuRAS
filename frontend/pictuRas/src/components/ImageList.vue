<template>
  <div class="wrapper">
    <div class="image-list">
      <div
        v-for="(image, index) in imageStore.images"
        :key="index"
        class="image-thumbnail"
        @click="selectImage(image)"
      >
        <img :src="image" alt="Thumbnail" />
      </div>
    </div>
    <div class="btn-flex">
      <button @click="triggerFileUpload">Upload</button>
      <input
        type="file"
        ref="fileInput"
        @change="handleFileUpload"
        accept="image/*"
        multiple
        style="display: none"
      />
      <button @click="downloadAllImagesAsZip()" >Download</button>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'; // Import ref
import { useImageStore } from '../stores/ImageStore';
import { useProjectStore } from '../stores/ProjectStore';
import axios from 'axios';

const api = import.meta.env.VITE_API_GATEWAY;

// Access the store
const imageStore = useImageStore();
const projectStore = useProjectStore();

// File input reference
const fileInput = ref(null);

// Select an image using the store's action
function selectImage(image) {
  imageStore.selectImage(image);
}

// Trigger file input click
function triggerFileUpload() {
  fileInput.value.click();
}

// Handle file upload
async function handleFileUpload(event) {
  const files = Array.from(event.target.files);

  // Filter only valid image files
  const validImageFiles = files.filter((file) =>
    file.type.startsWith("image/")
  );

  // Check if there are any invalid files
  if (validImageFiles.length !== files.length) {
    alert("Some files are not valid image formats. Only images are allowed.");
  }

  // Limit the upload to 20 images
  if (validImageFiles.length > 20) {
    alert("You can only upload up to 20 images at once.");
    return;
  }

  const projectStore = useProjectStore();
  const projectId = projectStore.selectedProject?.id;
  console.log(projectId)
  if (!projectId) {
    console.error("No project selected. Cannot upload files.");
    return;
  }
  let tempArray = [];
  // Iterate over each image file and send it in a separate request
  for (const file of validImageFiles) {
    const formData = new FormData();
    formData.append("image", file); // Append the file as 'image'
    formData.append("projectId", projectId); // Include the project ID

    try {
      const response = await axios.post(`${api}/api/projects/images`, formData, {
        headers: {
          "Content-Type": "multipart/form-data",
        },
        withCredentials: true, // Include credentials for authentication
      });
      tempArray.push(response.data)
          // Iterate through each image element returned by the API
    } catch (error) {
      console.error(`Failed to upload ${file.name}:`, error);
      alert(`Error uploading ${file.name}. Please try again.`);
    }
  }

      for (const element of tempArray) {
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
            imageStore.images.push(imageSrc);
             
    }
  console.log(imageStore.images)
  alert("All images have been uploaded.");
  event.target.value = "";
}


async function downloadAllImagesAsZip (){
  const projectStore = useProjectStore();
  const projectId = projectStore.selectedProject?.id;
  await imageStore.downloadAllImagesAsZip(projectId);
  alert("Download as finished!")
};

</script>


<style scoped>

.wrapper {
  display: flex;
  flex-direction: column;
  align-items: center;
  background-color: #f0f0f0;
  height: 100%;
  overflow-y: hidden;
}

.image-list {
  display: flex;
  flex-wrap: wrap;
  gap: 10px;
  padding-top: 10px;
  overflow-y: scroll;
  height: 90%;
  width: 100%;
  justify-content: center;
}

.image-list>div {
  width: 45%;
  display: flex;
  justify-content: center;
  align-items: center;
}

.image-thumbnail {
  cursor: pointer;
  border: 2px solid transparent;
  border-radius: 8px;
  transition: border-color 0.3s;
  align-self: center;
}

.image-thumbnail img {
  width: 150px;
  height: 150px;
  border-radius: 6px;
  display: block;
}

.image-thumbnail:hover {
  border-color: #000000;
}

.btn-flex {
  display: flex;
  flex-direction: row;
  width: 100%;
  position: relative;
  padding-top: 5%;
  justify-content: space-around;
  border-top: 1px solid #000000;
}

.btn-flex button {
    padding: 10px 30px;
    border-radius: 20px;
    background: #000000;
    color: #ffffff;
    border: none;
    cursor: pointer;
    overflow: hidden;
    border: 1px solid #000000;
    transition: 0.25s;
}

.btn-flex:nth-child(2) {
    right: 0;
}

.btn-flex button:hover {
    background-color: #ffffff;
    box-shadow: 0 0 6px #000000;
    color: #000000;
}



</style>
