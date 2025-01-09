<template>
    <div class="editing-space">
      <div v-if="imageStore.selectedImage" class="image-preview" id="prev">
        <img :src="imageStore.selectedImage" alt="Selected Image" />
      </div>
      <div v-else class="placeholder" id="prev">
        <p>No image selected</p>
      </div>
    </div>
  </template>
  
  <script setup>
  import { useImageStore } from '../stores/ImageStore';
  
  const imageStore = useImageStore();
  </script>
  
  <style scoped>
  .editing-space {
    background-color: #fff;
    border: 1px solid #ccc;
    display: grid;
    grid-template-rows: 20% 60% 20%;
    grid-template-columns: 30% 60% 10%;
    grid-template-areas:
      ". . ."   
      "tools prev ."
      ". . .";
    height: 100%;
    width: 100%;
  }

  .image-preview {
    display: flex;
    align-items: center;
    justify-content: center;
  }
  
  .image-preview img {
    max-width: 100%;
    max-height: 100%;
    object-fit: contain;
  }
  
  .placeholder {
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 3rem;
    color: #999;
  }
  #prev{
    grid-area: prev;
  }
  </style>
  