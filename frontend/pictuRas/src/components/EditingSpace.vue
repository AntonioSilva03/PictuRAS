<template>
    <div class="editing-space">
      <div v-if="imageStore.selectedImage" class="image-preview" id="prev">
        <img :src="imageStore.selectedImage" alt="Selected Image" />
      </div>
      <div v-else class="placeholder" id="prev">
        <p>No image selected</p>
      </div>
      <ToolsList id="tools"></ToolsList>
      <ParamsSelector v-if="imageStore.selectedImage" id="params"></ParamsSelector>
    </div>
  </template>
  
  <script setup>
  import { useImageStore } from '../stores/ImageStore';
  import ParamsSelector from './ParamsSelector.vue';
  import ToolsList from './ToolsList.vue';
  
  const imageStore = useImageStore();
  </script>
  
  <style scoped>
  .editing-space {
    background-color: #fff;
    border: 1px solid #ccc;
    display: grid;
    grid-template-rows: 10% 60% 30%;
    grid-template-columns: 30% 60% 10%;
    grid-template-areas:
      ". . ."   
      "tools prev ."
      ". params .";
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

  #tools{
    grid-area: tools;
  }

  #params{
    grid-area: params;
  }

  </style>
  