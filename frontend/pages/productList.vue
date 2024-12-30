<template>
  <div class="m-14">
    <div class="flex flex-col gap-4 items-center">
      <h1 class="poppins font-bold w-full text-center text-[40px]">OUR <span class="text-[#EA454C]">PRODUCTS</span></h1>
      <div class="poppins text-center text-base font-normal text-[#6C6C6C]">Look at our wide range of products</div>
    </div>
    <div class="flex justify-center items-center flex-col gap-8 mt-5 lg:flex-row">
      <div class="flex flex-wrap justify-center gap-8 bg-red px-10 py-8">
        <NuxtLink v-for="data in productlists" :to="`/products/${data.id}`" :key="data.id">
          <MerchCard
            :title="data.name"
            :type="data.type"
            :imageUrl="data.product_images[0]?.image" 
            :seller="data.seller"
            :price="data.price"
            :description="data.description"
            :colors="data.colors"
            :sizes="data.sizes"
            :tags="data.tags"
          />
        </NuxtLink>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import MerchCard from '@/components/MerchCard.vue';

const config = useRuntimeConfig();
const productlists = ref([]);

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

onMounted(() => fetchProductData());
</script>

<style>
.poppins {
  font-family: "Poppins", sans-serif;
  font-smooth: always;
}
</style>