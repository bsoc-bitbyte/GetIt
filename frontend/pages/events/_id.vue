<template>
    <div>
    <section class="flex justify-center bg-primary-50 bg-dotted-pattern bg-contain">
      <div class="grid grid-cols-1 md:grid-cols-2 2xl:max-w-7xl ">
        <img
          :src="event.cover_image"
          alt="hero image"
          class="max-h-[80vh]  object-cover object-center"
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
               by <span class="text-primary-500">{{ event.organizer }}</span>
              </p>
            </div>
          </div>
          <button @click="addToCartClick(event)" class="  gap-0 md:mr-[7%] md:px-[12%] pl-[40%] mr-0 items-center justify-center text-center pr-0 md:py-0 w-[15vw]  md:min-w-0 bg-white rounded-none font-black flex-none flex md:rounded-full md:bg-[#EA454C] flex flex-row md:py-2 md:px-3 md:font-normal">
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
  
      <!-- Related Events section -->
      <!-- You can use the eventList component to display related events -->

    </div>
  </template>
  
  <script>

  
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
    },
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
  