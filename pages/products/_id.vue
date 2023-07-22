<template>
  <div class="lg:m-8 mb-20 md:m-5 md:mt-8 m-3 mt-5">
        <h1 class="text-2xl font-medium sm:visible max-sm:my-4 md:invisible">{{ product[main].title }}</h1>
        <div class="md:flex flex-row mb-5">
          <div class="md:flex md:flex-col md:mt-24 hidden">
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
          <div class="flex flex-col w-full justify-between md:flex-row">
              <div class="flex flex-col h-3/2 md:w-2/5 gap-6 md:mb-0 mb-8">
                
                <img  class="max-w-lg mx-auto w-full mb-8 h-full rounded-xl object-contain aspect-square"
                :src="product[main].image" />
                
                <div class="mx-auto flex sm:hidden mb-4">
                  <div
                    class="w-6 h-6 ring-4 ring-white lg:h-3.5 m-3 bg-black rounded-full"
                  ></div>
                  <div
                    class="w-6 h-6 ring-4 ring-gray-300 m-3 bg-blue-300 rounded-full"
                  ></div>
                  <div
                    class="w-6 h-6 ring-4 ring-white m-3 bg-green-300 rounded-full"
                  ></div>
                  <div
                    class="w-6 h-6 ring-4 ring-white m-3 bg-red-300 rounded-full"
                  ></div>
                </div>
  
                <div class="flex flex-row items-center justify-between gap-2">
                  <img
                    class="w-4 h-4 mr-2 my-auto"
                    src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQuwFYGl859TlHkUrVFmrAvNWAOtPby6ZgWMg&usqp=CAU"
                    @click="i > 0 ? i-- : (i = 11)"
                  />
                  <img
                    class="w-2/12 h-2/6 md:w-1/5 md:h-4/6 aspect-square object-contain rounded-md"
                    :src="product[i].image"
                  />
                  <img
                    class="w-2/12 h-2/6 md:w-1/5 md:h-4/6 aspect-square object-contain rounded-md"
                    :src="product[i + 1].image"
                  />
                  <img
                    class="w-2/12 h-2/6 md:w-1/5 md:h-4/6 aspect-square object-contain rounded-md"
                    :src="product[i + 2].image"
                  />
                  <img
                    class="w-2/12 h-2/6 md:w-1/5 md:h-4/6 aspect-square object-contain rounded-md"
                    :src="product[i + 3].image"
                  />
                  <img
                    class="w-4 h-4 ml-2 transform rotate-180 my-auto"
                    src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQuwFYGl859TlHkUrVFmrAvNWAOtPby6ZgWMg&usqp=CAU"
                    @click="i < 12 ? i++ : (i = 0)"
                  />
                </div>
              </div>
  
              <div class="mt-8 md:mt-0 lg:mt-16 flex flex-col md:mt-7 md:w-1/2">
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
                        class="rounded-full float-left bg-gray-100 text-gray-500 font-medium py-1 px-2 lg:text-sm text-xs flex flex-row lg:mr-4 md:mr-2 m-1"
                      >
                        <input
                          type="radio"
                          name="Size"
                          value="small"
                          class="peer/small"
                          id="small"
                          checked
                        /><label for="small" class="peer-checked"
                          ><p class="ml-1">Small</p></label
                        >
                      </div>
                      <div
                        class="rounded-full float-left bg-gray-100 text-gray-500 font-medium px-2 py-1 text-xs lg:text-sm flex flex-row lg:mr-4 md:mr-2 m-1"
                      >
                        <input
                          type="radio"
                          name="Size"
                          value="medium"
                          class="peer/medium"
                          id="medium"
                        /><label for="medium" class="peer-checked0"
                          ><p class="ml-1">Medium</p></label
                        >
                      </div>
                      <div
                        class="rounded-full float-left bg-gray-100 text-gray-500 py-1 px-2 font-medium text-xs lg:text-sm flex flex-row lg:mr-4 md:mr-2 m-1"
                      >
                        <input
                          type="radio"
                          name="Size"
                          value="large"
                          class="peer/large"
                          id="large"
                        /><label for="large" class="peer-checked"
                          ><p class="ml-1">Large</p></label
                        >
                      </div>
                      <div
                        class="rounded-full float-left bg-gray-100 text-gray-500 py-1 px-2 font-medium text-xs lg:text-sm flex flex-row lg:mr-4 md:mr-2 m-1"
                      >
                        <input
                          type="radio"
                          name="Size"
                          value="extra"
                          class="peer/extra"
                          id="extra"
                        /><label for="extra" class="peer-checked"
                          ><p class="ml-1">Extra Large</p></label
                        >
                      </div>
                      <div
                class="rounded-full float-left bg-gray-100 text-gray-500 py-1 px-2 font-medium text-xs lg:text-sm flex flex-row lg:mr-4 md:mr-2 m-1"
              >
                <input
                  type="radio"
                  name="Size"
                  value="XXL"
                  class="peer/XXL"
                  id="XXL"
                />
                <label for="XXL" class="peer-checked"><p class="ml-1">XXL</p></label
                >
                      </div>
                  </div>
                  
                  
                  <hr class="invisible md:visible md:h-px md:lg:my-8 md:my-5 md:bg-gray-300 md:border-0 md:dark:bg-gray-700 ">
                  <div class=" bg-white shadow-[0px_40px_70px_4px_rgba(0,0,0,0.56)] md:shadow-none md:border-0 m-0 justify-center md:justify-start w-full fixed bottom-0 mx-0 mb-0 flex flex-row md:justify-left sm:mb-0 md:relative gap-0s">
                    <button @click="addToCartClick(product[main])" class="  gap-0 md:mr-[15%] md:px-[7%] pl-[44%] mr-0  md:ml-0 text-center pr-0 md:py-0 min-w-[88%]  md:min-w-0 bg-white rounded-none font-black flex-none flex items-center  md:rounded-full md:bg-[#EA454C] flex flex-row md:py-2 md:px-3 md:font-normal">
                        <img class=" visible md:invisible w-4 h-3 mr-0  filter px-0" src="../../assets/cart01.png">
                        <img class=" invisible md:visible w-5 h-5 mr-0 md:mr-1 md:-ml-[15px] filter" src="../../assets/cart02.png">
                        <p class="flex-none text-[12px] md:text-[15px] text-center text-black md:text-white sm:text-xs pl-0 md:pl-0 ">Add To Cart</p>
                    </button>
                    <button class="pl-[15%] md:px-[7%] md:py-4 ml-0 py-3 md:py-0 min-w-[92%] text-center md:min-w-0 bg-[#EA454C] font-bold flex-none items-center rounded-none  rounded-full md:bg-[#EA454C] flex flex-row md:rounded-full md:font-normal py-1 sm:ml-3 md:mr-[0%]">
                        <img class="w-4 h-4 mr-1 filter" src="../../assets/lightning.png">
                        <p class=" text-[12px] md:text-[15px] pr-2 pl-2 text-white sm:text-xs">Buy Now</p>
                    </button>
                  </div>
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
  
  </div>
</template>
  
<script>
  //import { mapMutations } from 'vuex';
  export default {
    async asyncData({ params }) {
        const response = await fetch(`https://fakestoreapi.com/products/`);
        const product = await response.json();
        console.log(product);
        return {
            i: 0,
            main:1,
            product
        };
    },
    methods: {
      //...mapMutations(['addToCart']),
      addToCartClick(item) {
          this.$store.commit('addToCart',item);
          
          this.$toast.show('Added to Cart',{
            theme: "bubble", 
            position: "top-right", 
            duration : 2000,
            type:'success',
            iconPack:'material',
            icon : 'add_shopping_cart'
          })
           
      }
      /*
      requestColor {
        this.$toast.show('Please select the color',{
            theme: "bubble", 
            position: "top-right", 
            duration : 2000,
            type:'warning',
            iconPack:'material',
            icon : 'warning'
        })
      }
      requestSize {
        this.$toast.show('Please select the size',{
            theme: "bubble", 
            position: "top-right", 
            duration : 2000,
            type:'warning',
            iconPack:'material',
            icon : 'warning'
        })
      }

       */
    }
  }
</script>
  
  