<template>
  <div class="overflow-x-auto w-11/12 flex flex-col justify-center mt-20 p-2">
    <div v-if="pending" class="text-center text-lg text-gray-500 my-10">
      Loading Products...
    </div>
    <div v-else-if="error" class="text-center text-lg text-gray-500 my-10">
      error loading products
    </div>
    <table v-else class="w-full shadow-lg rounded-xl">
      <thead class="min-w-full bg-gray-50">
        <tr>
          <th class="p-5">
            <input
              type="checkbox"
              class="w-5 h-5 cursor-pointer"
              @change="toggleSelectAll"
              :checked="isAllSelected"
            />
          </th>
          <th class="p-5"><p class="text-gray-500">IMAGE</p></th>
          <th class="p-5"><p class="text-gray-500">PRODUCT NAME</p></th>
          <th class="p-5"><p class="text-gray-500">SIZE</p></th>
          <th class="p-5"><p class="text-gray-500">STOCK</p></th>
          <th class="p-5"><p class="text-gray-500">PRICE</p></th>
          <th class="p-5"><p class="text-gray-500">DATE</p></th>
          <th class="p-5"><p class="text-gray-500">ACTIONS</p></th>
        </tr>
      </thead>
      <tbody class="min-w-full">
        <tr v-for="product in paginatedProducts" :key="product.id">
          <td class="p-5 flex justify-center">
            <input
              type="checkbox"
              class="w-5 h-5 cursor-pointer"
              v-model="selectedProducts"
              :value="product.id"
            />
          </td>
          <td class="p-5">
            <img
              :src="product.image"
              alt=""
              class="w-12 h-12 object-cover rounded"
            />
          </td>
          <td class="p-5">
            <p class="text-center">{{ product.name }}</p>
          </td>
          <td class="p-5">
            <p class="text-center">{{ product.size }}</p>
          </td>
          <td class="p-5">
            <div
              :class="[
                'p-2 rounded-2xl shadow flex justify-evenly items-center gap-1 w-40 mr-auto ml-auto',
                product.stock > 0
                  ? 'bg-green-500/50 text-green-800 text-xs'
                  : 'bg-red-500/50 text-red-800 text-xs',
              ]"
            >
              <img
                v-if="product.stock > 0"
                v-bind:src="correct"
                :alt="available"
                class="block w-5"
              />
              <img v-else :src="wrong" alt="not available" class="block w-5" />
              {{
                product.stock > 0
                  ? `In Stock (${product.stock})`
                  : "Out of Stock"
              }}
            </div>
          </td>
          <td class="p-5">
            <p class="text-center">Rs.{{ product.price }}</p>
          </td>
          <td class="p-5">
            <p class="text-gray-500 text-center">Last Modified</p>
            <p class="text-center">{{ product.dateModified }}</p>
          </td>
          <td class="flex gap-2 p-5 justify-center">
            <div
              class="bg-[#3B82F6] w-10 rounded-lg cursor-pointer p-1 hover:-translate-y-1 active:translate-y-1 transition-all duration-200 ease-in-out"
              @click="viewProduct(product)"
            >
              <img :src="view" alt="view product" class="block p-1" />
            </div>
            <div
              class="bg-[#F59E0B] w-10 rounded-lg cursor-pointer p-1 hover:-translate-y-1 active:translate-y-1 transition-all duration-200 ease-in-out"
              @click="editProduct(product)"
            >
              <img :src="edit" alt="edit product" class="block p-1" />
            </div>
            <div
              class="bg-[#EF4444] w-10 rounded-lg cursor-pointer p-1 hover:-translate-y-1 active:translate-y-1 transition-all duration-200 ease-in-out"
              @click="deleteProduct(product.id)"
            >
              <img :src="deleteIcon" alt="delete product" class="block p-1" />
            </div>
          </td>
        </tr>
      </tbody>
    </table>

    <div
      class="flex justify-between items-center mt-6 p-4 rounded-lg shadow-md"
    >
      <div class="text-sm text-gray-600">
        Showing {{ startIndex + 1 }}-{{
          Math.min(endIndex, filteredProducts.length)
        }}
        of {{ filteredProducts.length }} results
      </div>

      <div class="flex items-center gap-2">
        <button
          @click="goToPage(currentPage - 1)"
          :disabled="currentPage === 1"
          :class="[
            'px-3 py-2 rounded-lg text-sm font-medium transition-colors',
            currentPage === 1
              ? 'text-gray-400 cursor-not-allowed'
              : 'text-gray-700 hover:bg-gray-100',
          ]"
        >
          <img :src="prevBtn" alt="previous" class="w-1/2" />
        </button>

        <div class="flex gap-1">
          <button
            v-if="startPage > 1"
            @click="goToPage(1)"
            class="px-3 py-2 rounded-lg text-sm font-medium text-gray-700 hover:bg-gray-100"
          >
            1
          </button>

          <span v-if="startPage > 2" class="px-3 py-2 text-gray-500">...</span>

          <button
            v-for="page in visiblePages"
            :key="page"
            @click="goToPage(page)"
            :class="[
              'px-3 py-2 rounded-lg text-sm font-medium transition-colors',
              page === currentPage
                ? 'bg-red-600 text-white'
                : 'text-gray-700 hover:bg-gray-100',
            ]"
          >
            {{ page }}
          </button>

          <span v-if="endPage < totalPages - 1" class="px-3 py-2 text-gray-500"
            >...</span
          >

          <button
            v-if="endPage < totalPages"
            @click="goToPage(totalPages)"
            class="px-3 py-2 rounded-lg text-sm font-medium text-gray-700 hover:bg-gray-100"
          >
            {{ totalPages }}
          </button>
        </div>

        <button
          @click="goToPage(currentPage + 1)"
          :disabled="currentPage === totalPages"
          :class="[
            'px-3 py-2 rounded-lg text-sm font-medium transition-colors',
            currentPage === totalPages
              ? 'text-gray-400 cursor-not-allowed'
              : 'text-gray-700 hover:bg-gray-100',
          ]"
        >
          <img :src="nextBtn" alt="next" class="w-1/2" />
        </button>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, computed, watch, watchEffect } from "vue";
