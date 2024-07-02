<template>
  <div class="w-full relative">
    <div class="relative w-full h-[728px] overflow-hidden group">
      <div
        class="flex transition-transform w-full duration-500 h-full"
        :style="{ transform: `translateX(-${currentIndex * 100}%)` }"
      >
        <div
          v-for="(item, index) in items"
          :key="index"
          class="w-full flex-shrink-0 h-full"
        >
          <div class="h-full w-full flex items-center justify-center">
            <img
              class="object-cover h-full w-full"
              :src="item.image"
              alt="carouselimage"
            />
            <div
              class="h-full w-full bg-gradient-to-b from-transparent via-[#00000080] via-35% to-black fixed"
            >
              <div class="w-full absolute top-[100px] h-[180px] flex px-[10%]">
                <div
                  class="w-[60vw] h-[180px] sm:w-[50vw] sm:text-6xl/[90px] font-semibold text-5xl text-white poppins"
                >
                  {{item.title}}
                </div>
              </div>
              <div
                class="w-full relative top-[476px] h-[72px] flex px-[5%] justify-end"
              >
                <div
                  class="sm:w-[35vw] h-full w-[50vw] font-light text-sm sm:text-base text-white poppins text-right"
                >
                  {{item.description}}
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
      <div
        class="h-[15px] w-full absolute self-end bottom-[55px] flex gap-4 justify-center items-center"
      >
        <div
          v-for="i in items.length"
          :key="i"
          class="h-[10px] w-[10px] rounded-full bg-white"
          :class="{ active: currentIndex === i - 1 }"
        ></div>
      </div>

      <button
        v-if="currentIndex > 0"
        class="absolute left-5 top-1/2 transform -translate-y-1/2 p-2 bg-opacity-50 text-white hover:bg-opacity-75 transition-opacity opacity-0 group-hover:opacity-100"
        @click="prev"
      >
        <img
          src="../assets/arrowleft.svg"
          alt="arrowleft"
          class="h-[50px] w-[17px]"
        />
      </button>

      <button
        v-if="currentIndex < items.length - 1"
        class="absolute right-6 top-1/2 transform -translate-y-1/2 p-2 bg-opacity-50 text-white hover:bg-opacity-75 transition-opacity opacity-0 group-hover:opacity-100"
        @click="next"
      >
        <img
          src="../assets/arrowright.svg"
          alt="arrowright"
          class="h-[50px] w-[17px]"
        />
      </button>
    </div>
  </div>
</template>

<script>
export default {
  name: "IndexPage",
  data() {
    return {
      currentIndex: 0,
      items: [
        {
          image: "\carousel_image.png",
          title: "Lorem ipsum some text about it!",
          description:
            "lorem ipsum aaa Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla vitae ipsum sit amet velit feugiat fermentum. Lorem ipsum dolor sit amet, consectetur adipiscing elit.",
        },
        {
          image: "\carousel_image.png",
          title: "Lorem ipsum some text about it!",
          description:
            "lorem ipsum aaa Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla vitae ipsum sit amet velit feugiat fermentum. Lorem ipsum dolor sit amet, consectetur adipiscing elit.",
        },
        {
          image: "\carousel_image.png",
          title: "Lorem ipsum some text about it!",
          description:
            "lorem ipsum aaa Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla vitae ipsum sit amet velit feugiat fermentum. Lorem ipsum dolor sit amet, consectetur adipiscing elit.",
        },
        {
          image: "\carousel_image.png",
          title: "Lorem ipsum some text about it!",
          description:
            "lorem ipsum aaa Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla vitae ipsum sit amet velit feugiat fermentum. Lorem ipsum dolor sit amet, consectetur adipiscing elit.",
        },
      ],
    };
  },
  methods: {
    prev() {
      if (this.currentIndex > 0) {
        this.currentIndex--;
      }
    },
    next() {
      if (this.currentIndex < this.items.length - 1) {
        this.currentIndex++;
      }
    },
  },
};
</script>

<style scoped>
.poppins {
  font-family: "Poppins", sans-serif;
  font-smooth: always;
}
.active {
  background-color: #ea454c;
  height: 15px;
  width: 15px;
}
</style>
