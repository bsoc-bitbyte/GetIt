
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
    let found = state.cart.find(product => product.id == item.id);

    if (found) {
      if(found.quantity<5) {
        found.quantity++;
        found.totalPrice = found.quantity*found.price;
      } else {
        this.$toast.show('Sorry, Seller MAX limit <br>  is 5 only ',{
          theme: "toasted-primary", 
          position: "bottom-center", 
          duration : 3000,
          type:'error',
          iconPack:'material',
          icon : 'warning'
        })
      }
        
    } else {
      state.cart.push(item);
      item.quantity=1;
      item.totalPrice=item.price.toFixed(2);
    }
    
    this.$toast.show('Added to Cart',{
      theme: "toasted-primary", 
      position: "bottom-center", 
      duration : 2000,
      type:'success',
      iconPack:'material',
      icon : 'add_shopping_cart'
    })
    this.commit('saveCart');
  },
  removeFromCart(state, item) {
    let index = state.cart.indexOf(item);
    if (index > -1) {  
      state.cart.splice(index, 1);
    }
    this.$toast.show('Removed from Cart',{
      theme: "toasted-primary", 
      position: "bottom-center", 
      duration : 2000,
      type:'error',
      iconPack:'material',
      icon : 'remove_shopping_cart'
    })
    this.commit('saveCart');
  },
  increaseQuantity(state,item) {
    let found = state.cart.find(product => product.id == item.id);
    if(found.quantity<5) {
      found.quantity++;
      found.totalPrice = found.quantity*found.price;
      this.$toast.show('Increased the Quantity',{
        theme: "toasted-primary", 
        position: "bottom-center", 
        duration : 2000,
        type:'info',
        iconPack:'material',
        icon : 'check'
      })
    } else {
      this.$toast.show('Sorry, Seller MAX limit <br> is 5 only ',{
        theme: "toasted-primary", 
        position: "bottom-center", 
        duration : 3000,
        type:'info',
        iconPack:'material',
        icon : 'warning'
      })
    }
    this.commit('saveCart');
  },
  decreaseQuantity(state,item) {
    let found = state.cart.find(product => product.id == item.id);
    if(found.quantity>1) {
      found.quantity--;
      found.totalPrice =found.quantity*found.price.toFixed(2);
      this.$toast.show('Decreased the Quantity',{
        theme: "toasted-primary", 
        position: "bottom-center", 
        duration : 2000,
        type:'info',
        iconPack:'material',
        icon : 'check'
      })
    } 
    this.commit('saveCart');
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