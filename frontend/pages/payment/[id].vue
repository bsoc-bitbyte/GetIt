<template>
  <section class="flex h-full w-full justify-center items-center py-5 px-5">
    <div
      class="shadow-lg rounded-xl sm:px-8 py-10 max-sm:px-4 md:min-w-[50rem] flex flex-col gap-6 max-md:w-full"
    >
      <div class="flex flex-col justify-center items-center">
        <div
          class="bg-[#ea454c] size-10 rounded-full text-white flex items-center justify-center"
        >
          <img src="../../assets/tick.png" class="size-8 invert" />
        </div>

        <span class="mt-5 font-bold text-xl mb-3">We received your order!</span>
        <span class="text-sm">
          Your order #{{ orderDetails.id }} is completed
        </span>
      </div>
      <hr />
      <div class="flex justify-between gap-10">
        <div class="max-w-72">
          <span class="text-gray-400 uppercase font-bold text-sm"
            >Shipping Address</span
          >
          <div class="mt-5 flex flex-col gap-3">
            <span class="text-sm">{{ orderDetails.buyer }}</span>
            <span class="text-sm"
              >4517 Washington Ave. Manchester, Kentucky 39495, USA</span
            >
          </div>
        </div>
        <div>
          <span class="text-gray-400 uppercase font-bold text-sm"
            >Payment Info</span
          >
          <div class="mt-5 flex flex-col gap-1">
            <span class="text-sm">Credit Card VISA</span>
            <span class="text-sm">**** 4660</span>
          </div>
        </div>
      </div>

      <hr />

      <div class="flex flex-col">
        <span class="text-gray-400 uppercase font-bold text-sm"
          >Order Items</span
        >

        <div
          v-for="product in orderDetails.order_items"
          :key="product.id"
          class="flex flex-col gap-3 mt-6"
        >
          <div class="flex justify-between gap-8">
            <div class="flex gap-4">
              <img
                :src="product.ticket.event.cover_image"
                alt=""
                class="size-20 rounded-xl object-cover"
              />
              <div class="flex flex-col gap-3">
                <span class="font-bold">{{ product.ticket.event.title }}</span>
                <span class="text-sm text-gray-600"
                  >Quantity: {{ product.quantity }}</span
                >
              </div>
            </div>
            <span class="font-bold"
              >₹ {{ product.ticket.event.ticket_price }}</span
            >
          </div>
        </div>
      </div>

      <hr />
      <div class="flex flex-col gap-3">
        <div class="flex justify-between text-gray-600">
          <span>Sub Total</span><span>₹ {{ subTotal }}</span>
        </div>
        <div class="flex justify-between font-bold">
          <span>Total</span><span>₹ {{subTotal}}</span>
        </div>
      </div>
    </div>
  </section>
</template>

<script setup>
import { ref, onMounted } from "vue";
import { useRoute } from "vue-router";
import { useAuthStore } from "../../store/auth";
import { useNuxtApp } from "#app";
import { useRouter } from "vue-router";


const config = useRuntimeConfig();
const router = useRouter();
const orderDetails = ref({});
let subTotal = 0;
const authStore = useAuthStore();

onMounted(async () => {
  const nuxtApp = useNuxtApp();
  try {
    const orderId = route.params.id;
    const response = await nuxtApp.$authenticatedFetch(
      `${config.public.API_BASE_URL}/api/orders/${orderId}`
    );

    orderDetails.value = response;

    if(orderDetails.value.order_items.length > 0) {
      orderDetails.value.order_items.forEach((item) => {
        subTotal += item.ticket.event.ticket_price * item.quantity;
      });
    }
    console.log(subTotal);
  } catch (error) {
    console.error("Error fetching order data", error);
  }
});

if (!authStore.isAuthenticated) {
  router.push("/Signin");
}

</script>

<style scoped>
.dropdown-title svg {
  transition: transform 0.3s;
}

.rotate-180 {
  transform: rotate(180deg);
}
</style>
