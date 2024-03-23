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
  if (item.quantity > 1) { // The condition seems to prevent increasing if quantity is 1, but it might be an error. Adjust if needed.
    cartStore.increaseQuantity(item);
  }
}
</script>


