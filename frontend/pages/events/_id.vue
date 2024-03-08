<template>
    <!-- <div>
    <section class="flex justify-center bg-primary-50 bg-dotted-pattern bg-contain">
      <div class="grid grid-cols-1 md:grid-cols-2 w-[90vw]">
        <img
          :src="event.cover_image"
          alt="hero image"
          class="w-[90vw] h-[75vh] "
        />

        <div class="flex w-full flex-col gap-8 p-5 md:p-10">
          <div class="flex flex-col gap-6">
            <h2 class="text-3xl font-bold mb-4"> {{ event.title }}</h2>

            <div class="flex flex-col gap-3 sm:flex-row sm:items-center">
              <div class="flex gap-3">
                <p
                  class="rounded-full bg-green-500/10 px-5 py-2 text-green-700 font-semibold"
                >
                  {{ event.isFree ? 'FREE' : `₹${event.ticket_price}` }}
                </p>
                <p
                  class="rounded-full bg-gray-500/10 px-4 py-2.5 text-gray-500 font-semibold"
                >
                  {{ event.event_type }}
                </p>
              </div>

              <p class="text-sm ml-2 mt-2 sm:mt-0" v-if="event.organizer">
               by <span class="text-primary-500 font-bold">{{ event.organizer }}</span>
              </p>
            </div>
          </div>
          <button @click="addToCartClick(event)" class="  gap-0 md:mr-[7%] md:px-[12%] pl-[40%] mr-0 items-center justify-center text-center pr-0 w-[15vw]  md:min-w-0 bg-white rounded-none font-black flex-none flex md:rounded-full md:bg-[#EA454C] flex-row md:py-2 md:font-normal">
                  <div class="flex items-center justify-center md:justify-start ">
  <div class="flex items-center -ml-[15px]">
    <img class="invisible md:visible -pr-[2px] w-5 h-4 mr-0 md:mr-0 md:mt-0 md:mb-0" src="../../assets/cart02.png">
    <img class="visible md:invisible w-4 h-3 mr-1 -ml-[5px] mt-[0px] mb-0" src="../../assets/cart01.png">
  </div>
  <p class="flex-none text-[12px] pr-[0%] md:text-[14px] text-center text-black md:text-white md:font-extrabold font-extrabold sm:text-xs pl-0 md:pl-0 mt-0 mb-0">Add To Cart</p>
</div>



                </button>
          

          <div class="flex flex-col gap-5">
            <div class="flex gap-2 md:gap-3">
              <img src="../../assets/calendar.svg" alt="calendar" class="w-6 h-6" />
              <div class="flex flex-wrap items-center">
                <p class="text-sm">
                  {{ event.date }} - {{ event.time }}
                </p>
              </div>
            </div>

            <div class="flex items-center gap-3">
              <img src="../../assets/location.svg" alt="location" class="w-6 h-6" />
              <p class="text-sm">{{ event.location }}</p>
            </div>
          </div>

          <div class="flex flex-col gap-2">
            <p class="text-lg font-bold mb-2 text-gray-600">About Event:</p>
            <p class="text-lg">{{ event.description }}</p>
            <p class="text-sm text-blue-500 underline hover:text-blue-700">
              {{ event.url }}
            </p>
          </div>
        </div>
      </div>
    </section>
  
  

    </div> -->
    <section class="flex justify-center flex-col md:flex-row">
      <div class=""> 
        <img
          :src="event.cover_image"
          alt="hero image"
          class="h-[65vh] px-5"
        />
      </div>
    <div class="px-6 py-4 pb-20 lg:max-w-lg mt-auto">
    <span class="inline-block text-xs font-semibold uppercase tracking-widest text-[#fa4750] lg:mb-2">
      The Programming Club
    </span>

    <h1 class="mb-4 text-xl font-semibold text-tertiary text-[#2e191a] md:text-3xl lg:mb-5 lg:text-4xl">
      {{ event.title }}
    </h1>
