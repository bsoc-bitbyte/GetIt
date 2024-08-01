<template>
  <link rel="icon" type="image/png" href="\favicon.png">
  <div>
    <NavNew />
    <div class="flex gap-5">
      <Sidebar /> 
      <slot />
    </div>
    <Footer />
  </div>
</template>