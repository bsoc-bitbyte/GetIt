<template>
  <div class="overflow-x-auto w-full flex flex-col justify-center mt-20 p-2">
    <div v-if="pending" class="text-center text-lg text-gray-500 my-10">
      Loading Products...
    </div>
    <div v-else-if="error" class="text-center text-lg text-gray-500 my-10">
      Error loading products: {{ error }}
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
          <th class="p-5 text-gray-500">IMAGE</th>
          <th class="p-5 text-gray-500">PRODUCT NAME</th>
          <th class="p-5 text-gray-500">SIZE</th>
          <th class="p-5 text-gray-500">STOCK</th>
          <th class="p-5 text-gray-500">PRICE</th>
          <th class="p-5 text-gray-500">DATE</th>
          <th class="p-5 text-gray-500">ACTIONS</th>
        </tr>
      </thead>

      <tbody class="min-w-full">
        <tr v-for="product in paginatedProducts" :key="product.id">
          <td class="p-5 text-center">
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
              alt="Product"
              class="w-12 h-12 object-cover rounded"
            />
          </td>
          <td class="p-5 text-center">{{ product.name }}</td>
          <td class="p-5 text-center">{{ product.size }}</td>
          <td class="p-5">
            <div
              :class="[
                'p-2 rounded-2xl shadow flex justify-evenly items-center gap-1 w-40 mx-auto text-xs',
                product.stock > 0
                  ? 'bg-green-500/50 text-green-800'
                  : 'bg-red-500/50 text-red-800',
              ]"
            >
              <img
                :src="product.stock > 0 ? correct : wrong"
                :alt="product.stock > 0 ? 'available' : 'not available'"
                class="block w-5"
              />
              {{
                product.stock > 0
                  ? `In Stock (${product.stock})`
                  : "Out of Stock"
              }}
            </div>
          </td>
          <td class="p-5 text-center">Rs.{{ product.price }}</td>
          <td class="p-5 text-center">
            <p class="text-gray-500">Last Modified</p>
            <p>{{ product.dateModified }}</p>
          </td>
          <td class="p-5 flex gap-2 justify-center">
            <div class="action-btn bg-blue-500" @click="viewProduct(product)">
              <img :src="view" alt="view product" class="block p-1" />
            </div>
            <div class="action-btn bg-yellow-500" @click="editProduct(product)">
              <img :src="edit" alt="edit product" class="block p-1" />
            </div>
            <div
              class="action-btn bg-red-500"
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
        Showing {{ (currentPage - 1) * itemsPerPage + 1 }} -
        {{ Math.min(currentPage * itemsPerPage, totalCount) }} of
        {{ totalCount }} results
      </div>

      <div class="flex items-center gap-2">
        <button
          @click="goToPage(currentPage - 1)"
          :disabled="currentPage === 1"
          :class="buttonClass(currentPage === 1)"
        >
          <img :src="prevBtn" alt="previous" class="w-1/2" />
        </button>

        <div class="flex gap-1">
          <button v-if="startPage > 1" @click="goToPage(1)" class="page-btn">
            1
          </button>
          <span v-if="startPage > 2" class="ellipsis">...</span>

          <button
            v-for="page in visiblePages"
            :key="page"
            @click="goToPage(page)"
            :class="pageClass(page)"
          >
            {{ page }}
          </button>

          <span v-if="endPage < totalPages - 1" class="ellipsis">...</span>
          <button
            v-if="endPage < totalPages"
            @click="goToPage(totalPages)"
            class="page-btn"
          >
            {{ totalPages }}
          </button>
        </div>

        <button
          @click="goToPage(currentPage + 1)"
          :disabled="currentPage === totalPages"
          :class="buttonClass(currentPage === totalPages)"
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

function buildQuery(filters) {
  const query = new URLSearchParams();
  for (const key in filters) {
    const value = filters[key];
    if (value !== null && value !== undefined && value !== "") {
      query.append(key, value);
    }
  }
  return query.toString();
}

const props = defineProps({
  searchTerm: String,
  selectedType: String,
  minPrice: Number,
  maxPrice: Number,
  selectedSort: String,
  selectedCategory: String,
  selectedColor: String,
  selectedSize: String,
});

