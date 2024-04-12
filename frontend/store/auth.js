import { defineStore } from "pinia";
import { navigateTo } from "#app";
import { toast } from "vue3-toastify";
import { jwtDecode } from "jwt-decode";

const config = {
  API_BASE_URL: import.meta.env.VITE_API_BASE_URL || "http://localhost:8000",
};

export const useAuthStore = defineStore("auth", {
  state: () => ({
    access: null,
    refresh: null,
    user: null,
  }),

  actions: {
    async login({ email, password }) {
      console.log("inside login");
      console.log(process.env);

      let response = null;
      try {
        console.log(email, password, response);
        const { data, status } = await useFetch(
          `${config.API_BASE_URL}/api/token/`,
          {
            method: "POST",
            body: { email, password },
          }
        );
        if (status.value === "success") {
          this.access = data.value.access;
          this.refresh = data.value.refresh;
          this.user = email;
          await navigateTo("/");
          toast.success("Login successful", {
            autoClose: 2000,
            position: toast.POSITION.BOTTOM_CENTER,
          });
        } else {
          toast.error("Invalid Credential", {
            autoClose: 2000,
            position: toast.POSITION.BOTTOM_CENTER,
          });
        }
      } catch (error) {
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
      console.log(first_name, last_name, phone_number, email, password);
      try {
        const { data, status, error } = await useFetch(
          `${config.API_BASE_URL}/api/accounts/`,
          {
            method: "POST",
            body: {
              first_name,
              last_name,
              phone_number,
              email,
              password,
            },
          }
        );

        if (status.value === "success") {
          toast.success("Register successful", {
            autoClose: 2000,
            position: toast.POSITION.BOTTOM_CENTER,
          });
          await navigateTo("/Signin");
        } else {
          Object.entries(error.value.data).forEach(([field, errorMessages]) => {
            toast.error(`$${errorMessages[0]}`, {
              autoClose: 3000,
              position: toast.POSITION.BOTTOM_CENTER,
            });
          });
        }
      } catch (error) {
        toast.error(error.response.data.detail, {
          autoClose: 2000,
          position: toast.POSITION.BOTTOM_CENTER,
        });

        if (process.env.NODE_ENV == "production") {
          console.log(response);
        }
      }
    },

    async refreshToken() {
      if (!this.refresh) return;
      console.log("refresh", this.refresh, this.access, this.user);
      try {
        const response = await fetch(
          `${config.API_BASE_URL}/api/token/refresh`,
          {
            method: "POST",
            headers: {
              "Content-Type": "application/json",
            },
            body: JSON.stringify({ refresh: this.refresh }),
          }
        );
        if (!response.ok) {
          throw new Error(`HTTP error! status: ${response.status}`);
        }
        const data = await response.json();
        console.log("data refresh", data);
        this.access = data.access;
      } catch (error) {
        console.error("An error occurred while refreshing the token: ", error);
      }
    },

    tokenNeedsRefresh() {
      // Assuming you have a way to decode JWTs
      try {
        const decoded = jwtDecode(this.access); // Define jwtDecode or use a package
        const currentTime = Date.now() / 1000;
        return decoded.exp < currentTime;
      }
      catch (error) {
        console.error("Error Decoding JWT",error)
        return true
      }
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
    isAuthenticated() {
      return this.access && this.access !== "";
    },

    userEmail() {
      return this.user;
    },

    authToken() {
      return this.access;
    },
  },
  persist: true,
});
