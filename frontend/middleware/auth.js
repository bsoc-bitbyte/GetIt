import { defineNuxtRouteMiddleware, navigateTo, useNuxtApp, useRuntimeConfig } from "nuxt/app";
import { useAuthStore } from "../store/auth";
import { ref } from "vue";



export default defineNuxtRouteMiddleware((to,from)=>{
    const authStore = useAuthStore();
    const config = useRuntimeConfig();
    const isAdmin = ref(false);    

    const fetchUserData = async () => {
        const nuxtApp = useNuxtApp();
          const response = await nuxtApp.$authenticatedFetch(
            `${config.public.API_BASE_URL}/api/accounts/me/`
          );
          isAdmin.value = response.is_admin;
          if(!isAdmin.value){
              return navigateTo("/404");
          }
      };
    
    if(!authStore.isAuthenticated){ 
        return navigateTo("/404");
    }   
    else{
        fetchUserData();
    }
    
})
