<template>
  <div class="p-4 border rounded-xl shadow-lg bg-white w-full mt-6">
    <h2 class="text-xl font-bold mb-4">Filters</h2>
    <div
      class="grid p-2 w-full justify-between gap-4 grid-flow-col grid-rows-2 place-items-center"
    >
      <!-- Type -->
      <div>
        <label class="block mb-2 text-center">Type:</label>
        <input type="text" v-model="typeProxy" class="input-field" />
      </div>

      <!-- Category -->
      <div>
        <label class="block mb-2 text-center">Category:</label>
        <select v-model="categoryProxy" class="input-field custom-select">
          <option value="">All</option>
          <option value="clothing">Clothing</option>
          <option value="rsvp">RSVP</option>
        </select>
      </div>

      <!-- Min Price -->
      <div class="flex flex-col items-center">
        <label class="block mb-2 text-center">Min Price:</label>
        <input type="number" v-model.number="minProxy" class="input-field" />
      </div>

      <!-- Max Price -->
      <div class="flex flex-col items-center">
        <label class="block mb-2 text-center">Max Price:</label>
        <input type="number" v-model.number="maxProxy" class="input-field" />
      </div>

      <!-- Color -->
      <div class="flex flex-col items-center">
        <label class="block mb-2 text-center">Color:</label>
        <input type="text" v-model="colorProxy" class="input-field" />
      </div>

      <!-- Size -->
      <div class="flex flex-col items-center">
        <label class="block mb-2 text-center">Size:</label>
        <input type="text" v-model="sizeProxy" class="input-field" />
      </div>

      <!-- Sort By -->
      <div>
        <label class="block mb-2 text-center">Sort By:</label>
        <select v-model="sortProxy" class="input-field custom-select">
          <option value="">None</option>
          <option value="name">Name (A-Z)</option>
          <option value="-name">Name (Z-A)</option>
          <option value="price">Price (Low to High)</option>
          <option value="-price">Price (High to Low)</option>
          <option value="created_at">Newest</option>
          <option value="-created_at">Oldest</option>
        </select>
      </div>
    </div>
  </div>
</template>

<script setup>
import { computed } from "vue";

const props = defineProps({
  selectedType: String,
  selectedCategory: String,
  minPrice: Number,
  maxPrice: Number,
  selectedColor: String,
  selectedSize: String,
  selectedSort: String,
});

const emit = defineEmits([
  "update:selectedType",
  "update:selectedCategory",
  "update:minPrice",
  "update:maxPrice",
  "update:selectedColor",
  "update:selectedSize",
  "update:selectedSort",
]);

const typeProxy = computed({
  get: () => props.selectedType,
  set: (val) => emit("update:selectedType", val),
});

const categoryProxy = computed({
  get: () => props.selectedCategory,
  set: (val) => emit("update:selectedCategory", val),
});

const minProxy = computed({
  get: () => props.minPrice,
  set: (val) => emit("update:minPrice", val),
});

const maxProxy = computed({
  get: () => props.maxPrice,
  set: (val) => emit("update:maxPrice", val),
});

const colorProxy = computed({
  get: () => props.selectedColor,
  set: (val) => emit("update:selectedColor", val),
});

const sizeProxy = computed({
  get: () => props.selectedSize,
  set: (val) => emit("update:selectedSize", val),
});

const sortProxy = computed({
  get: () => props.selectedSort,
  set: (val) => emit("update:selectedSort", val),
});
</script>

<style scoped>
.input-field {
  @apply border-2 rounded-md px-3 py-2 w-40 focus:border-[#E43232] focus:outline-none shadow-lg;
  height: 42px;
  background-color: white;
}

/* Custom dropdown arrow and appearance */
.custom-select {
  -webkit-appearance: none;
  -moz-appearance: none;
  appearance: none;
  background-image: url("data:image/svg+xml;charset=US-ASCII,%3Csvg%20fill%3D%22%23E43232%22%20viewBox%3D%220%200%2020%2020%22%20xmlns%3D%22http://www.w3.org/2000/svg%22%3E%3Cpath%20fill-rule%3D%22evenodd%22%20d%3D%22M10%2012a.75.75%200%2001-.53-.22l-3-3a.75.75%200%20111.06-1.06L10%2010.19l2.47-2.47a.75.75%200%20011.06%201.06l-3%203a.75.75%200%2001-.53.22z%22%20clip-rule%3D%22evenodd%22%2F%3E%3C/svg%3E");
  background-repeat: no-repeat;
  background-position: right 0.75rem center;
  background-size: 1rem;
  padding-right: 2.5rem;
  box-shadow: 0 1px 4px rgba(0, 0, 0, 0.1);
}

/* Default options */
.custom-select option {
  background-color: white;
  color: black;
}

/* Attempt to style hovered options — not guaranteed across all browsers */
.custom-select option:hover {
  background-color: #e43232;
  color: white;
}
</style>
