<template>
    <div class="main h-full flex flex-col md:flex-row items-start justify-center bg-white-100 mt-3 lg:mt-0 xl:mt-8 m-4 lg:m-10 xl:m-16">

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
                        <div class="font-Mulish text-lg text-[#81858b] md:text-[#C3C6C9] text-center w-1/2 font-bold leading-6 ml-35 mt-6"> 900₹</div>
                    </div>
                    <hr class="w-11/12 ml-2">
                    <div class="flex"> 
                        <h3 class="font-medium md:font-extrabold text-2xl h-1/6 w-1/2 my-2 mt-6 ml-8 text-black font-Poppins " style="font-family: Poppins; font-style: 
                        normal; line-height: normal; letter-spacing: 0.04125rem;">Discount :</h3>
                        <div class="font-Mulish text-lg text-[#81858b] md:text-[#C3C6C9] text-center w-1/2 font-bold leading-6 ml-35 mt-6"> 0₹</div>
                    </div>
                    <hr class="w-11/12 ml-2">
                    <div class="flex"> 
                        <h3 class="font-medium md:font-extrabold text-2xl h-1/6 my-2 w-1/2 mt-6 ml-8 text-black font-Poppins " style="font-family: Poppins; font-style: normal; line-height: normal; letter-spacing: 0.04125rem;">Tax :</h3>
                        <div class="font-Mulish text-lg text-[#81858b] md:text-[#C3C6C9] text-center w-1/2 font-bold leading-6 ml-35 mt-6"> 5₹</div>
                    </div>
                    <hr class="w-11/12 ml-2">
                    <div class="flex"> 
                        <h3 class="font-medium md:font-extrabold text-2xl h-1/6 w-1/2 my-2 mt-6 ml-8 text-black font-Poppins " style="font-family: Poppins; font-style: normal; line-height: normal; letter-spacing: 0.04125rem;">Total :</h3>
                        <div class="font-Mulish text-lg text-[#81858b] md:text-[#C3C6C9] text-center w-1/2 font-bold leading-6 ml-35 mt-6"> 905₹</div>
                    </div>    
                </div>

            </div>

            <div class="Checkout button flex items-center justify-center text-center text-white w-full mt-8">

                <nuxt-link :to="this.$store.state.cart.length > 0 ? '/checkOut' : ''" class="checkout_Btn p-2 py-4 rounded-lg font-medium text-lg w-[25.3rem] md:w-[20rem] lg:w-[24rem] xl:w-[26.75rem]" style="font-family: Poppins; font-style: normal; letter-spacing: 0.03rem; background-color: #EA454C; height: 3.45813rem;">Checkout</nuxt-link>

            </div>
        </div>

    </div>

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

