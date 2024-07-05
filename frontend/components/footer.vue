<template>
    <footer class="">
        <div class="mx-auto lg:my-0 w-4/5 p-4 py-6 lg:py-8">
            <hr class="mt-8 mb-6 border-gray-500 sm:mx-auto lg:mt-6" />
            <div class="min-[800px]:flex min-[800px]:items-center min-[800px]:justify-between">
                <div class="flex-wrap md:justify-start md:text-start text-center">
                    <div class="inline-block mr-10 mb-6 text-sm text-gray-500"><nuxt-link  class="hover:underline" to="/productList">Products</nuxt-link></div>
                    <div class="inline-block mb-6 text-sm text-gray-500"><nuxt-link  class="hover:underline" to="/eventlist">Events</nuxt-link></div>
                    <div class="flex md:justify-start justify-center text-xs text-gray-500 items-center"><p class="text-2xl inline mr-2">©</p><nuxt-link  class="hover:underline " to="/">Getit 2024</nuxt-link>. All rights reserved
                    </div>
                </div>
                
                <nuxt-link class="justify-center text-3xl font-bold flex items-center text-black md:m-4 m-6" to="/">
                    <img class="h-12"
                        src="../assets/get_it.png"
                        alt="logo">
                      GetIt
                </nuxt-link>
                <div class="sm:flex-col sm:items-center">
                    <div class="flex md:justify-end justify-center mb-6">
                        <a href="https://github.com/bsoc-bitbyte/GetIt/issues/new?assignees=&labels=bug&projects=&template=1_bug_report_form.yml&title=%5BBUG%5D%3A+" target="_blank" class="text-sm text-gray-500 underline hover:text-gray-900 mr-4">
                            <img src="../assets/bug.svg" class="inline mr-2" />Report a bug
                        </a>

                        <button @click="handleEditPage" class="text-sm text-gray-500 underline hover:text-gray-900 ms-5">
                            <img src="../assets/githubCat.svg" class="inline mr-2" />Edit this page
                        </button>
                    </div>

                    <div class="flex md:justify-end justify-center">
                        <a href="https://discord.com/invite/W6crw7ajSs" target="_blank" class="text-sm text-gray-500 underline hover:text-gray-900 mr-4">
                            <img src="../assets/discord.svg" class="inline mr-2" />Join our discord
                        </a>

                        <a href="mailto:theprogclub@iiitdmj.ac.in" class="text-sm text-gray-500 underline hover:text-gray-900 ms-5">
                            <img src="../assets/mail.svg" class="inline mr-2" />Mail
                        </a>
                    </div>
                </div>
            </div>
        </div>
    </footer>
</template>

<script>
import { navigateTo, useRequestURL} from 'nuxt/app';
export default {
    setup(){
        const handleEditPage = async()=>{
            let url = useRequestURL().pathname;
            if(url==='/')url="/index"
            if(url==='/eventlist')url="/eventList"
            if(url==='/checkout')url="/checkOut"
            const redirectUrl = `https://github.com/bsoc-bitbyte/GetIt/tree/main/frontend/pages${url}.vue`;
            await navigateTo(redirectUrl, {
                open: {
                    target: '_blank',
                },
                external: true
            })
        }
        return{
            handleEditPage,
        }
    }
}
</script>