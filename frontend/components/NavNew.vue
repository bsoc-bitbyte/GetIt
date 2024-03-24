<template>
    <section class="relative mx-auto">
        <!-- navbar -->
        <nav class="flex justify-between max-lg:hidden border-b border-gray-400 ">
            <div class="px-5 xl:px-12 py-4 flex w-full items-center">
                <nuxt-link class="text-3xl font-bold flex items-center" to="/">
                    <img class="h-9"
                        src="https://raw.githubusercontent.com/bsoc-bitbyte/GetIt/10a0fcc39d52d116428dd49505ead2f597e7a30e/assets/get_it.png"
                        alt="logo">
                    GetIt
                </nuxt-link>
                <!-- Nav Links -->
                <ul class="hidden md:flex px-4 mx-auto font-semibold font-heading space-x-12">
                    <li><nuxt-link class="hover:border-b-2 border-[#ea454c]" to="/">Home</nuxt-link></li>
                    <li><nuxt-link class="hover:border-b-2 border-[#ea454c]" to="/eventList">Events</nuxt-link></li>
                </ul>

                <div class="flex gap-6 font-semibold font-heading items-center">
                    <nuxt-link class="flex items-center border-b-2 border-white hover:border-[#ea454c]" to="/cart">
                        <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="none" viewBox="0 0 24 24"
                            stroke="currentColor">
                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                                d="M3 3h2l.4 2M7 13h10l4-8H5.4M7 13L5.4 5M7 13l-2.293 2.293c-.63.63-.184 1.707.707 1.707H17m0 0a2 2 0 100 4 2 2 0 000-4zm-8 2a2 2 0 11-4 0 2 2 0 014 0z" />
                        </svg>
                        <span class="flex absolute -mt-5 ml-4" v-if="$store.getters['getQty'] >= 1">
                            <span
                                class="animate-ping absolute inline-flex h-5 w-5 rounded-full bg-[#ea454c] opacity-75"></span>
                            <span
                                class="relative rounded-full h-5 w-5 p-2 bg-[#ea454c] flex items-center justify-center text-gray-200">{{
                            $store.getters['getQty'] }}
                            </span>
                        </span>
                        Cart
                    </nuxt-link>

                    <button v-if="isAuth" class=" bg-[#ea454c] p-2 rounded-2xl text-white" to="/"
                        @click="handleLogout">Sign Out</button>

                    <nuxt-link v-else class="bg-[#ea454c] p-2 rounded-2xl text-white" to="/Signin">Sign In</nuxt-link>
                </div>
            </div>
        </nav>
        <div class="lg:hidden pb-14">
            <div class="fixed top-0 w-full bg-white mt-0 shadow-md z-[9999] px-2">
                <div class="flex flex-row justify-between px-3 py-2">
                    <div> <span class="sr-only">Open sidebar</span>
                        <svg class="h-8 w-8 text-black mt-2" viewBox="0 0 24 24" fill="none" stroke="currentColor"
                            stroke-width="2" stroke-linecap="round" stroke-linejoin="round"
                            v-on:click="isShow = !isShow">
                            <line x1="3" y1="12" x2="21" y2="12" />
                            <line x1="3" y1="6" x2="21" y2="6" />
                            <line x1="3" y1="18" x2="21" y2="18" />
                        </svg>
                    </div>
                    <aside v-show="isShow" class="fixed top-0 left-0 shadow-xl z-40 w-60 h-full">
                        <div class="h-full px-3 py-4 overflow-y-auto bg-white ">
                            <svg class="h-6 w-6 text-black" width="30" height="30" viewBox="0 0 24 24" stroke-width="2"
                                stroke="currentColor" fill="none" stroke-linecap="round" stroke-linejoin="round"
                                v-on:click="isShow = !isShow">
                                <path stroke="none" d="M0 0h24v24H0z" />
                                <line x1="18" y1="6" x2="6" y2="18" />
                                <line x1="6" y1="6" x2="18" y2="18" />
                            </svg>
                            <ul class="flex flex-col gap-4 w-full justify-center text-xl font-medium mt-5">

                                <li
                                    class="w-full flex justify-center border-b-2 hover:border-b-2 hover:border-[#ea454c] border-white">
                                    <nuxt-link to="/">Home</nuxt-link>
                                </li>
                                <li
                                    class="w-full flex justify-center border-b-2 hover:border-b-2 hover:border-[#ea454c] border-white">
                                    <nuxt-link to="/">Events</nuxt-link>
                                </li>
                                <li
                                    class="w-full flex justify-center border-b-2 hover:border-b-2 hover:border-[#ea454c] border-white">

                                    <button v-if="isAuth" 
                                        @click="handleLogout">Sign Out</button>
                                    <nuxt-link v-else to="/Signin">Sign In</nuxt-link>
                                </li>
                            </ul>
                        </div>
                    </aside>
                    <nuxt-link class="text-3xl font-bold flex items-center" to="/eventlist">
                        <img class="h-9"
                            src="https://raw.githubusercontent.com/bsoc-bitbyte/GetIt/10a0fcc39d52d116428dd49505ead2f597e7a30e/assets/get_it.png"
                            alt="logo">
                        GetIt
                    </nuxt-link>
                    <div class="flex xl:hidden items-center space-x-5 ">
                        <nuxt-link class="flex items-center hover:text-gray-500" to="/cart">
                            <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="none" viewBox="0 0 24 24"
                                stroke="currentColor">
                                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                                    d="M3 3h2l.4 2M7 13h10l4-8H5.4M7 13L5.4 5M7 13l-2.293 2.293c-.63.63-.184 1.707.707 1.707H17m0 0a2 2 0 100 4 2 2 0 000-4zm-8 2a2 2 0 11-4 0 2 2 0 014 0z" />
                            </svg>
                            <span class="flex absolute -mt-5 ml-4" v-if="$store.getters['getQty'] >= 1">
                                <span
                                    class="animate-ping absolute inline-flex h-5 w-5 rounded-full bg-[#ea454c] opacity-75"></span>
                                <span
                                    class="relative rounded-full h-5 w-5 p-2 bg-[#ea454c] flex items-center justify-center text-gray-200">{{
                            $store.getters['getQty'] }}
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
export default {
    data() {
        return {
            isShow: false,
            qty: 0,

        };
    },
    computed: {
        isAuth() {
            return this.$store.getters['auth/isAuthenticated']
        }

    },
    methods: {
        handleLogout() {
            this.$store.dispatch('auth/logout')
            this.$toast.show('Logged Out Successfully', {
                theme: "toasted-primary",
                position: "bottom-center",
                duration: 2000,
                type: "success",
                iconPack: "material",
                icon: "logout",
            })
        }
    },
};
</script>
