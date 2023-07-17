<template>
  <div class="main  min-[1120px]:-mt-4 min-[1120px]:flex bg-white min-[1120px]:justify-evenly py-[2rem] px-[0.1rem] mt-[3rem] max-[1119px]:pb-[2rem]">
    <div class="left-panel mt-[5.5rem] max-[1119px]:hidden min-[1120px]:block">
      <img src="../assets/37.order-delivered-3.png" class = "w-[34rem] h-[32rem] border-1 border-gray-400 min-[1120px]:order-1" alt="delivery-img">
    </div>
    <div class="right-panel max-[1119px]:px-[2rem] min-[1120px]:px-[0rem]">
      <form @submit = "submitForm" class="credentials">
        <div class="credentials - container min-[1120px]:order-2 min-[1120px]:mt-[2rem]">
        <div class="catch-line-outer">
            <div class="catch-line-inner">
              <p class = "text-gray-500 font-semibold py-[2rem] max-[1023px]:-mt-10">"Gear Up, Sign Up, Shop Now!"</p>
            </div>
      </div>
     <div class="credentials">
      <div class="username py-[0.5rem]">
          <p class = "font-bold text-slate-500/[.98] py-[0.1rem] tracking-wider text-slate-800">Username</p>
          <input type="text" class = "px-[1rem] border-2 h-[2.69rem] border-black-300 w-full items-center rounded-lg min-[1120px]:w-[35rem]" v-model.trim.lazy="credentials.username" placeholder="Username" required/>
        </div>
      <div class="email py-[0.5rem]">
          <p class = "font-bold text-slate-500/[.98] py-[0.1rem] tracking-wider text-slate-800">Email</p>
          <input type="email" class = "px-[1rem] border-2 h-[2.69rem] border-black-300 w-full rounded-lg min-[1120px]:w-[35rem]" v-model.trim.lazy="credentials.email" placeholder="Enter your email" required/>
        </div>
        <div class="password  py-[0.5rem]">
          <p class = "font-bold text-slate-500/[.98] tracking-wider py-[0.1rem] text-slate-800">Password</p>
          <input type="password"  class = "px-[1rem] border-2 h-[2.69rem] border-black-300 w-full items-center rounded-lg min-[1120px]:w-[35rem]" v-model.trim.lazy="credentials.password" placeholder="***********" required/>
        </div>
        <div class="confirm-password  py-[0.5rem]">
          <p class = "font-bold text-slate-500/[.98] tracking-wider py-[0.1rem] text-slate-800">Confirm Password</p>
          <input type="password"  class = "px-[1rem] border-2 h-[2.69rem] border-black-300 w-full items-center rounded-lg min-[1120px]:w-[35rem]" v-model.trim.lazy="credentials.password_check" placeholder="***********" required @input="checker"/>
          <p v-if="errorMessage" style="color:red">{{ errorMessage }}</p>
        </div>
     </div>
        <div class="sign-up  pt-[1rem] pb-[0rem]">
          <a href="#">
            <button type="submit" id="Sign-up" class = "signup w-full h-[3.25rem] rounded-[1.25rem] backdrop-blur-lg">
              <p class = "text-white hover:border-slate-500 tracking-wider">Sign Up</p>
            </button>
          </a>
        </div>
        <div class="sign-up-google  py-[0.5rem]">
          <button type="submit" id="submit-google" class = "hover:border-blue-600 mt-[1rem] border-2 border-slate-300 w-full bg-white-500 h-[3.25rem] rounded-[1.25rem]">
            <div class="google-img inline-flex items-center">
              <img src="../assets/google-icon.png" alt="" class = "w-[1.5rem]">
              <a href="#" class = "ml-[0.3rem] tracking-wide tracking-wider">Sign up with Google</a>
            </div>

          </button>
        </div>
        <div class="optional-sign-in mt-[0.7rem]">
          <p class = "flex justify-center">
            <span class="account-text tracking-wider">Already have an account? </span>
            <nuxt-link to="/Signin" class="text-red-500 hover:underlined tracking-wider">Sign in</nuxt-link>
          </p>
        </div>
      </div>
    </form>
    </div>
  </div>
</template>

<script>
  export default {
    name:'Signup',
    data()
    {
      return{
        credentials:{
          username:'',
          email:'',
          password:'',
          password_check:'',
          errorMessage:'',
      }
    }},
    methods:{
      submitForm(e){
        e.preventDefault();
        console.log(this.credentials);
      },
      checker(){
       if(this.credentials.password_check!==this.credentials.password){
          this.credentials.errorMessage='Passwords do not match';
          return false;
       }
       this.credentials.errorMessage='';
       return true;
      }
    }
  }
</script>

<style scoped>
.main{
  font-family: 'Poppins', sans-serif;
  font-smooth: always;
  position: inherit;
  width: 100%;
  height:100%;
  top:0;
  left:0;
  right:0;

}
.signup{
  background-color:rgba(234, 69, 76, 1)
}
</style>
