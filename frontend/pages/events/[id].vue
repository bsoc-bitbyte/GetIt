<template>
  <section v-if="loaded &&!error" class="flex justify-center flex-col md:flex-row items-center mt-10">
    <div class="h-[50vh] lg:h-[70vh]">
      <img
        :src="event.cover_image"
        alt="hero image"
        class="object-cover h-[50vh] lg:h-[70vh] px-5"
      />
    </div>
    <div class="px-6 py-4 pb-20 lg:max-w-lg mt-5 h-[75vh]">
      <span
        class="inline-block text-xs font-semibold uppercase tracking-widest text-[#fa4750] lg:mb-2"
      >
        The Programming Club
      </span>

      <h1
        class="mb-4 text-xl font-semibold text-tertiary text-[#2e191a] md:text-3xl lg:mb-5 lg:text-4xl"
      >
        {{ event.title }}
      </h1>
      <div id="$style.renderedDescription" v-html="event.description"></div>
      <div
        class="mb-2 flex items-center justify-between md:justify-start md:gap-8 lg:mb-8 lg:flex-col lg:items-start lg:gap-1"
      >
        <div class="flex items-center gap-4">
          <span class="font-semibold text-[#2e191a] text-xl"
            >₹{{ event.ticket_price }}</span
          >
        </div>
      </div>

      <div
        class="space-y-4 md:flex md:items-center md:gap-16 md:space-y-0 flex gap-16"
      >
        <div class="flex justify-center w-1/4 lg:w-1/2 h-[4vh] mt-5 lg:mt-0">
          <button
            :disabled="qty === 0"
            :class="{ 'opacity-50': qty === 0 }"
            @click="decrease"
            class="flex items-center justify-center rounded-l-md px-4 bg-gray-100 transition text-[#fa4750] hover:bg-[#EA454C] hover:text-white"
          >
            -
          </button>
          <div
            class="flex w-full items-center justify-center bg-gray-100 px-4 text-xs uppercase transition"
          >
            {{ qty }}
          </div>
          <button
            :disabled="qty >= 1"
            :class="{ 'opacity-50': qty === 1 }"
            @click="increase"
            class="flex items-center justify-center bg-gray-100 rounded-r-md px-4 text-[#fa4750] transition hover:bg-[#EA454C] hover:text-white"
          >
            +
          </button>
        </div>
        <button
          :disabled="qty === 0 || !loaded"
          :class="{ 'opacity-50': qty === 0 || !loaded }"
          @click="addToCartClick(event)"
          class="bg-[#EA454C] font-semibold py-3 text-sm text-white lg:w-full rounded-3xl w-1/2"
        >
          Add to cart
        </button>
      </div>
      <div class="faq-container max-w-md lg:mx-auto mt-4">
        <div class="dropdown mb-2">
          <div
            class="dropdown-title cursor-pointer"
            @click="toggleEventDetails"
          >
            Event Details
            <button
              class="drop-btn"
              :class="{ 'rotate-180': showEventDetails }"
            >
              <img
                class="inline-block w-4 h-4 ml-1 transform transition"
                src="https://img.icons8.com/ios-glyphs/30/000000/chevron-down.png"
              />
            </button>
          </div>
          <div
            v-if="showEventDetails"
            class="dropdown-content text-[#635e5f] px-5"
          >
            <p>Location: {{ event.location }}</p>
            <p>Date: {{ event.date }}</p>
            <p>Time: {{ event.time.slice(0, 5) }}</p>
            <p>Event-Type: {{ event.event_type }}</p>
          </div>
        </div>

        <div class="dropdown">
          <div class="dropdown-title cursor-pointer" @click="toggleContact">
            Contact
            <button class="drop-btn" :class="{ 'rotate-180': showContact }">
              <img
                class="inline-block w-4 h-4 ml-1 transform transition"
                src="https://img.icons8.com/ios-glyphs/30/000000/chevron-down.png"
              />
            </button>
          </div>
          <div
            v-if="showContact"
            class="dropdown-content text-[#635e5f] px-5"
            style="max-height: 200px; overflow-y: auto"
          >
            <p>Email: {{ event.email }}</p>
            <p>Phone: {{ event.phone }}</p>
            <!-- Add more contact information as needed -->
          </div>
        </div>
      </div>
    </div>
  </section>
</template>
<script setup>
import { ref, onMounted } from "vue";
import { useRoute } from "vue-router";
import { useCartStore } from "../../store/index.js"; // Assuming your store is located here
import { toast } from 'vue3-toastify';
import { useRouter } from 'vue-router';

const config = useRuntimeConfig();
const route = useRoute();
const event = ref({});
const showEventDetails = ref(false);
const showContact = ref(false);
const qty = ref(1);
const loaded = ref(false);
const cartStore = useCartStore();
const router = useRouter();
const error = ref();

const toggleEventDetails = () => {
  showEventDetails.value = !showEventDetails.value;
};

const toggleContact = () => {
  showContact.value = !showContact.value;
};

onMounted(async () => {
  try {
    const eventId = route.params.id;
    const response = await $fetch(
      `${config.public.API_BASE_URL}/api/events/${eventId}`
    );
    event.value = response;
    loaded.value = true;
  } catch (error) {
    error.value = error;
    if (error.response && error.response.status === 404) {
      router.push('/404');
    } else {
      console.error('Error fetching event data:', error);
      const message = `Error fetching event data (Status Code: ${error.response.status})`;
      toast.error(message,{
        autoClose: 2000,
        position:  toast.POSITION.BOTTOM_CENTER
      })
    }
  }
});



const addToCartClick = (item) => {
  console.log("dfvd");
  cartStore.addToCart(item);
  console.log("fcadscascasdcasdcascdasc"); // Check if the item is added to the cart
};

const increase = () => {
  qty.value++;
};

const decrease = () => {
  if (qty.value > 0) {
    qty.value--;
  }
};
</script>

<style scoped>
.dropdown-title svg {
  transition: transform 0.3s;
}

.rotate-180 {
  transform: rotate(180deg);
}
</style>
