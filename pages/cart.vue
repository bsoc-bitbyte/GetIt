<template>
    <div class="main h-full flex items-center justify-center bg-white-100 m-16 max-lg:-mt-6 -mt-14">

        <div class="cart h-full w-full bg-white-100 ">

            <div class="items-left" style=" width: 35rem; margin-left: auto; margin-right: auto;">
                <h3 class=" flex font-Poppins text-xl font-bold pl-0 px-12 " style="width: 19.417rem; top: 1rem;">Shopping Cart</h3>
            </div>    
            
            <div class=" flex-col items-center justify-around h-full w-full " 
                v-for=" (product, index ) in products" :key=" index " >
                
                <div id="selected_prod1" class=" h-32 flex justify-evenly border-2 item_1 rounded-lg mt-8" style=" width: 35rem; margin-left: auto; margin-right: auto;">

                    <div class="image_div flex items-center justify-center"> 

                        <img src="../assets/get_it.png" alt="Image description" class="w-24 h-24 object-cover">

                    </div>

                    <div class="prod_Description w-40 h-28 mt-6 flex-col justify-center ">

                        <h3 id="prod_Name" class="font-Poppins text-lg font-semibold leading-6" style="color: #271819;">{{ product.ProductName }}</h3>
                        <h4 id="prod_Price" class="font-Mulish text-lg font-bold leading-6" style="color: #C3C6C9;">{{ product.ProductPrice }}</h4>
                        <p id="prod_Size" class="font-Mulish text-lg font-semibold leading-12" style="color: #271819;">{{ product.ProductSize }}</p>

                    </div>

                    <div class="Quantity flex justify-evenly w-28 h-28 mt-2 "> 

                        <button onclick="" class="flex items-center justify-cente p-2 w-7 h-8 mt-10 text-black text-center rounded-lg border-2 " style="background-color: #EEF1F4;">-</button>

                        <p id="count" class="flex items-center justify-cente p-2 h-8 mt-10 " style="color: #C3C6C9; "> 1 </p>

                        <button onclick="" class="flex items-center justify-cente p-2 w-8 h-8 mt-10 text-black rounded-lg border-2 "  style="background-color: #EEF1F4;">+</button>

                    </div>

                    <div class="close_btn flex-row justify-end w-8 ">
                        <button class="flex-row justify-end ml-8 mt-2">X</button>
                    </div>

                </div>
            </div>
            

        </div>

        <div class="billing h-full w-full flex-col mb-32 items-center justify-center ">

            <div class="girl_img w-full h-1/2 flex items-center justify-center mt-32 ">

                <img class="h-full block" src="../assets/cart_girl.png" style=" margin-left: auto; margin-right: auto; width: 43%;">

            </div>

            <div class="Bill flex items-center justify-center w-full h-70 bg-white-100 mt-16"> 

                <div class=" w-3/5 h-full border-2 bg-white-100" style="width: 26.75rem"> 
                    <div class="flex">
                    <h3 class="font-medium text-2xl h-1/6 w-1/2 my-2 mt-6 ml-8 text-black font-Poppins " style="font-family: Poppins; font-weight: 800; font-style: normal; line-height: normal; letter-spacing: 0.04125rem;">Subtotal :</h3>
                    <div class="font-Mulish text-lg w-1/2 font-bold leading-6 ml-40 mt-6" style="color: #C3C6C9;"> 900$ </div>
                    </div>
                    <hr class="w-11/12 ml-2">
                    <div class="flex"> 
                    <h3 class="font-medium text-2xl h-1/6 w-1/2 my-2 mt-6 ml-8 text-black font-Poppins " style="font-family: Poppins; font-weight: 800; font-style: 
                    normal; line-height: normal; letter-spacing: 0.04125rem;">Discount :</h3>
                    <div class="font-Mulish text-lg w-1/2 font-bold leading-6 ml-40 mt-6" style="color: #C3C6C9;"> 0$ </div>
                    </div>
                    <hr class="w-11/12 ml-2">
                    <div class="flex"> 
                    <h3 class="font-medium text-2xl h-1/6 my-2 w-1/2 mt-6 ml-8 text-black font-Poppins " style="font-family: Poppins; font-weight: 800; font-style: normal; line-height: normal; letter-spacing: 0.04125rem;">Tax :</h3>
                    <div class="font-Mulish text-lg w-1/2 font-bold leading-6 ml-40 mt-6" style="color: #C3C6C9;"> 5$ </div>
                    </div>
                    <hr class="w-11/12 ml-2">
                    <div class="flex"> 
                    <h3 class="font-medium text-2xl h-1/6 w-1/2 my-2 mt-6 ml-8 text-black font-Poppins " style="font-family: Poppins; font-weight: 800; font-style: normal; line-height: normal; letter-spacing: 0.04125rem;">Total :</h3>
                    <div class="font-Mulish text-lg w-1/2 font-bold leading-6 ml-40 mt-6" style="color: #C3C6C9;"> 905$ </div>
                    </div>    
                </div>

            </div>

            <div class="Checkout button flex items-center justify-center text-center text-white w-full mt-8">

                <nuxt-link to="/checkOut" class="checkout_Btn p-2 py-4 rounded-lg font-medium text-lg"
                        style="font-family: Poppins; font-style: normal; letter-spacing: 0.03rem; background-color: #EA454C;  width: 26.75rem; height: 3.45813rem;">Checkout</nuxt-link>

            </div>
        </div>

    </div>

</template>

<script>
    export default {
        data: () => {
            return {
                products: [
                    {ProductName: 'Product1', ProductPrice: '69$', ProductSize: 'M'},
                    {ProductName: 'Product2', ProductPrice: '69$', ProductSize: 'M'},
                    {ProductName: 'Product3', ProductPrice: '69$', ProductSize: 'M'},
                    {ProductName: 'Product4', ProductPrice: '69$', ProductSize: 'M'}
                ]
            }
        },
    name:'cart'
  }
</script>

