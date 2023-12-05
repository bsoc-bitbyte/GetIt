
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
    let found = state.cart.find(product => {
      return ((product.id === item.id) && (product.color === item.color)&& (product.size === item.size))
    });

    if (found) {
      found.quantity++;
      found.totalPrice = found.quantity*found.price;  
    } else {
      let temp=item.id+"_"+item.color+"_"+item.size;
      let totalP=item.price.toFixed(2);
      state.cart.push({
        ...item,
        pid: temp,
        quantity: 1,
        totalPrice:totalP,
      });
    }
    this.commit('saveCart');
    this.$toast.show('Added to Cart',{
      theme: "toasted-primary", 
      position: "bottom-center", 
      duration : 2000,
      type:'success',
      iconPack:'material',
      icon : 'add_shopping_cart'
    })
  },
  removeFromCart(state, item) {
    let index = state.cart.indexOf(item);
    if (index > -1) {  
      state.cart.splice(index, 1);
    }
    this.commit('saveCart');
    this.$toast.show('Removed from Cart',{
      theme: "toasted-primary", 
      position: "bottom-center", 
      duration : 2000,
      type:'error',
      iconPack:'material',
      icon : 'remove_shopping_cart'
    })
  },
  increaseQuantity(state,item) {
    let found = state.cart.find(product => product.pid == item.pid);
    if(found) {
      found.quantity++;
      found.totalPrice = found.quantity*found.price;
      this.commit('saveCart');
      this.$toast.show('Increased the Quantity',{
        theme: "toasted-primary", 
        position: "bottom-center", 
        duration : 2000,
        type:'info',
        iconPack:'material',
        icon : 'check'
      })
    }
  },
  decreaseQuantity(state,item) {
    let found = state.cart.find(product => product.pid == item.pid);
    if(found.quantity>1) {
      found.quantity--;
      found.totalPrice =found.quantity*found.price.toFixed(2);
      this.commit('saveCart');
      this.$toast.show('Decreased the Quantity',{
        theme: "toasted-primary", 
        position: "bottom-center", 
        duration : 2000,
        type:'info',
        iconPack:'material',
        icon : 'check'
      })
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