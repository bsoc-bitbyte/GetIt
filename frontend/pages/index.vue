<template>
  <div class="w-full relative">
    <div class="relative w-full h-[728px] overflow-hidden group">
      <div
        class="flex transition-transform w-full duration-500 h-full"
        :style="{ transform: `translateX(-${currentIndex * 100}%)` }"
      >
        <div
          v-for="(item, index) in items"
          :key="index"
          class="w-full flex-shrink-0 h-full"
        >
          <div class="h-full w-full flex items-center justify-center">
            <img
              class="object-cover h-full w-full"
              :src="item.image"
              alt="carouselimage"
            />
            <div
              class="h-full w-full bg-gradient-to-b from-transparent via-[#00000080] via-35% to-black fixed"
            >
              <div class="w-full absolute top-[100px] h-[180px] flex px-[10%]">
                <div
                  class="w-[60vw] h-[180px] sm:w-[50vw] sm:text-6xl/[90px] font-semibold text-5xl text-white poppins"
                >
                  {{ item.title }}
                </div>
              </div>
              <div
                class="w-full relative top-[476px] h-[72px] flex px-[5%] justify-end"
              >
                <div
                  class="sm:w-[35vw] h-full w-[50vw] font-light text-sm sm:text-base text-white poppins text-right"
                >
                  {{ item.description }}
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
      <div
        class="h-[15px] w-full absolute self-end bottom-[55px] flex gap-4 justify-center items-center"
      >
        <div
          v-for="i in items.length"
          :key="i"
          class="h-[10px] w-[10px] rounded-full bg-white"
          :class="{ active: currentIndex === i - 1 }"
        ></div>
      </div>

      <button
        v-if="currentIndex > 0"
        class="absolute left-5 top-1/2 transform -translate-y-1/2 p-2 bg-opacity-50 text-white hover:bg-opacity-75 transition-opacity opacity-0 group-hover:opacity-100"
        @click="prev"
      >
        <img
          src="../assets/arrowleft.svg"
          alt="arrowleft"
          class="h-[50px] w-[17px]"
        />
      </button>

      <button
        v-if="currentIndex < items.length - 1"
        class="absolute right-6 top-1/2 transform -translate-y-1/2 p-2 bg-opacity-50 text-white hover:bg-opacity-75 transition-opacity opacity-0 group-hover:opacity-100"
        @click="next"
      >
        <img
          src="../assets/arrowright.svg"
          alt="arrowright"
          class="h-[50px] w-[17px]"
        />
      </button>
    </div>
  </div>

  <div class="m-14">
    <div class="flex flex-col gap-4 items-center">
      <h1 class="poppins font-bold w-full text-start text-[40px] px-20">
        <span class="text-black">PRODUCTS</span>
      </h1>
    </div>
    <div
      class="flex justify-center items-center flex-col gap-8 mt-1 lg:flex-row"
    >
      <div class="flex flex-wrap justify-center gap-20 bg-red px-10 py-8">
        <NuxtLink
          v-for="data in productlists"
          :to="`/products/${data.id}`"
          :key="data.id"
        >
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
    <div class="w-full h-[120px] grid place-items-center">
      <router-link to="/productList">
      <button
          class="rounded-[20px] bg-[#EA454C] w-[249px] h-[60px] font-poppins text-base font-semibold text-white flex items-center justify-center border-4 border-transparent hover:bg-transparent hover:border-[#EA454C] hover:text-black transition duration-300 ease-in-out shadow-custom"
      >
          <p>Products</p>
      </button>
    </router-link>
  </div>
  </div>

  <div class="m-14 owe">
    <div class="flex flex-col gap-8 items-center px-8">
      <h1 class="poppins font-bold w-full text-start text-4xl px-14"> 
        <span class="text-black">EVENTS</span>
      </h1>
    </div>
    <div
      class="flex justify-center items-center flex-col gap-8 mt-10 lg:flex-row"
    >
      <div class="flex flex-wrap justify-center gap-8">
        <NuxtLink
          v-for="data in eventLists"
          :to="`/events/${data.id}`"
          :key="data.id"
        >
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
      <router-link to="/eventList">
      <button
          class="rounded-[20px] bg-[#EA454C] w-[249px] h-[60px] font-poppins text-base font-semibold text-white flex items-center justify-center border-4 border-transparent hover:bg-transparent hover:border-[#EA454C] hover:text-black transition duration-300 ease-in-out shadow-custom">
          <p>Events</p>
      </button>
    </router-link>
  </div>
  
  </div>
</template>

<script>
import { ref, onMounted } from "vue";
import MerchCard from "@/components/MerchCard.vue";
import eventList from "@/components/eventList.vue";

export default {
  name: "IndexPage",
  components: {
    MerchCard,
    eventList
  },
  setup() {
    const config = useRuntimeConfig();

    const productlists = ref([]);
    const eventLists = ref([]);
    
    async function fetchProductData() {
      try {
        const response = await $fetch(
          `${config.public.API_BASE_URL}/api/products/`
        );
        productlists.value = response.map((product) => ({
          ...product,
          product_images: product.product_images.map((img) => ({
            ...img,
            image: `${config.public.API_BASE_URL}${img.image}`,
          })),
        }));
      } catch (error) {
        console.error("Error fetching product data", error);
      }
    }

    async function fetchEventData() {
      try {
        const response = await $fetch(
          `${config.public.API_BASE_URL}/api/events/`
        );
        eventLists.value = response;
      } catch (error) {
        console.error("Error fetching event data", error);
      }
    }

    onMounted(() => {
      fetchProductData();
      fetchEventData();
    });

    return {
      productlists,
      eventLists
    };
  },
  data() {
    return {
      currentIndex: 0,
      items: [
        {
          image: "\carousel_image.png",
          title: "Lorem ipsum some text about it!",
          description:
            "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla vitae ipsum sit amet velit feugiat fermentum. Lorem ipsum dolor sit amet, consectetur adipiscing elit.",
        },
        {
          image: "\carousel_image.png",
          title: "Lorem ipsum some text about it!",
          description:
            "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla vitae ipsum sit amet velit feugiat fermentum. Lorem ipsum dolor sit amet, consectetur adipiscing elit.",
        },
        {
          image: "\carousel_image.png",
          title: "Lorem ipsum some text about it!",
          description:
            "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla vitae ipsum sit amet velit feugiat fermentum. Lorem ipsum dolor sit amet, consectetur adipiscing elit.",
        },
        {
          image: "\carousel_image.png",
          title: "Lorem ipsum some text about it!",
          description:
            "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla vitae ipsum sit amet velit feugiat fermentum. Lorem ipsum dolor sit amet, consectetur adipiscing elit.",
        },
      ],
    };
  },
  methods: {
    prev() {
      if (this.currentIndex > 0) {
        this.currentIndex--;
      }
    },
    next() {
      if (this.currentIndex < this.items.length - 1) {
        this.currentIndex++;
      }
    },
  },
};
</script>


<style scoped>
.poppins {
  font-family: "Poppins", sans-serif;
  font-smooth: always;
}
.active {
  background-color: #ea454c;
  height: 15px;
  width: 15px;
}
.shadow-custom {
  box-shadow: 0px 6px 10px 1px #00000040;
}
</style>
