<template>
  <div class="m-20">
    <h1 class="text-4xl font-bold text-center">Event List</h1>
    <div class="flex justify-center items-center flex-col gap-8 mt-20 lg:flex-row">
      <eventList
        v-for="(data, index) in eventLists"
        :key="index"
        :title="data.title"
        :description="data.description"
        :email="data.email"
        :date="data.date"
        :event_type="data.event_type"
        :location="data.location"
        :ticket_price="data.ticket_price"
        :img_url="data.cover_image"
      />
    </div>
  </div>
</template>

<script>
import eventList from '@/components/eventList.vue';
import axios from 'axios';

export default {
  name: 'IndexPage',
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
        const response = await axios.get('https://backend-getit.onrender.com/api/events/');
        this.eventLists = response.data;
        console.log(this.eventLists) 
      } catch (error) {
        console.error('Error fetching event data', error);
      }
    },
  },
};
</script>

