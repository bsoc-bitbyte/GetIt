<template>
  <div class="m-20 owe">
    <div class="flex justify-center items-center flex-col gap-8 mt-20 lg:flex-row">
      <div class="flex flex-wrap justify-center lg:justify-start gap-8">
        <NuxtLink v-for="(data, index) in eventLists" :to="`/events/${data.id}`" :key="data.id">
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
  </div>
</template>


<script setup>
import eventList from '@/components/eventList.vue';

const config = useRuntimeConfig();
const eventLists = ref([]);
async function fetchEventData() {
  try {
    const response = await $fetch(`${config.public.API_BASE_URL}/api/events/`);
    eventLists.value = response;
  } catch (error) {
    console.error('Error fetching event data', error);
  }
}

onMounted(() => fetchEventData());
</script>
<style>
::-webkit-scrollbar {
  margin-top: 10px;
  width: 3px; /* Example width */
  background-color: #F5F5F5;
}

/* Scrollbar track */
::-webkit-scrollbar-track {
  background-color: #F5F5F5;
}

/* Scrollbar handle */
::-webkit-scrollbar-thumb {
  background-color: #ec4a52;
  border-radius: 5px;  /* Example rounding */
}

/* Optional: Scrollbar Corner */
::-webkit-scrollbar-corner {
  background-color: #F5F5F5;
}
</style>

