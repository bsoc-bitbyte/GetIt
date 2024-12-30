<template>
    <div class="flex group flex-col items-center bg-white rounded shadow relative transition-all overflow-clip max-w-[350px]">
        <div class="max-h-[350px] max-w-[350px] overflow-clip">
            <img width="29" height="29" src="../assets/cart.svg"
                class="absolute z-30 left-2 top-2 opacity-0 transition-all group-hover:opacity-100" />
            <div v-if="type!=''" class="absolute right-2 top-2 bg-white rounded-md py-1 px-2 text-[#9E3500] z-30 poppins  text-xs">{{ type }}</div>
            <img :src="imageUrl"
                alt="Merch Image" class="object-cover transition-all group-hover:scale-125 rounded-t">
        </div>
        <div
            class="hidden opacity-0 transition-all group-hover:opacity-100 w-full text-center text-white z-20 poppins group-hover:block -translate-y-24">
            View Product</div>
        <div
            class="absolute bottom-0 h-[50%] w-full bg-gradient-to-b from-transparent via-transparent to-black group-hover:-translate-y-36 transition-all">
        </div>
        <div
            class="relative flex flex-col z-20 justify-start w-full gap-2 bg-white pt-2 px-3 pb-5 transition-all group-hover:-translate-y-20">
            <div class="flex justify-between w-full text-base"><span class="text-[#9E3500] poppins font-bold">{{ seller
                    }}</span> <span class="poppins font-bold">₹{{ price }}</span></div>
            <p class="text-black font-normal text-xs poppins">{{ title }}</p>
            <div
                class=" gap-4 bg-white w-full flex absolute opacity-0 group-hover:opacity-100 group-hover:delay-150 ease-in-out group-hover:duration-300 transition duration-75 -bottom-6 h-min">
                <div v-for="item in colors" :key="item"
                    class="opacity-0 group-hover:opacity-100 group-hover:delay-150 ease-in-out group-hover:duration-300 duration-75 transition w-5 h-5 rounded-full"
                    :style="{ background: item }"></div> |
                <div v-for="item in sizes" :key="item"
                    class="poppinsopacity-0 group-hover:opacity-100 group-hover:delay-150 ease-in-out group-hover:duration-300 duration-75 transition p-1 text-xs flex items-center justify-center rounded border-solid h-5 w-5 border-2 border-[##63636440] text-gray-500">
                    {{ item }}</div>
            </div>
            <div
                class="gap-2 flex absolute opacity-0 group-hover:opacity-100 group-hover:delay-150 ease-in-out group-hover:duration-300 transition duration-75 -bottom-16 h-min">
                <div v-for="item in tags" :key="item"
                    class="poppins opacity-0 group-hover:opacity-100 group-hover:delay-150 ease-in-out group-hover:duration-300 duration-75 transition p-2 text-xs flex items-center justify-center rounded border-solid h-6 border-2 border-[##63636440] text-gray-600">
                    {{ item }}</div>
            </div>
            <p class="text-gray-400 poppins font-light text-xs group-hover:hidden">{{ colors.length }} shades | {{ sizes.length }} sizes</p>
        </div>
    </div>
</template>

<script>
export default {
    props: {
        title: {
            type: String,
            required: true
        },
        type: {
            type: String,
            required: false,
            default: ''
        },
        imageUrl: {
            type: String,
            required: true
        },
        seller: {
            type: String,
            required: true
        },
        price: {
            type: Number,
            required: true
        },
        description: {
            type: String,
            required: true
        },
        colors: {
            type: Array,
            required: true,
            default: () => []
        },
        sizes: {
            type: Array,
            required: true,
            default: () => []
        },
        tags: {
            type: Array,
            required: true,
            default: () => []
        }
    },
    name: "MerchCard",
}
</script>

<style scoped>
.poppins {
    font-family: "Poppins", sans-serif;
    font-smooth: always;
}
</style>