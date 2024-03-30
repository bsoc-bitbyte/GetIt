<template>
    <main>
        <form id="payment-form" @submit.prevent="handleSubmit">
            <div id="link-authentication-element" />
            <div id="payment-element" />
            <button id="submit" :class="{ 'cursor-not-allowed': isLoading }"
                :style="{ backgroundColor: isLoading ? 'rgba(234, 69, 76, 0.5)' : 'rgba(234, 69, 76, 1)' }"
                class="py-[1rem] text-[white] md:font-bold mt-[10px] ml-[0.2em] min-[1240px]:px-[6rem] rounded-3xl max-[1239px]:w-full" :disabled="isLoading"> Pay now
            </button>
            <sr-messages :messages="messages" />
        </form>
    </main>
</template>

<script setup>
import { ref, onMounted } from 'vue'; 

const isLoading = ref(false);
const messages = ref([]); 
let stripe = null, elements = null;

onMounted(async () => {
  // Load Stripe.js dynamically
  stripe = await Stripe(process.env.STRIPE_PUBLIC_KEY); 

  const { data, error } = await createPaymentIntent();

  if (data) {
    elements = stripe.elements({ clientSecret: data.clientSecret }); 
    // ... mount paymentElement and linkAuthenticationElement ...
  } else if (error) {
    messages.value.push(error.message);
  }

  isLoading.value = false; 
});

const createPaymentIntent = async () => {
  try {
    const requestData = {
      payment_method_types: ['card'],
      ticket_id: 1, // Replace with dynamic ticket ID (if needed) 
      amount: 10000, 
      currency: 'inr',
    };

    const response = await $fetch('/api/tickets/create-payment-intent/', {
      method: 'POST',
      body: requestData,
    });
    
    // Since $fetch directly returns the parsed response...
    return { data: response, error: null }; 

  } catch (error) {
     console.error(error);
     // Handle error gracefully (display to user, etc.)
     return { data: null, error }; 
  }
};

const handleSubmit = async (event) => {
  if (isLoading.value) return;

  isLoading.value = true;

  try {
    const { error } = await stripe.confirmPayment({
      elements: elements,
      confirmParams: {
        return_url: `${window.location.origin}/return`
      }
    });

    if (error.type === "card_error" || error.type === "validation_error") {
      messages.value.push(error.message);
    } else {
      messages.value.push("An unexpected error occured.");
    } 

  } catch (error) {
    // Handle unexpected errors
  } finally {
    isLoading.value = false;
  }
}
</script>