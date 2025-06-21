<template>
<div class="color-selector">
    <h3 class="header">Colours</h3>
    <div class="colors-container">
        <div v-for="(color, index) in customColors" :key="index" class="color-item">
            <div class="color-circle" :class="{ active: selectedColor === color.hex }" :style="{ backgroundColor: color.hex }" @click="selectColor(color.hex, color.name)" :title="color.name"></div>
            <span class="color-label">{{ color.name }}</span>
            <button @click="removeCustomColor(index)" class="remove-btn">×</button>
        </div>
        <div class="color-item">
            <div class="add-color-btn" @click="showColorPicker = !showColorPicker" :class="{ active: showColorPicker }">
                <span>+</span>
            </div>
            <span class="color-label">Add</span>
        </div>
    </div>
    <div v-if="showColorPicker" class="color-picker-modal">
        <div class="color-picker-content">
            <!-- Selected Color Preview -->
            <div class="color-preview">
                <div class="preview-circle" :style="{ backgroundColor: tempColor }"></div>
                <input v-model="colorName" type="text" placeholder="type name" class="color-name-input" />
            </div>

            <div class="format-toggle">
                <button :class="{ active: colorFormat === 'colorful' }" @click="colorFormat = 'colorful'" class="format-btn colorful">
                    Colourful
                </button>
                <button :class="{ active: colorFormat === 'grey' }" @click="colorFormat = 'grey'" class="format-btn grey">
                    Grey
                </button>
            </div>

            <div class="color-picker-area">
                <div v-if="colorFormat === 'colorful'" class="hue-slider-container">
                    <input type="range" min="0" max="360" v-model="hue" class="hue-slider" @input="updateColorFromHSL" />
                </div>

                <div class="shade-slider-container">
                    <span class="shade-label">{{ colorFormat === 'grey' ? 'Grey' : 'Lightness' }}</span>
                    <div class="shade-endpoints">
                        <div class="shade-dark" :style="{ backgroundColor: getDarkShade() }"></div>
                        <input type="range" min="0" max="100" v-model="lightness" class="shade-slider" :style="{ background: getSliderBackground() }" @input="updateColorFromHSL" />
                        <div class="shade-light" :style="{ backgroundColor: getLightShade() }"></div>
                    </div>
                </div>
            </div>

            <div class="hex-input">
                <input v-model="hexInput" type="text" placeholder="#FFFFFF" @input="updateColorFromHex" class="hex-field" />
            </div>

            <div class="modal-actions">
                <button @click="showColorPicker = false" class="cancel-btn">
                    Cancel
                </button>
                <button @click="addColor" class="add-btn" :disabled="!colorName.trim()">
                    Add +
                </button>
            </div>
        </div>
    </div>
</div>
</template>

