<template>
  <div class="lg:flex my-16 md:mx-32 m-4">
    <section class="w-full content-center">
      <div class="flex flex-col gap-4">
        <span class="text-2xl font-bold">Your Orders</span>
        <hr />
        <div
          class="p-4 flex flex-col gap-2 rounded-xl shadow-md"
          v-for="(order, index) in orders.reverse()"
          :key="index"
        >
          <div class="flex justify-between max-md:flex-col gap-2">
            <div class="flex gap-10">
              <div class="flex flex-col gap-1">
                <p class="font-semibold text-gray-700">Order Placed</p>
                <p class="text-sm">{{ order.created_at.slice(0, 10) }}</p>
              </div>
              <div class="flex flex-col gap-1">
                <p class="font-semibold text-gray-700">Email</p>
                <p class="text-sm">{{ order.buyer }}</p>
              </div>
            </div>
            <div>
              <p class="font-semibold text-gray-700">Order Id</p>
              <p class="text-sm"># {{ order.id }}</p>
            </div>
          </div>
          <hr />
          <div>
            <div
              class="flex mt-2"
              v-for="(orderItem, index) in order.order_items"
              :key="index"
            >
              <img
                class="size-24 object-cover rounded-xl"
                :src="orderItem.ticket.event.cover_image"
                alt="Watch"
              />

              <div class="px-4 flex justify-between w-full">
                <div>
                  <h5 class="font-bold">{{ orderItem.ticket.event.title }}</h5>
                  <p class="text-gray-500">
                    quantity : {{ orderItem.quantity }}
                  </p>
                  <p class="mt-4 font-bold">{{ order.price }}</p>
                </div>
                <div>
                  <span class="font-bold"
                    >₹ {{ orderItem.ticket.event.ticket_price }}</span
                  >
                </div>
              </div>
            </div>
          </div>
          <hr class="my-2" />
          <div
            class="flex max-md:flex-col md:gap-10 gap-2 justify-between w-full"
          >
            <div class="w-full">
              <p class="font-bold text-black-700 mb-1">Billing Address</p>
              <p class="mb-2">{{ order.buyer_name }}</p>
              <p>{{ order.address }}</p>
            </div>
            <hr />

            <div class="flex flex-col gap-2">
              <div class="flex gap-20 justify-between text-gray-600">
                <p>Subtotal</p>
                <p>₹{{ order.total }}</p>
              </div>
              <div class="flex gap-20 justify-between text-gray-600">
                <p>Shipping</p>
                <p>₹0</p>
              </div>
              <div class="flex gap-20 justify-between font-bold">
                <p>Total</p>
                <p>₹ {{ order.total }}</p>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>
  </div>
</template>
<script>
import { useAttrs } from "vue";
import { useAuthStore } from "../store/auth";
import { useNuxtApp } from "#app";
import { toast } from "vue3-toastify";

const config = useRuntimeConfig();
export default {
  data() {
    return {
      orders: [],
    };
  },
  async mounted() {
    await this.fetchOrders();
  },
  methods: {
    async fetchOrders() {
      const nuxtApp = useNuxtApp();

      try {
        const response = await nuxtApp.$authenticatedFetch(
          `${config.public.API_BASE_URL}/api/orders/`
        );

        this.orders = response;
      } catch (error) {
        console.error("Error fetching orders", error);
        toast.error("Error fetching orders", {
          autoClose: 2000,
          position: toast.POSITION.BOTTOM_CENTERAL,
        });
      }
    },
  },
};
</script>
