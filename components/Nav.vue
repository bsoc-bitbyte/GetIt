<template>
  <nav class="h-[70px] mb-[5px] mt-[5px]">
    <div class="max-lg:hidden  ml-8 mr-8 top-0">
      <div class="flex flex-row">
        <input class="hidden" type="checkbox" />
        <label class="menu__btn" for="menu__toggle"></label>
        <a href="#"><img class="max-w-none h-6 w-6  inline-block h-[60px] w-[65px] "
                src="https://raw.githubusercontent.com/bsoc-bitbyte/GetIt/10a0fcc39d52d116428dd49505ead2f597e7a30e/assets/get_it.png" /><span
                class="absolute top-[33px]">GetIt</span></a>
        <ul
          class="flex flex-row justify-end content-evenly  w-[100%] flex-nowrap font-sans pl-[2%] pr-[2%] whitespace-nowrap text-xl border-b-[solid] border-b-[#474747] relative">
          
          <li class="text-[#271819] w-[5.5%] top-[-5px] inline-block mr-[1.5%] py-[21px]">
            <a class="py-0.5 hover:border-b-2 hover:border-black h-[30px]" href="#">Home</a>
          </li>
          <li class="text-[#271819] font-sans w-[5.5%] top-[-5px] mr-[1.5%] inline-block  py-[21px]">
            <nuxt-link class=" py-0.5 hover:border-b-2 hover:border-black" to="/products/_id">Shop</nuxt-link>
          </li>
          
          
          <li class=" text-[black] mr-[4%] pr-[20px] py-[0]">
            <a href="#" class="text-[#271819]"><input type="text"
                class=" absolute w-[8%] h-10 font-sans  text-gray-600 text-[20px] pr-[35px] px-3 py-2.5 pb-3 rounded-[100px]  border-[2px] border-gray-400 top-[19px] content-center"
                placeholder="Search" />
              <svg class="absolute ml-[6%]  h-[15px]   top-[30px]" stroke="currentColor" fill="black" stroke-width="0"
                viewBox="0 0 512 512" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg">
                <path
                  d="M505 442.7L405.3 343c-4.5-4.5-10.6-7-17-7H372c27.6-35.3 44-79.7 44-128C416 93.1 322.9 0 208 0S0 93.1 0 208s93.1 208 208 208c48.3 0 92.7-16.4 128-44v16.3c0 6.4 2.5 12.5 7 17l99.7 99.7c9.4 9.4 24.6 9.4 33.9 0l28.3-28.3c9.4-9.4 9.4-24.6.1-34zM208 336c-70.7 0-128-57.2-128-128 0-70.7 57.2-128 128-128 70.7 0 128 57.2 128 128 0 70.7-57.2 128-128 128z">
                </path>
              </svg>
            </a>
          </li>
          <li class="text-[#271819] font-sans w-[5.5%]  top-[-5px] inline-block -ml-12 pl-[9%] py-[19px] mr-[3%]">
            <nuxt-link class=" py-0.5 ml-[28%] hover:border-b-2  hover:border-black" to="/Signin">Sign In</nuxt-link>
          </li>
          <li class="mt-5 ml-[4.5%]">
            <nuxt-link
              class="pl-[15%] pr-[11%] font-sans text-sm py-[12%] pb-[17%] hover:bg-gray-100  border-[solid] border-2 border-gray-400"
              to="/cart">Cart
              <img class="max-w-none h-7 w-8 inline-block fill-black"
                src="https://static.thenounproject.com/png/5645-200.png"></nuxt-link>
          </li>
        </ul>
      </div>
      <div class="hidden"><a href="#">GetIt</a></div>
      <hr class="h-px lg:my-4 my-5 bg-gray-400 border-0 dark:bg-gray-400" />
    </div>

    <div class="lg:hidden pb-14">
      <div class="fixed top-0 w-full bg-white mt-0  shadow-md  z-[9999]">
        <div class="flex flex-row pb-3 pt-2">
          <div class="pl-3"> <span class="sr-only">Open sidebar</span>
            <svg class="h-8 w-8 text-black mt-2" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"
              stroke-linecap="round" stroke-linejoin="round" v-on:click="isShow = !isShow">
              <line x1="3" y1="12" x2="21" y2="12" />
              <line x1="3" y1="6" x2="21" y2="6" />
              <line x1="3" y1="18" x2="21" y2="18" />
            </svg>
          </div>
          <aside v-show="isShow" class="fixed top-0 left-0 shadow-xl z-40 w-60 h-full">
            <div class="h-full px-3 py-4 overflow-y-auto bg-gray-200 dark:bg-gray-800">
              <svg class="h-5 w-5 text-black" width="24" height="24" viewBox="0 0 24 24" stroke-width="2"
                stroke="currentColor" fill="none" stroke-linecap="round" stroke-linejoin="round"
                v-on:click="isShow = !isShow">
                <path stroke="none" d="M0 0h24v24H0z" />
                <line x1="18" y1="6" x2="6" y2="18" />
                <line x1="6" y1="6" x2="18" y2="18" />
              </svg>
              <ul class="space-y-2 text-xl font-medium mt-7 ">
                <li>
                  <a href="#"
                    class="flex font-serif items-center p-2 text-gray-900 rounded-lg dark:text-white hover:bg-gray-300 dark:hover:bg-gray-700">
                    <span class="flex-1 ml-12 whitespace-nowrap">Home</span>
                  </a>
                </li>
                <li>
                  <nuxt-link
                    class=" flex font-serif items-center p-2 text-gray-900 rounded-lg dark:text-white hover:bg-gray-300 dark:hover:bg-gray-700"
                    to="/products/_id"><span class="flex-1 ml-12 whitespace-nowrap">Shop</span></nuxt-link>
                </li>
              
                <li>
                  <nuxt-link
                    class="flex font-serif items-center p-2 text-gray-900 rounded-lg dark:text-white hover:bg-gray-300 dark:hover:bg-gray-700"
                    to="/Signin"><span class="flex-1 ml-12 whitespace-nowrap">Sign In</span></nuxt-link>
                </li>
                <li>
                  <span class="flex"><nuxt-link
                      class="flex-1  font-serif whitespace-nowrap items-center p-2 pl-14 text-gray-900 rounded-lg dark:text-white hover:bg-gray-300 dark:hover:bg-gray-700"
                      to="/cart">10 Items<img class="max-w-none h-7 w-8 -mt-1 inline-block"
                        src="https://static.thenounproject.com/png/5645-200.png" /></nuxt-link></span>
                </li>
              </ul>
            </div>
          </aside>

          <div class="font-[bold] font-sans text-black text-[38px] -mt-2 ml-2 my-0 font-bold">
            <span>GetIt</span>
          </div>
          <li class=" list-none -mt-16">
            <a href="#">
              <input type="text"
                class="absolute w-[140px] h-10 right-[15px] text-[15px] pr-[35px] px-3 py-2.5 rounded-[100px] border-[solid] border-[2px] border-gray-400 top-[15px]"
                placeholder="Search" />
              <svg class="absolute w-[60px] h-[15px] right-[-1px] top-[29px]" stroke="currentColor" fill="grey"
                stroke-width="0" viewBox="0 0 512 512" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg">
                <path
                  d="M505 442.7L405.3 343c-4.5-4.5-10.6-7-17-7H372c27.6-35.3 44-79.7 44-128C416 93.1 322.9 0 208 0S0 93.1 0 208s93.1 208 208 208c48.3 0 92.7-16.4 128-44v16.3c0 6.4 2.5 12.5 7 17l99.7 99.7c9.4 9.4 24.6 9.4 33.9 0l28.3-28.3c9.4-9.4 9.4-24.6.1-34zM208 336c-70.7 0-128-57.2-128-128 0-70.7 57.2-128 128-128 70.7 0 128 57.2 128 128 0 70.7-57.2 128-128 128z">
                </path>
              </svg>
            </a>
          </li>
        </div>
      </div>
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