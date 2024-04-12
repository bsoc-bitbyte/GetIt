<template>
<div></div>
</template>
<script >
import { useAttrs } from "vue";
import { useAuthStore } from "../store/auth";
import { useNuxtApp } from "#app";
import { toast } from 'vue3-toastify';

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
      const authStore = useAuthStore();
      const nuxtApp = useNuxtApp();

      try {
        const response = await nuxtApp.$authenticatedFetch(
          `${config.public.API_BASE_URL}/api/orders/`
        );

        console.log("responsoe", response);
        this.orders = response;
      } catch (error) {
        console.log("Error", error);
        toast.error("Error fetching orders", {
          autoClose: 2000,
          position: toast.POSITION.BOTTOM_CENTERAL,
        });

      }
    },
  },
};
</script>
