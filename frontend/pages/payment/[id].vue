<template>
  <section class="flex h-full w-full justify-center items-center py-5 px-5">
    <div v-if="loading" class="fixed z-50 backdrop-blur-lg h-[100vh] w-[100vw]">
      <img
        src="../../assets/loader.gif"
        class="fixed top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 z-50"
      />
    </div>
    <div
      class="shadow-lg rounded-xl sm:px-8 py-10 max-sm:px-4 md:min-w-[50rem] flex flex-col gap-6 max-md:w-full"
    >
      <div class="flex flex-col justify-center items-center">
        <div
          class="size-12 rounded-full text-white flex items-center justify-center"
          :class="orderDetails.status === 'COMPLETED' ? 'bg-[#ea454c]' : ''"
        >
          <img
            v-if="orderDetails.status === 'COMPLETED'"
            src="../../assets/tick.png"
            class="size-12 invert"
          />
          <img
            v-if="orderDetails.status === 'CANCELLED'"
            src="../../assets/failed.png"
            class="size-12"
          />
          <img
            v-if="orderDetails.status === 'PENDING'"
            src="../../assets/warning.png"
            class="size-12"
          />
        </div>
        <span
          v-if="
            orderDetails.status === 'COMPLETED' ||
            orderDetails.status === 'PENDING'
          "
          class="mt-5 font-bold text-xl mb-3"
          >We received your order !</span
        >
        <span
          v-if="orderDetails.status === 'CANCELLED'"
          class="mt-5 font-bold text-xl mb-3"
          >Order Failed</span
        >
        <span v-if="orderDetails.status === 'COMPLETED'" class="text-sm">
          Your order #{{ orderDetails.id }} is successful
        </span>
        <span v-if="orderDetails.status === 'PENDING'" class="text-semibold">
          Your payment for order #{{ orderDetails.id }} is still pending
        </span>
        <span v-if="orderDetails.status === 'CANCELLED'" class="text-sm">
          Your order #{{ orderDetails.id }} is failed
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
            <span class="text-sm">{{ orderDetails.address }}</span>
          </div>
        </div>
        <div>
          <span class="text-gray-400 uppercase font-bold text-sm"
            >Payment Info</span
          >
          <div class="mt-5 flex flex-col gap-1">
            <span class="text-sm">UPI Gateway</span>
            <span class="text-sm">{{ orderDetails.transaction_id }}</span>
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
              <div class="flex flex-col gap-2">
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
          <span>Sub Total</span><span>₹ {{ orderDetails.total }}</span>
        </div>
        <div class="flex justify-between font-bold">
          <span>Total</span><span>₹ {{ orderDetails.total }}</span>
        </div>
        <div class="flex font-bold">
          <p
            v-if="orderDetails.status === 'PENDING'"
            class="flex text-gray-500"
          >
            Payment :
            <img src="../../assets/warning.png" class="size-5 mt-0.5 m-2" />
            <span class="font-semibold">Pending</span>
          </p>
          <p
            v-if="orderDetails.status === 'COMPLETED'"
            class="flex text-gray-500"
          >
            Payment :
            <img src="../../assets/check.png" class="size-5 mt-0.5 m-2" />
            <span class="font-semibold">Completed</span>
          </p>
          <p
            v-if="orderDetails.status === 'CANCELLED'"
            class="flex text-gray-500"
          >
            Payment :
            <img src="../../assets/failed.png" class="size-5 mt-0.5 m-2" />
            <span class="font-semibold">Failed</span>
          </p>
        </div>
      </div>
    </div>
  </section>

  <div class="flex h-10 justify-center items-center">
    <nuxt-link class="bg-[#ea454c] py-2 px-3 rounded-xl text-white" to="/order">
      My Orders
    </nuxt-link>
  </div>
</template>
<script setup>
import { ref, onMounted } from "vue";
import { useAuthStore } from "../../store/auth";
import { useNuxtApp } from "#app";
import { useRouter, useRoute } from "vue-router";
const loading = ref(true);
const config = useRuntimeConfig();
const router = useRouter();
const route = useRoute();
const orderDetails = ref({});
const authStore = useAuthStore();
onMounted(async () => {
  const nuxtApp = useNuxtApp();
  try {
    await new Promise((r) => setTimeout(r, 2000));
    const orderId = route.params.id;
    const response = await nuxtApp.$authenticatedFetch(
      `${config.public.API_BASE_URL}/api/orders/${orderId}`
    );
    orderDetails.value = response;
  } catch (error) {
    console.error("Error fetching order data", error);
  }
  loading.value = false;
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
