<template>
  <link rel="icon" type="image/png" href="\favicon.png">
  <div>
    <Navbar/>
    <slot />
    <Footer/>
  </div>
</template>

<script>
import Navbar from '@/components/NavNew.vue';
import Footer from '~/components/footer.vue';
export default {
components: {
  Navbar,
  Footer
},
}
</script>