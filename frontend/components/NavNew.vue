
<template>
  <section class="sticky top-0 bg-white z-50 mx-auto w-full Mulish">
      <!-- navbar -->
      <nav class="flex justify-between max-lg:hidden border-b border-gray-[#D9D9D9] border-b-[2.5px] h-[90px] px-6">
          <div class="px-5 xl:px-12 py-4 flex w-full items-center">
              <nuxt-link class="text-4xl font-medium flex items-center w-[124px] h-[55px] PalanquinDark" to="/">
                  <img class="h-10"
                      src="https://raw.githubusercontent.com/bsoc-bitbyte/GetIt/10a0fcc39d52d116428dd49505ead2f597e7a30e/assets/get_it.png"
                      alt="logo">
                  GetIt
              </nuxt-link>
              <!-- Nav Links -->
              <ul class="hidden md:flex px-4 mx-auto font-semibold font-heading space-x-12 text-[#6C6C6C] Mulish flex gap-4">
                  <li><nuxt-link class="hover:border-b-[2.5px] py-[4px] border-[#ea454c]" to="/">Home</nuxt-link></li>
                  <li><nuxt-link class="hover:border-b-[2.5px] py-[4px] border-[#ea454c]" to="/productList">Products</nuxt-link></li>
                  <li><nuxt-link class="hover:border-b-[2.5px] py-[4px] border-[#ea454c]" to="/eventList">Events</nuxt-link></li>
               </ul>

              <div class="flex gap-8 font-semibold font-heading items-center h-[27px]">

                  <nuxt-link class=" flex items-center" to="/cart">
                      <img src="../assets/cart03.svg" alt="carticon" class="h-[27px] w-[28px]">
                      <span class="flex absolute -mt-5 ml-4 " v-if="cartQuantity >= 1">
                          <span
                              class="animate-ping absolute inline-flex h-5 w-5 rounded-full bg-[#ea454c] opacity-75"></span>
                          <span
                              class="relative rounded-full h-5 w-5 p-2 bg-[#ea454c] flex items-center justify-center text-gray-200">{{ cartQuantity }}
                          </span>
                      </span>
                  </nuxt-link>

                    <div v-if="isAuthenticated" >
                        <button @click="toggle_profile" class="ml-1 mr-5 rounded-[1000px] h-[53px] w-[53px] flex items-center justify-center icon">                    
                        <img src="../assets/user_icon.svg" alt="usericon" class="h-[26px] w-[25px]">
                        </button>

                        <div :class="showprofile ? 'opacity-100': 'opacity-0'" class="transition-all duration-500" >
                             
                            <div v-show="showprofile" class=" w-[231px] fixed bg-white right-28 top-[100px] rounded-md shadow-md flex flex-col px-5 py-1 poppins font-light text-base z-[9999]" >
                            
                                <div class="w-full min-h-[95px]  items-start justify-center flex flex-col" >
                                    <h3 class="font-semibold">{{name}}</h3>
                                    <p class="text-xs text-balance w-full break-words ">{{email}}</p>
                                </div>
                                <div @click="toggle_profile">
                                    <nuxt-link class="w-full h-[47px] flex items-center justify-start border-t-[1px] border-b-[1px] gap-3" to="/order" >
                                        <img src="../assets/orders.svg" alt="orders" class="h-[22px] w-[24px] bg-white">
                                        <p>Your orders</p>
                                    </nuxt-link>
                                    <nuxt-link v-if="isAdmin" class="w-full h-[47px] flex items-center justify-start border-t-[1px] border-b-[1px] gap-3" to="/addNewProduct" >
                                        <img src="../assets/admin_icon.svg" alt="adminicon" class="h-[22px] w-[24px] bg-white">
                                        <p>Admin Dashboard</p>
                                    </nuxt-link>
                                    <button class="w-full h-[47px] flex items-center justify-start" @click="handleLogout" >
                                        <img src="../assets/logout.svg" alt="logouticon" class="h-[22px] w-[24px] absolute left-5">
                                        <p class="w-full p-0 flex px-9 justify-start">Logout</p>
                                    </button>
                                </div>
                            </div>
                            <div v-show="showprofile" class="h-screen w-screen bg-transparent fixed right-0 top-0 " @click="toggle_profile"></div>
                        </div>
                    </div>
                     
                    <button v-else class=" p-2 flex gap-2 text-[#6C6C6C]" @click="handleLogin">
                        <img src="../assets/sign_in.svg" alt="signinicon" class="h-[26px] w-[25px]">
                        Sign In
                    </button>
              </div>
          </div>
      </nav>
      <div class="lg:hidden pb-14">
          <div class="fixed top-0 w-full bg-white mt-0 shadow-md z-[9999] px-2">
              <div class="flex flex-row justify-between px-3 py-2">
                  <div> <span class="sr-only">Open sidebar</span>
                      <div class="hamburger-menu" @click="toggle" :class="{ open: isShow}">
                          <span class="line line-1"></span>
                          <span class="line line-2"></span>
                          <span class="line line-3"></span>
                      </div>
                  </div>
                  <aside  class="fixed mt-10 shadow-xl z-40 w-60 h-full"  :class="{open:isShow}">
                      <div class="h-full px-3 py-4 overflow-y-auto bg-white ">
                          <ul class="flex flex-col gap-4 w-full justify-center text-xl font-medium mt-5">

                              <li
                                  class="w-full flex justify-center border-b-2 hover:border-b-2 hover:border-[#ea454c] border-white">
                                  <nuxt-link to="/" @click="toggle">Home</nuxt-link>
                                  
                              </li>
                              <li
                                  class="w-full flex justify-center border-b-2 hover:border-b-2 hover:border-[#ea454c] border-white">
                                  <nuxt-link to="/eventList" @click="toggle">Events</nuxt-link>
                              </li>
                              <li
                                  class="w-full flex justify-center border-b-2 hover:border-b-2 hover:border-[#ea454c] border-white">
                                  <nuxt-link to="/order" @click="toggle">My Orders</nuxt-link>
                              </li>
                              <li
                                  class="w-full flex justify-center border-b-2 hover:border-b-2 hover:border-[#ea454c] border-white">

                                  <button v-if="isAuthenticated"
                                      @click="handleLogout">Sign Out</button>
                                  <button v-else @click="handleLogin">Sign In</button>
                                  
                              </li>
                          </ul>
                      </div>
                  </aside>
                  <nuxt-link class="text-3xl font-bold flex items-center" to="/">
                      <img class="h-9"
                          src="https://raw.githubusercontent.com/bsoc-bitbyte/GetIt/10a0fcc39d52d116428dd49505ead2f597e7a30e/assets/get_it.png"
                          alt="logo">
                      GetIt
                  </nuxt-link>
                  <div class="flex xl:hidden items-center space-x-5 ">
                      <nuxt-link class="flex items-center hover:text-gray-500" to="/cart">
                          <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6 mr-3" fill="none" viewBox="0 0 24 24"
                              stroke="currentColor">
                              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                                  d="M3 3h2l.4 2M7 13h10l4-8H5.4M7 13L5.4 5M7 13l-2.293 2.293c-.63.63-.184 1.707.707 1.707H17m0 0a2 2 0 100 4 2 2 0 000-4zm-8 2a2 2 0 11-4 0 2 2 0 014 0z" />
                          </svg>
                          <span class="flex absolute -mt-5 ml-4" v-if="cartQuantity >= 1">
                              <span
                                  class="animate-ping absolute inline-flex h-5 w-5 rounded-full bg-[#ea454c] opacity-75"></span>
                              <span
                                  class="relative rounded-full h-5 w-5 p-2 bg-[#ea454c] flex items-center justify-center text-gray-200">{{
                                  cartQuantity}}
                              </span>
                          </span>
                      </nuxt-link>
                  </div>
              </div>
          </div>
      </div>
  </section>

