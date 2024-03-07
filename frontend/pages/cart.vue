<template >
    <!-- <div class="main h-full flex flex-col md:flex-row items-start justify-center bg-white-100 mt-3 lg:mt-0 xl:mt-8 m-4 lg:m-10 xl:m-16">

        <div class="cart flex flex-col h-auto w-auto lg:w-[35rem] xl:w-[35rem] bg-white-100 items-center justify-center md:items-start">
            
            <div v-if="$store.state.cart.length > 0">
                <div class="flex w-full lg:w-[30rem] xl:w-[35rem] " >
                    <h3 class="font-Poppins text-xl font-bold pl-0 px-1 mt-[1rem]">Shopping Cart</h3>
                </div>
                <p>You have {{ nofItems}} in your cart. You can checkout now </p>
                <div class="products flex justify-center h-full w-full"
                    v-for="item in $store.state.cart" :key="item.pid">
                
                <div id="selected_prod1" class=" h-auto w-auto lg:w-[30rem] xl:w-[35rem] flex  border-2 item_1 rounded-lg mt-8 sm:px-0" >

                    <div class="image_div flex items-center justify-center"> 

                        <img :src="item.cover_image" alt="Image description" class="w-24 lg:w-28 lg:h-28 lg:mx-2 mx-1 h-24 object-cover">

                    </div>

                    <div class="prod_Description w-40 px-1 lg:w-60 h-32 mt-3 flex-col sm-35">

                        <h3 id="prod_Name" class="font-Poppins text-lg font-semibold leading-6 line-clamp-3" style="color: #271819;">{{ item.title }}</h3>
                        <h4 id="prod_Price" class="font-Mulish text-lg font-bold leading-6" style="color: #C3C6C9;">₹ {{ item.totalPrice}}</h4>
                        <p id="prod_Size" class="font-Mulish text-base lg:text-sm  leading-6 lg:leading-8" style="color: #271819;">{{item.location}}</p>

                    </div>

                    <div class="Quantity flex justify-evenly w-28 lg:w-32 lg:ml-10 h-28 mt-7 ">

                        <button @click="decreaseQ(item)" class="flex items-center justify-cente p-2 w-7 h-8 mt-10 text-black text-center rounded-lg border-2 " style="background-color: #EEF1F4;">-</button>

                        <p id="count" class="flex items-center justify-cente p-2 h-8 mt-10 sm:w-4 " style="color: #C3C6C9; "> {{ item.quantity }} </p>

                        <button @click="increaseQ(item)" class="flex items-center justify-cente p-2 w-8 h-8 mt-10 text-black rounded-lg border-2 "  style="background-color: #EEF1F4;">+</button>

                    </div>

                    <div class="close_btn flex-row justify-end w-5 md:w-8 sm:w-2">
                        <button @click.prevent="removeFromCart(item)" class="flex-row justify-end ml-0  mt-2">X</button>
                    </div>

                </div>
                </div>
            </div>
            <div v-else class="navbar-dropdown is-boxed is-right h-full w-full">
                <div class="flex w-full md: lg:w-[30rem] xl:w-[35rem] " >
                    <h3 class="font-Poppins text-xl font-bold pl-0 px-1 mt-[1rem]">Shopping Cart</h3>
                </div>
                <p>Your Cart is Empty. Take a look on our awesome products and add them to your cart</p>
            </div>
            

        </div>

        <div class="billing h-full w-full flex flex-col  items-center justify-center">

            <div class="girl_img w-0 md:w-full h-1/2 flex items-center justify-center ">

                <img class="h-full block w-60 lg:w-3/5 xl:w-[19rem]" src="../assets/cart_girl.png">

            </div>

            <div class="Bill flex items-center justify-center w-full h-70 bg-white-100 mt-16"> 

                <div class="h-full border-2 bg-white-100 w-[25rem] md:w-[20rem] lg:w-[24rem] xl:w-[26.75rem]"> 
                    <div class="flex">
                        <h3 class="font-medium md:font-extrabold text-2xl h-1/6 w-1/2 my-2 mt-6 ml-8 text-black font-Poppins " style="font-family: Poppins; font-style: normal; line-height: normal; letter-spacing: 0.04125rem;">Subtotal :</h3>
                        <div class="font-Mulish text-lg text-[#81858b] md:text-[#C3C6C9] text-center w-1/2 font-bold leading-6 ml-35 mt-6">₹{{ $store.getters['getPrice'] }}</div>
                    </div>
                    <hr class="w-11/12 ml-2">
                    <div class="flex"> 
                        <h3 class="font-medium md:font-extrabold text-2xl h-1/6 w-1/2 my-2 mt-6 ml-8 text-black font-Poppins " style="font-family: Poppins; font-style: 
                        normal; line-height: normal; letter-spacing: 0.04125rem;">Discount :</h3>
                        <div class="font-Mulish text-lg text-[#81858b] md:text-[#C3C6C9] text-center w-1/2 font-bold leading-6 ml-35 mt-6"> ₹0</div>
                    </div>
                    <hr class="w-11/12 ml-2">
                    <div class="flex"> 
                        <h3 class="font-medium md:font-extrabold text-2xl h-1/6 my-2 w-1/2 mt-6 ml-8 text-black font-Poppins " style="font-family: Poppins; font-style: normal; line-height: normal; letter-spacing: 0.04125rem;">Dilevery fee:</h3>
                        <div class="font-Mulish text-lg text-[#81858b] md:text-[#C3C6C9] text-center w-1/2 font-bold leading-6 ml-35 mt-6"> ₹0</div>
                    </div>
                    <hr class="w-11/12 ml-2">
                    <div class="flex"> 
                        <h3 class="font-medium md:font-extrabold text-2xl h-1/6 w-1/2 my-2 mt-6 ml-8 text-black font-Poppins " style="font-family: Poppins; font-style: normal; line-height: normal; letter-spacing: 0.04125rem;">Total :</h3>
                        <div class="font-Mulish text-lg text-[#81858b] md:text-[#C3C6C9] text-center w-1/2 font-bold leading-6 ml-35 mt-6"> ₹{{ $store.getters['getPrice'] }}</div>
                    </div>    
                </div>

            </div>

            <div class="Checkout button flex items-center justify-center text-center text-white w-full mt-8">

                <nuxt-link :to="this.$store.state.cart.length > 0 ? '/checkOut' : ''" class="checkout_Btn p-2 py-4 rounded-lg font-medium text-lg w-[25.3rem] md:w-[20rem] lg:w-[24rem] xl:w-[26.75rem]" style="font-family: Poppins; font-style: normal; letter-spacing: 0.03rem; background-color: #EA454C; height: 3.45813rem;">Checkout</nuxt-link>

            </div>
        </div>

    </div> -->
