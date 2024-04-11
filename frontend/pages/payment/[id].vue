<template>

</template>
<script setup>
import { ref, onMounted } from 'vue';
import { useRoute } from 'vue-router';
import { useAuthStore } from '../../store/auth';

const config = useRuntimeConfig();
const route = useRoute();
const orderDetails = ref({});

onMounted(async () => {
    const authStore = useAuthStore();
    try {
        const orderId = route.params.id;
        const token = authStore.authToken;
        const setup = {
          headers: { Authorization: `Bearer ${token}` },
        }
        const response = await $fetch(`${config.public.API_BASE_URL}/api/orders/${orderId}`,setup); 
        console.log(response);

        orderDetails.value = response;
        console.log(orderDetails.value);

    } catch (error) {
        console.error('Error fetching order data', error);
    }
});

</script>

<style scoped>
.dropdown-title svg {
    transition: transform 0.3s;
}

.rotate-180 {
    transform: rotate(180deg);
}
</style>
