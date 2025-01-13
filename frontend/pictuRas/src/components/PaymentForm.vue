<template>
    <div class="payment-form">
        <div v-if="loading" class="loading">
            Loading payment form...
        </div>
        <div v-else>
            <div class="amount-section">
                <h3>Amount to Pay: ${{ amount.toFixed(2) }}</h3>
            </div>
            <form @submit.prevent="handleSubmit">
                <div ref="paymentElement" class="payment-element"></div>
                <LoadingButton 
                    :loading="processing" 
                    :disabled="!stripe || processing"
                    class="pay-button"
                >
                    Pay Now
                </LoadingButton>
                <div v-if="errorMessage" class="error-message">
                    {{ errorMessage }}
                </div>
            </form>
        </div>
    </div>
</template>

<script>
import { loadStripe } from '@stripe/stripe-js';
import LoadingButton from './LoadingButton.vue';

export default {
    name: 'PaymentForm',
    components: {
        LoadingButton
    },
    data() {
        return {
            stripe: null,
            elements: null,
            loading: true,
            processing: false,
            errorMessage: '',
            amount: 99.99 // Replace with your actual amount
        };
    },
    async mounted() {
        try {
            // Initialize Stripe
            this.stripe = await loadStripe('your_publishable_key');
            await this.createPaymentIntent();
        } catch (error) {
            this.errorMessage = 'Failed to load payment form';
            console.error('Stripe initialization error:', error);
        }
    },
    methods: {
        async createPaymentIntent() {
            try {
                const response = await fetch('/api/create-payment-intent', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json'
                    },
                    body: JSON.stringify({
                        amount: this.amount * 100 // Convert to cents
                    })
                });

                const { clientSecret } = await response.json();

                // Create Elements instance
                this.elements = this.stripe.elements({
                    clientSecret,
                    appearance: {
                        theme: 'stripe',
                        variables: {
                            colorPrimary: '#0066cc',
                        }
                    }
                });

                // Create and mount the Payment Element
                const paymentElement = this.elements.create('payment');
                paymentElement.mount(this.$refs.paymentElement);
                this.loading = false;
            } catch (error) {
                this.errorMessage = 'Failed to initialize payment';
                console.error('Payment intent creation error:', error);
            }
        },
        async handleSubmit() {
            if (!this.stripe || !this.elements) {
                return;
            }

            this.processing = true;
            this.errorMessage = '';

            try {
                const { error } = await this.stripe.confirmPayment({
                    elements: this.elements,
                    confirmParams: {
                        return_url: `${window.location.origin}/payment/success`,
                    },
                });

                if (error) {
                    this.errorMessage = error.message;
                }
            } catch (error) {
                this.errorMessage = 'Payment failed. Please try again.';
                console.error('Payment confirmation error:', error);
            } finally {
                this.processing = false;
            }
        }
    }
};
</script>

<style scoped>
.payment-form {
    width: 100%;
}

.loading {
    text-align: center;
    padding: 2rem;
    color: #666;
}

.amount-section {
    margin-bottom: 2rem;
    text-align: center;
}

.payment-element {
    margin-bottom: 1.5rem;
}

.pay-button {
    width: 100%;
    padding: 0.75rem;
    background-color: #0066cc;
    color: white;
    border: none;
    border-radius: 4px;
    font-size: 1rem;
    cursor: pointer;
    transition: background-color 0.2s;
}

.pay-button:disabled {
    background-color: #ccc;
    cursor: not-allowed;
}

.error-message {
    margin-top: 1rem;
    color: #dc3545;
    text-align: center;
}
</style>