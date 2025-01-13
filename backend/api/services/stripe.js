const config = require('../config/stripe_config');
const stripe = require('stripe')(config.secretKey);

class StripeService {
    async createPaymentIntent(amount, currency = config.currency, paymentMethods = config.paymentMethods) {
    try {
        const paymentIntent = await stripe.paymentIntents.create({
            amount: amount,
            currency: currency,
            payment_method_types: paymentMethods,
        });
        return paymentIntent;
    } catch (error) {
        throw new Error(`Error creating payment intent: ${error.message}`);
    }
}

    async constructWebhookEvent(payload, signature) {
        try {
            const event = stripe.webhooks.constructEvent(
                payload,
                signature,
                config.webhookSecret
            );
            return event;
        } catch (error) {
            throw new Error(`Webhook Error: ${error.message}`);
        }
    }
}

module.exports = new StripeService();