<template>
  <div class="flex flex-col items-center w-full min-h-screen mr-3">
    <div class="w-full p-2 mt-8 mb-8 rounded-xl shadow-md">
      <h2 class="text-4xl font-extrabold p-2">Product Management</h2>
      <p class="text-gray-500 p-2">Manage your products and inventory</p>
    </div>
    <div
      class="flex justify-between items-center w-full shadow-md p-5 rounded-xl"
    >
      <div
        class="bg-[#E43232] rounded-md p-3 shadow-lg flex justify-evenly items-center cursor-pointer hover:-translate-y-1 active:translate-y-1 transition-all duration-200 ease-in-out"
      >
        <img :src="add" alt="add item" class="block w-8 p-1" />
        <p class="p-1 text-white font-bold">Add new Product</p>
      </div>
      <div class="flex justify-between items-center gap-6">
        <div
          class="w-auto border-gray-200 border-2 flex justify-evenly items-center rounded-lg shadow-lg focus-within:border-gray-800 p-2"
        >
          <img
            :src="search"
            alt="search"
            class="block w-10 p-2 cursor-pointer hover:-translate-y-1 active:translate-y-1 transition-all duration-200 ease-in-out"
          />
          <input
            v-model="searchTerm"
            type="search"
            placeholder="Search Products..."
            class="block p-2 focus-within:outline-none"
          />
        </div>
        <div
          @click="toggleFilterBar"
          class="flex justify-evenly p-4 border-gray-200 border-2 rounded-md cursor-pointer hover:-translate-y-1 active:translate-y-1 transition-all duration-200 ease-in-out"
        >
          <img :src="filter" alt="filter" class="block w-6" />
          <p>Filter</p>
        </div>
        <div
          @click="clearFilters"
          class="p-4 bg-[#F3F4F6] rounded-md shadow-lg w-20 flex items-center justify-center cursor-pointer border-gray-200 border-2 hover:-translate-y-1 active:translate-y-1 transition-all duration-200 ease-in-out"
        >
          <p>Clear</p>
        </div>
      </div>
    </div>
    <FilterPanel
      v-if="showFilter"
      v-model:selectedType="selectedType"
      v-model:minPrice="minPrice"
      v-model:maxPrice="maxPrice"
      v-model:selectedSort="selectedSort"
      v-model:selectedCategory="selectedCategory"
      v-model:selectedColor="selectedColor"
      v-model:selectedSize="selectedSize"
    />
    <ProductTable
      :searchTerm="searchTerm"
      :selectedType="selectedType"
      :minPrice="minPrice"
      :maxPrice="maxPrice"
      :selectedSort="selectedSort"
      :selectedCategory="selectedCategory"
      :selectedColor="selectedColor"
      :selectedSize="selectedSize"
    />
  </div>
</template>

<script setup>
import add from "../assets/productManagement/add.svg";
import filter from "../assets/productManagement/filter.svg";
import search from "../assets/productManagement/search.svg";
import ProductTable from "~/components/ProductTable.vue";
import FilterPanel from "~/components/FilterPanel.vue";

const searchTerm = ref("");
const selectedType = ref("");
const minPrice = ref(null);
const maxPrice = ref(null);
const selectedSort = ref("");
const selectedCategory = ref("");
const selectedColor = ref("");
const selectedSize = ref("");
const showFilter = ref(false);

const toggleFilterBar = () => {
  showFilter.value = !showFilter.value;
};

const clearFilters = () => {
  searchTerm.value = "";
  selectedType.value = "";
  minPrice.value = null;
  maxPrice.value = null;
  selectedSort.value = "";
  selectedCategory.value = "";
  selectedColor.value = "";
  selectedSize.value = "";
};

definePageMeta({
  layout: "admin-layout",
  middleware: "admin-auth",
});
</script>
