<template>
  <div class="main zoom md:flex bg-gray-100 md:justify-evenly py-[2rem] px-[0.1rem]">
    <div class="left-panel mt-[6.9rem] hidden md:block">
      <img src="../assets/37.order-delivered-3.png" class = "w-80 h-80 border-1 border-gray-400 md:order-2" alt="delivery-img">
    </div>
    <div class="right-panel px-[2rem] md:px-[0rem]">
      <div class="credentials - container md:order-2 md:mt-[2rem]">
        <div class="catch-line-outer">
            <div class="catch-line-inner">
              <p class = "text-gray-500 font-semibold py-[2rem]">"Gear Up, Sign Up, Shop Now!"</p>
            </div>
      </div>
     <div class="credentials">
      <div class="username py-[1rem]">
          <p class = "font-bold subpixel-antialiased text-slate-500/[.98] py-[0.1rem] tracking-wide text-slate-800">Username</p>
          <input type="text" class = "px-[1rem] border-2 h-[2.69rem] border-black-300 w-full items-center rounded-lg md:w-[35rem]" name="" placeholder="Username"/>
        </div>
      <div class="email py-[1rem]">
          <p class = "font-bold subpixel-antialiased text-slate-500/[.98] py-[0.1rem] tracking-wide text-slate-800">Email</p>
          <input type="email" class = "px-[1rem] border-2 h-[2.69rem] border-black-300 w-full rounded-lg md:w-[35rem]" name="" placeholder="Enter your email"/>
        </div>
        <div class="password  py-[1rem]">
          <p class = "font-bold subpixel-antialiased text-slate-500/[.98] tracking-wide py-[0.1rem] text-slate-800">Password</p>
          <input type="password"  class = "px-[1rem] border-2 h-[2.69rem] border-black-300 w-full items-center rounded-lg md:w-[35rem]" name="" placeholder="***********"/>
        </div>
        <div class="confirm-password  py-[1rem]">
          <p class = "font-bold subpixel-antialiased text-slate-500/[.98] tracking-wide py-[0.1rem] text-slate-800">Confirm Password</p>
          <input type="password"  class = "px-[1rem] border-2 h-[2.69rem] border-black-300 w-full items-center rounded-lg md:w-[35rem]" name="" placeholder="***********"/>
        </div>
     </div>
        <div class="sign-up  py-[1rem]">
          <a href="#">
            <button type="submit" id="Sign-up" class = " hover:bg-red-400 w-full bg-red-500 h-[3.25rem] rounded-[1.25rem] backdrop-blur-lg">
              <p class = "text-white hover:border-slate-500">Sign Up</p>
            </button>
          </a>
        </div>
        <div class="sign-up-google  py-[1rem]">
          <button type="submit" id="submit-google" class = "hover:border-blue-600 mt-[1rem] border-2 border-slate-300 w-full bg-white-500 h-[3.25rem] rounded-[1.25rem]">
            <div class="google-img inline-flex items-center">
              <img src="../assets/google-icon.png" alt="" class = "w-[1.5rem]">
              <a href="#" class = "ml-[0.3rem] tracking-wide tracking-wide">Sign up with Google</a>
            </div>

          </button>
        </div>
        <div class="optional-sign-in mt-[0.7rem]">
          <p class = "flex justify-center">
            <span class="account-text tracking-wide">Already have an account? </span>
            <nuxt-link to="/Signin" class="text-red-500 hover:underlined tracking-wide">Sign in</nuxt-link>
          </p>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
  export default {
    name:'signUpTailwind'
  }
</script>

<style scoped>
.main{
  font-family: 'Poppins', sans-serif;
  font-smooth: always;
}
  @media screen and (min-height: 977px){
  .zoom{
      min-height: 100vh
  }
}
</style>
