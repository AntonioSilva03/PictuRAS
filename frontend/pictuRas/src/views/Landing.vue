<template>
    <div class="main-layout">
        <Navbar id="nav"></Navbar>
        <div class="landing-container">

           <!-- Content 1 -->
          <div class="content1-layout">

              <!-- Coluna da Esquerda -->
              <div class="left1-column">

                <div class="content1-wrapper">
                  <div class="logo1-container">
                      <img src="../assets/logo.png" alt="Logo" class="logo1" />
                      <span class="app-name">PictuRAS</span>
                  </div>
                      <h1 class="title">Edit at the speed of your imagination</h1>
                      <p class="description">
                        Give wings to your creativity with the most advanced image editing app ever made. Transform your photos with a single click and achieve stunning, professional-level results. Expand your imagination with our innovative tools designed to take your visuals beyond limits. 
                      </p>
                      <p>
                        Start now for free and explore premium features at an unbeatable price. Unlock your full creative potential with PictuRAS for only €9.99/month (VAT included). Let your imagination lead the way. Terms apply.
                      </p>
                      <Button1 label="Start Now" />
                  </div>

              </div>

              <!-- Coluna da Direita -->
              <div class="right1-column">
                  <video
                      ref="videoElement"
                      class="video-bg"
                      autoplay
                      muted
                      loop
                      playsinline
                  >
                      <source src="../assets/VideoLanding.mp4" type="video/mp4" />
                      Your browser does not support the video element.      
                  </video>
                  <button @click="toggleVideo" class="video-control">
                    <span v-if="isPlaying"><font-awesome-icon icon="fa-solid fa-pause" /></span>
                    <span v-else><font-awesome-icon icon="play" /></span>
                </button>
              </div>

          </div>

          <!-- Content 2 -->
          <div class="content2-layout">

          </div>

      </div>
    </div>
</template>
  
<script>

    import Navbar from '../components/Navbar.vue';
    import Button1 from '../components/Button-style1.vue';
   

    export default {
    name: 'Landing',
    components: {
        Navbar,
        Button1,
    },
    data() {
        return {
            isPlaying: true, 
        };
    },
    methods: {
        toggleVideo() {
            const video = this.$refs.videoElement;
            if (this.isPlaying) {
                video.pause();
            } else {
                video.play();
            }
            this.isPlaying = !this.isPlaying;
        },
    },
    };

</script>
  
  <style scoped>
  
  
  .main-layout {
      display: flex;
      flex-direction: column;
      grid-template-areas:
        "nav nav"
        ". .";
      overflow: auto;
      gap:0px;
      overflow-x: hidden;
  }

  #nav{
    grid-area: nav;
    
  }

  .login-container {
    display: flex;
    justify-content: center;
    align-items: center;
    min-height: 100vh;
    background-color: #f7f7f7;
  }


  .content1-layout {
    grid-area: content;
    display: grid;
    grid-template-columns: 50% 50%; 
    height: 80vh;
  }

  .left1-column {
      padding: 1rem;
      display: flex;
      align-items:center;
      justify-content: right;
  }

  .content1-wrapper {
    margin-right: 20%;
    max-width: 50%; 
}


.content1-wrapper p{
  text-align: justify;
}

.logo1-container {
    display: flex;
    align-items: center; 
    margin-bottom: 1rem;
}

.logo1 {
    width: 50px;
    height: 50px; 
    margin-right: 1rem; 
}

.app-name {
    font-size: 1.2rem;
    font-weight: bold;
    color: #333;
}


.title {
    font-size: 2rem;
    font-weight: bold;
    margin-bottom: 1rem;
    color: #333;
    font-family:Verdana, Geneva, Tahoma, sans-serif;
}

  

  .right1-column {
    padding-top: 0.5em;
    background-color: #fff; 
    display: flex;
    align-items: center;
    justify-content: center;
    position: relative; 
}

.video-bg {
    width: 100%;
    height: 100%;
    object-fit: cover; 
    top: 0;
    left: 0;
}

.video-control {
    position: absolute;
    bottom: 15px;
    right: 15px;
    z-index: 10; 
    background-color: rgba(0, 0, 0, 0.5); 
    color: white;
    border: none;
    padding: 10px 15px;
    width: 40px; 
    height: 40px; 
    border-radius: 50%; 
    cursor: pointer;
    font-size: 1em;
    transition: background-color 0.3s;
}

.video-control:hover {
    background-color: rgba(0, 0, 0, 0.8); 
}



.content2-layout {
    grid-area: content;
    background-color: rgba(170, 170, 170, 0.534);
    display: grid;
    grid-template-columns: 50% 50%;
    height: 80vh;
  }

  </style>
  