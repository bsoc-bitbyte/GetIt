<template>
  <div
    class="main min-[1120px]:flex min-[1120px]:justify-evenly py-[2rem] md:py-[0rem] px-[0.1rem] md:mt-[2rem] mt-[1rem]"
  >
    <div class="left-panel mt-[5.5rem] max-[1119px]:hidden min-[1120px]:block">
      <img
        src="../assets/37.order-delivered-3.png"
        class=" border-1 border-gray-400 min-[1120px]:order-1 h-[50vh]"
        alt="delivery-img"
      />
    </div>
    <div class="right-panel max-[1119px]:px-[2rem] min-[1120px]:px-[0rem]">
      <form @submit="submitForm" class="credentials">
        <div
          class="credentials - container min-[1120px]:order-2 min-[1120px]:mt-[2rem]"
        >
          <div class="catch-line-outer">
            <div class="catch-line-inner">
              <p
                class="text-gray-500 font-semibold py-[2rem] max-[1023px]:-mt-10"
              >
                "Gear Up, Sign Up, Shop Now!"
              </p>
            </div>
          </div>
          <div class="credentials">
            <div class="username py-[0.5rem]">
              <p
                class="font-bold text-slate-500/[.98] py-[0.1rem] tracking-wider text-slate-800"
              >
                Full Name
                Full Name
              </p>
              <input
                type="text"
                class="px-[1rem] border-2 h-[2.69rem] border-black-300 w-full items-center rounded-lg min-[1120px]:w-[35rem]"
                v-model.trim.lazy="credentials.username"
                placeholder="John Doe"
                placeholder="John Doe"
                required
              />
            </div>
            <div class ="phone-number py-[0.5rem]">
              <p class = "font-bold text-slate-500/[.98] py-[0.1rem] tracking-wider text-slate-800">Phone Number</p>
              <input type="tel" class = "px-[1rem] border-2 h-[2.69rem] border-black-300 w-full items-center rounded-lg min-[1120px]:w-[35rem]" 
              v-model.trim.lazy = "credentials.phone_number" 
              placeholder="Enter your phone number" required/>
            </div>
            <div class="email py-[0.5rem]">
              <p
                class="font-bold text-slate-500/[.98] py-[0.1rem] tracking-wider text-slate-800"
              >
                Email
              </p>
              <input
                type="email"
                class="px-[1rem] border-2 h-[2.69rem] border-black-300 w-full rounded-lg min-[1120px]:w-[35rem]"
                v-model.trim.lazy="credentials.email"
                placeholder="Enter your email"
                required
              />
            </div>
            <div class="password py-[0.5rem]">
              <p
                class="font-bold text-slate-500/[.98] tracking-wider py-[0.1rem] text-slate-800"
              >
                Password
              </p>
              <input
                type="password"
                class="px-[1rem] border-2 h-[2.69rem] border-black-300 w-full items-center rounded-lg min-[1120px]:w-[35rem]"
                v-model.trim.lazy="credentials.password"
                placeholder="***********"
                required
              />
            </div>
            <div class="confirm-password py-[0.5rem]">
              <p
                class="font-bold text-slate-500/[.98] tracking-wider py-[0.1rem] text-slate-800"
              >
                Confirm Password
              </p>
              <input
                type="password"
                class="px-[1rem] border-2 h-[2.69rem] border-black-300 w-full items-center rounded-lg min-[1120px]:w-[35rem]"
                v-model.trim.lazy="credentials.password_check"
                placeholder="***********"
                required
                @input="checker"
              />
              <p v-if="errorMessage" style="color: red">{{ errorMessage }}</p>
            </div>
          </div>
          <div class="sign-up pt-[1rem] pb-[0rem]">
            <a href="#">
              <button
                type="submit"
                id="Sign-up"
                class="signup w-full h-[3.25rem] rounded-[1.25rem] backdrop-blur-lg" onclick=(submitForm)
              >
                <p class="text-white hover:border-slate-500 tracking-wider">
                  Sign Up
                </p>
              </button>
            </a>
          </div>
      
          <div class="optional-sign-in mt-[0.7rem] hi">
            <p class="flex justify-center hi">
              <span class="account-text tracking-wider dha"
                >Already have an account?
              </span>
              <nuxt-link to="/Signin" class="text-red-500 hover:underlined tracking-wider suf">Sign up for free</nuxt-link>
            </p>
          </div>
        </div>
      </form>
    </div>
  </div>
</template>

<script>
import { toast } from 'vue3-toastify'
import { useAuthStore } from '../store/auth'
import { useRouter } from 'vue-router'

export default {
  name: 'Signup',
  setup() {
    const credentials = {
      username: '',
      phone_number: "",
      email: '',
      password: '',
      password_check: '',
    }
    const store = useAuthStore()
    const router = useRouter()

    const submitForm = async (e) => {
      e.preventDefault();

      if (checker()){
        
        store.register(credentials);
      }
      else{
        toast.error("Passwords do not match",{
          autoClose: 2000,
          position:  toast.POSITION.BOTTOM_CENTER
        })
      }
      
    }

    const checker = () => {
      if (credentials.password !== credentials.password_check) {
        return false;
      }
      return true;
    }

    return {
      credentials,
      submitForm,
      checker
    }
  }
}
</script>


<style scoped>
.main {
  font-family: "Poppins", sans-serif;
  font-smooth: always;
  position: inherit;
  width: 100%;
  height: 100%;
  top: 0;
  left: 0;
  right: 0;
}
.signup {
  background-color: rgba(234, 69, 76, 1);
}

@media (max-width: 325px) {
  .hi {
    display: flex;
    flex-direction: column !important;
    gap: 5px;
    margin-left: 16px !important;
  }
  .dha {
    display: inline-block;
    /* font-size:larger; */
    margin-left: -48px !important;
    margin-right: -20px !important;
    text-align: center !important;
  }

  .suf {
    display: inline-block;
    /* font-size:larger; */
    margin-left: -48px !important;
    margin-right: 5px !important;
    text-align: center !important;
  }

}
</style>
