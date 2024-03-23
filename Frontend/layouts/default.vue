<template>
    <div>
      <Navbar/>
      <slot />
    </div>
  </template>

<script>
import Navbar from '@/components/NavNew.vue';
export default {
  components: {
    Navbar
  },
}
</script>