</template>

<script>
import { computed,ref ,onMounted} from 'vue'
import { useCartStore } from '../store/index'
import { useAuthStore } from '../store/auth'
import { toast } from 'vue3-toastify';
import { extractPath } from '~/utils/url';
import { navigateTo } from 'nuxt/app';
import { useNuxtApp } from "#app";

export default {
  setup() {
    const isAdmin = ref(false)
    const name = ref()
    const email = ref()
    const config = useRuntimeConfig();
    const showprofile = ref(false)
    const cartStore = useCartStore()
    const authStore = useAuthStore()

    const cartQuantity = computed(() => cartStore.getQty)
    const isShow = ref(false);
    const isAuthenticated = computed(() => authStore.isAuthenticated)

    const fetchUserData = async () => {
      const nuxtApp = useNuxtApp();
        const response = await nuxtApp.$authenticatedFetch(
          `${config.public.API_BASE_URL}/api/accounts/me/`
        );
        name.value = response.first_name;
        email.value = response.email;
        isAdmin.value = response.is_admin;
    };

    const handleLogout = () => {
        toggle();
        authStore.logout();
        toast.error("Logged out",{
            autoClose: 2000,
            position:  toast.POSITION.BOTTOM_CENTER
        })
    }

    const toggle = () => {
      isShow.value = !isShow.value;
    }
    const handleLogin = async() => {
        toggle();
        const encodedValue = window.location.href;
        const path = extractPath(encodedValue);
        const redirectUrl = `/Signin?redirect=${path}`;
        await navigateTo(redirectUrl);
    }
    
    const toggle_profile=()=>{
        fetchUserData()
        showprofile.value = !showprofile.value
    }
    onMounted(() => fetchUserData());

    return {
      cartQuantity,
      isAuthenticated,
      handleLogout,
      isShow,
      toggle,
      handleLogin,
      name,
      email,
      showprofile,
      toggle_profile,
      isAdmin
    }
  }
  


};
</script>


<style>
@import url('https://fonts.googleapis.com/css2?family=Palanquin+Dark:wght@400;500;600;700&display=swap');
@import url('https://fonts.googleapis.com/css2?family=Mulish:ital,wght@0,200..1000;1,200..1000&display=swap');
.Mulish{
     
    font-family: "Mulish", sans-serif;
    font-smooth: always;
      
}
.PalanquinDark{
    font-family: "Palanquin Dark", sans-serif;
    font-smooth: always;
}
.poppins {
    font-family: "Poppins", sans-serif;
    font-smooth: always;
  }
.icon:hover {
    box-shadow: 0px 0px 6px 2px rgb(0 0 0 / 0.1);
}
aside {

position: fixed;
left: -100%;
transition: left 0.3s ease-in-out;
}
aside.open {
left: 0;
}
.hamburger-menu {
width: 25px;
height: 20px;
position: relative;
cursor: pointer;
}
.hamburger-menu.open {
z-index: 100;
}

.line {
width: 100%;
height: 3px;
background-color: #363131;
display: block;
position: absolute;
transition: all 0.3s ease-in-out;
}

.line-1 { top: 5px; }
.line-2 { top: 12px; }
.line-3 { top: 19px; }
.hamburger-menu.open .line-1 {
transform: rotate(45deg) translate(4px, 6px);
}

.hamburger-menu.open .line-2 {
opacity: 0;
}

.hamburger-menu.open .line-3 {
transform: rotate(-45deg) translate(4px, -6px);
}</style>
