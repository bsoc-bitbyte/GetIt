<template>
  <div class="color-selector">
    <h2 class="title">Colours</h2>
    <div class="color-list">
      <span v-for="(color, idx) in colors" :key="'color_' + idx" class="color-item" :style="{backgroundColor: color}">
        <span v-if="isHex(color)" class="color-circle"></span>
        <span v-else class="color-name">{{ color }}</span>
        <button class="remove-btn" @click="removeColor(idx)">×</button>
      </span>
      <button class="add-btn" @click="toggleDropdown">+</button>
    </div>
    
    <div v-if="dropdownOpen" class="dropdown">
      <input v-model="inputColor" placeholder="Enter hex code or color name" @keyup.enter="addColor" class="color-input" />
      <button class="confirm-btn" @click="addColor">Add</button>
      <div v-if="error" class="error">{{ error }}</div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'ColorSelector',
  props: {
    colors: {
      type: Array,
      required: true
    }
  },
  data() {
    return {
      dropdownOpen: false,
      inputColor: '',
      error: ''
    };
  },
  methods: {
    toggleDropdown() {
      this.dropdownOpen = !this.dropdownOpen;
      this.inputColor = '';
      this.error = '';
    },
    isHex(val) {
      return /^#([0-9A-Fa-f]{6}|[0-9A-Fa-f]{3})$/.test(val);
    },
    isColorName(val) {
      const tempElement = document.createElement('div');
      tempElement.style.color = val;
      return tempElement.style.color !== '' || val.toLowerCase() === 'transparent';
    },
    addColor() {
      const val = this.inputColor.trim();
      if (!val) {
        this.error = 'Please enter a color';
        return;
      }
      if (!this.isHex(val) && !this.isColorName(val)) {
        this.error = 'Enter a valid hex code or color name';
        return;
      }
      if (this.colors.includes(val)) {
        this.error = 'Color already added';
        return;
      }
      this.$emit('update', [...this.colors, val]);
      this.inputColor = '';
      this.error = '';
      this.dropdownOpen = false;
    },
    removeColor(idx) {
      const updated = [...this.colors];
      updated.splice(idx, 1);
      this.$emit('update', updated);
    }
  }
};
</script>

<style scoped>
.color-selector {
  display: flex;
  flex-direction: column;
  gap: 20px;
  max-width: 500px; 
  /* margin: 0 auto;
  padding: 40px;
  background: #f8f9fa;
  min-height: 100vh; */
}

.title {
  font-size: 36px;
  font-weight: 300;
  color: #333;
  margin: 0 0 30px 0;
  text-align: left;
}

.color-list {
  display: flex;
  align-items: center;
  gap: 20px;
  flex-wrap: wrap;
}

.color-item {
  position: relative;
  display: flex;
  align-items: center;
  justify-content: center;
  width: 80px;
  height: 80px;
  border-radius: 50%;
  border: none;
  font-size: 14px;
  color: #666;
  cursor: pointer;
  flex-shrink: 0;
}

.color-circle {
  display: inline-block;
  width: 80px;
  height: 80px;
  border-radius: 50%;
  border: 0.5px solid #415a77;
}

.color-name {
  font-weight: 500;
  color: #666;
  font-size: 14px;
  text-align: center;
}

.remove-btn {
  position: absolute;
  top: -5px;
  right: -5px;
  background: #ff4444;
  border: 1px solid #aa0000;
  border-radius: 50%;
  width: 20px;
  height: 20px;
  font-size: 12px;
  color: #fff;
  cursor: pointer;
  display: none;
}

.color-item:hover .remove-btn {
  display: flex;
  align-items: center;
  justify-content: center;
}

.add-btn {
  background: transparent;
  border: 2px dashed #ccc;
  border-radius: 50%;
  width: 80px;
  height: 80px;
  font-size: 24px;
  color: #ff6b6b;
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: center;
  transition: all 0.2s;
  flex-shrink: 0;
}

.add-btn:hover {
  border-color: #ff6b6b;

}

.dropdown {
  display: flex;
  align-items: center;
  gap: 10px;
  margin-top: 10px;
}

.color-input {
  padding: 8px 12px;
  border: 1px solid #ccc;
  border-radius: 6px;
  font-size: 14px;
  flex: 1;
}

.confirm-btn {
  background: #007bff;
  color: white;
  border: none;
  border-radius: 6px;
  padding: 8px 16px;
  cursor: pointer;
  font-size: 14px;
}

.confirm-btn:hover {
  background: #0056b3;
}

.error {
  color: #dc3545;
  font-size: 12px;
  margin-left: 8px;
}
</style>