<!-- PaymentForm.vue -->
<template>
    <div class="payment-form">
        <div class="order-summary">
            <h3>Order Summary</h3>
            <div class="plan-details">
                <div class="selected-plan">
                    <span class="label">Selected Plan:</span>
                    <span class="value">{{ planName }}</span>
                </div>
                <div class="total-amount">
                    <span class="label">Total Amount:</span>
                    <span class="value">${{ amount.toFixed(2) }}</span>
                </div>
            </div>
        </div>

        <div v-show="loading" class="loading">
            Loading payment form...
        </div>
        <div v-show="!loading">
            <form @submit.prevent="handleSubmit">
                <div ref="paymentElement" class="payment-element"></div>
                <LoadingButton :loading="processing" :disabled="!stripe || processing" class="pay-button">
                    Pay ${{ amount.toFixed(2) }}
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
    props: {
        amount: {
            type: Number,
            required: true
        },
        planName: {
            type: String,
            required: true
        }
    },
    data() {
        return {
            stripe: null,
            elements: null,
            loading: true,
            processing: false,
            errorMessage: ''
        };
    },
    async mounted() {
        try {
            // Initialize Stripe
            this.stripe = await loadStripe('pk_test_51QgoxwFpyquVPMmLaU6S8izTAjKmlZNmlKaP1zoU4u3P1dcZwiHkc2ENEGyAJR8FrasD28ACG9lR53wdtMMLVHwn00e13yJ07b');
            await this.createPaymentIntent();
        } catch (error) {
            this.errorMessage = 'Failed to load payment form';
            console.error('Stripe initialization error:', error);
        }
    },
    methods: {
        async createPaymentIntent() {
            try {
                const requestData = {
                    amount: Math.round(this.amount * 100), // Convert to cents
                };
                console.log('Sending payment intent request:', requestData);

                const response = await fetch('http://localhost:3000/api/create-payment-intent', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json'
                    },
                    body: JSON.stringify(requestData)
                });

                if (!response.ok) {
                    const errorData = await response.text();
                    console.error('Error response:', errorData);
                    throw new Error(`HTTP error! status: ${response.status}`);
                }

                const { clientSecret } = await response.json();

                if (!this.stripe) {
                    throw new Error('Stripe not initialized');
                }

                this.elements = this.stripe.elements({
                    clientSecret,
                    appearance: {
                        theme: 'stripe',
                        variables: {
                            colorPrimary: '#0066cc',
                        }
                    }
                });

                const paymentElement = this.elements.create('payment');
                console.log(this.$refs.paymentElement);
                paymentElement.mount(this.$refs.paymentElement);
                this.loading = false;
            } catch (error) {
                this.errorMessage = `Failed to initialize payment: ${error.message}`;
                console.error('Payment intent creation error:', error);
                this.loading = false;
            }
        },
        async handleSubmit() {
            if (!this.stripe || !this.elements) {
                return;
            }

            this.processing = true;
            this.errorMessage = '';

            try {
                const { error, paymentIntent } = await this.stripe.confirmPayment({
                    elements: this.elements,
                    confirmParams: {
                        return_url: `${window.location.origin}/payment/result?status=success`, // Success URL
                    },
                });

                if (error) {
                    this.errorMessage = error.message;
                    // Redirect to failure page if payment fails
                    this.$router.push('/payment/result?status=failure');
                } else if (paymentIntent && paymentIntent.status === 'succeeded') {
                    // Redirect to success page if payment is successful
                    this.$router.push('/payment/result?status=success');
                }
            } catch (error) {
                this.errorMessage = 'Payment failed. Please try again.';
                console.error('Payment confirmation error:', error);
                // Redirect to failure page if there was an error
                this.$router.push('/payment/result?status=failure');
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
    max-width: 600px;
    margin: 0 auto;
}

.order-summary {
    background: #f8f9fa;
    border-radius: 8px;
    padding: 1.5rem;
    margin-bottom: 2rem;
}

.order-summary h3 {
    margin: 0 0 1rem;
    color: #333;
}

.plan-details {
    display: flex;
    flex-direction: column;
    gap: 0.75rem;
}

.selected-plan,
.total-amount {
    display: flex;
    justify-content: space-between;
    align-items: center;
}

.label {
    color: #666;
}

.value {
    font-weight: 600;
    color: #333;
}

.total-amount .value {
    color: #0066cc;
    font-size: 1.2rem;
}

.loading {
    text-align: center;
    padding: 2rem;
    color: #666;
}

.payment-element {
    margin-bottom: 1.5rem;
    padding: 1rem;
    border-radius: 8px;
    background: white;
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
    padding: 0.75rem;
    border-radius: 4px;
    background-color: #fee2e2;
    color: #dc3545;
    text-align: center;
}
</style>