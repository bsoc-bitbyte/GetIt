<template>
    <main>
        <form id="payment-form" @submit.prevent="handleSubmit">
            <div id="link-authentication-element" />
            <div id="payment-element" />
            <button id="submit" :disabled="isLoading">
                Pay now
            </button>
            <sr-messages :messages="messages" />
        </form>
    </main>
</template>

<script>
export default {
    name: 'CheckoutComp',
    props : {
        ticket_price: {
            type: Number,
            required: true,
        },
    },
    data() {
        return {
            stripe: null,
            elements: null,
            isLoading: false,
            messages: [],
        }
    },
   async mounted() {
        this.stripe = Stripe('pk_test_51OK0jxSCqTflNj8ZV0Ia9yT26uoVr6bopgfSrnlkhpUTZsBX8oyUTXg4YbYlbOOjdcXqraA71vtKPbOpMyIGeNF800MpWzhMHB'); // Use environment variable in production

        const { clientSecret, error: backendError } = await this.createPaymentIntent({
            payment_method_types: ['card'],
            amount:  10000,
            currency: 'inr',
        });
        console.log("clientSecret", clientSecret);
        if (backendError) {
            this.messages.push(backendError.message);
        }
        this.messages.push(`Client secret returned.`);

        this.elements = this.stripe.elements({clientSecret})
        const paymentElement = this.elements.create('payment');
        paymentElement.mount("#payment-element");
        const linkAuthenticationElement = this.elements.create("linkAuthentication");
        linkAuthenticationElement.mount("#link-authentication-element");
        this.isLoading = false;
    },
    methods: {

        async createPaymentIntent(requestData) {
            console.log("requestData", requestData);
            let clientSecret,backendError ;

            try {
                const response = await this.$axios.post('/api/tickets/create-payment-intent/', requestData);
                console.log("response", response);
                clientSecret = response.data.clientSecret;
            }
            catch (error) {
                backendError = error.response;
                console.log("error", error)
            }
            return { clientSecret, backendError };
        },
        async handleSubmit () {
            if (this.isLoading) {
                return;
            }

            this.isLoading = true;

            const { error } = await this.stripe.confirmPayment({
                elements : this.elements,
                confirmParams: {
                    return_url: `${window.location.origin}/return`
                }
            });

            if (error.type === "card_error" || error.type === "validation_error") {
                this.messages.push(error.message);
            } else {
               this.messages.push("An unexpected error occured.");
            }

            this.isLoading = false;
        }
    }
}
</script>