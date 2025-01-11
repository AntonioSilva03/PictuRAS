<template>
    <div class="register-layout">
  
      <!-- navbar  -->
      <Navbar id="nav"></Navbar>
  
      <!-- register  -->
      <div class="register-container">
        <div class="register-box">
          <img src="../assets/logo.png" alt="Logo" class="register-logo" />
          <form @submit.prevent="handleRegister" class="register-form-group ">
            <Inputs
              id="email"
              label=""
              type="email"
              placeholder="Email"
              v-model="email"
              required
            />
            <Inputs
              id="Username"
              label=""
              type="username"
              placeholder="Username"
              v-model="username"
              required
            />

            <div class="password-container">
                <Inputs
                    id="password"
                    label=""
                    type="password"
                    placeholder="Password"
                    v-model="password"
                    @focus="toggleModal(true)"
                    @blur="toggleModal(false)"
                    required
                />


                <!-- Modal de Validação -->
                <PasswordValidationModal
                    :show="showPasswordModal"
                    :password="password"
                />
            </div>


            <Button1 type="submit" @click="handleRegister" label="Register" />
          </form>
          <GoogleButton label="Sign Up with google" />
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
    import PasswordValidationModal from "../components/PasswordValidationModal.vue"
    import Toastify from "toastify-js";
    import "toastify-js/src/toastify.css";

  
    export default {
      name: 'Register',
      components: {
          Navbar,
          Inputs,
          Button1,
          GoogleButton,
          PasswordValidationModal,
      },
      data() {
      return {
        email: "",
        username:"",
        password: "",
        showPasswordModal: false,
      };
    },
    methods: {
        handleRegister() {

            console.log("Chamando o handleRegister...");

            if (!this.email || !this.username || !this.password) {
                Toastify({
                    text: '⚠️ Please fill in all required fields!',
                    duration: 3000, 
                    close: true,
                    gravity: "bottom",
                    position: "right", 
                    backgroundColor: "White", 
                    stopOnFocus: true, 
                    style:{
                        fontWeight: "bold",
                        boxShadow: "0px 4px 6px rgba(0, 0, 0, 0.3)",
                        color: "black",
                    }
                }).showToast();
                return;
            }

            console.log("Email:", this.email);
            console.log("Username:", this.username);
            console.log("Password:", this.password);
            
        },

        validatePassword() {
        console.log("Validando senha...");
        },

        toggleModal(state) {
            console.log("Modal state:", state);
            this.showPasswordModal = state;
        },
    },
    };
</script>
  
  
  
  <!-- CSS-->
<style scoped>
  
    .register-layout{
        max-height: 100%;
        overflow: hidden;
    }
    
    .register-container {
        display: flex;
        justify-content: center;
        align-items: center;
        height: 100vh;
        background-color: #f7f7f7;
    }
    
    .register-box {
        background: white;
        padding: 2rem;
        border-radius: 8px;
        box-shadow: rgba(0, 0, 0, 0.25) 0px 54px 55px, rgba(0, 0, 0, 0.12) 0px -12px 30px, rgba(0, 0, 0, 0.12) 0px 4px 6px, rgba(0, 0, 0, 0.17) 0px 12px 13px, rgba(0, 0, 0, 0.09) 0px -3px 5px;
        text-align: center;
        width: 100%;
        max-width: 400px;
        height: 60%;
    }
    
    .register-logo {
        max-width: 200px;
        margin-bottom: 1rem;
    }
    
    .register-form-group {
        margin-bottom: 1rem;
    }

    .password-container {
        position: relative;
        }

  
</style>