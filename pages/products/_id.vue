<template>
  <div class="poppins-paragraph lg:m-8 mb-20 md:m-5 md:mt-8 m-3 mt-5">
       <div class="md:flex flex-row mb-5">
        <div class="md:flex md:flex-col md:mt-24 invisible md:visible">
          <div
  @click="selectColor('black')"
  :class="[
    'lg:w-3.5 lg:m-2.5 lg:mt-20 lg:h-3.5 md:w-2.5 md:h-2.5 bg-black md:m-1.5 h-3.5 w-3.5 m-3 rounded-full',
    { 'custom-ring': selectedColor === 'black' }
  ]"
></div>

<div
  @click="selectColor('blue')"
  :class="[
    'lg:w-3.5 lg:m-2.5 lg:h-3.5 md:w-2.5 md:h-2.5 md:m-1.5 bg-[#ABC6D6] h-3.5 w-3.5 m-3 rounded-full',
    { 'custom-ring': selectedColor === 'blue' }
  ]"
></div>

<div
  @click="selectColor('green')"
  :class="[
    'lg:w-3.5 lg:m-2.5 lg:h-3.5 ring-grey md:w-2.5 md:h-2.5 md:m-1.5 bg-[#58D7C4] h-3.5 w-3.5 m-3 rounded-full',
    { 'custom-ring': selectedColor === 'green' }
  ]"
></div>

<div
  @click="selectColor('red')"
  :class="[
    'lg:w-3.5 lg:m-2.5 lg:h-3.5 ring-grey md:w-2.5 md:h-2.5 md:m-1.5 bg-[#F2CEC6] h-3.5 w-3.5 m-3 rounded-full',
    { 'custom-ring': selectedColor === 'red' }
  ]"
></div>


    </div>
          <div class="flex flex-col w-full justify-between md:flex-row">
            <div class="flex flex-col h-3/2 md:w-2/5 gap-6 md:mb-0 mb-8">
              
              <img  class="max-w-lg mx-auto w-full mb-8 h-full rounded-xl object-contain aspect-square"
          :src="product[main].image" /> 
           <div class="mx-auto flex sm:hidden mb-4">
            <div
  @click="selectColor('black')"
  :class="[
    'lg:w-3.5 lg:m-2.5 lg:mt-20 lg:h-3.5 md:w-2.5 md:h-2.5 bg-black md:m-1.5 h-3.5 w-3.5 m-3 rounded-full',
    { 'custom-ring': selectedColor === 'black' }
  ]"
></div>
<div
  @click="selectColor('blue')"
  :class="[
    'lg:w-3.5 lg:m-2.5 lg:h-3.5 md:w-2.5 md:h-2.5 md:m-1.5 bg-[#ABC6D6] h-3.5 w-3.5 m-3 rounded-full',
    { 'custom-ring': selectedColor === 'blue' }
  ]"
></div>
<div
  @click="selectColor('green')"
  :class="[
    'lg:w-3.5 lg:m-2.5 lg:h-3.5 ring-grey md:w-2.5 md:h-2.5 md:m-1.5 bg-[#58D7C4] h-3.5 w-3.5 m-3 rounded-full',
    { 'custom-ring': selectedColor === 'green' }
  ]"
></div>
<div
  @click="selectColor('red')"
  :class="[
    'lg:w-3.5 lg:m-2.5 lg:h-3.5 ring-grey md:w-2.5 md:h-2.5 md:m-1.5 bg-[#F2CEC6] h-3.5 w-3.5 m-3 rounded-full',
    { 'custom-ring': selectedColor === 'red' }
  ]"
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
                  <h1 class="lg:text-2xl lg:mr-20 md:text-xl font-extrabold md:font-extrabold  mr-10">{{ product[main].title }}
                  </h1>
                  <div class="image-container">
  <img class="w-4 h-4 md:mt-2 broader-darker"
       src="https://static.vecteezy.com/system/resources/thumbnails/001/505/003/small/share-icon-free-vector.jpg">
