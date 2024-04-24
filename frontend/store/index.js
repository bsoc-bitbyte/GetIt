import { defineStore } from 'pinia';
import { toast } from 'vue3-toastify';


export const useCartStore = defineStore({
  id: 'cart',
  state: () => ({
    cart: process.browser ? JSON.parse(window.localStorage.getItem("cart")) || [] : []
  }),
  getters: {
    cartCount() {
      return this.cart.length;
    },
    getQty() {
      return this.cart.reduce((qty, item) => qty + item.quantity, 0);
    },
    getPrice() {
      return this.cart.reduce((price, item) => price + item.quantity * item.ticket_price, 0);
    }
  },
  actions: {
    addToCart(item) {
      const found = this.cart.find(product => product.id === item.id);
      if (found) {
        console.log("found")
        toast.error("Item already added", {
          autoClose: 2000,
          position: toast.POSITION.BOTTOM_CENTER,

        });
      } else {
        this.cart.push({
          ...item,
          quantity: 1,
          totalPrice: item.ticket_price
        });
        toast.success("Added to Cart", {
          autoClose: 2000,
          position: toast.POSITION.BOTTOM_CENTER,
        });
      }
      this.saveCart();
    },
    removeFromCart(item) {
      const index = this.cart.indexOf(item);
      if (index > -1) {
        this.cart.splice(index, 1);
      }
      this.saveCart();
      toast.error("Removed from cart", {
        autoClose: 2000,
        position: toast.POSITION.BOTTOM_CENTER,
      });
    },
    increaseQuantity(item) {
      if (!item.id) {
        const found = this.cart.find(product => product.id === item.id);
        if (found) {
          toast.error("Item already added", {
            autoClose: 2000,
            position: toast.POSITION.BOTTOM_CENTER,
          });
        } else {
          this.cart.push({
            ...item,
            quantity: 1,
            totalPrice: item.ticket_price,
          });
          toast.success("Added to Cart", {
            autoClose: 2000,
            position: toast.POSITION.BOTTOM_CENTER,
          });
        }
        this.saveCart();
      } else {
        const found = this.cart.find(product => product.id === item.id);
        if (found) {
          found.quantity++;
          found.totalPrice = found.quantity * found.ticket_price;
          this.saveCart();
          toast.success("Increased the quantity", {
          autoClose: 2000,
          position: toast.POSITION.BOTTOM_CENTER,
        });
        }
      }
    },
    decreaseQuantity(item) {
      const found = this.cart.find(product => product.id === item.id);
      if (found && found.quantity > 1) {
        found.quantity--;
        found.totalPrice = found.quantity * found.ticket_price;
        this.saveCart();
        toast.error("Decreased the Quantity", {
          autoClose: 2000,
          position: toast.POSITION.BOTTOM_CENTER,
        });
      }
    },
    saveCart() {
      if (process.browser) {
        window.localStorage.setItem("cart", JSON.stringify(this.cart));
      }
    },
    setCart(cartData) {
      this.cart = cartData;
    },
    clearCart(){
      this.setCart([]);
      this.saveCart();
    },
  },
  persist: true,
});

