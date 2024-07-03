<template>
  <div>
    <Navbar/>
    <slot />
    <Footer/>
  </div>
</template>

<script>
import Navbar from '@/components/NavNew.vue';
import Footer from '~/components/Footer.vue';
export default {
components: {
  Navbar,
  Footer
},
}
</script>