<template>
  <div class="image-upload lg:w-1/3 h-[650px] md:w-1/2">
    <input
      id="hidden-file-input"
      ref="fileInput"
      type="file"
      @change="onFileChange"
      accept="image/*"
      multiple
      class="hidden"
    />
    
    <div
      v-if="imageSrcs.length === 0"
      class="w-full h-full bg-gray-100 rounded-2xl flex flex-col items-center justify-center p-4"
    >
      <button
        @click="triggerFileInput"
        class="flex flex-col items-center cursor-pointer w-1/2 max-w-xs"
      >
        <img src="../assets/uploadimage.png" alt="uploadBtn" class="w-48 mb-2" />
        <span class="text-gray-600 text-center"
          >Click to upload a new image</span
        >
      </button>
    </div>

    <div
      v-if="imageSrcs.length === 1"
      class="w-full h-full rounded-2xl grid grid-cols-1 gap-2 p-4"
    >
      <div
        class="relative w-full overflow-hidden flex items-center justify-center bg-gray-100 rounded-lg"
      >
        <img
          :src="imageSrcs[0].src"
          alt="Uploaded Image"
          class="w-auto h-full object-contain"
        />
        <button
          class="absolute top-2 right-2 bg-white bg-opacity-80 rounded-full p-1 shadow hover:bg-red-500 hover:text-white transition-colors z-20"
          @click="removeImage(0)"
          title="Remove image"
          type="button"
        >
          <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"/></svg>
        </button>
      </div>
      <button
        v-if="imageSrcs.length < 8"
        @click="triggerFileInput"
        class="flex flex-col items-center cursor-pointer w-full bg-gray-100 rounded-lg p-4"
      >
        <img
          src="../assets/uploadimage.png"
          alt="uploadBtn"
          class="max-w-28 max-h-28"
        />
        <span class="text-gray-600 text-center text-sm"
          >Click to upload a new image</span
        >
      </button>
      <div
        v-if="imageSrcs.length >= 8"
        class="w-full bg-gray-100 border border-gray-300 text-gray-700 px-4 py-3 rounded-lg text-center"
      >
        <p class="text-sm font-medium">Maximum 8 images uploaded</p>
        <p class="text-xs">Remove an image to upload a new one</p>
      </div>
    </div>

    <div
      v-if="imageSrcs.length === 2"
      class="w-full h-full rounded-2xl grid grid-rows-2 grid-cols-2 gap-2 p-4"
    >
      <div
        v-for="(imageObj, index) in imageSrcs"
        :key="imageObj.id"
        class="relative overflow-hidden flex items-center justify-center bg-gray-100 rounded-lg"
      >
        <img
          :src="imageObj.src"
          alt="Uploaded Image"
          class="w-full h-full object-contain rounded-lg"
        />
        <button
          class="absolute top-2 right-2 bg-white bg-opacity-80 rounded-full p-1 shadow hover:bg-red-500 hover:text-white transition-colors z-20"
          @click="removeImage(index)"
          title="Remove image"
          type="button"
        >
          <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"/></svg>
        </button>
      </div>
      <button
        v-if="imageSrcs.length < 8"
        @click="triggerFileInput"
        class="row-span-1 col-span-2 flex flex-col items-center justify-center cursor-pointer bg-gray-100 rounded-lg p-4"
      >
        <img
          src="../assets/uploadimage.png"
          alt="uploadBtn"
          class="max-w-28 max-h-28 mb-2"
        />
        <span class="text-gray-600 text-center text-sm">
          Click to upload a new image
        </span>
      </button>
      <div
        v-if="imageSrcs.length >= 8"
        class="row-span-1 col-span-2 bg-gray-100 border border-gray-300 text-gray-700 px-4 py-3 rounded-lg text-center"
      >
        <p class="text-sm font-medium">Maximum 8 images uploaded</p>
        <p class="text-xs">Remove an image to upload a new one</p>
      </div>
    </div>

    <div
      v-if="imageSrcs.length === 3"
      class="w-full h-full rounded-2xl grid grid-rows-2 grid-cols-2 gap-2 p-4"
    >
      <div
        v-for="(imageObj, index) in imageSrcs"
        :key="imageObj.id"
        class="relative overflow-hidden flex items-center justify-center bg-gray-100 rounded-lg"
      >
        <img
          :src="imageObj.src"
          alt="Uploaded Image"
          class="w-full h-full object-contain rounded-lg"
        />
        <button
          class="absolute top-2 right-2 bg-white bg-opacity-80 rounded-full p-1 shadow hover:bg-red-500 hover:text-white transition-colors z-20"
          @click="removeImage(index)"
          title="Remove image"
          type="button"
        >
          <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"/></svg>
        </button>
      </div>
      <button
        v-if="imageSrcs.length < 8"
        @click="triggerFileInput"
        class="row-span-1 col-span-1 flex flex-col items-center justify-center cursor-pointer bg-gray-100 rounded-lg p-4"
      >
        <img
          src="../assets/uploadimage.png"
          alt="uploadBtn"
          class="max-w-28 max-h-28 mb-2"
        />
        <span class="text-gray-600 text-center text-sm">
          Click to upload a new image
        </span>
      </button>
      <div
        v-if="imageSrcs.length >= 8"
        class="row-span-1 col-span-1 bg-yellow-100 border border-yellow-400 text-yellow-800 px-4 py-3 rounded-lg flex flex-col items-center justify-center"
      >
        <p class="text-sm font-medium">Maximum 8 images uploaded</p>
        <p class="text-xs text-center">Remove an image to upload a new one</p>
      </div>
    </div>

    <div
      v-if="imageSrcs.length === 4"
      class="w-full h-full rounded-2xl grid grid-rows-3 grid-cols-2 gap-2 p-4"
    >
      <div
        v-for="(imageObj, index) in imageSrcs"
        :key="imageObj.id"
        class="relative overflow-hidden flex items-center justify-center bg-gray-100 rounded-lg"
      >
        <img
          :src="imageObj.src"
          alt="Uploaded Image"
          class="w-full h-full object-contain rounded-lg"
        />
        <button
          class="absolute top-2 right-2 bg-white bg-opacity-80 rounded-full p-1 shadow hover:bg-red-500 hover:text-white transition-colors z-20"
          @click="removeImage(index)"
          title="Remove image"
          type="button"
        >
          <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"/></svg>
        </button>
      </div>
      <button
        v-if="imageSrcs.length < 8"
        @click="triggerFileInput"
        class="col-span-2 row-span-1 flex flex-col items-center justify-center cursor-pointer bg-gray-100 rounded-lg p-4"
      >
        <img
          src="../assets/uploadimage.png"
          alt="uploadBtn"
          class="max-w-24 max-h-24 mb-2"
        />
        <span class="text-gray-600 text-center text-sm">
          Click to upload a new image
        </span>
      </button>
      <div
        v-if="imageSrcs.length >= 8"
        class="col-span-2 row-span-1 bg-gray-100 border border-gray-300 text-gray-700 px-4 py-3 rounded-lg text-center"
      >
        <p class="text-sm font-medium">Maximum 8 images uploaded</p>
        <p class="text-xs">Remove an image to upload a new one</p>
      </div>
    </div>

    <div
      v-if="imageSrcs.length === 5"
      class="w-full h-full rounded-2xl grid grid-rows-3 grid-cols-2 gap-2 p-4"
    >
      <div
        v-for="(imageObj, index) in imageSrcs"
        :key="imageObj.id"
        class="relative overflow-hidden flex items-center justify-center bg-gray-100 rounded-lg"
      >
        <img
          :src="imageObj.src"
          alt="Uploaded Image"
          class="w-full h-full object-contain rounded-lg"
        />
        <button
          class="absolute top-2 right-2 bg-white bg-opacity-80 rounded-full p-1 shadow hover:bg-red-500 hover:text-white transition-colors z-20"
          @click="removeImage(index)"
          title="Remove image"
          type="button"
        >
          <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"/></svg>
        </button>
      </div>
      <button
        v-if="imageSrcs.length < 8"
        @click="triggerFileInput"
        class="row-span-1 col-span-1 flex flex-col items-center justify-center cursor-pointer bg-gray-100 rounded-lg p-4"
      >
        <img
          src="../assets/uploadimage.png"
          alt="uploadBtn"
          class="max-w-28 max-h-28 mb-2"
        />
        <span class="text-gray-600 text-center text-sm">
          Click to upload a new image
        </span>
      </button>
      <div
        v-if="imageSrcs.length >= 8"
        class="row-span-1 col-span-1 bg-yellow-100 border border-yellow-400 text-yellow-800 px-4 py-3 rounded-lg flex flex-col items-center justify-center"
      >
        <p class="text-sm font-medium">Maximum 8 images uploaded</p>
        <p class="text-xs text-center">Remove an image to upload a new one</p>
      </div>
    </div>

    <div
      v-if="imageSrcs.length >= 6 && imageSrcs.length <= 8"
      class="w-full h-full rounded-2xl grid grid-rows-3 grid-cols-2 gap-2 p-4"
    >
      <div
        v-for="(imageObj, i) in imageSrcs.slice(0, 5)"
        :key="imageObj.id"
        class="relative overflow-hidden flex items-center justify-center bg-gray-100 rounded-lg"
      >
        <template v-if="i < 4">
          <img
            :src="imageObj.src"
            alt="Uploaded Image"
            class="w-full h-full object-contain rounded-lg"
          />
          <button
            class="absolute top-2 right-2 bg-white bg-opacity-80 rounded-full p-1 shadow hover:bg-red-500 hover:text-white transition-colors z-20"
            @click="removeImage(i)"
            title="Remove image"
            type="button"
          >
            <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"/></svg>
          </button>
        </template>
        <template v-else>
          <div class="absolute inset-0 bg-black opacity-50 z-10"></div>
          <span class="absolute z-20 text-white text-lg font-semibold">
            +{{ imageSrcs.length - 4 }} more
          </span>
          <img
            :src="imageObj.src"
            alt="Uploaded Image"
            class="w-auto h-full object-contain blur-sm"
          />
          <button
            class="absolute top-2 right-2 bg-white bg-opacity-80 rounded-full p-1 shadow hover:bg-red-500 hover:text-white transition-colors z-30"
            @click="removeImage(4)"
            title="Remove image"
            type="button"
          >
            <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"/></svg>
          </button>
        </template>
      </div>
      <button
        v-if="imageSrcs.length < 8"
        @click="triggerFileInput"
        class="row-span-1 col-span-1 flex flex-col items-center justify-center cursor-pointer bg-gray-100 rounded-lg p-4"
      >
        <img
          src="../assets/uploadimage.png"
          alt="uploadBtn"
          class="max-w-28 max-h-28 mb-2"
        />
        <span class="text-gray-600 text-center text-sm">
          Click to upload a new image
        </span>
      </button>
      <div
        v-if="imageSrcs.length >= 8"
        class="row-span-1 col-span-1 bg-yellow-100 border border-yellow-400 text-yellow-800 px-4 py-3 rounded-lg flex flex-col items-center justify-center"
      >
        <p class="text-sm font-medium">Maximum 8 images uploaded</p>
        <p class="text-xs text-center">Remove an image to upload a new one</p>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue';

