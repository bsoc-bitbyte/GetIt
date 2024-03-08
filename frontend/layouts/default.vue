<template>
  <div>
    <Navbar />
    <AppHeader />
    <Nuxt />
  </div>
</template>

<script>
// import Navbar from '@/components/Nav.vue';
import Navbar from '@/components/NavNew.vue';
export default {
  components: {
    Navbar
  },
}
</script>