</div>



              </div>
              <p class="text-sm font-medium text-[#B9BBBF] mt-1 mb-2">TPC</p>
              <div class="text-xs font-medium flex flex-row">
                   <br>
              </div>
              <hr class="h-px bg-[#CFCFCF] border-0">
              <p class="lg:mt-7 lg:text-3xl  mt-4 text-2xl text-[#271819] font-extrabold md:font-extrabold font- "><b></b> ${{ product[main].price }}</p>
              <p class="lg:mt-5 text-sm text-[#B9BBBF] font-medium lg:mb-2 pb-.5 mt-4 mb-2">Choose a Size</p>
              
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
            class="rounded-full  text-[#726C6C] float-left bg-gray-100 text-gray-500 font-medium px-2 py-1 text-xs lg:text-sm flex flex-row lg:mr-4 md:mr-2 m-1"
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
              
              
        <hr class="invisible md:visible md:h-px md:lg:my-8 md:my-5 md:bg-[#CFCFCF] md:border-0 md:dark:bg-[#CFCFCF]">

              <div class="md:flex bg-white shadow-[0px_40px_70px_4px_rgba(0,0,0,0.56)] md:shadow-none md:border-0 m-0 justify-center md:justify-start w-full fixed bottom-0 mx-0 mb-0 flex flex-row md:justify-left sm:mb-0 md:relative gap-0s">
                <button class="  gap-0 md:mr-[7%] md:px-[12%] pl-[40%] mr-0 items-center justify-center text-center pr-0 md:py-0 min-w-[88%]  md:min-w-0 bg-white rounded-none font-black flex-none flex md:rounded-full md:bg-[#EA454C] flex flex-row md:py-2 md:px-3 md:font-normal">
                  <div class="flex items-center justify-center md:justify-start ">
  <div class="flex items-center -ml-[15px]">
    <img class="invisible md:visible -pr-[2px] w-5 h-4 mr-0 md:mr-0 md:mt-0 md:mb-0" src="../../assets/cart02.png">
    <img class="visible md:invisible w-4 h-3 mr-1 -ml-[5px] mt-[0px] mb-0" src="../../assets/cart01.png">
  </div>
  <p class="flex-none text-[12px] pr-[0%] md:text-[14px] text-center text-black md:text-white md:font-extrabold font-extrabold sm:text-xs pl-0 md:pl-0 mt-0 mb-0">Add To Cart</p>
</div>



                </button><button class="pl-[15%] md:px-[12%] md:py-4 ml-0 py-3 md:py-0 min-w-[92%] text-center md:min-w-0 bg-[#EA454C] font-bold flex-none items-center rounded-none  rounded-full md:bg-[#EA454C] flex flex-row md:rounded-full md:font-normal py-1 sm:ml-3 md:mr-[0%]">
                    <img class="w-4 h-4 mr-[1px] md:mr-[3px]  filter" src="../../assets/lightning.png" >
                    <p class=" poppins-paragraph text-[12px] md:text-[14px] pr-2 pl-2 text-white md:font-extrabold font-extrabold sm:text-xs font-poppins">Buy Now</p>

                </button>
            </div>
          </div>
      </div>
    </div>

    <hr class="h-0.5 mt-12 bg-[#CFCFCF] border-0 dark:bg-[#CFCFCF]">

  <div>

      <p class="lg:mt-3.5 mt-2 "><b class="lg:text-2xl md:text-xl  lg:mb-3 md:font-extrabold font-extrabold flex text-[#271819]">Product Description</b><b
              class="font-medium md:text-xs lg:text-sm text-[#667085]">{{ product[main].description }}</b> </p>
      <p class="lg:mt-3.5 md:mt-2" ><b
              class="lg:text-2xl md:text-xl text-[#344054] md:font-extrabold font-extrabold mt-6 lg:mb-3 flex">Product Details</b><b
              class="font-medium md:text-xs lg:text-sm text-[#667085]"> {{ product[main].category }}</b></p>
  </div>

</div></template>

<style>
.poppins-paragraph {
  font-family: 'Poppins', sans-serif;
}
#small , #medium , #large , #extra , #XXL{
  accent-color: #EA454C;
}
.custom-ring {
  box-shadow: 0 0 0 4px rgba(169, 169, 169, 0.5);
  outline: 4px solid rgba(169, 169, 169, 0.5);
}
.image-container {
  display: inline-block;
}

.broader-darker {
  transform: scaleX(1.4);
  transform: scaleY(1.2);
 }


</style>

<script>
export default {
  data() {
    return {
      i: 0,
      main: 1,
      product: [],
      selectedColor: null,
    };
  },
  async asyncData({ params }) {
    const productId = params.id;
    const response = await fetch(`https://fakestoreapi.com/products/`);
    const product = await response.json();
    console.log(product);
    return {
      product,
    };
  },
  methods: {
    selectColor(color) {
      this.selectedColor = color;
    },
  },
};
</script>

