<template>
  <nav>
  <div class="hamburger-menu">
    <input id="menu__toggle" type="checkbox" />
    <label class="menu__btn" for="menu__toggle">
      <span></span>
    </label>

    <ul class="nav-links" > 
        <li class="nav-link"><a href="#">Home</a></li>
        <li class="nav-link"><a href="#">Shop</a></li>
        <li class="nav-link"><a href="#">About Us</a></li>
        <li class="get_it"><a href="#"><img src="../assets/get_it.png"><span>GetIt</span></a></li> 
        <li class="nav-link"><a href="#" class="sign_in">Sign In</a></li>
        <li class="cart"><a href="#">Cart <img src="../assets/cart.png"></a></li>                
    </ul>
    </div>
    
    <li class="search"><a href="#"><input type="text"  class="s-btn" placeholder="Search...">
    <svg stroke="currentColor" fill="grey" stroke-width="0" viewBox="0 0 512 512" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg"><path d="M505 442.7L405.3 343c-4.5-4.5-10.6-7-17-7H372c27.6-35.3 44-79.7 44-128C416 93.1 322.9 0 208 0S0 93.1 0 208s93.1 208 208 208c48.3 0 92.7-16.4 128-44v16.3c0 6.4 2.5 12.5 7 17l99.7 99.7c9.4 9.4 24.6 9.4 33.9 0l28.3-28.3c9.4-9.4 9.4-24.6.1-34zM208 336c-70.7 0-128-57.2-128-128 0-70.7 57.2-128 128-128 70.7 0 128 57.2 128 128 0 70.7-57.2 128-128 128z">
    </path></svg></a>
    </li>
    <div class="text"><a href="#">GetIt</a></div>

  </nav>
</template>

<style>

#menu__toggle {
  display: none;
}

img{
  max-width: none;
  height: 20px;
  width: 20px;
  display: inline-block;
}

.get_it {
  font-weight:bold;
  margin: 0 23%;
  margin-left: 8%;
  font-size: 35px;
}

.get_it img{
  height: 55px;
  width: 60px;
}

.get_it span{
  position: absolute;
  top: 26px;
}

.search {
  margin-left: 70%;
  position: fixed;
}

.nav-links{
  position: fixed;
  width: 100%;
  white-space: nowrap;
  font-family:Arial, Helvetica, sans-serif;
  font-size: 20px;
  border-bottom: solid thin #474747;
}

.nav-links li {
  font-family: Poppins;
  color:  #271819;
  width: 10.5%;
  top: -5px;
  display: inline-block;
  padding: 19px 3%;
}

.nav-links .cart {
  padding-right: 3%;
}

.nav-links .cart a{
  border: solid ;
  border-width: 2px;
  border-color: black;
  padding: 15% 20% ;
  border-radius: 10px ;
}

.nav-links li a {
  padding: 2px 4px;
}

li.search {
  list-style-type: none;
}

li .s-btn {
  position: absolute;
  width: 120px;
  height: 40px;
  top: 30px;
  right: -55px;
  padding: 10px 12px;
  padding-right: 35px ;
  border-radius: 100px;
  font-size: 15px;
  border: solid rgb(113, 113, 113) 2px;
}

.search svg {
  position: absolute;
  width: 60px;
  height: 15px;
  top: 41px;
  right: -65px;
}

a.sign_in {
  margin-left: 28%;
}

.text {
  display: none;
}

/*hover effects*/

.nav-link a:hover  {
  border-bottom: solid 3px rgb(49, 46, 46) ;
  border-radius: 2px;
  transition: ease-in;
  transition-duration: 0.2s;
}

.cart a:hover {
  background-color: #ECEFF1;
  transition: ease-in-out;
  transition-duration: 0.5s;
}


/* media query for 900px */

@media (max-width: 900px) {

  /* hamburger menu */
  
  #menu__toggle {
    opacity: 0;
  }

  #menu__toggle:checked + .menu__btn > span {
    transform: rotate(45deg);
  }

  #menu__toggle:checked + .menu__btn > span::before {
    top: 0;
    transform: rotate(0deg);
  }

  #menu__toggle:checked + .menu__btn > span::after {
    top: 0;
    transform: rotate(90deg);
  }

  #menu__toggle:checked ~ .nav-links {
    left: 0 !important;
  }

  .menu__btn {
    position: fixed;
    top: 40px;
    left: 20px;
    width: 25px;
    cursor: pointer;
    z-index: 1;
  }

  .menu__btn > span,
  .menu__btn > span::before,
  .menu__btn > span::after {
    display: block;
    position: absolute;
    width: 100%;
    height: 2px;
    background-color: #616161;
    transition-duration: .25s;
  }

  .menu__btn > span::before {
    content: '';
    top: -8px;
  }

  .menu__btn > span::after {
    content: '';
    top: 8px;
  }

  /* hamburger menu done */

  .text {
    display:inline-block;
  }

  .text a {
    position: fixed;
    font-size: 35px;
    color: #271819;
    font-weight: bold;
    font-family: Poppins;
    margin-left: 60px;
    margin-top: -3px;
    z-index: -1;
  }

  .nav-links {
    display: block;
    position: fixed;
    top: 0;
    left: -100%;
    width: 200px;
    height: 100%;
    margin: 0;
    padding: 80px 0;
    background-color: #ECEFF1;
    box-shadow: 2px 2px 6px rgba(0, 0, 0, .4);
    transition-duration: .25s;
  }

  .nav-links li{
    display: flex;
    flex-direction: column;
    color: #333;
    font-size: 20px;
    font-weight: 600;
    text-decoration: none;
    transition-duration: .25s;
    width: 100%;
    position: relative;
    padding: 12px 52px;
  }

  .nav-link:hover {
    background-color: #CFD8DC;
  }
  
  li.get_it {
    display: none;
  }

  .nav-links .cart a{
    border: none ;
    background-color: inherit;
    padding: 0;
    padding-left: 3px;
    margin: 0;
  }

  li.search {
    right: 65px;
    top: -10px;
    list-style: none;
    height: 40px;
    z-index: -1;
  }
  
  li .s-btn {
    width: 140px;
  }

  .search svg {
    position: absolute;
    width: 60px;
    height: 18px;
    top: 40px;
    right: -60px;
  }

  a.sign_in {
    margin-left: 0;
  }

  /* hover effects */

  .nav-links li:hover {
    background-color: #CFD8DC;
    transition: ease-in-out;
    transition-duration: 0.5s;
  }
  
  .nav-link a:hover  {
    border-bottom: none;
  }  

}

/* media query for 280px */

@media (max-width: 280px) {

  li .s-btn {
    width: 120px;
  }

  .menu__btn {
    left: 10px;
  }

  .nav-links {
    width: 144px;
    height: 100%;
  }

  li.nav-link {
    left: 0;
    padding-left: 30px;
    
  }

  .nav-links .cart {
    padding-left: 30px;
  }

  .text a{
    margin-left: 50px;
    font-size: 35px;
  }

}

</style>
