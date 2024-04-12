<template>
  <!-- <div class="bg-white p-8 rounded-md w-full">
    <div class=" flex items-center justify-between pb-6">
      <div>
        <h2 class="text-gray-600 font-semibold">Products Oder</h2>
        <span class="text-xs">All products item</span>
      </div>
      <div class="flex items-center justify-between">
        <div class="flex bg-gray-50 items-center p-2 rounded-md">
          <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 text-gray-400" viewBox="0 0 20 20" fill="currentColor">
            <path fill-rule="evenodd"
              d="M8 4a4 4 0 100 8 4 4 0 000-8zM2 8a6 6 0 1110.89 3.476l4.817 4.817a1 1 0 01-1.414 1.414l-4.816-4.816A6 6 0 012 8z"
              clip-rule="evenodd" />
          </svg>
          <input class="bg-gray-50 outline-none ml-1 block " type="text" name="" id="" placeholder="search...">
        </div>
        <div class="lg:ml-40 ml-10 space-x-8">
          <button class="bg-indigo-600 px-4 py-2 rounded-md text-white font-semibold tracking-wide cursor-pointer">New
            Report</button>
          <button
            class="bg-indigo-600 px-4 py-2 rounded-md text-white font-semibold tracking-wide cursor-pointer">Create</button>
        </div>
      </div>
    </div>
    <div>
      <div class="-mx-4 sm:-mx-8 px-4 sm:px-8 py-4 overflow-x-auto">
        <div class="inline-block min-w-full shadow rounded-lg overflow-hidden">
          <table class="min-w-full leading-normal">
            <thead>
              <tr>
                <th
                  class="px-5 py-3 border-b-2 border-gray-200 bg-gray-100 text-left text-xs font-semibold text-gray-600 uppercase tracking-wider">
                  Name
                </th>
                <th
                  class="px-5 py-3 border-b-2 border-gray-200 bg-gray-100 text-left text-xs font-semibold text-gray-600 uppercase tracking-wider">
                  products
                </th>
                <th
                  class="px-5 py-3 border-b-2 border-gray-200 bg-gray-100 text-left text-xs font-semibold text-gray-600 uppercase tracking-wider">
                  Created at
                </th>
                <th
                  class="px-5 py-3 border-b-2 border-gray-200 bg-gray-100 text-left text-xs font-semibold text-gray-600 uppercase tracking-wider">
                  QRT
                </th>
                <th
                  class="px-5 py-3 border-b-2 border-gray-200 bg-gray-100 text-left text-xs font-semibold text-gray-600 uppercase tracking-wider">
                  Status
                </th>
              </tr>
            </thead>
            <tbody>
              <tr v-for="(order, index) in  orders " :key="index">
                <td class="px-5 py-5 border-b border-gray-200 bg-white text-sm">
                  <div class="flex items-center">
                    <div class="ml-3">
                      <p class="text-gray-900 whitespace-no-wrap">
                        {{ order.buyerName }}
                      </p>
                    </div>
                  </div>
                </td>
                <td class="px-5 py-5 border-b border-gray-200 bg-white text-sm">
                  <p class="text-gray-900 whitespace-no-wrap">{{ order.productName }}</p>
                </td>
                <td class="px-5 py-5 border-b border-gray-200 bg-white text-sm">
                  <p class="text-gray-900 whitespace-no-wrap">
                    {{ order.createdAt | formatDate }}
                  </p>
                </td>
                <td class="px-5 py-5 border-b border-gray-200 bg-white text-sm">
                  <p class="text-gray-900 whitespace-no-wrap">
                    {{ order.quantity }}
                  </p>
                </td>
                <td class="px-5 py-5 border-b border-gray-200 bg-white text-sm">
                  <span
                    :class="['relative inline-block px-3 py-1 font-semibold leading-tight', order.status === 'Activo' ? 'text-green-900' : 'text-red-900']">
                    <span aria-hidden class="absolute inset-0"
                      :class="order.status === 'Activo' ? 'bg-green-200' : 'bg-red-200' opacity - 50 rounded - full"></span>
                    <span class="relative">{{ order.status }}</span>
                  </span>
                </td>
              </tr>
            </tbody>

          </table>
          <div class="px-5 py-5 bg-white border-t flex flex-col xs:flex-row items-center xs:justify-between          ">
            <span class="text-xs xs:text-sm text-gray-900">
              Showing 1 to 4 of 50 Entries
            </span>
            <div class="inline-flex mt-2 xs:mt-0">
              <button
                class="text-sm text-indigo-50 transition duration-150 hover:bg-indigo-500 bg-indigo-600 font-semibold py-2 px-4 rounded-l">
                Prev
              </button>
              &nbsp; &nbsp;
              <button
                class="text-sm text-indigo-50 transition duration-150 hover:bg-indigo-500 bg-indigo-600 font-semibold py-2 px-4 rounded-r">
                Next
              </button>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div> -->
</template>
<script >
import { useAttrs } from "vue";
import { useAuthStore } from "../store/auth";
import { useNuxtApp } from "#app";

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
        const response = await await nuxtApp.$authenticatedFetch(
          `${config.public.API_BASE_URL}/api/orders/`
        );

        console.log("responsoe", response);
        this.orders = response;
      } catch (error) {
        console.log("Error", error);
        if (error.response && error.response.status === 401) {
          await authStore.refreshToken();

          const token = authStore.authToken;
          const setup = {
            headers: { Authorization: `Bearer ${token}` },
          };
          try {
            const response = await $fetch(
              `${config.public.API_BASE_URL}/api/orders/`,
              setup
            );
            console.log("response after refresh", response);
          } catch (error) {
            console.error("Error fetching orders after refresh", error);
          }
        }
      }
    },
  },
};
</script>
