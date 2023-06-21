<template>
  <div class="main  md:flex  bg-gray-100 md:justify-evenly py-[2rem] px-[0.1rem]">
    <div class="left-panel mt-[5rem] hidden md:block">
      <img src="../assets/37.order-delivered-3.png" class = "w-80 h-80 border-1 border-gray-400 md:order-2" alt="delivery-img">
    </div>
    <div class="right-panel px-[2rem] md:px-[0rem]">
      <div class="credentials - container md:order-2 md:mt-[3rem]">
        <div class="catch-line-outer">
            <div class="catch-line-inner">
                <p class = "text-gray-700 font-semibold">"Welcome back! Please enter your details"</p>
            </div>
      </div>
     <div class="credentials">
      <div class="email py-[1rem]">
          <p class = "font-bold subpixel-antialiased text-slate-500/[.98] py-[0.1rem] tracking-wide text-slate-800 ">Email</p>
          <input type="email" class = "px-[1rem] border-2 h-[2.69rem] border-black-300 w-full md:w-[35rem] rounded-lg" name="" placeholder="Enter your email"/>
        </div>
        <div class="password  py-[1rem]">
          <p class = "font-bold subpixel-antialiased text-slate-500/[.98] tracking-wide py-[0.1rem] text-slate-800">Password</p>
          <input type="password"  class = "px-[1rem] border-2 h-[2.69rem] border-black-300 w-full md:w-[35rem] rounded-lg" name="" placeholder="***********"/>
        </div>
     </div>
        <div class="remember-forgot flex justify-between py-[1rem] md:justify-between">
          <div class="remember-me">
            <input type="checkbox" name="check" id="checkbox">
            <span class="checkmark font-bold subpixel-antialiased tracking-wide">Remember me</span>
          </div>
          <div class="forgot-password">
            <a href="#" class = "font-bold subpixel-antialiased tracking-wide text-slate-800">Forgot password</a>
          </div>
        </div>
        <div class="sign-in  py-[1rem]">
          <a href="#">
            <button type="submit" id="Sign-up" class = "w-full hover:bg-red-400 bg-red-500 h-[3.25rem] rounded-[1.25rem]">
              <p class = "text-white hover:border-slate-500">Sign in</p>
            </button>
          </a>
        </div>
        <div class="sign-up-google  py-[1rem]">
          <button type="submit" id="submit-google" class = "hover:border-blue-600 mt-[1rem] border-2 border-slate-300 w-full bg-white-500 h-[3.25rem] rounded-[1.25rem]">
            <div class="google-img inline-flex items-center">
              <img src="../assets/google-icon.png" alt="" class = "w-[1.5rem]">
              <a href="#" class = "ml-[0.3rem] tracking-wide tracking-wide">Sign in with Google</a>
            </div>

          </button>
        </div>
        <div class="optional-sign-in mt-[0.7rem]">
          <p class = "flex justify-center">
            <span class="account-text tracking-wide">Already have an account?</span>
            <a href="#" class="text-red-500 hover:underlined tracking-wide">Sign up for free</a>
          </p>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
  export default {
    name:'signinTailwind'
  }
</script>

<style scoped>
.main{
  font-family: 'Poppins', sans-serif;
  font-smooth: always;  
}
</style>