<script>
export default {
    name: 'ColorSelector',
    props: {
        modelValue: {
            type: String,
            default: ''
        }
    },
    emits: ['update:modelValue', 'colorSelected'],
    data() {
        return {
            selectedColor: this.modelValue,
            showColorPicker: false,
            colorFormat: 'colorful',
            colorName: '',
            tempColor: '#ff6b35',
            hue: 15,
            saturation: 100,
            lightness: 60,
            hexInput: '#ff6b35',
            customColors: [],
            previousSaturation: 100
        }
    },
    watch: {
        modelValue(newVal) {
            this.selectedColor = newVal;
        },
        colorFormat(newFormat) {
            if (newFormat === 'grey') {
                if (this.saturation > 0) {
                    this.previousSaturation = this.saturation;
                }
                this.saturation = 0;
            } else {
                this.saturation = this.previousSaturation || 100;
            }
            this.updateColorFromHSL();
        }
    },
    methods: {
        selectColor(hex, name) {
            this.selectedColor = hex;
            this.$emit('update:modelValue', hex);
            this.$emit('colorSelected', {
                hex,
                name
            });
        },

        updateColorFromHSL() {
            const h = this.hue / 360;
            const s = this.saturation / 100;
            const l = this.lightness / 100;

            const hex = this.hslToHex(h, s, l);
            this.tempColor = hex;
            this.hexInput = hex;
        },

        updateColorFromHex() {
            if (this.isValidHex(this.hexInput)) {
                this.tempColor = this.hexInput;
                const hsl = this.hexToHsl(this.hexInput);
                this.hue = Math.round(hsl.h * 360);
                this.saturation = Math.round(hsl.s * 100);
                this.lightness = Math.round(hsl.l * 100);

                if (hsl.s === 0) {
                    this.colorFormat = 'grey';
                } else {
                    this.colorFormat = 'colorful';
                    this.previousSaturation = this.saturation;
                }
            }
        },

        addColor() {
            if (this.colorName.trim()) {
                const newColor = {
                    name: this.colorName.trim(),
                    hex: this.tempColor
                };
                this.customColors.push(newColor);
                this.selectColor(this.tempColor, this.colorName.trim());
                this.colorName = '';
                this.showColorPicker = false;
            }
        },

        removeCustomColor(index) {
            this.customColors.splice(index, 1);
        },

        getDarkShade() {
            if (this.colorFormat === 'grey') {
                return '#000000';
            }
            const h = this.hue / 360;
            const s = this.saturation / 100;
            return this.hslToHex(h, s, 0);
        },

        getLightShade() {
            if (this.colorFormat === 'grey') {
                return '#ffffff';
            }
            const h = this.hue / 360;
            const s = this.saturation / 100;
            return this.hslToHex(h, s, 1);
        },

        getSliderBackground() {
            if (this.colorFormat === 'grey') {
                return 'linear-gradient(to right, #000, #fff)';
            } else {
                const h = this.hue / 360;
                const s = this.saturation / 100;
                const darkColor = this.hslToHex(h, s, 0);
                const lightColor = this.hslToHex(h, s, 1);
                return `linear-gradient(to right, ${darkColor}, ${lightColor})`;
            }
        },

        hslToHex(h, s, l) {
            const c = (1 - Math.abs(2 * l - 1)) * s;
            const x = c * (1 - Math.abs((h * 6) % 2 - 1));
            const m = l - c / 2;
            let r = 0,
                g = 0,
                b = 0;

            if (0 <= h && h < 1 / 6) {
                r = c;
                g = x;
                b = 0;
            } else if (1 / 6 <= h && h < 1 / 3) {
                r = x;
                g = c;
                b = 0;
            } else if (1 / 3 <= h && h < 1 / 2) {
                r = 0;
                g = c;
                b = x;
            } else if (1 / 2 <= h && h < 2 / 3) {
                r = 0;
                g = x;
                b = c;
            } else if (2 / 3 <= h && h < 5 / 6) {
                r = x;
                g = 0;
                b = c;
            } else if (5 / 6 <= h && h < 1) {
                r = c;
                g = 0;
                b = x;
            }

            r = Math.round((r + m) * 255);
            g = Math.round((g + m) * 255);
            b = Math.round((b + m) * 255);

            return "#" + ((1 << 24) + (r << 16) + (g << 8) + b).toString(16).slice(1);
        },

        hexToHsl(hex) {
            const r = parseInt(hex.slice(1, 3), 16) / 255;
            const g = parseInt(hex.slice(3, 5), 16) / 255;
            const b = parseInt(hex.slice(5, 7), 16) / 255;

            const max = Math.max(r, g, b);
            const min = Math.min(r, g, b);
            let h, s, l = (max + min) / 2;

            if (max === min) {
                h = s = 0;
            } else {
                const d = max - min;
                s = l > 0.5 ? d / (2 - max - min) : d / (max + min);
                switch (max) {
                    case r:
                        h = (g - b) / d + (g < b ? 6 : 0);
                        break;
                    case g:
                        h = (b - r) / d + 2;
                        break;
                    case b:
                        h = (r - g) / d + 4;
                        break;
                }
                h /= 6;
            }

            return {
                h,
                s,
                l
            };
        },

        isValidHex(hex) {
            return /^#[0-9A-F]{6}$/i.test(hex);
        }
    }
}
</script>

<style scoped>
.color-selector {
    max-width: 500px;
    top: 10px;
    left: 500px;
    font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
    position: fixed;
}

.header {
    font-size: 18px;
    font-weight: 500;
    color: #333;
    margin-bottom: 16px;
}

.colors-container {
    display: flex;
    flex-wrap: wrap;
    gap: 16px;
    margin-bottom: 20px;
    align-items: flex-start;
}

.color-item {
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 8px;
    position: relative;
}

.color-circle {
    width: 50px;
    height: 50px;
    border-radius: 50%;
    cursor: pointer;
    border: 3px solid transparent;
    transition: all 0.2s ease;
    position: relative;
}

.color-circle:hover {
    transform: scale(1.1);
}

.color-circle.active {
    border-color: #007AFF;
    box-shadow: 0 0 0 2px rgba(0, 122, 255, 0.2);
}

.add-color-btn {
    width: 50px;
    height: 50px;
    border-radius: 50%;
    border: 2px dashed #ccc;
    display: flex;
    align-items: center;
    justify-content: center;
    cursor: pointer;
    color: #666;
    font-size: 24px;
    transition: all 0.2s ease;
    background: white;
}

.add-color-btn:hover,
.add-color-btn.active {
    border-color: #ff0000;
    color: #ff0000;
}

