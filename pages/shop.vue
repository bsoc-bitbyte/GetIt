<template>
    <div class="main w-screen h-screen">
        <div class="body flex w-full h-full"> 
            <div v-if="showFilteroptions" class="sidebar h-[20px] md:h-[544px] w-[40px] md:w-[317px] m-4 md:border-r-2">
                <div class="flex h-[30px] w-full top-[24px] relative cursor-pointer" @click="dropDown">
                    <img class=" h-[28px] w-[28px] left-[22px] relative" src="../assets/image 66.png">
                    <div class="font-Poppins font-semibold text-xl leading-6 left-[40px] md:left-[70px] relative">
                        Filters
                    </div>
                </div>
                <div v-if="showFilters" class="filterOptions absolute z-10 md:z-0 w-1/3 md:w-[310px] text-center md:text-left ml-24 md:ml-24 mt-12 bg-white md:bg-transparent border md:border-0 border-gray-300 rounded-md shadow-md md:shadow-none">
                    <ul>
                        <li class="h-[33px] font-Poppins font-semibold text-l text-[#808080] hover:text-[#252B42] leading-6 cursor-pointer" @click="toggleClubFilters"> Clubs </li>
                        <li class="h-[33px] font-Poppins font-semibold text-l text-[#808080] hover:text-[#252B42] leading-6 cursor-pointer" @click="togglePriceFilters"> Price </li>
                        <li class="h-[33px] font-Poppins font-semibold text-l text-[#808080] hover:text-[#252B42] leading-6 cursor-pointer" @click="toggleCategoryFilters"> Categories </li>
                    </ul>
                </div>
            </div>
            <div v-if="showClubFilters" class="ClubsFilters absolute md:relative z-10 md:z-0 h-[660px] md:h-[900px] w-[232px] md:w-[282px] m-4 ml-12 mt-16 md:mt-0 md:border-r-2 drop-shadow-lg bg-white md:bg-transparent border md:border-0 border-gray-300 rounded-md shadow-md md:shadow-none" >
                <div class="flex m-4 ">
                    <p class="font-bold font-Montserrat text-[20px] ml-8">CLUBS</p>
                </div>
                <div class="ClubNames h-[558px] overflow-hidden">
                    <div v-for="club in Clubs" :key="club" class="h-[33px] mt-8 ml-12 font-Poppins font-semibold text-[14px] text-[#808080] leading-6 cursor-pointer" :class="{'text-[#211B1B] text-xl' : isSelectedClub(club) }" @click="toggleSelectedClub(club)"> {{ club }} </div>
                </div>
                <div class="Btns flex justify-around">
                    <button class="ApplyBtn w-[105px] h-[34px] rounded-[30px] font-Poppins font-normal text-[12px] text-[#FFFEFE] bg-[#EA454C]" @click="toggleClubFilters">APPLY</button>
                    <button class="ClearBtn w-[105px] h-[34px] rounded-[30px] font-Poppins font-normal text-[12px] text-[#FFFEFE] bg-[#EA454C]" @click="clearClubs">CLEAR</button>
                </div>
            </div>
            <div v-if="showPriceFilters" class="PriceFilters absolute md:relative z-10 md:z-0 h-[480px] md:h-[900px] w-[232px] md:w-[282px] m-4 ml-12 mt-16 md:mt-0 md:border-r-2 drop-shadow-lg bg-white md:bg-transparent border md:border-0 border-gray-300 rounded-md shadow-md md:shadow-none" >
                <div class="flex m-4 ">
                    <p class="font-bold font-Montserrat text-[20px] ml-8">Price</p>
                </div>
                <div class="PriceRanges h-[360px] md:h-[558px] overflow-hidden">
                    <div v-for="price in Price" :key="price" class="h-[33px] mt-8 ml-12 font-Poppins font-semibold text-[14px] text-[#808080] leading-6 cursor-pointer" :class="{'text-[#211B1B] text-xl' : isSelectedPrice(price) }" @click="toggleSelectedPrice(price)"> {{ price }} </div>
                </div>
                <div class="Btns flex justify-around">
                    <button class="ApplyBtn w-[105px] h-[34px] rounded-[30px] font-Poppins font-normal text-[12px] text-[#FFFEFE] bg-[#EA454C]" @click="togglePriceFilters">APPLY</button>
                    <button class="ClearBtn w-[105px] h-[34px] rounded-[30px] font-Poppins font-normal text-[12px] text-[#FFFEFE] bg-[#EA454C]" @click="clearPrice">CLEAR</button>
                </div>
            </div>
            <div v-if="showCategoryFilters" class="CategoryFilters absolute md:relative z-10 md:z-0 h-[260px] md:h-[350px] w-[232px] md:w-[282px] m-4 ml-12 mt-16 md:mt-0 md:border-r-2 drop-shadow-lg bg-white md:bg-transparent border md:border-0 border-gray-300 rounded-md shadow-md md:shadow-none" >
                <div class="flex m-4 ">
                    <p class="font-bold font-Montserrat text-[20px] ml-8">Category</p>
                </div>
                <div class="Categories h-[150px] md:h-[238px] overflow-hidden">
                    <div v-for="category in Category" :key="category" class="h-[33px] mt-8 ml-12 font-Poppins font-semibold text-[14px] text-[#808080] leading-6 cursor-pointer" :class="{'text-[#211B1B] text-xl' : isSelectedCategory(category) }" @click="togleSelectedCategory(category)"> {{ category }} </div>
                </div>
                <div class="Btns flex justify-around">
                    <button class="ApplyBtn w-[105px] h-[34px] rounded-[30px] font-Poppins font-normal text-[12px] text-[#FFFEFE] bg-[#EA454C]" @click="toggleCategoryFilters">APPLY</button>
                    <button class="ClearBtn w-[105px] h-[34px] rounded-[30px] font-Poppins font-normal text-[12px] text-[#FFFEFE] bg-[#EA454C]" @click="clearCategoories">CLEAR</button>
                </div>
            </div>
            <div class="products-secton w-[995.7px] h-full mx-4 mt-24 md:mt-4 px-16 grid md:grid-cols-3 gap-2">
                <div class="product-1 w-[278.4px] h-[426.4px]" v-for="product in Products" :key=" product.ProductId " > 
                    <div class="productImage">
                        <img src='../assets/Rectangle.png'>
                    </div>
                    <div class="productInfo "> 
                        <div class="productType mt-2 font-medium text-sm leading-6 text-[#9E3500]"> {{ product.ProductType }} </div>
                        <div class="productName font-medium text-sm leading-6 text-[#111111]"> {{ product.ProductName }} </div>
                        <div class="productClub font-normal text-sm leading-5 text-[#757575]"> {{ product.ProductClub}}</div>
                        <div class="productPrice font-medium text-sm leading-6 text-[#111111]"> {{ product.ProductPrice }}</div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
    export default {
        name: 'shop',
        data() {
            return {
                                                        /* Filter Parameters */
                Clubs: ["TPC" , "BMC" , "APS" , "AFC" , "SAMVAAD" , "SAAZ", "JAZBAAT" , "FOOTBALL" , "CRICKET" ],
                SelectedClubs: [],
                Price: ["< 100" , "100-300", "300-500", "500-800", "800+"],
                SelectedPrice: [],
                Category : ["Male" , "Female"],
                SelectedCategory : [],
                                                        /* Products Data */
                Products : [
                    { ProductId: 1, ProductImage: '../assets/Rectangle.png', ProductType: 'T-shirt', ProductName: 'Product1', ProductClub : 'TPC', ProductPrice: '399$'},
                    { ProductId: 2, ProductImage: '../assets/Rectangle.png', ProductType: 'Hoodie', ProductName: 'Product2', ProductClub : 'TPC', ProductPrice: '599$'},
                    { ProductId: 3, ProductImage: '../assets/Rectangle.png', ProductType: 'T-shirt', ProductName: 'Product3', ProductClub : 'BMC', ProductPrice: '299$'},
                    { ProductId: 4, ProductImage: '../assets/Rectangle.png', ProductType: 'Sticker', ProductName: 'Product4', ProductClub : 'TPC', ProductPrice: '69$'},
                    { ProductId: 5, ProductImage: '../assets/Rectangle.png', ProductType: 'T-shirt', ProductName: 'Product5', ProductClub : 'AFC', ProductPrice: '349$'},
                    { ProductId: 6, ProductImage: '../assets/Rectangle.png', ProductType: 'Jacket', ProductName: 'Product6', ProductClub : 'APS', ProductPrice: '569$'},
                ],
                                                        /* Booleans controlling states */
                showFilteroptions : true,
                showFilters : false,
                showClubFilters : false,
                showPriceFilters : false,
                showCategoryFilters : false,
                };
        },
        methods :{
            toggleClubFilters () {
                this.showClubFilters = !this.showClubFilters ;
                this.showFilteroptions = !this.showFilteroptions;
            },
            togglePriceFilters () {
                this.showFilteroptions = !this.showFilteroptions;
                this.showPriceFilters = !this.showPriceFilters
            },
            toggleCategoryFilters () {
                this.showFilteroptions = !this.showFilteroptions;
                this.showCategoryFilters = !this.showCategoryFilters;
            },
            toggleSelectedClub(club) {
                const index = this.SelectedClubs.indexOf(club);
                if (index > -1) {
                    this.SelectedClubs.splice(index, 1);
                 } else {
                    this.SelectedClubs.push(club);
                 }
            },
            toggleSelectedPrice (price) {
                const index = this.SelectedPrice.indexOf(price);
                if (index > -1) {
                    this.SelectedPrice.splice(index,1);
                } else {
                    this.SelectedPrice.push(price);
                }
            },
            togleSelectedCategory (category) {
                const index = this.SelectedCategory.indexOf(category);
                if(index > -1) {
                    this.SelectedCategory.splice(index, 1);
                } else {
                    this.SelectedCategory.push(category);
                }
            },
            isSelectedClub(club) {
               return this.SelectedClubs.includes(club);
            },
            isSelectedPrice(price) {
               return this.SelectedPrice.includes(price);
            },
            isSelectedCategory(category) {
                return this.SelectedCategory.includes(category);        
            },
            clearClubs () {
               this.SelectedClubs = [];
            },
            clearPrice () {
                this.SelectedPrice = [];
            },
            clearCategoories () {
                this.SelectedCategory = [];
            },
            dropDown () {
                this.showFilters = !this.showFilters;
            }
        },
    }
</script>
