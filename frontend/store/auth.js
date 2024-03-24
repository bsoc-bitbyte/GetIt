import { defineStore } from 'pinia';
import { navigateTo } from '#app'; 
import { toast } from 'vue3-toastify';

export const useAuthStore = defineStore('auth', {
  state: () => ({
    access: null, 
    refresh: null, 
    user: null, 
  }),
  // export const actions = {
  //   async login({ commit, dispatch }, { email, password }) {
  //     // make an API call to login the user with an email address and password
  //     console.log("inside login")
  //     let response = null;
  //     try {
  //       response = await this.$axios.post("token/", { email, password });
  //       if (response.status == 200) {
  //         commit(AUTH_MUTATIONS.SET_PAYLOAD, {
  //           access: response.data.access,
  //           refresh: response.data.refresh,
  //           user: {
  //             email: email,
  //           }
  //         }
  //         );
  //         this.$toast.show("Logged In Successfully", {
  //           theme: "toasted-primary",
  //           position: "bottom-center",
  //           duration: 2000,
  //           type: "success",
  //           iconPack: "material",
  //           icon: "login",
  //         });
  //       }
  
  //     }
  //     catch (error) {
  //       this.$toast.show(error.response.data.detail, {
  //         theme: "toasted-primary",
  //         position: "bottom-center",
  //         duration: 2000,
  //         type: "error",
  //         iconPack: "material",
  //         icon: "login",
  //       });
  //       throw error;
  //     }
  //   },
  
  //   async register({ commit }, { username, phone_number, email, password }) {
  //     let first_name = username.split(" ")[0];
  //     let last_name = username.split(" ")[1];
  //     try {
  //       const response = await this.$axios.post("accounts/", {
  //         first_name,
  //         last_name,
  //         phone_number,
  //         email,
  //         password,
  //       });
  //       if (response.status == 201 || response.status == 200) {
  //         this.$toast.show("Registered Successfully", {
  //           theme: "toasted-primary",
  //           position: "bottom-center",
  //           duration: 2000,
  //           type: "success",
  //           iconPack: "material",
  //           icon: "login",
  //         });
  //       }
  //     }
  //     catch (error) {
  //       this.$toast.show(error.response.data.detail, {
  //         theme: "toasted-primary",
  //         position: "bottom-center",
  //         duration: 2000,
  //         type: "error",
  //         iconPack: "material",
  //         icon: "login",
  //       });
  //       throw error;
  //     }
  //     if (process.env.NODE_ENV == "production") {
  //       console.log(response);
  //     }

  actions: {
    async login({ email, password }) {
      console.log("inside login")
      let response = null;
      try {
        console.log(email,password,response);
        const {data,status} = await useFetch("http://localhost:8000/api/token/", {
          method: 'POST', 
          body: { email, password }
        }); 
        if(status.value === "success") {
          this.access = data.value.access;
          this.refresh = data.value.refresh || null; 
          this.user = email || null;
          await navigateTo('/'); 
          toast.success("Login successful", {
            autoClose: 2000,
            position: toast.POSITION.BOTTOM_CENTER,
          });

        }
      else{
        toast.error("Invalid Credential", {
          autoClose: 2000,
          position: toast.POSITION.BOTTOM_CENTER,
        });
      }}
        catch (error) {
          toast.error("Invalid Credential/Account does not Exist", {
            autoClose: 2000,
            position: toast.POSITION.BOTTOM_CENTER,
          });
          throw error;
      }
    },

    async register({ username, phone_number, email, password }) {
      let first_name = username.split(" ")[0];
      let last_name = username.split(" ")[1];
      console.log(first_name, last_name,phone_number, email, password);
      try{
      const {data,status,error} = await useFetch("http://localhost:8000/api/accounts/", { method:'POST', body: {
              first_name,
              last_name,
              phone_number,
              email,
              password,
      }});

      if(status.value === 'success'){
        toast.success("Register successful", {
          autoClose: 2000,
          position: toast.POSITION.BOTTOM_CENTER,
        });
        await navigateTo('/Signin')
      }
      else{
        Object.entries(error.value.data).forEach(([field, errorMessages]) => {
          toast.error(`$${errorMessages[0]}`,
          {
            autoClose: 3000,
            position: toast.POSITION.BOTTOM_CENTER,
          
          })
        });
      }



    
    }catch(error){
        toast.error(error.response.data.detail, {
          autoClose: 2000,
          position: toast.POSITION.BOTTOM_CENTER,
        });
      

      if (process.env.NODE_ENV == "production") {
        console.log(response);
      }
    }},

    async refresh() {
      if (!this.refresh) return;
      const { data } = await $fetch("http://localhost:8000/api/token/refresh", { method:'POST', body: { refresh: this.refresh }});
      this.SET_PAYLOAD(data);
    },

    logout() {
      this.access = null;
      this.refresh = null;
      this.user = null;
    },

    SET_PAYLOAD(payload) {
      this.access = payload.access;
      this.refresh = payload.refresh || null; 
      this.user = payload.user || null;
    },
  },

  getters: {
    isAuthenticated(){
      return this.access && this.access !== ""} ,

    userEmail(){
      return this.user
    }
  },
  persist: true,
});
