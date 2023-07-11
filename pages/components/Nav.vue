<template>
  <nav>
    <div class="max-lg:hidden m-4 ml-6 mr-6">
      <div class="">
        <input class="hidden" type="checkbox" />
        <label class="menu__btn" for="menu__toggle"></label>

        <ul class="flex flex-row font-sans whitespace-nowrap text-xl border-b-[solid] border-b-[#474747]">
          <li class="text-[#271819] w-[10.5%] top-[-5px] inline-block px-[1.5%] xl:px-[4%] py-[19px]">
            <a class="px-1 py-0.5 hover:border-b-2 hover:border-black" href="#">Home</a>
          </li>
          <li class="text-[#271819] font-sans w-[10.5%] top-[-5px] inline-block px-[3%] py-[19px]">
            <a class="px-1 py-0.5 hover:border-b-2 hover:border-black" href="#">Shop</a>
          </li>
          <li class="text-[#271819] font-sans w-[10.5%] top-[-5px] inline-block px-[3%] py-[19px]">
            <a class="px-1 py-0.5 hover:border-b-2 hover:border-black" href="#">About Us</a>
          </li>
          <li class="font-[bold] font-sans text-[50px] ml-[13%] mx-[29%] my-0 font-bold">
            <a href="#"><img class="max-w-none h-6 w-6 mt-2 inline-block h-[60px] w-[65px]"
                src="https://raw.githubusercontent.com/bsoc-bitbyte/GetIt/10a0fcc39d52d116428dd49505ead2f597e7a30e/assets/get_it.png" /><span
                class="absolute top-[33px]">GetIt</span></a>
          </li>
          <li class="text-[#271819]font-sans w-[15.5%] top-[-5px] inline-block -ml-12 px-[3%] py-[19px]">
            <a class="px-1 py-0.5 ml-[28%] hover:border-b-2 hover:border-black" href="#">Sign In</a>
          </li>
          <li class="mt-5 pr-[3%]">
            <a class="px-[15%] font-sans text-sm py-[12%] pb-[17%] hover:bg-gray-100  border-[solid] border-2 border-gray-400"
              href="#">14 items
              <img class="max-w-none h-4 w-4 inline-block"
                src="https://raw.githubusercontent.com/bsoc-bitbyte/GetIt/10a0fcc39d52d116428dd49505ead2f597e7a30e/assets/cart.png" /></a>
          </li>
        </ul>
      </div>

      <div class="fixed ml-[70%] list-none -mt-16">
        <a href="#" class="text-[#271819]"><input type="text"
            class=" absolute w-[120px] h-10 right-[-60px] text-[#271819] text-[20px] pr-[35px] px-3 py-2.5 rounded-[100px] border-hidden border-[2px] border-gray-400 top-[15px]"
            placeholder="Search"/>
          <svg class="absolute w-[60px] h-[15px] right-[-65px] top-[29px]" stroke="currentColor" fill="black"
            stroke-width="0" viewBox="0 0 512 512" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg">
            <path
              d="M505 442.7L405.3 343c-4.5-4.5-10.6-7-17-7H372c27.6-35.3 44-79.7 44-128C416 93.1 322.9 0 208 0S0 93.1 0 208s93.1 208 208 208c48.3 0 92.7-16.4 128-44v16.3c0 6.4 2.5 12.5 7 17l99.7 99.7c9.4 9.4 24.6 9.4 33.9 0l28.3-28.3c9.4-9.4 9.4-24.6.1-34zM208 336c-70.7 0-128-57.2-128-128 0-70.7 57.2-128 128-128 70.7 0 128 57.2 128 128 0 70.7-57.2 128-128 128z">
            </path>
          </svg>
        </a>
      </div>
      <div class="hidden"><a href="#">GetIt</a></div>
      <hr class="h-px lg:my-4 my-5 bg-gray-400 border-0 dark:bg-gray-400" />
    </div>

    <div class="lg:hidden">
      <button type="button" 
        class="fixed inline-flex items-center p-2 mt-2 ml-[0.5%] text-sm text-gray-500 focus:outline-none dark:text-gray-400 dark:hover:bg-gray-700 dark:focus:ring-gray-600">
        <span class="sr-only">Open sidebar</span>
        <svg class="h-8 w-8 text-black" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"
          stroke-linecap="round" stroke-linejoin="round" v-on:click="isShow = !isShow">
          <line x1="3" y1="12" x2="21" y2="12" />
          <line x1="3" y1="6" x2="21" y2="6" />
          <line x1="3" y1="18" x2="21" y2="18" />
        </svg>
        <aside v-show="isShow" class="fixed top-0 left-0 shadow-2xl z-40 w-60 h-full">
          <div class="h-full px-3 py-4 overflow-y-auto bg-gray-200 dark:bg-gray-800">
            <svg class="h-5 w-5 text-black" width="24" height="24" viewBox="0 0 24 24" stroke-width="2"
              stroke="currentColor" fill="none" stroke-linecap="round" stroke-linejoin="round" v-on:click="isShow = !isShow">
              <path stroke="none" d="M0 0h24v24H0z" />
              <line x1="18" y1="6" x2="6" y2="18" />
              <line x1="6" y1="6" x2="18" y2="18" />
            </svg>
            <ul class="space-y-2 text-xl font-medium mt-7">
              <li>
                <a href="#"
                  class="flex items-center p-2 text-gray-900 rounded-lg dark:text-white hover:bg-gray-300 dark:hover:bg-gray-700">
                  <span class="flex-1 ml-3 whitespace-nowrap">Home</span>
                </a>
              </li>
              <li>
                <a href="#"
                  class="flex items-center p-2 text-gray-900 rounded-lg dark:text-white hover:bg-gray-300 dark:hover:bg-gray-700">
                  <span class="flex-1 ml-3 whitespace-nowrap">Shop</span>
                </a>
              </li>
              <li>
                <a href="#"
                  class="flex items-center p-2 text-gray-900 rounded-lg dark:text-white hover:bg-gray-300 dark:hover:bg-gray-700">
                  <span class="flex-1 ml-3 whitespace-nowrap">About Us</span>
                </a>
              </li>
              <li>
                <a href="#"
                  class="flex items-center p-2 text-gray-900 rounded-lg dark:text-white hover:bg-gray-300 dark:hover:bg-gray-700">
                  <span class="flex-1 ml-3 whitespace-nowrap">Sign In</span>
                </a>
              </li>
              <li>
                <span class="flex"><a
                    class="flex-1 ml-1 whitespace-nowrap items-center p-2 text-gray-900 rounded-lg dark:text-white hover:bg-gray-300 dark:hover:bg-gray-700"
                    href="#">Cart<img class="max-w-none h-5 w-5 inline-block"
                      src="https://raw.githubusercontent.com/bsoc-bitbyte/GetIt/10a0fcc39d52d116428dd49505ead2f597e7a30e/assets/cart.png" /></a></span>
              </li>
            </ul>
          </div>
        </aside>

        <div class="fixed font-[bold] text-black text-[35px] ml-11 mx-[29%] my-0 font-bold">
          <span class="absolute -mt-2">GetIt</span>
        </div>
        <li class="fixed ml-[78%] sm:ml-[86%] md:ml-[90%] list-none -mt-16">
          <a href="#">
            <input type="text"
              class="absolute w-[140px] h-10 right-[-55px] text-[15px] pr-[35px] px-3 py-2.5 rounded-[100px] border-[solid] border-[2px] border-gray-400 top-[15px]"
              placeholder="Search..." />
            <svg class="absolute w-[60px] h-[15px] right-[-65px] top-[29px]" stroke="currentColor" fill="grey"
              stroke-width="0" viewBox="0 0 512 512" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg">
              <path
                d="M505 442.7L405.3 343c-4.5-4.5-10.6-7-17-7H372c27.6-35.3 44-79.7 44-128C416 93.1 322.9 0 208 0S0 93.1 0 208s93.1 208 208 208c48.3 0 92.7-16.4 128-44v16.3c0 6.4 2.5 12.5 7 17l99.7 99.7c9.4 9.4 24.6 9.4 33.9 0l28.3-28.3c9.4-9.4 9.4-24.6.1-34zM208 336c-70.7 0-128-57.2-128-128 0-70.7 57.2-128 128-128 70.7 0 128 57.2 128 128 0 70.7-57.2 128-128 128z">
              </path>
            </svg>
          </a>
        </li>
      </button>
    </div>
  </nav>
</template>
  
<script>
export default {
  data() {
    return {
      isShow: false,
    };
  },
};
</script>