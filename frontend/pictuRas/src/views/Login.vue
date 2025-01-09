<template>
  <div class="login-layout">

    <!-- navbar  -->
    <Navbar id="nav"></Navbar>

    <!-- Login  -->
    <div class="login-container">
      <div class="login-box">
        <img src="../assets/logo.png" alt="Logo" class="login-logo" />
        <form @submit.prevent="handleLogin" class="login-form-group ">
          <Inputs
            id="email"
            type="email"
            placeholder="Username or email"
            v-model="email"
            required
          />
          <Inputs
            id="password"
            type="password"
            placeholder="Password"
            v-model="password"
            required
          />
          <Button1 type="submit" label="Login" />
        </form>
        <GoogleButton />
      </div>
    </div>
  </div>


</template>


 <!-- Logic--> 
<script>
  import Navbar from '../components/Navbar.vue';
  import Inputs from "../components/Inputs.vue";
  import Button1 from "../components/Button-style1.vue";
  import GoogleButton from "../components/GoogleButton.vue"; 

  export default {
    name: 'Login',
    components: {
        Navbar,
        Inputs,
        Button1,
        GoogleButton,
    },
    data() {
    return {
      email: "",
      password: "",
    };
  },
  methods: {
    handleLogin() {
      console.log("Email:", this.email);
      console.log("Password:", this.password);
      
    },
  },
  };
</script>



<!-- CSS-->
<style scoped>

.login-layout{
  max-height: 100%;
  overflow: hidden;
}

.login-container {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100vh;
  background-color: #f7f7f7;
}

.login-box {
  background: white;
  padding: 2rem;
  border-radius: 8px;
  box-shadow: rgba(0, 0, 0, 0.25) 0px 54px 55px, rgba(0, 0, 0, 0.12) 0px -12px 30px, rgba(0, 0, 0, 0.12) 0px 4px 6px, rgba(0, 0, 0, 0.17) 0px 12px 13px, rgba(0, 0, 0, 0.09) 0px -3px 5px;
  text-align: center;
  width: 100%;
  max-width: 400px;
  height: 60%;
}

.login-logo {
  max-width: 200px;
  margin-bottom: 1rem;
}

.login-form-group {
  margin-bottom: 3rem;
}


</style>