<template>
    <div class="flex flex-col items-center justify-center h-[80svh] gap-4">
        <p class="font-semibold text-4xl">{{ activationStatus }}</p>
    </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import { useRouter } from "vue-router";

const config = useRuntimeConfig();
const activationStatus = ref('');
const router = useRouter();


async function activateUser() {
    const urlParams = new URLSearchParams(window.location.search);
    const uuid = urlParams.get('uuid');
    const token = urlParams.get('token');
    let status = '';
    try {
        const response = await $fetch(`${config.public.API_BASE_URL}/api/accounts/activate/${uuid}/${token}`);
        status = await response.text();
        if (response.type === '200') {
            router.push({ path: '/signin', query: { msg: 'account activated' } });
        }
    } catch (error) {
        console.error(error);
        status = 'Activation failed';
    }

    return status;
}

onMounted(async () => {
    const status = await activateUser();
    activationStatus.value = status +' !!';
});
</script>
