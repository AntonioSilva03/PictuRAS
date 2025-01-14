<template>
    <div class="payment-result">
      <div v-if="status === 'success'" class="payment-success">
        <h1>Payment Successful</h1>
        <p>Your transaction was successful. Thank you for your payment!</p>
        <button @click="goHome">Back to Profile Page</button>
      </div>
  
      <div v-if="status === 'failure'" class="payment-failure">
        <h1>Payment Failed</h1>
        <p>Unfortunately, your payment could not be processed. Please try again.</p>
        <button @click="retryPayment">Retry Payment</button>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    name: 'PaymentResult',
    data() {
      return {
        status: 'pending', // status can be 'success', 'failure', or 'pending'
      };
    },
    mounted() {
      // Check the URL for the success or failure status
      const status = this.$route.query.status; // The status will come from the query params
      if (status === 'success') {
        this.status = 'success';
      } else if (status === 'failure') {
        this.status = 'failure';
      }
    },
    methods: {
      goHome() {
        this.$router.push('/profile'); // Redirect to profile page
      },
      retryPayment() {
        this.$router.push('/payment'); // Redirect to payment page to retry
      },
    },
  };
  </script>
  
  <style scoped>
  .payment-result {
    text-align: center;
    margin-top: 50px;
  }
  
  .payment-success,
  .payment-failure {
    margin-top: 30px;
  }
  
  button {
    padding: 10px 20px;
    background-color: #0066cc;
    color: white;
    border: none;
    border-radius: 4px;
    cursor: pointer;
  }
  
  button:hover {
    background-color: #005bb5;
  }
  </style>
  