<template>
    <div class="m-20">
      <!-- <h1 class="text-4xl font-bold text-center">Event List</h1> -->
      <div class="flex justify-center items-center flex-col gap-8 mt-20 lg:flex-row">
        <div class="flex flex-wrap justify-center lg:justify-start gap-8">
          <nuxt-link v-for="(data, index) in eventLists" :to="'/events/'+ (index + 1)" :key="index">
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
          </nuxt-link>
        </div>
      </div>
    </div>
  </template>
  
  
  <script>
  import eventList from '@/components/eventList.vue';
  
  
  export default {
    name: 'EventPage',
    data() {
      return {
        eventLists: [],
      };
    },
    components: {
      eventList,
    },
  
    
    
    mounted() {
      this.fetchEventData();
    },
    methods: {
      async fetchEventData() {
        try {
          const response = await this.$axios.get('events/');
          this.eventLists = response.data;
       
        } catch (error) {
          console.error('Error fetching event data', error);
        }
      },
    },
  };
  </script>