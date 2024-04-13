<template>
  <section v-if="cartStore.cart.length > 0">
    <div class="container mx-auto mt-20 hidden lg:block">
      <div class="flex shadow-md my-10">
        <div class="w-3/4 bg-white px-10 py-10">
          <div class="flex justify-between border-b pb-8">
            <h1 class="font-semibold text-2xl">Shopping Cart</h1>
            <h2 class="font-semibold text-2xl">{{ cartStore.cartCount }} Products</h2>
          </div>
          <div class="flex mt-10 mb-5">
            <h3 class="font-semibold text-gray-600 text-xs uppercase w-2/5">Product Details</h3>
            <h3 class="font-semibold text-gray-600 text-xs uppercase w-1/5 text-center">Quantity</h3>
            <h3 class="font-semibold text-gray-600 text-xs uppercase w-1/5 text-center">Price</h3>
            <h3 class="font-semibold text-gray-600 text-xs uppercase w-1/5 text-center">Total</h3>
          </div>
          <div class="flex items-center hover:bg-gray-100 -mx-8 px-6 py-5" v-for="item in cartStore.cart" :key="item.pid">
            <div class="flex w-2/5"> <!-- product -->
              <div class="w-20">
                <img class="h-24 w-24 max-w-full rounded-lg object-cover" :src="item.cover_image" alt="" />
              </div>
              <div class="flex flex-col justify-between ml-4 flex-grow">
                <span class="font-bold text-sm">{{ item.title }}</span>
                <span class="text-red-500 text-xs">{{ item.location }}</span>
                <a href="#" @click.prevent="removeFromCart(item)" class="font-semibold hover:text-red-500 text-gray-500 text-xs">Remove</a>
              </div>
            </div>
            <div class="flex justify-center w-1/5">
              <button @click="decreaseQ(item)" class="flex items-center justify-center rounded-l-md bg-gray-200 px-4 transition hover:bg-[#EA454C]  hover:text-white">-</button>
              <div class="flex w-full items-center justify-center bg-gray-100 px-4 text-xs uppercase transition">{{ item.quantity }} </div>
              <button @click="increaseQ(item)" class="flex items-center justify-center rounded-r-md bg-gray-200 px-4 transition hover:bg-[#EA454C]  hover:text-white">+</button>
            </div>
            <span class="text-center w-1/5 font-semibold text-sm">₹{{ item.ticket_price }}</span>
            <span class="text-center w-1/5 font-semibold text-sm">₹{{ item.totalPrice }}</span>
          </div>
          <nuxt-link to="/eventList" class="flex font-semibold text-indigo-600 text-sm mt-10">
            <svg class="fill-current mr-2 text-indigo-600 w-4" viewBox="0 0 448 512"><path d="M134.059 296H436c6.627 0 12-5.373 12-12v-56c0-6.627-5.373-12-12-12H134.059v-46.059c0-21.382-25.851-32.09-40.971-16.971L7.029 239.029c-9.373 9.373-9.373 24.569 0 33.941l86.059 86.059c15.119 15.119 40.971 4.411 40.971-16.971V296z"/></svg>
            Continue Shopping
          </nuxt-link>
        </div>
        <div id="summary" class="w-1/4 px-8 py-10">
          <h1 class="font-semibold text-2xl border-b pb-8 mb-5">Order Summary</h1>
          <div>
            <label class="font-medium inline-block mb-1 text-sm uppercase">Shipping</label>
            <div class="block p text-gray-600 w-full text-sm">
              <option>Standard shipping - ₹00.00</option>
            </div>
          </div>
          <div class="flex justify-between mt-16 mb-5">
            <span class="font-semibold text-sm uppercase">Items {{ cartStore.getQty }}  </span>
            <span class="font-semibold text-sm">₹{{ cartStore.getPrice }}</span>
          </div>
          <div class="border-t mt-8">
            <nuxt-link to="/checkOut"><button class="bg-[#EA454C] font-semibold  py-3 text-sm text-white w-full rounded-3xl">Checkout</button></nuxt-link>
          </div>
        </div>
      </div>
    </div>
  </section>
  <section v-else class="py-10 sm:py-16 lg:py-20">
    <div class="flex justify-center">
      <img class="h-[50vh]" src="../assets/empty_cart.png">
    </div>
    <div>
      <h1 class="text-2xl font-semibold text-center -mt-20">Your Cart is Empty</h1>
      <p class="text-center mt-2">Take a look on our awesome products and add them to your cart</p>
    </div>
  </section>

  <section class="py-12 sm:py-16 lg:py-20 flex lg:hidden" v-if="cartStore.cartCount > 0">
    <img src="../assets/cart_girl.png" class="h-[50vh] mx-auto hidden lg:block" alt="cart">
    <div class="mx-auto px-4 sm:px-6 lg:px-8 flex flex-row">
      <div class="mx-auto mt-8 max-w-2xl md:mt-12">
        <div class="bg-white shadow">
          <div class="px-4 py-6 sm:px-8 sm:py-10">
            <div class="flow-root">
              <ul class="-my-8">
                <li v-for="item in cartStore.cart" :key="item.pid" class="flex flex-col space-y-3 py-6 text-left sm:flex-row sm:space-x-5 sm:space-y-0">
                  <div class="shrink-0">
                    <img class="h-24 w-24 max-w-full rounded-lg object-cover" :src="item.cover_image" alt="" />
                  </div>
                  <div class="relative flex flex-1 flex-col justify-between">
                    <div class="sm:col-gap-5 sm:grid sm:grid-cols-2">
                      <div class="pr-8 sm:pr-5">
                        <p class="text-base font-semibold text-gray-700">{{ item.title }}</p>
                        <p class="mx-0 mt-1 mb-0 text-sm text-gray-400">{{ item.location }}</p>
                      </div>
                      <div class="mt-4 flex items-end justify-between sm:mt-0 sm:items-start sm:justify-end">
                        <p class="shrink-0 w-20 text-base font-semibold text-gray-700 sm:order-2 sm:ml-8 sm:text-right">₹{{ item.totalPrice }}</p>
                        <div class="sm:order-1">
                          <div class="mx-auto flex h-8 items-stretch text-gray-600">
                            <button @click="decreaseQ(item)" class="flex items-center justify-center rounded-l-md bg-gray-200 px-4 transition hover:bg-[#EA454C] hover:text-white">-</button>
                            <div class="flex w-full items-center justify-center bg-gray-100 px-4 text-xs uppercase transition">{{ item.quantity }} </div>
                            <button @click="increaseQuantity(item)" class="flex items-center justify-center rounded-r-md bg-gray-200 px-4 transition hover:bg-[#EA454C] hover:text-white">+</button>
                          </div>
                        </div>
                      </div>
                    </div>
                    <div class="absolute top-0 right-0 flex sm:bottom-0 sm:top-auto">
                      <button @click.prevent="removeFromCart(item)" type="button" class="flex rounded p-2 text-center text-gray-500 transition-all duration-200 ease-in-out focus:shadow hover:text-gray-700">
                        <svg class="h-5 w-5" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12" class=""></path>
                        </svg>
                      </button>
                    </div>
                  </div>
                </li>
              </ul>
            </div>
            <!-- Subtotal, Shipping, Total -->
            <div class="mt-6 border-t border-b py-2">
              <div class="flex items-center justify-between">
                <p class="text-sm text-gray-400">Subtotal</p>
                <p class="text-lg font-semibold text-gray-700">₹{{ cartStore.getPrice }}</p>
              </div>
              <div class="flex items-center justify-between">
                <p class="text-sm text-gray-400">Shipping</p>
                <p class="text-lg font-semibold text-gray-700">₹ 0</p>
              </div>
            </div>
            <div class="mt-6 flex items-center justify-between">
              <p class="text-2xl font-semibold text-gray-700"><span class="text-xs font-normal text-gray-400">₹</span>{{ cartStore.getPrice }}</p>
              <p class="text-sm font-medium text-gray-700">Total</p>
            </div>
            <!-- Checkout Button -->
            <div class="mt-6 text-center">
              <nuxt-link to="/checkOut" class="group inline-flex w-full items-center justify-center rounded-md bg-[#EA454C] px-6 py-4 text-lg font-semibold text-white transition-all duration-200 ease-in-out focus:shadow">
                Checkout
                <svg xmlns="http://www.w3.org/2000/svg" class="group-hover:ml-8 ml-4 h-6 w-6 transition-all" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2">
                  <path stroke-linecap="round" stroke-linejoin="round" d="M13 7l5 5m0 0l-5 5m5-5H6" />
                </svg>
              </nuxt-link>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>

<script setup>
import { useCartStore } from '../store/index.js'; // Adjust the path based on where your store is located

// No need to define a name in script setup, as it is inferred from the file name in Vue 3

const cartStore = useCartStore();

// Computed properties
const nofItems = computed(() => {
  const itemCount = cartStore.cartCount;
  if (itemCount === 1) {
    return `${itemCount} item`;
  } else {
    return `${itemCount} items`;
  }
});

// Methods
function removeFromCart(item) {
  cartStore.removeFromCart(item);
}

function decreaseQ(item) {
  if (item.quantity === 1) {
    cartStore.removeFromCart(item);
  } else if (item.quantity > 1) {
    cartStore.decreaseQuantity(item);
  }
}

function increaseQ(item) {
  if (item.quantity ==0 ) { // The condition seems to prevent increasing if quantity is 1, but it might be an error. Adjust if needed.
    cartStore.increaseQuantity(item);
  }
}
</script>


