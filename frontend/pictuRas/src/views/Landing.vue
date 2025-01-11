<template>
    <div class="main-layout">
        <Navbar id="nav"></Navbar>
        <div class="landing-container">

           <!-- Content 1 -->
          <div class="content1-layout" ref="content1">

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
                  <VideoControlButton
                        :isPlaying="isPlaying"
                        :bottom="'20px'"
                        :right="'20px'"
                        @toggle="toggleVideo"
                    />
              </div>

          </div>

          <!-- Content 2 -->
          <div class="content2-layout">
                <div class="content2-wrapper">

                    <!-- Conteúdo da coluna esquerda -->
                    <div class="left2-column">
                        <div class="video2-container">
                            <video
                                ref="videoElement"
                                class="video-bg2"
                                autoplay
                                muted
                                loop
                                playsinline
                            >
                                <source src="../assets/RecorteImagem.mp4" type="video/mp4" />
                                Your browser does not support the video element.
                            </video>
                            <VideoControlButton
                                :isPlaying="isPlaying"
                                :bottom="'15px'"
                                :right="'85%'"
                                @toggle="toggleVideo"
                            />
                        </div>
                    </div>

                    <!-- Conteúdo da coluna direita -->
                    <div class="right2-column">
                        <p class="p2">Recortar imagens</p>
                        <h2 class="title2">Faça edições instantâneas</h2>
                        <p class="p21">
                            Descubra ferramentas avançadas para recortar, ajustar e transformar imagens com precisão. Experimente edições rápidas e eficientes, deixando suas fotos exatamente como você imaginou. Tudo isso em um ambiente fácil de usar e com resultados profissionais.
                        </p>
                    </div>
                </div>
          </div>

          <!-- Content 3 -->
          <div class="content3-layout">
                <div class="content3-wrapper">
                    <img src="../assets/logo.png" alt="Logo" class="content3-logo" />
                    <h2 class="content3-title">Precisa de uma edição rápida?</h2>
                    <h3 class="content3-subtitle">Disponibilizamos ferramentas avançadas para facilitar a sua vida.</h3>
                    <p class="content3-description">
                        Explore as ferramentas mais modernas para recortar, redimensionar e personalizar imagens. 
                        Crie designs únicos e impressionantes com facilidade e rapidez.
                    </p>
                    <Button2 :onClick="myFunction">
                        Veja todos os recursos
                    </Button2>

                </div>
          </div>

          <!-- Content 4 -->
          <div class="content4-layout">

          </div>

           <!-- Content 5 -->
           <div class="margin-bot">

            </div>

      </div>
      <Footer :showFooter="showFooter" />
    </div>
</template>
  
<script>

    import Navbar from '../components/Navbar.vue';
    import Button1 from '../components/Button-style1.vue';
    import VideoControlButton from '../components/VideoControlButton.vue';
    import Button2 from '../components/Button-style2.vue';
    import Footer from "../components/FooterLanding.vue";

    export default {
    name: 'Landing',
    components: {
        Navbar,
        Button1,
        VideoControlButton,
        Button2,
        Footer
    },
    data() {
        return {
            isPlaying: true, 
            showFooter: false,
        };
    },
    mounted() {
    window.addEventListener("scroll", this.handleScroll);
    },
    beforeDestroy() {
        window.removeEventListener("scroll", this.handleScroll);
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
        handleScroll() {
        const content1 = this.$refs.content1;
        const rect = content1.getBoundingClientRect();

        // Mostra o footer quando content1 desaparece
        this.showFooter = rect.bottom < 0;
        },
    },
    };

</script>
  
  <style scoped>
  

  /* Content 1 */
  
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
    margin-right: 18%;
    max-width: 55%; 
    text-align: justify;
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
    background: linear-gradient(
        82.3deg,
        #000000 0%, 
        rgba(150, 93, 233, 1) 24.8%,
        rgba(99, 88, 238, 1) 70.3%
    );
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent; 
    background-clip: text; 
    
}

  

.right1-column {
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

/* Content 2 */

.content2-layout {
    background-color: rgba(170, 170, 170, 0.534);
    display: flex;
    justify-content: center;
    align-items: center;
    grid-template-columns: 50% 50%;
    height: 80vh;
  }

  .content2-wrapper {
  display: grid;
  grid-template-columns: 40% 60%; 
  width: 70%; 
  height: 100%; 
 
}

.left2-column,
.right2-column {
  display: flex;
  align-items: center; 
  justify-content: center; 
  padding: 1rem; 
}


.left2-column {
    display: flex;
    align-items: center;
    justify-content: end;
    position: relative; 
    
}

.video-bg2 {
    top: 0;
    left: 0; 
}

.video2-container {
    position: relative;
    display: flex;
    align-items: center;
    justify-content: center;
    width: auto; 
    height: auto; 
}

.right2-column{
    display: flex;
    flex-direction: column;
    align-items: start;
    justify-content: start;
    height: 30%;
    margin: auto;
    text-align: start;
    width: 70%;
}

.p2{
    font-weight: 700;
    text-transform: uppercase;
    font-family: 'Adobe Clean', adobe-clean, 'Trebuchet MS', sans-serif;
    font-size: 12px;
}

.title2{
    font-size: 33px;
    font-family: 'Adobe Clean', adobe-clean, 'Trebuchet MS', sans-serif;
    line-height: 35px;
    margin-bottom: 1em;

}

.p21{
    word-wrap: break-word;
    text-align: justify;
    font-size: 16px;
    font-weight: 70;
}
    

/* Content 3 */

.content3-layout {
    background-color: rgba(255, 174, 0, 0.534);
    display: flex;
    justify-content: center;
    align-items: center;
    height: 60vh;
    font-family: 'Adobe Clean', adobe-clean, 'Trebuchet MS', sans-serif;
    background: linear-gradient(90deg, #ff00ffcc, #ff6600c2, #ffcc00); 
  }

.content3-wrapper {
  text-align: center;
  width: 70%;
  height: 70%;
  margin: auto;
}

.content3-logo {
  width: 80px;
  height: 80px;
  margin-bottom: 1rem;
}

.content3-title {
  font-size: 2rem;
  font-weight: bold;
  margin-bottom: 0.5rem;
}

.content3-subtitle {
  font-size: 1.5rem;
  margin-bottom: 1rem;
  font-weight: bold;
  font-weight: 400;
}

.content3-description {
  font-size: 1rem;
  margin-bottom: 4rem;
  line-height: 1.5;
  max-width: 600px;
  margin-left: auto;
  margin-right: auto;
}




/* Content 4 */

.content4-layout {
    background-color: rgba(255, 255, 255, 0.534);
    display: flex;
    justify-content: center;
    align-items: center;
    grid-template-columns: 50% 50%;
    min-height: 80vh;
}



.margin-bot{
    height: 15vh;
    width: 100%;

}


  </style>
  