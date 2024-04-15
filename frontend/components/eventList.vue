<template>
  <div
    class="w-94 bg-white shadow-md rounded-xl duration-500 hover:scale-105 hover:shadow-xl p-5"
  >
    <img class="w-96 h-80 object-cover" :src="img_url" />
    <div class="py-3 w-96">
      <p class="text-lg font-bold text-black truncate block capitalize">
        {{ title }}
      </p>
      <span class="text-gray-400 mr-3 uppercase text-xs">{{ location }}</span>
      <div class="flex items-center">
        <p
          class="text-lg rounded-full bg-green-500/10 px-5 py-2 text-green-700 font-semibold cursor-auto my-3"
        >
          ₹{{ ticket_price }}
        </p>
        <div class="ml-auto">{{ date }}</div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  props: {
    title: {
      type: String,
      required: true,
    },
    description: {
      type: String,
      required: true,
    },
    email: {
      type: String,
      required: true,
    },
    date: {
      type: String,
      required: true,
    },
    location: {
      type: String,
      required: true,
    },
    ticket_price: {
      type: String,
      required: true,
    },
    img_url: {
      type: String,
      required: true,
    },
  },
  name: "eventList",
};
</script>
