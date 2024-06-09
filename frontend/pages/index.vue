<template>
    
  <title>GetIt</title>
  <link rel="icon" type="image/png" href="\Favicon.svg">
     
  <div class="justify-center items-center h-[80vh] ml-48 overflow-y-hidden hidden lg:flex">
    <div class="">
      <p class="text-xl text-gray-600 mb-2">Don't miss out on the Events! Get your tickets now.</p>
      <router-link to="/eventList">
        <button class="btn bg-[#ea454c] text-white w-48 h-12 rounded-3xl">Explore events
                  </button>    
      </router-link>
    </div>
    <div class="animation-container ">
      <client-only>
        <Vue3Lottie 
          animationLink="https://lottie.host/d825e1b5-1261-4260-af09-953428d23a6a/eKnQiaIKbM.json"
          :height="1000"
        />
      </client-only>
    </div>
  </div>


    <div class="flex flex-col justify-center items-center h-[50vh] lg:hidden">
      <div class="animation-container ">
      <client-only>
        <Vue3Lottie 
          animationLink="https://lottie.host/d825e1b5-1261-4260-af09-953428d23a6a/eKnQiaIKbM.json"
          :height="400"
        />
      </client-only>
    </div>
      <div class="text-center">
        <p class="text-xl text-gray-600 mb-2">Don't miss out on the Events! Get your tickets now.</p>
        <router-link to="/eventList">
          <button class="btn bg-[#ea454c] text-white w-48 h-12 rounded-3xl">Explore events
                    </button>    
        </router-link>
      </div>
    </div>
</template>

<script>



export default {
  name: 'IndexPage',
  mounted() {
   
  },
  methods: {
    
}};
</script>
