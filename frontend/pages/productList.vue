<template>
    <div class="m-14">
      <div class="flex flex-col gap-5 items-center">
        <h1 class="poppins font-bold w-full text-center text-4xl">OUR <span class="text-[#EA454C]">PRODUCTS</span></h1>
        <div class="poppins text-base font-normal  flex gap-1 text-[#6C6C6C] ">Total <span class="font-semibold">
            {{ productlists.length }} </span> products </div>
      </div>
  
      <div class="flex justify-center items-center flex-col gap-8 mt-5 lg:flex-row ">
        <div class="flex flex-wrap justify-center gap-8 bg-red px-10 py-5">
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
    </div>
  </template>
  
  
  <script setup>
  import MerchCard from '@/components/MerchCard.vue';
  const config = useRuntimeConfig();
  const productlists = ref([]);
   
  async function fetchEventData() {
     try {
      const response = await $fetch(`${config.public.API_BASE_URL}/api/products/`);
      productlists.value = response.map(product => {
        return {
          ...product,
          product_images: product.product_images.map(img => ({
            ...img,
            image: `${config.public.API_BASE_URL}${img.image}`
          }))
        };
      });
    }
    catch (error) {
      console.error('Error fetching event data', error);
    }
  }
  onMounted(() => fetchEventData());
  </script>
  
  
  <style>
  .poppins {
    font-family: "Poppins", sans-serif;
    font-smooth: always;
  }
  </style>
