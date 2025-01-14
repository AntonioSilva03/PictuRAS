<template>
    <div class="main-layout">
        <Navbar id="nav"></Navbar>
        <div class="payment-container">
            <h2>Complete Your Payment</h2>
            <PaymentForm 
                :amount="amount"
                :planName="planName"
            />
        </div>
    </div>
</template>

<script>
import Navbar from '../components/Navbar.vue';
import PaymentForm from '../components/PaymentForm.vue';

export default {
    name: 'Payment',
    components: {
        Navbar,
        PaymentForm
    },
    data() {
        return {
            amount: 1000,
            planName: 'anual premium'
        }
    }/*,
    created() {
        // Get the amount and plan name from route query params or state management
        this.amount = this.$route.query.amount ? parseFloat(this.$route.query.amount) : 0;
        this.planName = this.$route.query.plan || '';
    }*/
};
</script>

<style scoped>
.main-layout {
    background-color: rgb(255, 255, 255);
}

.payment-container {
    max-width: 600px;
    margin: 2rem auto;
    padding: 2rem;
    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    border-radius: 8px;
}

h2 {
    text-align: center;
    margin-bottom: 2rem;
    color: #333;
}
</style>