.color-label {
    font-size: 12px;
    color: #666;
    text-align: center;
    max-width: 60px;
    overflow: hidden;
    text-overflow: ellipsis;
    white-space: nowrap;
}

.remove-btn {
    position: absolute;
    top: -5px;
    right: -5px;
    width: 20px;
    height: 20px;
    border: none;
    background: rgb(255, 253, 253);
    color: rgb(19, 17, 17);
    border-radius: 50%;
    cursor: pointer;
    font-size: 12px;
    display: flex;
    align-items: center;
    justify-content: center;
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.2);
}

.remove-btn:hover {
    background: rgb(255, 23, 23);
}

.color-picker-modal {
    position: relative;
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;
    display: flex;
    align-items: center;
    justify-content: center;
    z-index: 1000;
    border: 2px solid #000;
}

.color-picker-content {
    background: white;
    padding: 24px;
    border-radius: 12px;
    width: 320px;
    box-shadow: 0 8px 32px rgba(0, 0, 0, 0.2)
  }

.color-preview {
    display: flex;
    align-items: center;
    gap: 12px;
    margin-bottom: 20px;
}

.preview-circle {
    width: 40px;
    height: 40px;
    border-radius: 50%;
    border: 1px solid #ddd;
}

.color-name-input {
    flex: 1;
    padding: 8px 12px;
    border: 1px solid #ddd;
    border-radius: 6px;
    font-size: 14px;
}

.format-toggle {
    display: flex;
    gap: 8px;
    margin-bottom: 20px;
}

.format-btn {
    flex: 1;
    padding: 8px 16px;
    border: 1px solid #ddd;
    border-radius: 6px;
    background: white;
    cursor: pointer;
    font-size: 14px;
    transition: all 0.2s ease;
}

.format-btn.active.colorful {
    background: #ff4757;
    color: white;
    border-color: #ff4757;
}

.format-btn.active.grey {
    background: #666;
    color: white;
    border-color: #666;
}

.color-picker-area {
    margin-bottom: 20px;
}

.hue-slider-container {
    margin-bottom: 16px;
}

.hue-slider {
    width: 100%;
    height: 20px;
    border-radius: 10px;
    background: linear-gradient(to right,
            #ff0000 0%,
            #ffff00 17%,
            #00ff00 33%,
            #00ffff 50%,
            #0000ff 67%,
            #ff00ff 83%,
            #ff0000 100%);
    appearance: none;
    cursor: pointer;
}

.hue-slider::-webkit-slider-thumb {
    appearance: none;
    width: 20px;
    height: 20px;
    border-radius: 50%;
    background: white;
    border: 2px solid #333;
    cursor: pointer;
}

.shade-slider-container {
    display: flex;
    align-items: center;
    gap: 12px;
}

.shade-label {
    font-size: 14px;
    color: #666;
    min-width: 50px;
}

.shade-endpoints {
    display: flex;
    align-items: center;
    gap: 8px;
    flex: 1;
}

.shade-dark {
    width: 16px;
    height: 16px;
    border-radius: 50%;
    background: #000;
}

.shade-light {
    width: 16px;
    height: 16px;
    border-radius: 50%;
    background: #fff;
    border: 1px solid #ddd;
}

.shade-slider {
    flex: 1;
    height: 6px;
    border-radius: 3px;
    appearance: none;
    cursor: pointer;
}

.shade-slider::-webkit-slider-thumb {
    appearance: none;
    width: 16px;
    height: 16px;
    border-radius: 50%;
    background: white;
    border: 2px solid #333;
    cursor: pointer;
}

.hex-input {
    margin-bottom: 20px;
}

.hex-field {
    width: 100%;
    padding: 8px 12px;
    border: 1px solid #ddd;
    border-radius: 6px;
    font-size: 14px;
    font-family: monospace;
}

.modal-actions {
    display: flex;
    gap: 12px;
}

.cancel-btn {
    flex: 1;
    padding: 12px;
    background: white;
    color: #666;
    border: 1px solid #ddd;
    border-radius: 6px;
    font-size: 16px;
    font-weight: 500;
    cursor: pointer;
    transition: all 0.2s ease;
}

.cancel-btn:hover {
    background: rgb(230, 45, 45);
}

.add-btn {
    flex: 1;
    padding: 12px;
    background: #ff4757;
    color: white;
    border: none;
    border-radius: 6px;
    font-size: 16px;
    font-weight: 500;
    cursor: pointer;
    transition: background 0.2s ease;
}

.add-btn:hover:not(:disabled) {
    background: #ff3742;
}

.add-btn:disabled {
    background: #ccc;
    cursor: not-allowed;
}
</style>