<template>
  <nav>
    <button class="toggle-button" @click="isOpen = !isOpen">
      <span></span>
      <span></span>
      <span></span>
    </button>
    <ul class="nav-links" :class="{ 'show': isOpen }">
        <li class="pages"><a href="#">Home</a></li>
        <li class="pages"><a href="#">Shop</a></li>
        <li class="pages"><a href="#">About Us</a></li>
        <li class="get_it"><a href="#"><img src="get_it.png"><span>GetIt</span></a></li> 
        <li class="search"><a href="#"><input type="text"  class="s-btn" placeholder="Search...">
          <svg stroke="currentColor" fill="grey" stroke-width="0" viewBox="0 0 512 512" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg"><path d="M505 442.7L405.3 343c-4.5-4.5-10.6-7-17-7H372c27.6-35.3 44-79.7 44-128C416 93.1 322.9 0 208 0S0 93.1 0 208s93.1 208 208 208c48.3 0 92.7-16.4 128-44v16.3c0 6.4 2.5 12.5 7 17l99.7 99.7c9.4 9.4 24.6 9.4 33.9 0l28.3-28.3c9.4-9.4 9.4-24.6.1-34zM208 336c-70.7 0-128-57.2-128-128 0-70.7 57.2-128 128-128 70.7 0 128 57.2 128 128 0 70.7-57.2 128-128 128z">
          </path></svg></a></li> 
        <li class="pages"><a href="#">Sign In</a></li>
        <li class="cart"><a href="#">Cart <img src="cart.png"></a></li>                
    </ul>
  </nav>
</template>

<script>
export default {
  data() {
    return {
      isOpen: false
    };
  }
};
</script>

<style>

nav {
  display: flex;
  align-items: center;
  height: 80px;
  background-color: #F8F8F8;
  padding-left: 10px;
}

img{
  max-width: none;
  height: 20px;
  width: 20px;
  display: inline-block;
}

.get_it {
  font-weight:bold;
  margin: 0 10%;
  font-size: 35px;
}

.get_it img{
  height: 50px;
  width: 60px;
}

.get_it span{
  position: absolute;
  top: 22px;
}

.search {
  margin-right: 26px;
  position: relative;
}

.nav-links{
  width: 100%;
  white-space: nowrap;
  font-family:Arial, Helvetica, sans-serif;
  font-size: 20px;
}

.nav-links li {
  width: 10%;
  display: inline-block;
  padding: 0 3%;
}

.nav-links .cart {
  padding-right: 3%;
}

.nav-links .cart a{
  border: solid ;
  border-width: 2px;
  border-color: black;
  padding: 15% 20% ;
  background-color: #f1f1f1;
  border-radius: 10px ;
}

.nav-links li a {
  padding: 2px 4px;
}

li .s-btn {
    position: absolute;
    width: 120px;
    height: 40px;
    top: -5px;
    right: -40px;
    padding: 10px 12px;
    padding-right: 35px ;
    border-radius: 100px;
    font-size: 15px;
    border: solid rgb(113, 113, 113) 2px;
}

.search svg {
    position: absolute;
    width: 60px;
    height: 55%;
    top: 5px;
    right: -49px;
}

/*hover*/

.pages a:hover  {
  border-bottom: solid 3px rgb(49, 46, 46) ;
  border-radius: 2px;
  transition: ease-in;
  transition-duration: 0.2s;
}

.cart a:hover {
  background-color: rgb(218, 223, 223);
  transition: ease-in-out;
  transition-duration: 0.5s;
}

/*button for media query 900px*/

.toggle-button {
  display: none;
  flex-direction: column;
  justify-content: space-between;
  align-items: center;
  width: 30px;
  height: 21px;
  background-color: transparent;
  border: none;
  cursor: pointer;
  padding: 0;
  z-index: 1;
}

.toggle-button span {
  width: 100%;
  height: 3px;
  background-color: #333;
}

/* media query for 900px */

@media (max-width: 900px) {

  .toggle-button {
    position: absolute;
    display: flex;
    align-self: center;
    left: 50px;
  }
  
  .nav-links {
    display: none;
    flex-direction: column;
    background-color: #ffffff;
    padding: 20px;
  }

  .nav-links.show {
    display: flex;
  }
  
  .nav-links li {
    margin-bottom: 10px;
  }

  .get_it img , .get_it span , .search input , .search svg {
    display: none;
  }

}

</style>
