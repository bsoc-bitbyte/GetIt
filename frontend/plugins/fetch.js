import { useAuthStore } from "../store/auth";

export default defineNuxtPlugin(nuxtApp => {
  nuxtApp.provide('authenticatedFetch', async (url, options = {}) => {
    console.log("comming")
    const authStore = useAuthStore();

    if (authStore.tokenNeedsRefresh()) {
      try {
        await authStore.refreshToken();
        options.headers = { ...options.headers, Authorization: `Bearer ${authStore.access}` };
      } catch (error) {
        authStore.logout();
        return { error: 'Authentication failed, please login again.' };
      }
    } else {
      options.headers = { ...options.headers, Authorization: `Bearer ${authStore.access}` };
    }

    return await $fetch(url, options);
  });
});