const imageSrcs = ref([]);
const emit = defineEmits(["update-images"]);

// Generate unique ID for each image
const generateUniqueId = () => {
  return Date.now().toString(36) + Math.random().toString(36).substr(2);
};

// Function to trigger file input click
const triggerFileInput = () => {
  const hiddenInput = document.querySelector('#hidden-file-input');
  if (hiddenInput) {
    hiddenInput.click();
  }
};

const onFileChange = (event) => {
  const files = event.target.files;
  
  if (files && files.length > 0) {
    // Check if adding new files would exceed the limit of 8
    if (imageSrcs.value.length >= 8) {
      alert("Maximum 8 images allowed. You have already uploaded 8 images.");
      return;
    }
    
    const fileArray = Array.from(files);
    let remainingSlots = 8 - imageSrcs.value.length;
    
    if (fileArray.length > remainingSlots) {
      alert(`You can only upload ${remainingSlots} more image(s). Maximum 8 images allowed.`);
      return;
    }
    
    fileArray.forEach((file) => {
      if (file.type.startsWith("image/")) {
        const image = new FileReader();
        image.onload = (e) => {
          const imageObject = {
            id: generateUniqueId(),
            src: e.target.result,
            file: file
          };
          imageSrcs.value.push(imageObject);
          emit("update-images", imageSrcs.value);
        };
        image.onerror = (error) => {
          console.error("Error reading file:", error);
          alert("There was an error reading the file. Please try again.");
        };
        if (file.size > 5 * 1024 * 1024) {
          alert("File is too large. Please upload images smaller than 5MB.");
        } else {
          image.readAsDataURL(file);
        }
      } else {
        alert("Please upload a valid image file.");
      }
    });
    
    // Reset the input value to allow re-selecting the same file
    event.target.value = '';
  }
};

const removeImage = (index) => {
  imageSrcs.value.splice(index, 1);
  emit("update-images", imageSrcs.value);
};
</script>

<style scoped>
.image-upload {
  text-align: center;
}
.image-preview {
  margin-top: 10px;
}
.image-preview img {
  max-width: 100%;
  height: auto;
}
</style>