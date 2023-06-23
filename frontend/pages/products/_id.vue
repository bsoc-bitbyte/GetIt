<template>
    <div class="lg:m-8 mb-20 md:m-5 md:mt-8 m-3 mt-5">
        <h1 class="text-2xl font-medium sm:visible max-sm:my-4 md:invisible">{{ product[main].title }}</h1>
        <div class="md:flex flex-row mb-5">
            <div class="md:flex md:flex-col flex flex-row md:mt-24">
                <div
                    class="lg:w-3.5 lg:m-2.5 Lg:mt-20  ring-4 ring-white lg:h-3.5 md:w-2.5 md:h-2.5 md:m-1.5 h-3.5 w-3.5 m-3 bg-black rounded-full">
                </div>
                <div
                    class="lg:w-3.5 lg:m-2.5 lg:h-3.5 ring-4 ring-gray-300 md:w-2.5 md:h-2.5 md:m-1.5 h-3.5 w-3.5 m-3 bg-blue-300 rounded-full">
                </div>
                <div
                    class="lg:w-3.5 lg:m-2.5 lg:h-3.5 ring-4 ring-white md:w-2.5 md:h-2.5 md:m-1.5 h-3.5 w-3.5 m-3 bg-green-300 rounded-full">
                </div>
                <div
                    class="lg:w-3.5 lg:m-2.5 lg:h-3.5 ring-4 ring-white md:w-2.5 md:h-2.5 md:m-1.5 h-3.5 w-3.5 m-3 bg-red-300 rounded-full">
                </div>
            </div>
            <div class="flex flex-col md:w-1/2">
                <img class="ml-6 w-9/12 float-left rounded-xl mr-15" :src="product[main].image" />
                <div class="flex flex-row mt-6 mb-10 md:w-11/12 ml-4">
                    <img class="w-4 h-4 mr-2 lg:mt-12 md:mt-7 mt-8"
                        src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQuwFYGl859TlHkUrVFmrAvNWAOtPby6ZgWMg&usqp=CAU"
                        @click="i > 0 ? i-- : i = 11">
                    <img class="w-1/6  mr-4" :src="product[i].image">
                    <img class="w-1/6  mr-4" :src="product[i+1].image">
                    <img class="w-1/6  mr-4" :src="product[i+2].image">
                    <img class="w-1/6" :src="product[i+3].image">
                    <img class="w-4 h-4 ml-2 lg:mt-12 md:mt-7 transform rotate-180 mt-8"
                        src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQuwFYGl859TlHkUrVFmrAvNWAOtPby6ZgWMg&usqp=CAU"
                        @click="i < 12 ? i++ : i = 0">
                </div>
            </div>
            <div class="lg:mt-16 flex flex-col md:mt-7 md:w-1/2">
                <div class="flex flex-row">
                    <h1 class="lg:text-2xl lg:mr-20 md:font-medium lg:font-medium md:text-xl  mr-10">{{ product[main].title }}
                    </h1>
                    <img class="w-4 h-4 md:mt-2"
                        src="https://static.vecteezy.com/system/resources/thumbnails/001/505/003/small/share-icon-free-vector.jpg">
                </div>
                <p class="text-sm font-medium text-gray-400 mt-1 mb-2">TPC</p>
                <div class="text-xs font-medium flex flex-row">
                    <!---p class="flex flex-row">4.8
                    <div class="text-green-500 w-3 h-3 flex flex-row mb-2">&starf;</div>| 15 Ratings</p-->
                    <br>
                </div>
                <hr class="h-px  bg-gray-300 border-0 dark:bg-gray-700">


                <p class="lg:mt-7 lg:text-3xl font-medium mt-4 text-2xl"><b></b> ${{ product[main].price }}</p>
                <p class="lg:mt-5 text-sm text-gray-400 font-medium lg:mb-2 pb-.5 mt-4 mb-2">Choose a Size</p>
                <div class="">
                    <div
                        class="rounded-full float-left bg-gray-100 text-gray-500 font-medium py-1 px-2  text-xs flex flex-row lg:mr-4 md:mr-2 m-1">
                        <input type="radio" name="Size" value="Small" class="peer/small" id="Small"><label for="small"
                            class="peer-checked/small:text-pink-500">
                            <p class="ml-1">Small</p>
                        </label></div>
                    <div
                        class="rounded-full float-left bg-gray-100 text-gray-500 font-medium  px-2 py-1 text-xs flex flex-row lg:mr-4 md:mr-2 m-1">
                        <input type="radio" name="Size" value="Medium" class="peer/medium" id="Medium"><label for="medium"
                            class="peer-checked/medium:text-pink-500">
                            <p class="ml-1">Medium</p>
                        </label></div>
                    <div
                        class="rounded-full float-left bg-gray-100 text-gray-500 py-1 px-2 font-medium text-xs flex flex-row lg:mr-4 md:mr-2 m-1">
                        <input type="radio" name="Size" value="Large" class="peer/large" id="Large"><label for="large"
                            class="peer-checked/large:text-pink-500">
                            <p class="ml-1">Large</p>
                        </label></div>
                    <div
                        class="rounded-full float-left bg-gray-100 text-gray-500 py-1 px-2 font-medium text-xs flex flex-row lg:mr-4 md:mr-2 m-1">
                        <input type="radio" name="Size" value="Extra Large" class="peer/extra" id="Extra"><label for="extra"
                            class="peer-checked/extra:text-pink-500">
                            <p class="ml-1">Extra Large</p>
                        </label></div>
                    <div
                        class="rounded-full float-left bg-gray-100 text-gray-500 py-1 px-2 font-medium text-xs flex flex-row lg:mr-4 md:mr-2 m-1">
                        <input type="radio" name="Size" value="XXL" class="peer/xxl" id="XXL"><label for="xxl"
                            class="peer-checked/xxl:text-pink-500">
                            <p class="ml-1">XXL</p>
                        </label></div>
                </div>
                <hr class="h-px lg:my-8 my-5 bg-gray-300 border-0 dark:bg-gray-700">
                <div class="flex flex-row lg:mt-7 mt-1 sm:mb-5 content-center">
                    <button class="ml-3 rounded-full bg-rose-600 flex flex-row py-2 lg:px-12 lg:mr-5 px-6 mr-8 max-sm:ml-4"><img
                            class="w-4 h-4 mr-1 filter invert" src="https://cdn-icons-png.flaticon.com/512/711/711895.png">
                        <p class="text-xs text-white ">Add To Cart</p>
                    </button>
                    <button class="lg:ml-9  md:ml-5 rounded-full bg-rose-600 flex flex-row py-2 lg:px-14 px-8 sm:ml-3"><img
                            class="w-4 h-4 mr-1 filter invert"
                            src="https://icon-library.com/images/current-icon/current-icon-1.jpg">
                        <p class="text-xs text-white ">Buy Now</p>
                    </button>
                </div>
            </div>
        </div>

    <hr class="h-0.5 mt-12 bg-gray-300 border-0 dark:bg-gray-700">
    <div>

        <p class="lg:mt-3.5 mt-2"><b class="lg:text-2xl md:text-xl font-medium lg:mb-3 flex">Product Description</b><b
                class="font-medium md:text-xs lg:text-sm text-gray-400">{{ product[main].description }}</b> </p>
        <p class="lg:mt-3.5 md:mt-2"><b
                class="lg:text-2xl md:text-xl font-medium text-gray-700 mt-6 lg:mb-3 flex">Product Details</b><b
                class="font-medium md:text-xs lg:text-sm text-gray-400"> {{ product[main].category }}</b></p>
    </div>

</div></template>

<script>
export default {
    async asyncData({ params }) {
        const productId = params.id;
        const response = await fetch(`https://fakestoreapi.com/products/`);
        const product = await response.json();
        console.log(product);
        return {
            i: 0,
            main:1,
            product
        };
    },
}
</script>
