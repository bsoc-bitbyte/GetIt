
if(process.browser) {
	var cart = window.localStorage.getItem('cart');
}
export const state =() => ({
  cart: (cart ? JSON.parse(cart) :[]) 
});   
export const getters = {
  cartCount(state) {
    return state.cart.length
  }
}
export const mutations = 	{
  addToCart(state, item) {
    state.cart.push(item);
    this.commit('saveCart');
  },
  removeFromCart(state, item) {
    let index = state.cart.indexOf(item);
    if (index > -1) {
              //let product = state.cart[index];  
      state.cart.splice(index, 1);
      this.commit('saveCart');
    }
  },
  saveCart(state) {
    if(process.browser) {
      window.localStorage.setItem('cart', JSON.stringify(state.cart));
    }
  },
  setCart(state, cartData) {
    state.cart = cartData;
  }
};
export const persistent = true;