<template>
  <div class="">
    <div class="flex justify-center mb-4">
      <img
        class="h-auto max-w-full rounded-lg"
        :src="`${config.public.API_BASE_URL}${product.product_images[imageIdx].image}`"
        :alt="`Product Image ${imageIdx + 1}`"
      />
    </div>
    <div class="flex justify-center items-center">
      <div
        v-if="product.product_images.length >= 4"
        class="flex justify-center items-center"
      >
        <div>
          <button class="w-4" @click="prev" :disabled="imageGalleryIndex === 0">
            <img class="w-4" src="assets/prevBtn.svg" alt="left" />
          </button>
        </div>
        <div class="grid grid-cols-4 gap-4 mx-3">
          <div
            v-for="(image, index) in visibleImages"
            :key="index"
            class="max-h-32"
          >
            <img
              class="max-h-32 max-w-full rounded-lg"
              :src="`${config.public.API_BASE_URL}${image.image}`"
              :alt="`Product Image ${index + 1}`"
              @click="imageSelector(index + imageGalleryIndex)"
              :style="{
                outline:
                  index + imageGalleryIndex === imageIdx
                    ? '2px solid black'
                    : 'none',
                outlineOffset:
                  index + imageGalleryIndex === imageIdx ? '2px' : '0',
              }"
            />
          </div>
        </div>

        <div>
          <button
            class="w-4"
            @click="next"
            :disabled="imageGalleryIndex + 4 >= product.product_images.length"
          >
            <img class="w-4" src="assets/nextBtn.svg" alt="right" />
          </button>
        </div>
      </div>
      
      <div
        v-if="product.product_images.length < 4"
        class="grid gap-4 mx-3"
        :class="gridClass"
      >
        <div
          v-for="(image, index) in visibleImages"
          :key="index"
          class="max-h-32"
        >
          <img
            class="max-h-32 max-w-full rounded-lg"
            :src="`${config.public.API_BASE_URL}${image.image}`"
            :alt="`Product Image ${index + 1}`"
            @click="imageSelector(index + imageGalleryIndex)"
            :style="{
              outline:
                index + imageGalleryIndex === imageIdx
                  ? '2px solid black'
                  : 'none',
              outlineOffset:
                index + imageGalleryIndex === imageIdx ? '2px' : '0',
            }"
          />
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  props: {
    product: Object,
    config: Object,
  },
  data() {
    return {
      imageIdx: 0,
      imageGalleryIndex: 0,
    };
  },
  computed: {
    visibleImages() {
      return this.product.product_images.slice(
        this.imageGalleryIndex,
        this.imageGalleryIndex + 4
      );
    },
    gridClass() {
      const numColumns = this.product.product_images.length;
      return `grid-cols-${numColumns}`;
    },
  },
  methods: {
    imageSelector(index) {
      this.imageIdx = index;
    },
    next() {
      if (this.imageGalleryIndex + 4 < this.product.product_images.length) {
        this.imageGalleryIndex += 1;
      }
    },
    prev() {
      if (this.imageGalleryIndex > 0) {
        this.imageGalleryIndex -= 1;
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
</style>
