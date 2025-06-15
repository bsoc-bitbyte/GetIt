<template>
  <div class="size-selector">
    <div class="label">Sizes</div>

    <div class="size-row">
      <div v-for="size in selectedSizes" :key="size" class="pill small">{{ size }}</div>

      <div class="add-button-container" @click="toggleDropdown">
        <div class="pill small add-circle">
          <svg class="plus-icon red" xmlns="http://www.w3.org/2000/svg" width="15" height="14" viewBox="0 0 15 14" fill="none">
            <path d="M13.0714 7.85714H8.42857V12.1429C8.42857 12.3702 8.33074 12.5882 8.1566 12.7489C7.98246 12.9097 7.74627 13 7.5 13C7.25373 13 7.01754 12.9097 6.8434 12.7489C6.66926 12.5882 6.57143 12.3702 6.57143 12.1429V7.85714H1.92857C1.6823 7.85714 1.44611 7.76684 1.27197 7.60609C1.09783 7.44535 1 7.22733 1 7C1 6.77267 1.09783 6.55465 1.27197 6.39391C1.44611 6.23316 1.6823 6.14286 1.92857 6.14286H6.57143V1.85714C6.57143 1.62981 6.66926 1.4118 6.8434 1.25105C7.01754 1.09031 7.25373 1 7.5 1C7.74627 1 7.98246 1.09031 8.1566 1.25105C8.33074 1.4118 8.42857 1.62981 8.42857 1.85714V6.14286H13.0714C13.3177 6.14286 13.5539 6.23316 13.728 6.39391C13.9022 6.55465 14 6.77267 14 7C14 7.22733 13.9022 7.44535 13.728 7.60609C13.5539 7.76684 13.3177 7.85714 13.0714 7.85714Z" fill="red" stroke="red"/>
          </svg>
        </div>
        <span class="add-label">Add</span>
      </div>
    </div>

    <div v-if="dropdownOpen" class="dropdown-wrapper">
      <svg class="dropdown-border" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 244" fill="none">
        <g filter="url(#filter0_d_1343_914)">
          <path d="M10 10H390V214C390 225.046 381.046 234 370 234H30C18.9543 234 10 225.046 10 214V10Z" fill="white"/>
          <path d="M389.5 10.5V214C389.5 224.77 380.77 233.5 370 233.5H30C19.2304 233.5 10.5 224.77 10.5 214V10.5H389.5Z" stroke="black"/>
        </g>
        <defs>
          <filter id="filter0_d_1343_914" x="0" y="0" width="400" height="244" filterUnits="userSpaceOnUse" color-interpolation-filters="sRGB">
            <feFlood flood-opacity="0" result="BackgroundImageFix"/>
            <feColorMatrix in="SourceAlpha" type="matrix" values="0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 127 0" result="hardAlpha"/>
            <feOffset/>
            <feGaussianBlur stdDeviation="5"/>
            <feComposite in2="hardAlpha" operator="out"/>
            <feColorMatrix type="matrix" values="0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0.1 0"/>
            <feBlend mode="normal" in2="BackgroundImageFix" result="effect1_dropShadow_1343_914"/>
            <feBlend mode="normal" in="SourceGraphic" in2="effect1_dropShadow_1343_914" result="shape"/>
          </filter>
        </defs>
      </svg>

      <div class="dropdown">
        <div class="size-grid">
          <div
            v-for="size in availableSizes"
            :key="size"
            :class="['pill', 'small', getPillClass(size)]"
            @click="handleSelect(size)"
          >
            {{ size }}
          </div>
        </div>

        <button class="add-btn" @click="addSizes">
          Add
          <svg class="plus-icon inverse" xmlns="http://www.w3.org/2000/svg" width="15" height="14" viewBox="0 0 15 14" fill="none">
            <path d="M13.0714 7.85714H8.42857V12.1429C8.42857 12.3702 8.33074 12.5882 8.1566 12.7489C7.98246 12.9097 7.74627 13 7.5 13C7.25373 13 7.01754 12.9097 6.8434 12.7489C6.66926 12.5882 6.57143 12.3702 6.57143 12.1429V7.85714H1.92857C1.6823 7.85714 1.44611 7.76684 1.27197 7.60609C1.09783 7.44535 1 7.22733 1 7C1 6.77267 1.09783 6.55465 1.27197 6.39391C1.44611 6.23316 1.6823 6.14286 1.92857 6.14286H6.57143V1.85714C6.57143 1.62981 6.66926 1.4118 6.8434 1.25105C7.01754 1.09031 7.25373 1 7.5 1C7.74627 1 7.98246 1.09031 8.1566 1.25105C8.33074 1.4118 8.42857 1.62981 8.42857 1.85714V6.14286H13.0714C13.3177 6.14286 13.5539 6.23316 13.728 6.39391C13.9022 6.55465 14 6.77267 14 7C14 7.22733 13.9022 7.44535 13.728 7.60609C13.5539 7.76684 13.3177 7.85714 13.0714 7.85714Z" fill="white" stroke="white"/>
          </svg>
        </button>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'