const currentPage = ref(1);
const itemsPerPage = ref(15);
const selectedProducts = ref([]);

const queryString = computed(() =>
  buildQuery({
    search: props.searchTerm,
    type: props.selectedType,
    category: props.selectedCategory,
    color: props.selectedColor,
    size: props.selectedSize,
    min_price: props.minPrice,
    max_price: props.maxPrice,
    ordering: props.selectedSort,
    page: currentPage.value,
  }).toString()
);

const {
  data: fetchedProducts,
  pending,
  error,
  refresh,
} = useFetch(
  () => `${config.public.API_BASE_URL}/api/products/?${queryString.value}`
);

const paginatedProducts = computed(() => fetchedProducts.value?.results || []);
const totalCount = computed(() => fetchedProducts.value?.count || 0);
const totalPages = computed(() =>
  Math.ceil(totalCount.value / itemsPerPage.value)
);

const isAllSelected = computed(() => {
  const ids = paginatedProducts.value.map((p) => p.id);
  return (
    ids.length > 0 && ids.every((id) => selectedProducts.value.includes(id))
  );
});

const visiblePageCount = 5;
const startPage = computed(() =>
  Math.min(
    Math.max(1, currentPage.value - Math.floor(visiblePageCount / 2)),
    Math.max(1, totalPages.value - visiblePageCount + 1)
  )
);
const endPage = computed(() =>
  Math.min(totalPages.value, startPage.value + visiblePageCount - 1)
);
const visiblePages = computed(() =>
  Array.from(
    { length: endPage.value - startPage.value + 1 },
    (_, i) => startPage.value + i
  )
);

const goToPage = (page) => {
  if (page >= 1 && page <= totalPages.value) currentPage.value = page;
};

const toggleSelectAll = () => {
  const ids = paginatedProducts.value.map((p) => p.id);
  if (isAllSelected.value) {
    selectedProducts.value = selectedProducts.value.filter(
      (id) => !ids.includes(id)
    );
  } else {
    selectedProducts.value.push(
      ...ids.filter((id) => !selectedProducts.value.includes(id))
    );
  }
};

const deleteProduct = async (id) => {
  if (!confirm("Are you sure you want to delete this product?")) return;
  try {
    const res = await fetch(
      `${config.public.API_BASE_URL}/api/products/${id}`,
      { method: "DELETE" }
    );
    if (!res.ok) throw new Error("Failed to delete product");
    selectedProducts.value = selectedProducts.value.filter((pid) => pid !== id);
    if (paginatedProducts.value.length === 1 && currentPage.value > 1)
      currentPage.value--;
  } catch (err) {
    console.error("Delete Failed:", err);
    alert("Something went wrong while trying to delete the product.");
  }
};

const viewProduct = (product) => console.log("View product:", product);
const editProduct = (product) => console.log("Edit product:", product);

watch(
  () => paginatedProducts.value.length,
  () => {
    if (currentPage.value > totalPages.value) {
      currentPage.value = Math.max(1, totalPages.value);
    }
  }
);

const pageClass = (page) =>
  page === currentPage.value
    ? "bg-red-600 text-white px-3 py-2 rounded-lg text-sm font-medium"
    : "text-gray-700 hover:bg-gray-100 px-3 py-2 rounded-lg text-sm font-medium";

const buttonClass = (disabled) => [
  "px-3 py-2 rounded-lg text-sm font-medium transition-colors",
  disabled
    ? "text-gray-400 cursor-not-allowed"
    : "text-gray-700 hover:bg-gray-100",
];
</script>

<style scoped>
.action-btn {
  width: 2.5rem;
  border-radius: 0.5rem;
  cursor: pointer;
  padding: 0.25rem;
  transition: transform 0.2s ease-in-out;
}
.action-btn:hover {
  transform: translateY(-2px);
}
.action-btn:active {
  transform: translateY(1px);
}
.page-btn {
  padding: 0.5rem 0.75rem;
  border-radius: 0.5rem;
  font-size: 0.875rem;
  font-weight: 500;
  color: #374151;
  background-color: transparent;
  transition: background-color 0.2s;
}
.page-btn:hover {
  background-color: #f3f4f6;
}
.ellipsis {
  padding: 0.5rem 0.75rem;
  color: #6b7280;
}
</style>
