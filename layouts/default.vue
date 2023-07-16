<template>
    <div>
      <Navbar />
      <AppHeader />
      <Nuxt />
    </div>
  </template>

<script>
import Navbar from '@/components/Nav.vue';
export default {
    components: {
    Navbar
  },
}
</script>