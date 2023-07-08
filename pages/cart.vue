<template>
    <div class="main h-full flex items-center justify-center bg-white-100 ">

        <div class="cart h-full w-full bg-white-100 ">

            <h1 class="py-8 px-12 text-black-500 text-4xl">Shopping Cart</h1>

            <div class=" flex-col items-center justify-around h-full w-full  ">

                <div id="selected_prod1" class="flex justify-evenly border-2 item_1 rounded-lg mt-24" style="width: 70%; height: 8rem; margin-left: auto; margin-right: auto;">

                    <div class="image_div flex items-center justify-center"> 

                        <img src="../assets/get_it.png" alt="Image description" class="w-24 h-24 object-cover">

                    </div>

                    <div class="prod_Description w-32 h-28 mt-6 flex-col justify-center ">

                        <h3 id="prod_Name" class=""> PRODUCT NAME </h3>
                        <h4 id="prod_Price" class="">69$</h4>
                        <p id="prod_Size" class="">Size : M </p>

                    </div>

                    <div class="Quantity flex justify-evenly w-28 h-28 mt-2 "> 

                        <button onclick="" class="flex items-center justify-cente p-2 w-7 h-8 mt-10 text-black rounded-lg border-2  bg-slate-300">-</button>

                        <p id="count" class="flex items-center justify-cente p-2 h-8 mt-10 text-black "> 1 </p>

                        <button onclick="" class="flex items-center justify-cente p-2 w-8 h-8 mt-10 text-black rounded-lg border-2  bg-slate-300">+</button>

                    </div>

                    <div class="close_btn flex-row justify-end w-8 ">
                        <button class="flex-row justify-end ml-8 mt-2">X</button>
                    </div>

                </div>

                <div id="selected_prod1" class="flex justify-evenly border-2 item_1 rounded-lg mt-24" style="width: 70%; height: 8rem; margin-left: auto; margin-right: auto;">

                    <div class="image_div flex items-center justify-center"> 

                        <img src="../assets/get_it.png" alt="Image description" class="w-24 h-24 object-cover">

                    </div>

                    <div class="prod_Description w-32 h-28 mt-6 flex-col justify-center ">

                        <h3 id="prod_Name" class=""> PRODUCT NAME </h3>
                        <h4 id="prod_Price" class="">69$</h4>
                        <p id="prod_Size" class="">Size : M </p>

                    </div>

                    <div class="Quantity flex justify-evenly w-28 h-28 mt-2 "> 

                        <button onclick="" class="flex items-center justify-cente p-2 w-7 h-8 mt-10 text-black rounded-lg border-2  bg-slate-300">-</button>

                        <p id="count" class="flex items-center justify-cente p-2 h-8 mt-10 text-black "> 1 </p>

                        <button onclick="" class="flex items-center justify-cente p-2 w-8 h-8 mt-10 text-black rounded-lg border-2  bg-slate-300">+</button>

                    </div>

                    <div class="close_btn flex-row justify-end w-8 ">
                        <button class="flex-row justify-end ml-8 mt-2">X</button>
                    </div>

                </div>

                <div id="selected_prod1" class="flex justify-evenly border-2 item_1 rounded-lg mt-24" style="width: 70%; height: 8rem; margin-left: auto; margin-right: auto;">

                    <div class="image_div flex items-center justify-center"> 

                        <img src="../assets/get_it.png" alt="Image description" class="w-24 h-24 object-cover">

                    </div>

                    <div class="prod_Description w-32 h-28 mt-6 flex-col justify-center ">

                        <h3 id="prod_Name" class=""> PRODUCT NAME </h3>
                        <h4 id="prod_Price" class="">69$</h4>
                        <p id="prod_Size" class="">Size : M </p>

                    </div>

                    <div class="Quantity flex justify-evenly w-28 h-28 mt-2 "> 

                        <button onclick="" class="flex items-center justify-cente p-2 w-7 h-8 mt-10 text-black rounded-lg border-2  bg-slate-300">-</button>

                        <p id="count" class="flex items-center justify-cente p-2 h-8 mt-10 text-black "> 1 </p>

                        <button onclick="" class="flex items-center justify-cente p-2 w-8 h-8 mt-10 text-black rounded-lg border-2  bg-slate-300">+</button>

                    </div>

                    <div class="close_btn flex-row justify-end w-8 ">
                        <button class="flex-row justify-end ml-8 mt-2">X</button>
                    </div>

                </div>

            </div>
            

        </div>

        <div class="billing h-full w-full flex-col items-center justify-center ">

            <div class="girl_img w-full flex items-center justify-center mt-32 " style="height: 16rem;">

                <img class="h-full w-3/5 block" src="../assets/cart_girl.png" style=" margin-left: auto; margin-right: auto;">

            </div>

            <div class="Bill flex items-center justify-center w-full h-76 bg-white-100 mt-4"> 

                <div class=" w-3/5 h-full border-2 bg-white-100"> 

                    <h3 class="font-medium text-xl my-4 ml-4 ">Subtotal :</h3>
                    
                    <h3 class="font-medium text-xl my-4 ml-4">Discount :</h3>
                    
                    <h3 class="font-medium text-xl my-4 ml-4">Tax :</h3>
                    
                    <h3 class="font-medium text-xl my-4 ml-4">Total :</h3>

                </div>

            </div>

            <div class="Checkout button flex items-center justify-center text-center text-white w-full mt-8">

                <btn class="checkout_Btn bg-rose-600 w-3/5 p-2 rounded-lg" >Checkout</btn>

            </div>
        </div>

    </div>

</template>

<script>
  export default {
    name:'cart'
  }
</script>