<template>
    <div class="flex group flex-col items-center bg-white rounded shadow relative transition-all overflow-clip">
        <div class="max-h-[350px] max-w-[350px] overflow-clip">
            <svg width="29" height="29" viewBox="0 0 29 29" fill="none"
                class="absolute z-30 left-2 top-2 opacity-0 transition-all group-hover:opacity-100"
                xmlns="http://www.w3.org/2000/svg">
                <circle cx="14.8203" cy="14.5" r="14" fill="white" />
                <path
                    d="M19.6203 19.3C20.0447 19.3 20.4516 19.4686 20.7517 19.7686C21.0517 20.0687 21.2203 20.4757 21.2203 20.9C21.2203 21.3243 21.0517 21.7313 20.7517 22.0314C20.4516 22.3314 20.0447 22.5 19.6203 22.5C19.196 22.5 18.789 22.3314 18.4889 22.0314C18.1889 21.7313 18.0203 21.3243 18.0203 20.9C18.0203 20.012 18.7323 19.3 19.6203 19.3ZM6.82031 6.5H9.43631L10.1883 8.1H22.0203C22.2325 8.1 22.436 8.18429 22.586 8.33431C22.736 8.48434 22.8203 8.68783 22.8203 8.9C22.8203 9.036 22.7803 9.172 22.7243 9.3L19.8603 14.476C19.5883 14.964 19.0603 15.3 18.4603 15.3H12.5003L11.7803 16.604L11.7563 16.7C11.7563 16.753 11.7774 16.8039 11.8149 16.8414C11.8524 16.8789 11.9033 16.9 11.9563 16.9H21.2203V18.5H11.6203C11.196 18.5 10.789 18.3314 10.4889 18.0314C10.1889 17.7313 10.0203 17.3243 10.0203 16.9C10.0203 16.62 10.0923 16.356 10.2123 16.132L11.3003 14.172L8.42031 8.1H6.82031V6.5ZM11.6203 19.3C12.0447 19.3 12.4516 19.4686 12.7517 19.7686C13.0517 20.0687 13.2203 20.4757 13.2203 20.9C13.2203 21.3243 13.0517 21.7313 12.7517 22.0314C12.4516 22.3314 12.0447 22.5 11.6203 22.5C11.196 22.5 10.789 22.3314 10.4889 22.0314C10.1889 21.7313 10.0203 21.3243 10.0203 20.9C10.0203 20.012 10.7323 19.3 11.6203 19.3ZM18.8203 13.7L21.0443 9.7H10.9323L12.8203 13.7H18.8203Z"
                    fill="#636364" fill-opacity="0.5" />
            </svg>
            <div class="absolute right-2 top-2 bg-white rounded-md py-1 px-2 text-[#9E3500] z-30">{{ type }}</div>
            <img :src="'https://s3-alpha-sig.figma.com/img/9838/788b/17de65d98211bea5b3eed9f863fc570a?Expires=1718582400&Key-Pair-Id=APKAQ4GOSFWCVNEHN3O4&Signature=oZBWA6vf-8Cr8OQzsop4kOVyVpuxmPcrRviebWY3gK-GUWMNPEvhd6jFLNW5~pMy6mvFK0tJ7ZZ~kU3a6UrhmKiiXiQUvwS2fBZv3F8hy8TnNAfEAtEQOlRvSDOA22ung8rhh1zsEC-CL6G28iUdmWWsbCVoPOelBH0vz2rEpfuOI~qPn0d5EuKYtONY7p3M5SWXOuS40vdeNybNASIrq2kHFawhfq-AOlowMu6FX6ad7BuTRpXQtqu18H-qiacXrsz1XsDqcAEjwpDTyTEYc4vWPwZpOkxqfzJIZ8XZQ0Hj7FMEEUs88RqJ0yuuA2wxf9qbDGvCeONxyLfsjhjVpw__'"
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
            <!-- <h2 class="text-xl font-bold mb-2">h</h2> -->
            <p class="text-black font-normal text-xs">{{ description }}</p>
            <div
                class="gap-4 bg-white w-full flex absolute opacity-0 group-hover:opacity-100 group-hover:delay-150 ease-in-out group-hover:duration-300 transition duration-75 -bottom-6 h-min">
                <div v-for="item in colors" :key="item"
                    class="opacity-0 group-hover:opacity-100 group-hover:delay-150 ease-in-out group-hover:duration-300 duration-75 transition w-5 h-5 rounded-full"
                    :style="{ background: '#496BC1' }"></div> |
                <div v-for="item in sizes" :key="item"
                    class="opacity-0 group-hover:opacity-100 group-hover:delay-150 ease-in-out group-hover:duration-300 duration-75 transition p-1 text-xs flex items-center justify-center rounded border-solid h-5 w-5 border-2 border-[##63636440] text-gray-500">
                    S</div>
            </div>
            <div
                class="gap-2 flex absolute opacity-0 group-hover:opacity-100 group-hover:delay-150 ease-in-out group-hover:duration-300 transition duration-75 -bottom-16 h-min">
                <div v-for="item in tags" :key="item"
                    class="opacity-0 group-hover:opacity-100 group-hover:delay-150 ease-in-out group-hover:duration-300 duration-75 transition p-2 text-xs flex items-center justify-center rounded border-solid h-6 border-2 border-[##63636440] text-gray-600">
                    Cotton</div>
            </div>
            <p class="text-gray-400 poppins font-light text-xs group-hover:hidden">2 shades | 4 sizes</p>
        </div>
    </div>
</template>

<script>
export default {
    props: {
        title: {
            type: String,
            required: false
        },
        type: {
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
            required: true
        },
        sizes: {
            type: Array,
            required: true
        },
        tags: {
            type: Array,
            required: true
        }
    },
    name: "MerchCard"
}
</script>

<style scoped>
.poppins {
    font-family: poppins, sans-serif;
    font-smooth: always;
}

</style>