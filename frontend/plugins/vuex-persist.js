export default ({ store }) => {
  if (process.client) {
    window.onNuxtReady(() => {
      // Load cart data from localStorage, if available
      const cartData = localStorage.getItem('cart');
     
      if (cartData) {
        store.commit('setCart', JSON.parse(cartData));
      }

      // Save the cart data to localStorage whenever the cart state changes
      store.subscribe((mutation, state) => {
        if (mutation.type === 'setCart') {
          localStorage.setItem('cart', JSON.stringify(state.cart));
        }
      });
    });
  }
};