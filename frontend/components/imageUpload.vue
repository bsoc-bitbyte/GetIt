<template>
  <div class="image-upload lg:w-1/3 h-[650px] md:w-1/2">
    <div
      v-if="imageSrcs.length === 0"
      class="w-full h-full bg-gray-100 rounded-2xl flex flex-col items-center justify-center p-4"
    >
      <label
        for="dropzone-file"
        class="flex flex-col items-center cursor-pointer w-1/2 max-w-xs"
      >
        <img src="../assets/addImage.svg" alt="uploadBtn" class="w-48 mb-2" />
        <input
          id="dropzone-file"
          type="file"
          @change="onFileChange"
          accept="image/*"
          class="hidden"
        />
        <span class="text-gray-600 text-center"
          >Click to upload a new image</span
        >
      </label>
    </div>

    <div
      v-if="imageSrcs.length === 1"
      class="w-full h-full rounded-2xl grid grid-cols-1 gap-2 p-4"
    >
      <div
        class="w-full overflow-hidden flex items-center justify-center bg-gray-100 rounded-lg"
      >
        <img
          :src="imageSrcs[0]"
          alt="Uploaded Image"
          class="w-auto h-full object-contain"
        />
      </div>
      <label
        for="dropzone-file"
        class="flex flex-col items-center cursor-pointer w-full bg-gray-100 rounded-lg p-4"
      >
        <img
          src="../assets/addImage.svg"
          alt="uploadBtn"
          class="max-w-28 max-h-28"
        />
        <input
          id="dropzone-file"
          type="file"
          @change="onFileChange"
          accept="image/*"
          class="hidden"
        />
        <span class="text-gray-600 text-center text-sm"
          >Click to upload a new image</span
        >
      </label>
    </div>

    <div
      v-if="imageSrcs.length === 2"
      class="w-full h-full rounded-2xl grid grid-rows-2 grid-cols-2 gap-2 p-4"
    >
      <div
        v-for="(src, index) in imageSrcs"
        :key="index"
        class="overflow-hidden flex items-center justify-center bg-gray-100 rounded-lg"
      >
        <img
          :src="src"
          alt="Uploaded Image"
          class="w-full h-full object-contain rounded-lg"
        />
      </div>
      <label
        for="dropzone-file"
        class="row-span-1 col-span-2 flex flex-col items-center justify-center cursor-pointer bg-gray-100 rounded-lg p-4"
      >
        <img
          src="../assets/addImage.svg"
          alt="uploadBtn"
          class="max-w-28 max-h-28 mb-2"
        />
        <input
          id="dropzone-file"
          type="file"
          @change="onFileChange"
          accept="image/*"
          class="hidden"
        />
        <span class="text-gray-600 text-center text-sm">
          Click to upload a new image
        </span>
      </label>
    </div>

    <div
      v-if="imageSrcs.length === 3"
      class="w-full h-full rounded-2xl grid grid-rows-2 grid-cols-2 gap-2 p-4"
    >
      <div
        v-for="(src, index) in imageSrcs"
        :key="index"
        class="overflow-hidden flex items-center justify-center bg-gray-100 rounded-lg"
      >
        <img
          :src="src"
          alt="Uploaded Image"
          class="w-full h-full object-contain rounded-lg"
        />
      </div>
      <label
        for="dropzone-file"
        class="row-span-1 col-span-1 flex flex-col items-center justify-center cursor-pointer bg-gray-100 rounded-lg p-4"
      >
        <img
          src="../assets/addImage.svg"
          alt="uploadBtn"
          class="max-w-28 max-h-28 mb-2"
        />
        <input
          id="dropzone-file"
          type="file"
          @change="onFileChange"
          accept="image/*"
          class="hidden"
        />
        <span class="text-gray-600 text-center text-sm">
          Click to upload a new image
        </span>
      </label>
    </div>

    <div
      v-if="imageSrcs.length === 4"
      class="w-full h-full rounded-2xl grid grid-rows-3 grid-cols-2 gap-2 p-4"
    >
      <div
        v-for="(src, index) in imageSrcs"
        :key="index"
        class="overflow-hidden flex items-center justify-center bg-gray-100 rounded-lg"
      >
        <img
          :src="src"
          alt="Uploaded Image"
          class="w-full h-full object-contain rounded-lg"
        />
      </div>
      <label
        for="dropzone-file"
        class="col-span-2 row-span-1 flex flex-col items-center justify-center cursor-pointer bg-gray-100 rounded-lg p-4"
      >
        <img
          src="../assets/addImage.svg"
          alt="uploadBtn"
          class="max-w-24 max-h-24 mb-2"
        />
        <input
          id="dropzone-file"
          type="file"
          @change="onFileChange"
          accept="image/*"
          class="hidden"
        />
        <span class="text-gray-600 text-center text-sm">
          Click to upload a new image
        </span>
      </label>
    </div>

    <div
      v-if="imageSrcs.length === 5"
      class="w-full h-full rounded-2xl grid grid-rows-3 grid-cols-2 gap-2 p-4"
    >
      <div
        v-for="(src, index) in imageSrcs"
        :key="index"
        class="overflow-hidden flex items-center justify-center bg-gray-100 rounded-lg"
      >
        <img
          :src="src"
          alt="Uploaded Image"
          class="w-full h-full object-contain rounded-lg"
        />
      </div>
      <label
        for="dropzone-file"
        class="row-span-1 col-span-1 flex flex-col items-center justify-center cursor-pointer bg-gray-100 rounded-lg p-4"
      >
        <img
          src="../assets/addImage.svg"
          alt="uploadBtn"
          class="max-w-28 max-h-28 mb-2"
        />
        <input
          id="dropzone-file"
          type="file"
          @change="onFileChange"
          accept="image/*"
          class="hidden"
        />
        <span class="text-gray-600 text-center text-sm">
          Click to upload a new image
        </span>
      </label>
    </div>

    <div
      v-if="imageSrcs.length > 5"
      class="w-full h-full rounded-2xl grid grid-rows-3 grid-cols-2 gap-2 p-4"
    >
      <div
        v-for="(src, index) in imageSrcs.slice(0, 4)"
        :key="index"
        class="overflow-hidden flex items-center justify-center bg-gray-100 rounded-lg"
      >
        <img
          :src="src"
          alt="Uploaded Image"
          class="w-full h-full object-contain rounded-lg"
        />
      </div>
      <div
        class="w-full overflow-hidden flex items-center justify-center bg-gray-100 rounded-lg"
      >
        <div class="absolute inset-0 bg-black opacity-50"></div>
        <span class="absolute z-10 text-white text-lg font-semibold">
          +{{ imageSrcs.length - 4 }} more
        </span>
        <img
          :src="imageSrcs[4]"
          alt="Uploaded Image"
          class="w-auto h-full object-contain blur-sm"
        />
      </div>
      <label
        for="dropzone-file"
        class="row-span-1 col-span-1 flex flex-col items-center justify-center cursor-pointer bg-gray-100 rounded-lg p-4"
      >
        <img
          src="../assets/addImage.svg"
          alt="uploadBtn"
          class="max-w-28 max-h-28 mb-2"
        />
        <input
          id="dropzone-file"
          type="file"
          @change="onFileChange"
          accept="image/*"
          class="hidden"
        />
        <span class="text-gray-600 text-center text-sm">
          Click to upload a new image
        </span>
      </label>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue';

const imageSrcs = ref([]);
const emit = defineEmits(["update-images"]);

const onFileChange = (event) => {
  const files = event.target.files;
  if (files.length) {
    const fileArray = Array.from(files);

    fileArray.forEach((file) => {
      if (file.type.startsWith("image/")) {
        const image = new FileReader();

        image.onload = (e) => {
          imageSrcs.value.push(e.target.result);
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
  } else {
    alert("No files selected.");
  }
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