<p class="mb-6 max-w-md text-tertiary-ligh text-[#635e5f]">
      {{ event.description }}
    </p>
    
    <div class="mb-2 flex items-center justify-between md:justify-start md:gap-8 lg:mb-8 lg:flex-col lg:items-start lg:gap-1">
      <div class="flex items-center gap-4">
        <span class="font-semibold text-[#2e191a] text-xl">₹{{ event.ticket_price }}</span>
        <span class="rounded-md bg-[#ffcccfc2] px-2 font-bold text-[#fa4750] text-xs">
          50%
        </span>
      </div>
      <span class="font-semibold text-[#776f70] text-xs">
        <s>₹{{ (2 * event.ticket_price).toFixed(2)}}</s>
      </span>
    </div>

    <div class="space-y-4 md:flex md:items-center md:gap-16 md:space-y-0 flex gap-16">
      <div class="flex justify-center w-1/4 lg:w-1/2 h-[4vh] mt-5 lg:mt-0">
            <button @click="decreaseQ(item)" class="flex items-center justify-center rounded-l-md px-4 bg-gray-100 transition text-[#fa4750] hover:bg-[#EA454C]  hover:text-white">-</button>
              <div class="flex w-full items-center justify-center bg-gray-100 px-4 text-xs uppercase transition">0 </div>
            <button @click="increaseQ(item)" class="flex items-center justify-center bg-gray-100 rounded-r-md  px-4 text-[#fa4750] transition hover:bg-[#EA454C]  hover:text-white">+</button>
          </div>

          <button @click="addToCartClick(event)" class="bg-[#EA454C] font-semibold  py-3 text-sm text-white lg:w-full rounded-3xl w-1/2">Add to cart</button>
    </div>
    <div class="faq-container max-w-md lg:mx-auto mt-4 ">
    <div class="dropdown mb-2" >
      <div class="dropdown-title cursor-pointer" @click="toggleEventDetails">
        Event Details
        <button class="drop-btn" :class="{'rotate-180': showEventDetails}">
          <img class="inline-block w-4 h-4 ml-1 transform transition" src="https://img.icons8.com/ios-glyphs/30/000000/chevron-down.png" />
        </button>
      </div>
      <div v-if="showEventDetails" class="dropdown-content text-[#635e5f] px-5">
        <p>Location: {{ event.location }}</p>
        <p>Date: {{ event.date }}</p>
        <p>Time: {{ event.time.slice(0,5)}}</p>
        <p>Event-Type: {{ event.event_type}}</p>
   
        <!-- Add more event details as needed -->
      </div>
    </div>

    <div class="dropdown">
      <div class="dropdown-title cursor-pointer" @click="toggleContact">
        Contact
        <button class="drop-btn" :class="{'rotate-180': showContact}">
          <img class="inline-block w-4 h-4 ml-1 transform transition" src="https://img.icons8.com/ios-glyphs/30/000000/chevron-down.png" />
        </button>
      </div>
      <div v-if="showContact" class="dropdown-content text-[#635e5f] px-5">
        <p>Email: {{ event.email }}</p>
        <p>Phone: {{ event.phone }}</p>
        <!-- Add more contact information as needed -->
      </div>
    </div>
  </div>
  </div>
  
</section>
  </template>
  
  <script>

import { ref } from 'vue';

  export default {
    data() {
      return {
        event: {}, 
        eventId: null,
      };
    },
    mounted() {
      this.eventId = this.$route.params.id;
      this.fetchEventData();
    },setup() {
      const showEventDetails = ref(false);
    const showContact = ref(false);

    const toggleEventDetails = () => {
      showEventDetails.value = !showEventDetails.value;
    };

    const toggleContact = () => {
      showContact.value = !showContact.value;
    };

    // const closeDropdown = () => {
    //   showEventDetails.value = false;
    //   showContact.value = false;
    // };

    return { showEventDetails, toggleEventDetails, showContact, toggleContact};
  }

  ,
    methods: {
      async fetchEventData() {
        try {
          const response = await this.$axios.get(`events/${this.eventId}`);
          this.event = response.data;
          console.log(response.data);
        } catch (error) {
          console.error('Error fetching event data', error);
        }
      },
      addToCartClick(item) {
          this.$store.commit('addToCart',item);
    }
    },
  };
  </script>
  <style scoped>
  /* .dropdown-content {
    display: none;
  }
  
  .dropdown-title:hover + .dropdown-content {
    display: block;
  } */
  
  .dropdown-title svg {
    transition: transform 0.3s;
  }
  
  .rotate-180 {
    transform: rotate(180deg);
  }
  </style>