<template>
   <div
    class=" relative h-[479px] w-[380px] bg-white shadow-md shadow-[#00000040]	overflow-hidden rounded-md duration-500  hover:h-[511px] group transition-all responsive">
    <img class="w-full h-[360px] object-cover group-hover:h-[315px] duration-500 responsive" :src="img_url" />
    <img width="29" height="29" src="../assets/cart.svg"
      class="absolute z-30 left-2 top-2 opacity-0 transition-all group-hover:opacity-100 duration-500" />

    <div class="py-3 w-full p-5 h-[119px] group-hover:h-[143px] transition-all duration-500 ">
      <div class="flex justify-between h-1/3 items-center poppins">
        <p class="text-base font-semibold  text-[#9E3500] ">{{organizer}}</p>
         <p class="text-base rounded-full font-semibold cursor-auto poppins ">
          ₹{{ parseInt(ticket_price) }}
        </p>
      </div>

      <div class=" flex h-1/3 items-center transition-all duration-500">
        <p class="text-xs font-medium text-black truncate block capitalize poppins transition-all duration-1000">
          {{ title }}
        </p>
      </div>

      <div
        class="flex h-1/3 gap-1 items-center opacity-100  group-hover:hidden group-hover:opacity-0 duration-1000 transition-all">
        <span class="text-gray-400 uppercase text-xs">{{location.split(",")[0]}}</span>
        <p class="text-gray-400 text-xs">|</p>
        <div class="text-xs text-gray-400">{{ date.split("-")[0] }}</div>
      </div>

      <div
        class="flex h-1/3 gap-1 items-center opacity-0 group-hover:opacity-100 group-hover:delay-200 ease-in-out group-hover:duration-500 transition-all duration-0">
        <span class="text-gray-400 uppercase text-xs"> {{ location }}</span>
        <p class="text-gray-400 text-xs">|</p>
        <div class="text-xs text-gray-400">{{ date }}</div>
      </div>

      <div
        class="flex w-full justify-center group-hover:my-2 items-center opacity-0 group-hover:opacity-100 group-hover:delay-200 ease-in-out group-hover:duration-500 transition-all duration-0">
        <button
          class="flex items-center rounded-md text-[#17813C] bg-[#edfaf0] text-xs font-semibold poppins px-[8px] py-[10px] h-[34px] transition-all duration-100  hover:border-2 hover:border-[#00000026]">View
          Product
        </button>
      </div>

    </div>
  </div>
</template>


<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Poppins:ital,wght@0,100;0,200;0,300;0,400;0,500;0,600;0,700;0,800;0,900;1,100;1,200;1,300;1,400;1,500;1,600;1,700;1,800;1,900&display=swap');

.poppins {
  font-family: "Poppins", sans-serif;
  font-smooth: always;
}

.responsive {
  @media (max-width: 410px) {
    width: 90vw;
  }
}
</style>

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
    organizer:{
      type: String,
      required: true,
    }
  },
  name: "eventList",
};
</script>
