<template>
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
  </template>
  
  
  <script setup>
  import { useImageStore } from '../stores/ImageStore';
  
  // Access the store
  const imageStore = useImageStore();
  const images = imageStore.images;
  
  // Select an image using the store's action
  function selectImage(image) {
    imageStore.selectImage(image);
  }
  </script>
  
  <style scoped>
  .image-list {
    display: flex;
    flex-wrap: wrap;
    flex-direction: column;
    gap: 5px;
    background-color: #f0f0f0;
    height: 100%;
    overflow-y: scroll;
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
  </style>
  