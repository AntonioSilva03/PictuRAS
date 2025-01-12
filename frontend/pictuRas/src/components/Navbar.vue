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
    padding-top: 1rem;
    padding-bottom: 1rem;
    display: flex;
    align-items: center;
    width: 100%;
    justify-content: center; /* Align everything to the left */
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

  .navbar-links li {
    text-decoration: none;
    position: relative;
    overflow: hidden;
    transition: background-color 0.3s, color 0.3s, transform 0.3s;
    border: none;
    cursor: pointer;
    padding: 5px 10px;
  }

  .navbar-links li:after{
    content: '';
    position: absolute;
    bottom: 0;
    left: 50%;
    width: 0;
    height: 2px;
    background-color: #fff;
    transition: width 0.3s ease, left 0.3s ease;
  }

  .navbar-links li:hover::after{
    width: 100%;
    left: 0;
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
  