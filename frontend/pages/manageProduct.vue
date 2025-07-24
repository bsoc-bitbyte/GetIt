<script setup>
import add from "../assets/productManagement/add.svg";
import filter from "../assets/productManagement/filter.svg";
import search from "../assets/productManagement/search.svg";
import ProductTable from "~/components/ProductTable.vue";
</script>

<template>
  <div class="flex flex-col items-center max-w-screen min-h-screen">
    <div class="w-11/12 p-2 mt-8 mb-8 rounded-xl shadow-md">
      <h2 class="text-4xl font-extrabold p-2">Product Management</h2>
      <p class="text-gray-500 p-2">Manage your products and inventory</p>
    </div>
    <div
      class="flex justify-between items-center w-11/12 shadow-md p-5 rounded-xl"
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
            type="text"
            placeholder="Search Products..."
            class="block p-2 focus-within:outline-none"
          />
        </div>
        <div
          class="flex justify-evenly p-4 border-gray-200 border-2 rounded-md cursor-pointer hover:-translate-y-1 active:translate-y-1 transition-all duration-200 ease-in-out"
        >
          <img :src="filter" alt="filter" class="block w-6" />
          <p>Filter</p>
        </div>
        <div
          class="p-4 bg-[#E43232] rounded-md shadow-lg w-20 flex items-center justify-center cursor-pointer hover:-translate-y-1 active:translate-y-1 transition-all duration-200 ease-in-out"
        >
          <p class="text-white">Add</p>
        </div>
        <div
          class="p-4 bg-[#F3F4F6] rounded-md shadow-lg w-20 flex items-center justify-center cursor-pointer border-gray-200 border-2 hover:-translate-y-1 active:translate-y-1 transition-all duration-200 ease-in-out"
        >
          <p>Clear</p>
        </div>
      </div>
    </div>
    <ProductTable />
  </div>
</template>

<script>
// definePageMeta({
//     layout: 'admin-layout',
//     middleware: 'admin-auth'
// })
</script>
