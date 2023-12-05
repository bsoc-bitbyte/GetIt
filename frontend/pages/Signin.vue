<template>
  <div class="main min-[1120px]:flex min-[1120px]:justify-evenly py-[2rem] md:py-[0rem] px-[0.1rem] md:mt-[2rem] mt-[1rem]">
    <div class="left-panel mt-[5.5rem] max-[1119px]:hidden min-[1120px]:block">
      <img src="../assets/37.order-delivered-3.png" class = "w-[34rem] h-[32rem] border-1 border-gray-400 min-[1120px]:order-1" alt="delivery-img">
    </div>
    <div class="right-panel max-[1119px]:px-[2rem] min-[1120px]:px-[0rem]">
      <div class="form-container">
        <form @submit="submitForm">
          <div class="credentials - container min-[1120px]:order-2 min-[1120px]:mt-[3rem]">
        <div class="catch-line-outer">
            <div class="catch-line-inner">
                <p class = "text-slate-500 font-semibold py-[2rem]">"Welcome back! Please enter your details"</p>
            </div>
      </div>
     <div class="credentials">
      <div class="email py-[1.0rem]">
          <p class = "font-bold subpixel-antialiased text-slate-500/[.98] py-[0.1rem] tracking-wide text-slate-800 ">Email</p>
          <input type="email" class = "px-[1rem] border-2 h-[2.69rem] border-black-300 max-[1119px]:w-full min-[1120px]:w-[35rem] rounded-lg" v-model.trim.lazy = "credentials.email" name="" placeholder="Enter your email"/>
        </div>
        <div class="password  py-[1.0rem]">
          <p class = "font-bold subpixel-antialiased text-slate-500/[.98] tracking-wide py-[0.1rem] text-slate-800">Password</p>
          <input type="password"  class = "px-[1rem] border-2 h-[2.69rem] border-black-300 max-[1119px]:w-full min-[1120px]:w-[35rem] rounded-lg" v-model.trim.lazy = "credentials.password" name="" placeholder="***********"/>
        </div>
     </div>
        <div class="remember-forgot py-[1.0rem] flex justify-between hi">
          <div class="remember-me hil">
            <input type="checkbox" name="check" id="checkbox" true-value = "yes" false-value = "no" v-model.trim.lazy="credentials.rememberMe">
            <label for="checkbox" class = " subpixel-antialiased font-bold text-slate-800 cursor-pointer">Remember me</label>
          </div>
          <div class="forgot-password hir">
            <a href="#" class = "font-bold subpixel-antialiased tracking-wide text-slate-800 fp">Forgot password ?</a>
          </div>
        </div>
        <div class="sign-in  pt-[1rem] pb-[0rem]">
          <a href="#">
            <button type="submit" id="Sign-in" class = "signin w-full h-[3.25rem] rounded-[1.25rem]">
              <p class = "text-white hover:border-slate-500 py-[0rem]">Sign in</p>
            </button>
          </a>
        </div>
        <div class="sign-up-google  py-[0.5rem]">
          <button type="submit" id="submit-google" class = "hover:border-blue-600 mt-[1rem] border-2 border-slate-300 w-full bg-white-500 h-[3.25rem] rounded-[1.25rem]">
            <div class="google-img inline-flex items-center">
              <img src="../assets/google-icon.png" alt="" class = "w-[1.5rem]">
              <a href="#" class = "ml-[0.3rem] tracking-wider">Sign in with Google</a>
            </div>

          </button>
        </div>
        <div class="optional-sign-in mt-[0.7rem] hi">
          <p class = "flex justify-center hi">
            <span class="account-text tracking-wider dha">Don't have an account?</span>
            <nuxt-link to="/Signup" class="text-red-500 hover:underlined tracking-wider suf">Sign up for free</nuxt-link>
          </p>
        </div>
      </div>
        </form>
      </div>
    </div>
  </div>
</template>

<script>
  export default {
    name:'Signin',
    data(){
      return{
        credentials:{
        email:'',
        password:'',
        rememberMe:false
        }
      }
    },
    methods:{
      submitForm(e) {
      e.preventDefault();
      console.log(this.credentials);
    }
    }
  }
</script>

<style scoped>
.main{
  font-family: 'Poppins', sans-serif;
  font-smooth: always;
  position: inherit;
  height: 100%;
  width: 100%;
  left: 0;
  right: 0;
  top: 0;
  bottom: 0;
  background-color: white;
}
.signin{
  background-color:rgba(234, 69, 76, 1);
}
@media (max-width: 420px) {
  .hil{
    margin-left: -20px !important;
  }
  .hir
  {
    margin-right: -20px !important;
  }

}
@media (max-width: 420px) {
  /* .hil{
    margin-left: -20px !important;
  }
  .hir
  {
    margin-right: -40px !important;
  } */
  .hi
  {
    display: flex;
    flex-direction: column !important;
    gap: 5px;
    /* margin-left: 25px !important; */
    /* margin-left: 0px !important; */
    /* justify-content: center; */
    text-align: center;
  }
  .dha
  {
    display: inline-block;
    /* font-size:larger; */
    margin-left: -30px !important;
    margin-right: -40px !important;
    text-align: center !important;

  }
  .suf
  {
    display: inline-block;
    /* font-size:larger; */
    margin-left: -48px !important;
    margin-right: -45px !important;
    text-align: center !important;
  }
  .fp
  {
    margin-left: -25px !important;
    text-align: center;

  }
  /* .hil{
    margin-left: 16px !important;
  } */
}
/* @media (max-width: 281px) {
  .hil{
    margin-left: -30px !important;
  }
  .hir
  {
    margin-right: -43px !important;
  }
} */
</style>
