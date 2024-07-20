<template>
  <section v-if="loaded && !error" class="w-full overflow-hidden">
    <div class="flex justify-center">
      <div
        class="w-4/5 md:flex justify-center border-b border-gray-300 pt-10 pb-6"
      >
        <div class="xl:w-2/5 md:w-1/2 grid gap-4">
          <productImageGallery
            :product="product"
            :config="config"
          ></productImageGallery>
        </div>
        <div class="xl:w-2/5 md:w-1/2 lg:ml-8 md:ml-6 md:mt-0 mt-6">
          <div class="border-b border-gray-300 pb-4 flex justify-between">
            <div>
              <p class="text-sm font-semibold leading-none text-gray-500 pb-3">
                {{ product.seller }}
              </p>
              <h1
                class="text-2xl font-semibold lg:leading-6 leading-7 text-gray-800 mt-2 pb-3"
              >
                {{ product.name }}
              </h1>
              <h1
                class="text-2xl font-semibold lg:leading-6 leading-7 text-gray-800 mt-2"
              >
                ₹{{ product.price }}
              </h1>
            </div>
            <div>
              <img
                class="h-6 hover:cursor-pointer"
                src="assets/share_icon.svg"
                alt="share_icon"
                @click="copyUrlToClipboard"
              />
            </div>
          </div>
          <div class="py-4 flex items-center justify-between">
            <p class="text-sm leading-4 text-gray-500">Select Size</p>
            <div
              class="dropdown-title cursor-pointer text-sm leading-none underline text-gray-500"
              @click="toggleSizeChart"
            >
              Size Chart
              <button class="drop-btn" :class="{ 'rotate-180': showSizeChart }">
                <img
                  class="inline-block w-4 h-4 ml-2 mr-2 transform transition"
                  src="assets/dropdown_icon.svg"
                />
              </button>
            </div>
          </div>
          <div class="flex gap-5">
            <button
              v-for="item in sizeList"
              :key="item"
              :class="{
                'w-8 h-8 text-sm text-gray-600 rounded-full border border-gray-500 font-sans': true,
                'outline outline-1 outline-offset-2 outline-black':
                  item === userInput.size.value,
              }"
              @click="sizeSelector(item)"
            >
              {{ item }}
            </button>
          </div>

          <div v-if="showSizeChart" class="dropdown-content mt-5">
            <img src="assets/sizeChart.png" />
          </div>
          <div class="py-4 text-sm leading-4 text-gray-500">Select Colour</div>
          <div class="flex gap-5 mb-5">
            <button
              v-for="item in colorList"
              :key="item"
              :class="{
                'w-8 h-8 text-sm text-gray-600 rounded-full border border-gray-500 font-sans': true,
                'outline outline-1 outline-offset-2 outline-black':
                  item === userInput.color.value,
              }"
              :style="{ background: item }"
              @click="colorSelector(item)"
            ></button>
          </div>
          <button
            class="focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-gray-800 text-2xl rounded-[15px] flex items-center justify-center leading-none text-white bg-[#EA454C] border-2 border-[#EA454C] w-full py-3 my-3 font-semibold"
            @click="
              addToCartClick(
                product,
                userInput.size.value,
                userInput.color.value
              )
            "
          >
            <img class="h-6 mr-5" src="assets/cart_icon.svg" alt="cart" />
            Add To Cart
          </button>
          <button
            class="focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-gray-800 text-2xl rounded-[15px] flex items-center justify-center leading-none text-[#EA454C] bg-white border-2 border-[#EA454C] w-full py-3 my-3 font-semibold"
            @click="
              buyNowClick(product, userInput.size.value, userInput.color.value)
            "
          >
            <img class="h-6 mr-5" src="assets/buynow_icon.svg" alt="buynow" />
            Buy Now
          </button>
        </div>
      </div>
    </div>
    <div class="flex justify-center">
      <div class="w-4/5 py-4">
        <div
          class="dropdown-title cursor-pointer text-base leading-none text-gray-900"
          @click="toggleProductDescription"
        >
          Product Details
          <button
            class="drop-btn"
            :class="{ 'rotate-180': showProductDescription }"
          >
            <img
              class="inline-block w-4 h-4 ml-2 mr-2 transform transition"
              src="assets/dropdown_icon.svg"
            />
          </button>
        </div>
        <div
          v-if="showProductDescription"
          class="dropdown-content text-gray-500 text-sm my-4"
        >
          {{ product.description }}
        </div>
      </div>
    </div>
    <div class="mt-4 flex justify-center">
      <div class="w-4/5">
        <div class="flex flex-col gap-4 items-center">
          <h1 class="poppins font-bold w-full text-start text-[40px]">
            <span class="text-[#EA454C] mr-3">MORE</span
            ><span class="text-black">PRODUCTS</span>
          </h1>
        </div>
        <div
          class="flex justify-center items-center flex-col gap-8 mt-1 lg:flex-row"
        >
          <div class="flex flex-wrap justify-center gap-10 bg-red px-10 py-8">
            <NuxtLink
              v-for="data in productlists"
              :to="`/products/${data.id}`"
              :key="data.id"
            >
              <MerchCard
                v-if="data.product_images.length != 0"
                :title="data.name"
                :type="data.type"
                :imageUrl="data.product_images[0].image"
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
        <div class="w-full h-[120px] grid place-items-center">
          <nuxt-link to="/productList">
            <button
              class="rounded-[20px] bg-white w-[249px] h-[60px] font-poppins text-base font-semibold flex items-center justify-center border-4 border-[#EA454C] hover:bg-[#EA454C] hover:border-transparent hover:text-white transition duration-300 ease-in-out shadow-custom"
            >
              <p>See all products</p>
            </button>
          </nuxt-link>
        </div>
      </div>
    </div>
  </section>
