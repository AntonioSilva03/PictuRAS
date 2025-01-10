<template>
    <div class="plan-layout">
      <Navbar id="nav"></Navbar>
  
      <div class="plan-container">
        <!-- Plano Gratuito -->
        <div class="plan-box" :class="{'active': currentPlan === 'free', 'free-plan': true}">
          <h2>Gratuito</h2>
          <ul>
            <li>5 Operações p/dia</li>
            <li>Imagens de todos os tamanhos</li>
            <li>3 Downloads p/dia</li>
            <li>Downloads de baixa resolução com limite de 1GB</li>
            <li>Limitação de ferramentas</li>
          </ul>
          <h3>Grátis</h3>
          <div v-if="currentPlan === 'free'">
          </div>
          <!-- O botão tem a cor do plano -->
          <button v-else @click="choosePlan('free')" class="free-plan-btn">
            Prosseguir →
          </button>
          <div v-if="currentPlan === 'free'">
            <button disabled>Plano Selecionado</button>
          </div>
        </div>
  
        <!-- Plano Mensal -->
        <div class="plan-box" :class="{'active': currentPlan === 'monthly', 'monthly-plan': true}">
          <h2>Mensal</h2>
          <ul>
            <li>∞ Operações p/dia</li>
            <li>Imagens de todos os tamanhos</li>
            <li>∞ Downloads p/dia</li>
            <li>Downloads HD s/limite</li>
            <li>Disponíveis todas as ferramentas</li>
          </ul>
          <h3>X,xx € p/mês</h3>
          <div v-if="currentPlan === 'monthly'">
          </div>
          <!-- O botão tem a cor do plano -->
          <button v-else @click="choosePlan('monthly')" class="monthly-plan-btn">
            Prosseguir →
          </button>
          <div v-if="currentPlan === 'monthly'">
            <button disabled>Plano Selecionado</button>
          </div>
        </div>
  
        <!-- Plano Anual -->
        <div class="plan-box" :class="{'active': currentPlan === 'annual', 'annual-plan': true}">
          <h2>Anual</h2>
          <ul>
            <li>∞ Operações p/dia</li>
            <li>Imagens de todos os tamanhos</li>
            <li>∞ Downloads p/dia</li>
            <li>Downloads HD s/limite</li>
            <li>Disponíveis todas as ferramentas</li>
          </ul>
          <h3>Y,yy € p/ano</h3>
          <div v-if="currentPlan === 'annual'">
          </div>
          <!-- O botão tem a cor do plano -->
          <button v-else @click="choosePlan('annual')" class="annual-plan-btn">
            Prosseguir →
          </button>
          <div v-if="currentPlan === 'annual'">
            <button disabled>Plano Selecionado</button>
          </div>
        </div>
      </div>
    </div>
  </template>

  




  
  <script>
  import Navbar from '../components/Navbar.vue';
  
  export default {
    name: 'Plan',
    components: {
      Navbar
    },
    data() {
      return {
        // Plano atual (exemplo, inicialmente é 'free')
        currentPlan: 'free', // Pode ser 'free', 'monthly', 'annual'
      };
    },
    methods: {
      choosePlan(plan) {
        // Alterar o plano do usuário
        this.currentPlan = plan;
        console.log(`Plano escolhido: ${plan}`);
      },
    },
  };
  </script>
  








  
  <style scoped>
  .plan-container {
    display: grid;
    grid-template-columns: 1fr 1fr 1fr; /* Divisão em 3 colunas */
    gap: 20px;
    justify-items: center;
    padding: 2rem;
  }
  
  .plan-box {
    background: white;
    padding: 2rem;
    border-radius: 8px;
    box-shadow: rgba(0, 0, 0, 0.25) 0px 4px 6px;
    text-align: center;
    width: 300px;
    height: 350px;
    transition: transform 0.3s ease;
  }
  
  /* Cores para cada plano */
  .free-plan h2, .free-plan h3, .free-plan button {
    color: #007bff; /* Azul */
  }
  
  .monthly-plan h2, .monthly-plan h3, .monthly-plan button {
    color: #8a2be2; /* Roxo */
  }
  
  .annual-plan h2, .annual-plan h3, .annual-plan button {
    color: #d415cb; /* Rosa */
  }
  
  .plan-box h2 {
    font-size: 1.5rem;
    margin-bottom: 1rem;
  }
  
  .plan-box p {
    font-size: 1rem;
    margin-bottom: 1rem;
  }
  
  .plan-box ul {
    list-style-type: none;
    padding: 0;
    margin-bottom: 1rem;
  }
  
  .plan-box ul li {
    margin: 0.5rem 0;
  }
  
  .plan-box button {
    color: white;
    padding: 0.5rem 1rem;
    border: none;
    border-radius: 5px;
    cursor: pointer;
    transition: background-color 0.3s ease;
  }

  .free-plan-btn {
    background-color: #007bff; /* Azul para o plano gratuito */
  }
  
  .monthly-plan-btn {
    background-color: #8a2be2; /* Roxo para o plano mensal */
  }
  
  .annual-plan-btn {
    background-color: #d415cb; /* Rosa para o plano anual */
  }
  
  .plan-box button:hover {
    background-color: #0056b3; /* Cor mais escura ao passar o mouse */
  }
  
  .plan-box button[disabled] {
    background-color: #d3d3d3;
    cursor: not-allowed;
  }
  
  .plan-box.active {
    background-color: #e3f2fd; /* Azul claro para o plano ativo */
  }
  
  .free-plan.active {
    background-color: #d0e7ff; /* Azul claro */
  }
  
  .monthly-plan.active {
    background-color: #d6bbe4; /* Roxo claro */
  }
  
  .annual-plan.active {
    background-color: #fcbade; /* Rosa claro */
  }
  </style>
  