<!-- <div class="flex flex-row justify-between"> -->
<section class="h-screen  py-12 sm:py-16 lg:py-20 scale-110">
  <div class="mx-auto px-4 sm:px-6 lg:px-8 flex flex-row">
    <div class="mx-auto mt-8 max-w-2xl md:mt-12">
      <div class="bg-white shadow">
        <div class="px-4 py-6 sm:px-8 sm:py-10">
          <div class="flow-root">
            <ul class="-my-8" v-for="item in $store.state.cart" :key="item.pid">
              <li class="flex flex-col space-y-3 py-6 text-left sm:flex-row sm:space-x-5 sm:space-y-0">
                <div class="shrink-0">
                  <img class="h-24 w-24 max-w-full rounded-lg object-cover" :src="item.cover_image" alt="" />
                </div>

                <div class="relative flex flex-1 flex-col justify-between">
                  <div class="sm:col-gap-5 sm:grid sm:grid-cols-2">
                    <div class="pr-8 sm:pr-5">
                      <p class="text-base font-semibold text-gray-700">{{ item.title }}</p>
                      <p class="mx-0 mt-1 mb-0 text-sm text-gray-400">{{ item.location }}</p>
                    </div>

                    <div class="mt-4 flex items-end justify-between sm:mt-0 sm:items-start sm:justify-end">
                      <p class="shrink-0 w-20 text-base font-semibold text-gray-700 sm:order-2 sm:ml-8 sm:text-right">${{ item.totalPrice }}</p>

                      <div class="sm:order-1">
                        <div class="mx-auto flex h-8 items-stretch text-gray-600">
                          <button @click="decreaseQ(item)" class="flex items-center justify-center rounded-l-md bg-gray-200 px-4 transition hover:bg-black hover:text-white">-</button>
                          <div class="flex w-full items-center justify-center bg-gray-100 px-4 text-xs uppercase transition">{{ item.quantity }} </div>
                          <button @click="increaseQ(item)" class="flex items-center justify-center rounded-r-md bg-gray-200 px-4 transition hover:bg-black hover:text-white">+</button>
                        </div>
                      </div>
                    </div>
                  </div>

                  <div class="absolute top-0 right-0 flex sm:bottom-0 sm:top-auto">
                    <button @click.prevent="removeFromCart(item)" type="button" class="flex rounded p-2 text-center text-gray-500 transition-all duration-200 ease-in-out focus:shadow hover:text-gray-700">
                      <svg  class="h-5 w-5" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12" class=""></path>
                      </svg>
                    </button>
                  </div>
                </div>
              </li> 
            </ul>
          </div>

          <div class="mt-6 border-t border-b py-2">
            <div class="flex items-center justify-between">
              <p class="text-sm text-gray-400">Subtotal</p>
              <p class="text-lg font-semibold text-gray-700">₹{{ $store.getters['getPrice'] }}</p>
            </div>
            <div class="flex items-center justify-between">
              <p class="text-sm text-gray-400">Shipping</p>
              <p class="text-lg font-semibold text-gray-700">₹ 0 </p>
            </div>
          </div>
          <div class="mt-6 flex items-center justify-between">
            <p class="text-sm font-medium text-gray-700">Total</p>
            <p class="text-2xl font-semibold text-gray-700"><span class="text-xs font-normal text-gray-400">RS</span>{{ $store.getters['getPrice'] }}</p>
          </div>

          <div class="mt-6 text-center">
            <button type="button" class="group inline-flex w-full items-center justify-center rounded-md bg-[#EA454C] px-6 py-4 text-lg font-semibold text-white transition-all duration-200 ease-in-out focus:shadow">
              Checkout
              <svg xmlns="http://www.w3.org/2000/svg" class="group-hover:ml-8 ml-4 h-6 w-6 transition-all" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2">
                <path stroke-linecap="round" stroke-linejoin="round" d="M13 7l5 5m0 0l-5 5m5-5H6" />
              </svg>
            </button>
          </div>
        </div>
      </div>
    </div>
    
  </div>
  
</section>
<!-- <div class="h-screen  py-12 mt-5 sm:py-16 lg:py-20 ">
    <img class="h-[50vh] px-32 hidden " src="../assets/cart_girl.png">
</div>
</div> -->
</template>

<script>
    export default {
        name:'cart',
        computed : {
            nofItems() {
                if(this.$store.state.cart.length===1) {
                    let tempItems=this.$store.state.cart.length+" item";
                    return tempItems;
                } else if(this.$store.state.cart.length>1) {
                    let tempItems=this.$store.state.cart.length+" items";
                    return tempItems;
                }
            }
        },
        methods: {
            removeFromCart(item) {
                this.$store.commit('removeFromCart', item);
            },           
            decreaseQ(item){
                if(item.quantity===1) {
                    this.$store.commit('removeFromCart', item);
                } else if(item.quantity>1) {
                    this.$store.commit('decreaseQuantity', item);
                }
            },
            increaseQ(item){
                this.$store.commit('increaseQuantity', item);
            } 
        }
  }
</script>

