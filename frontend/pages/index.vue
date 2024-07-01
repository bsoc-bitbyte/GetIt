<template>
  <div class="m-14">
    <div class="flex flex-col gap-4 items-center">
      <h1 class="poppins font-bold w-full text-start text-[40px] px-20" ><span class="text-black">PRODUCTS</span></h1>
      
    </div>
    <div class="flex justify-center items-center flex-col gap-8 mt-1 lg:flex-row">
      <div class="flex flex-wrap justify-center gap-20 bg-red px-10 py-8">
        <NuxtLink v-for="data in productlists" :to="`/products/${data.id}`" :key="data.id">
          <MerchCard
          :title= "data.title"
              :type= "data.type"
              :imageUrl= "data.product_images" 
              :seller = "data.seller"
              :price = "data.price"
              :description = "data.description"
              :colors= "data.colors"
              :sizes= "data.sizes"
              :tags = "data.tags"
          />
        </NuxtLink>
      </div>
    </div>
    <div class="w-full h-[60px] grid place-items-center">
      <button class="rounded-[20px] bg-[#EA454C] w-[249px] h-[60px] font-poppins text-base font-semibold text-white flex items-center justify-center border-4 border-transparent hover:bg-transparent hover:border-[#EA454C] hover:text-black transition duration-300 ease-in-out">
        <p>Check-out Merch</p>
      </button>
    </div>
    
  </div>

  <div class="m-14 owe">
    <div class="flex flex-col gap-8 items-center px-8">
      <h1 class="poppins font-bold w-full text-start text-4xl px-14"> <span class="text-black">EVENTS</span></h1>
      
    </div>
    <div class="flex justify-center items-center flex-col gap-8 mt-10 lg:flex-row">
      <div class="flex flex-wrap justify-center gap-8">
        <NuxtLink v-for="data in eventLists" :to="`/events/${data.id}`" :key="data.id">
          <eventList
          :title="data.title"
          :description="data.description"
          :email="data.email"
          :date="data.date"
          :event_type="data.event_type"
          :location="data.location"
          :ticket_price="data.ticket_price"
          :img_url="data.cover_image"
          />
        </NuxtLink>
      </div>
    </div>
    <div class="w-full h-[120px] grid place-items-center">
      <button class="rounded-[20px] bg-[#EA454C] w-[249px] h-[60px] font-poppins text-base font-semibold text-white flex items-center justify-center border-4 border-transparent hover:bg-transparent hover:border-[#EA454C] hover:text-black transition duration-300 ease-in-out">
        <p>Events</p>
      </button>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import MerchCard from '@/components/MerchCard.vue';
import eventList from '@/components/eventList.vue';
const config = useRuntimeConfig();

const productlists = ref([]);
const eventLists = ref([]);

async function fetchProductData() {
  try {
    const response = await $fetch(`${config.public.API_BASE_URL}/api/products/`);
    productlists.value = response.map(product => ({
      ...product,
      product_images: product.product_images.map(img => ({
        ...img,
        image: `${config.public.API_BASE_URL}${img.image}`
      }))
    }));
  } catch (error) {
    console.error('Error fetching product data', error);
  }
}

async function fetchEventData() {
  try {
    const response = await $fetch(`${config.public.API_BASE_URL}/api/events/`);
    eventLists.value = response;
  } catch (error) {
    console.error('Error fetching event data', error);
  }
}

onMounted(() => {
  fetchProductData();
  fetchEventData();
});
</script>

<style>
.poppins {
  font-family: "Poppins", sans-serif;
  font-smooth: always;
}
</style>
