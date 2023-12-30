<template>
  <div class="m-20">
    <h1 class="text-4xl font-bold text-center">Event List</h1>
    <div class="flex justify-center flex-row gap-8 mt-20">
      <eventList v-for="(data, index) in eventLists" :key="index" :title="data.title" :description="data.description"
        :email="data.email" :date="data.date" :event_type="data.event_type" :location="data.location"
        :ticket_price="data.ticket_price" />
    </div>
  </div>
</template>

<script>
import eventList from '@/components/eventList.vue';

export default {
  name: 'IndexPage',
  data() {
    return {
      eventLists: [

        {
          "title": "HackByte",
          "organizer": 1,
          "description": "hello this is hackbyte",
          "email": "manojpanjwani111@gmail.com",
          "phone": "6250008650",
          "date": "2023-11-06",
          "time": "00:00:00",
          "event_type": "physical",
          "location": "India",
          "ticket_price": "150.00",
          "created_at": "2023-11-16T12:51:11.859857Z",
          "updated_at": "2023-12-05T11:31:54.331323Z"
        },
        {
          "title": "CodeRumble",
          "organizer": 2,
          "description": "this is coderumble",
          "email": "manojpanjwani111@gmail.com",
          "phone": "+916350008650",
          "date": "2023-12-09",
          "time": "18:00:00",
          "event_type": "physical",
          "location": "India",
          "ticket_price": "100.00",
          "created_at": "2023-12-05T10:10:20.536673Z",
          "updated_at": "2023-12-05T10:10:20.536708Z"
        },
        {
          "title": "Aperta",
          "organizer": 3,
          "description": "open source event",
          "email": "manojpanjwani111@gmail.com",
          "phone": "7597842278",
          "date": "2023-12-07",
          "time": "20:26:00",
          "event_type": "virtual",
          "location": "online",
          "ticket_price": "0.00",
          "created_at": "2023-12-05T10:54:14.490047Z",
          "updated_at": "2023-12-05T10:54:14.490079Z"
        }
      ],
    };
  },
  components: {
    eventList
  },
}
</script>