</template>

<script setup>
import { ref, onMounted } from "vue";
import { useRoute } from "vue-router";
import { useCartStore } from "../../store/index.js"; // Assuming your store is located here
import { toast } from "vue3-toastify";
import { useRouter } from "vue-router";
import MerchCard from "@/components/MerchCard.vue";
import productImageGallery from "@/components/productImageGallery.vue";

const config = useRuntimeConfig();
const route = useRoute();
const product = ref({});
const productlists = ref([]);
const showSizeChart = ref(false);
const showProductDescription = ref(false);
const loaded = ref(false);
const cartStore = useCartStore();
const router = useRouter();
const error = ref();
// const colorList = ["#32a852", "blue", "green"];
// const sizeList = ["XS", "S", "M", "L", "XL"];
const userInput = {
  size: ref(null),
  color: ref(null),
};

const toggleSizeChart = () => {
  showSizeChart.value = !showSizeChart.value;
};

const toggleProductDescription = () => {
  showProductDescription.value = !showProductDescription.value;
};

onMounted(async function fetchProductDetails() {
  try {
    const productId = route.params.id;
    const response = await $fetch(
      `${config.public.API_BASE_URL}/api/products/${productId}`
    );
    product.value = response;

    const responseList = await $fetch(
      `${config.public.API_BASE_URL}/api/products/`
    );
    productlists.value = responseList.map((product) => ({
      ...product,
      product_images: product.product_images.map((img) => ({
        ...img,
        image: `${config.public.API_BASE_URL}${img.image}`,
      })),
    }));

    loaded.value = true;
  } catch (error) {
    error.value = error;
    if (error.response && error.response.status === 404) {
      router.push("/404");
    } else {
      console.error("Error fetching product data:", error);
      const message = `Error fetching product data (Status Code: ${error.response.status})`;
      toast.error(message, {
        autoClose: 2000,
        position: toast.POSITION.BOTTOM_CENTER,
      });
    }
  }
});

const copyUrlToClipboard = () => {
  const url = window.location.href;
  navigator.clipboard
    .writeText(url)
    .then(() => {
      console.log("Link copied to clipboard");
      toast.success("Link copied to clipboard", {
        autoClose: 2000,
        position: toast.POSITION.BOTTOM_CENTER,
      });
    })
    .catch((err) => {
      console.error("Failed to copy URL to clipboard", err);
      toast.error("Failed to copy link to clipboard", {
        autoClose: 2000,
        position: toast.POSITION.BOTTOM_CENTER,
      });
    });
};

const sizeSelector = (item) => {
  userInput.size.value = item;
};

const colorSelector = (item) => {
  userInput.color.value = item;
};

const addToCartClick = (item, size, color) => {
  if (size === null || color === null) {
    toast.error("Select size & color before adding to cart", {
      autoClose: 2000,
      position: toast.POSITION.BOTTOM_CENTER,
    });
  } else {
    console.log(item, size, color);
    addToCart(item);
  }
};

const buyNowClick = (item, size, color) => {
  console.log({ size }, { color });
  if (size === null || color === null) {
    toast.error("Select size & color before adding to cart", {
      autoClose: 2000,
      position: toast.POSITION.BOTTOM_CENTER,
    });
  } else {
    console.log(item, size, color);
    addToCart(item);
    router.push("/checkOut");
  }
};

const addToCart = (item) => {
  cartStore.addToCart(item);
};
</script>

<style scoped>
.rotate-180 {
  transform: rotate(180deg);
}
.poppins {
  font-family: "Poppins", sans-serif;
  font-smooth: always;
}
</style>