const props = defineProps({
  availableSizes: {
    type: Array,
    default: () => ['XXS', 'XS', 'S', 'M', 'L', 'XL', 'XXL', 'XXXL']
  },
  selectedSizes: {
    type: Array,
    default: () => []
  }
})

const emit = defineEmits(['update:selectedSizes'])

const dropdownOpen = ref(false)
const tempSelected = ref([])

const toggleDropdown = () => {
  dropdownOpen.value = !dropdownOpen.value
  tempSelected.value = []
}

const handleSelect = (size) => {
  if (props.selectedSizes.includes(size)) return
  if (tempSelected.value.includes(size)) {
    tempSelected.value = tempSelected.value.filter(s => s !== size)
  } else {
    tempSelected.value.push(size)
  }
}

const addSizes = () => {
  const newSizes = [...props.selectedSizes, ...tempSelected.value]
  emit('update:selectedSizes', newSizes)
  dropdownOpen.value = false
  tempSelected.value = []
}

const getPillClass = (size) => {
  if (props.selectedSizes.includes(size)) return 'disabled'
  if (tempSelected.value.includes(size)) return 'active'
  return ''
}
</script>

<style scoped>
.size-selector {
  width: 100%;
  max-width: 380px;
  font-family: 'Poppins', sans-serif;
  position: relative;
  padding: 1rem;
  box-sizing: border-box;
}

.label {
  font-size: 1.5rem;
  color: #6c6c6c;
  margin-bottom: 0.75rem;
}

.size-row {
  display: flex;
  flex-wrap: wrap;
  gap: 0.75rem;
  align-items: flex-start;
  margin-bottom: 0.5rem;
}

.pill {
  background: white;
  border-radius: 50%;
  box-shadow: 0 0 8px rgba(0, 0, 0, 0.1);
  font-weight: 500;
  color: #6c6c6c;
  display: flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
}

.pill.small {
  width: 38px;
  height: 38px;
  font-size: 0.875rem;
}

.add-button-container {
  display: flex;
  flex-direction: column;
  align-items: center;
  cursor: pointer;
}

.pill.add-circle {
  background: white;
  border-radius: 50%;
  width: 38px;
  height: 38px;
  display: flex;
  align-items: center;
  justify-content: center;
  box-shadow: 0 0 8px rgba(0, 0, 0, 0.1);
}

.add-label {
  font-size: 0.75rem;
  color: #6c6c6c;
  margin-top: 0.25rem;
  text-align: center;
}

.dropdown-wrapper {
  position: relative;
  width: 100%;
}

.dropdown-border {
  width: 100%;
  height: auto;
  display: block;
}

.dropdown {
  position: absolute;
  top: 10px;
  left: 0;
  width: 100%;
  padding: 1.25rem;
  box-sizing: border-box;
}

.size-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(38px, 1fr));
  gap: 0.75rem;
  justify-items: center;
  margin-bottom: 1.25rem;
}

.pill.active {
  border: 2px solid #ea454c;
}

.pill.disabled {
  opacity: 0.3;
  cursor: not-allowed;
}

.add-btn {
  background: #ea454c;
  color: white;
  border: none;
  padding: 0.5rem 1.25rem;
  border-radius: 5px;
  font-size: 1rem;
  font-weight: 700;
  display: flex;
  align-items: center;
  justify-content: center;
  margin: auto;
  cursor: pointer;
}

.add-btn .plus-icon.inverse {
  margin-left: 0.5rem;
  color: white;
}

@media (max-width: 480px) {
  .size-selector {
    padding: 0.75rem;
  }
  .pill.small {
    width: 34px;
    height: 34px;
    font-size: 0.75rem;
  }
  .label {
    font-size: 1.25rem;
  }
  .add-btn {
    width: 100%;
  }
  .pill.add-circle {
    width: 34px;
    height: 34px;
  }
}

.plus-icon {
  width: 15px;
  height: 14px;
  display: inline-block;
}

.plus-icon.red {
  fill: red;
  stroke: red;
}

.plus-icon.inverse {
  fill: white;
  stroke: white;
}
</style>