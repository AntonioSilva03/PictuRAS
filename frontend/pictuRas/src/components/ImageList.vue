<template>
  <div class="wrapper">
    <div class="image-list">
      <div
        v-for="(image, index) in images"
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
      <button>Download</button>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'; // Import ref
import { useImageStore } from '../stores/ImageStore';

// Access the store
const imageStore = useImageStore();
const images = imageStore.images;

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
function handleFileUpload(event) {
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

  // Create object URLs for valid images
  // const imageUrls = validImageFiles.map((file) => URL.createObjectURL(file));
  // imageStore.addImages(imageUrls); // Assuming `addImages` is a store action
}

</script>


<style scoped>
.wrapper {
  display: flex;
  flex-direction: column;
  align-items: center;
  background-color: #f0f0f0;
  height: 100%;
  overflow-y: scroll;
}
.image-list {
  display: flex;
  flex-wrap: wrap;
  gap: 10px;
  padding-left: 10px;
  padding-top: 10px;
  overflow: inherit;
  height: 90%;
}

.image-list>div {
  width: 45%;
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
  border-color: #1e90ff;
}

.btn-flex {
  display: flex;
  flex-direction: row;
  gap: 10px;
}
</style>
