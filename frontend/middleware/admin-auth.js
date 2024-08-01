import { defineNuxtRouteMiddleware, navigateTo } from "nuxt/app";
import { useAuthStore } from "../store/auth";

export default defineNuxtRouteMiddleware((to,from)=>{
    const authStore = useAuthStore();    
    if(!authStore.isAuthenticated){ 
        return navigateTo("/404");
    }   
    else{
        if(!authStore.is_Admin){
            return navigateTo("/404");
        }
    }
})
