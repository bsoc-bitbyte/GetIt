<template>
  <div class="flex flex-col space-y-2 w-96">
    <div
      class="relative flex justify-between items-start flex-col sm:flex-row sm:h-16 h-20 w-full"
    >
      <div class="px-5 sm:px-2">
        <h1 class="font-normal poppins text-2xl text-[#6C6C6C]">Tags</h1>
      </div>
      <div class="relative h-[36px] w-[251px] mb-1 sm:mb-0">
        <!-- Input field for adding new tags -->
        <input
          type="text"
          v-model="input"
          @keydown.enter.prevent="handleEnter"
          @focus="isFocused = true"
          @blur="isFocused = false"
          placeholder="search for tags here"
          class="h-[36px] w-[251px] poppins text-sm font-normal px-5 rounded-full searchbar focus:outline-none focus:ring-2 focus:ring-blue-500"
        />
        <img
          src="../assets/searchicon.svg"
          class="absolute top-[25%] right-[10%]"
          alt="searchicon"
        />

        <!-- Suggestions dropdown -->
        <ul
          v-if="suggestions.length && isFocused"
          class="absolute mt-1 border-2 border-[#808080] rounded-b-3xl bg-white max-h-48 overflow-y-auto w-[251px] z-1 mt-5 py-2 px-4 poppins"
        >
          <li
            v-for="(suggestion, index) in suggestions"
            :key="index"
            @mousedown.prevent="selectSuggestion(suggestion)"
            class="py-1 px-2 cursor-pointer hover:bg-gray-100 text-black rounded-md"
          >
            {{ suggestion }}
          </li>
        </ul>
      </div>
    </div>

    <!-- Display selected tags -->
    <div class="flex flex-wrap gap-3 mb-2 poppins">
      <span
        v-for="(tag, index) in selectedTags"
        :key="index"
        class="text-[#808080] h-[36px] px-3 ml-1 flex items-center bg-transparent border-[2.5px] border-[#808080] rounded-full text-xs shadow"
      >
        {{ tag }}
        <button
          @click="removeTag(index)"
          class="ml-7 hover:text-red-800 h-4 w-4 flex justify-end items-center"
        >
          <img src="../assets/cross.svg" alt="removetag" />
        </button>
      </span>
    </div>
  </div>
</template>

<script setup>
import { ref, computed } from "vue";

const props = defineProps({
  availableTags: {
    type: Array,
    default: () => [],
  },
  initialTags: {
    type: Array,
    default: () => [],
  },
});

const emit = defineEmits(["update:tags"]);

const input = ref("");
const isFocused = ref(false);
const selectedTags = ref([...props.initialTags]);

const suggestions = computed(() => {
  if (!input.value) return [];
  const lowercaseInput = input.value.toLowerCase();
  return props.availableTags
    .filter(
      (tag) =>
        tag.toLowerCase().includes(lowercaseInput) &&
        !selectedTags.value.includes(tag)
    )
    .slice(0, 3);
});

const handleEnter = () => {
  const tag = input.value.trim();
  if (tag) {
    addTag(tag);
    input.value = "";
  }
};

const addTag = (tag) => {
  if (!selectedTags.value.includes(tag)) {
    selectedTags.value.push(tag);
    emit("update:tags", selectedTags.value);
  }
};

const removeTag = (index) => {
  selectedTags.value.splice(index, 1);
  emit("update:tags", selectedTags.value);
};

const selectSuggestion = (suggestion) => {
  addTag(suggestion);
  input.value = "";
};
</script>

<style scoped>
.searchbar {
  box-shadow: 0px 0px 8px 1.5px rgb(0 0 0 / 0.1);
}
.poppins {
  font-family: "Poppins", sans-serif;
  font-smooth: always;
}
</style>