import deleteIcon from "../assets/productManagement/deleteIcon.svg";
import edit from "../assets/productManagement/edit.svg";
import view from "../assets/productManagement/view.svg";
import correct from "../assets/productManagement/correct.svg";
import wrong from "../assets/productManagement/wrong.svg";
import prevBtn from "./assets/prevBtn.svg";
import nextBtn from "./assets/nextBtn.svg";
import { useFetch } from "#app";

const config = useRuntimeConfig();

const {
  data: fetchedProducts,
  pending,
  error,
} = await useFetch(`${config.public.API_BASE_URL}/api/products/`);

const products = ref([]);
watchEffect(() => {
  if (fetchedProducts.value) {
    products.value = fetchedProducts.value;
  }
});

const currentPage = ref(1);
const itemsPerPage = ref(15);
const selectedProducts = ref([]);

const filteredProducts = computed(() => products.value);

const totalPages = computed(() =>
  Math.ceil(filteredProducts.value.length / itemsPerPage.value)
);

const startIndex = computed(() => (currentPage.value - 1) * itemsPerPage.value);

const endIndex = computed(() => startIndex.value + itemsPerPage.value);

const paginatedProducts = computed(() =>
  filteredProducts.value.slice(startIndex.value, endIndex.value)
);

const isAllSelected = computed(() => {
  const currentPageProductIds = paginatedProducts.value.map((p) => p.id);
  return (
    currentPageProductIds.length > 0 &&
    currentPageProductIds.every((id) => selectedProducts.value.includes(id))
  );
});

const visiblePageCount = 5;
const startPage = computed(() => {
  const start = Math.max(
    1,
    currentPage.value - Math.floor(visiblePageCount / 2)
  );
  return Math.min(start, Math.max(1, totalPages.value - visiblePageCount + 1));
});

const endPage = computed(() =>
  Math.min(totalPages.value, startPage.value + visiblePageCount - 1)
);

const visiblePages = computed(() => {
  const pages = [];
  for (let i = startPage.value; i <= endPage.value; i++) {
    pages.push(i);
  }
  return pages;
});

const goToPage = (page) => {
  if (page >= 1 && page <= totalPages.value) {
    currentPage.value = page;
  }
};

const toggleSelectAll = () => {
  const currentPageProductIds = paginatedProducts.value.map((p) => p.id);

  if (isAllSelected.value) {
    selectedProducts.value = selectedProducts.value.filter(
      (id) => !currentPageProductIds.includes(id)
    );
  } else {
    const newSelections = currentPageProductIds.filter(
      (id) => !selectedProducts.value.includes(id)
    );
    selectedProducts.value.push(...newSelections);
  }
};

const deleteProduct = (productId) => {
  if (confirm("Are you sure you want to delete this product?")) {
    products.value = products.value.filter(
      (product) => product.id !== productId
    );

    selectedProducts.value = selectedProducts.value.filter(
      (id) => id !== productId
    );

    if (paginatedProducts.value.length === 0 && currentPage.value > 1) {
      currentPage.value = currentPage.value - 1;
    }
  }
};

const editProduct = (product) => {
  console.log("Edit product:", product);
};

const viewProduct = (product) => {
  console.log("View product:", product);
};

watch(
  () => products.value.length,
  () => {
    if (currentPage.value > totalPages.value) {
      currentPage.value = Math.max(1, totalPages.value);
    }
  }
);
</script>
