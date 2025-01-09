<template>
    <nav class="navbar">
      <div class="navbar-container">
        <!-- Logo -->
        <div class="navbar-logo">
          <RouterLink to="/">PictuRAS</RouterLink>
        </div>
  
        <!-- Navigation Links -->
        <ul class="navbar-links">
          <li><RouterLink to="/profile">Profile</RouterLink></li>
          <li><RouterLink to="/projects">My Projects</RouterLink></li>
          <li v-if="isLoggedIn">
            <button @click="signOut">Sign Out</button>
          </li>
          <li v-else>
            <RouterLink to="/login">Login</RouterLink>
          </li>
        </ul>
      </div>
    </nav>
  </template>
  
  <script setup>
  import { ref } from 'vue';
  import { RouterLink } from 'vue-router';
  
  // Mock logged-in state
  const isLoggedIn = ref(false);
  
  function signOut() {
    // Handle sign-out logic here
    alert('You have been signed out.');
    isLoggedIn.value = false;
  }
  </script>
  
  <style scoped>
  /* Navbar styles */
  .navbar {
    background-color: #333;
    color: #fff;
    padding: 1rem;
    display: flex;
    align-items: center;
    height: 36px;
    width: 100%;
    justify-content: flex-start; /* Align everything to the left */
  }
  
  .navbar-container {
    display: flex;
    justify-content: space-between;
    align-items: center;
    width: 95%;
  }
  
  .navbar-logo {
    font-size: 1.5rem;
    font-weight: bold;
  }
  
  .navbar-logo a {
    text-decoration: none;
    color: #fff;
  }
  
  .navbar-links {
    list-style: none;
    display: flex;
    gap: 1rem;
    margin: 0;
    padding: 0;
  }
  
  .navbar-links a {
    text-decoration: none;
    color: #fff;
    font-weight: 500;
  }
  
  .navbar-links button {
    background: none;
    border: none;
    color: #fff;
    font-size: 1rem;
    cursor: pointer;
    font-weight: 500;
  }

  </style>
  