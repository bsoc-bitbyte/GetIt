// reusable aliases for mutations
export const AUTH_MUTATIONS = {
  SET_USER: "SET_USER",
  SET_PAYLOAD: "SET_PAYLOAD",
  LOGOUT: "LOGOUT",
};

export const state = () => ({
  access: null, // JWT access token
  refresh: null, // JWT refresh token
  user: null, // user object
});

export const mutations = {
  // store new or updated token fields in the state
  [AUTH_MUTATIONS.SET_PAYLOAD](state, { access, refresh = null, user = null }) {
    state.access = access;

    // refresh token is optional, only set it if present
    if (refresh) {
      state.refresh = refresh;
    }

    if (user) {
      state.user = user;
    }
  },

  // clear out the state, essentially logging out the user
  [AUTH_MUTATIONS.LOGOUT](state) {
    state.access = null;
    state.refresh = null;
  },
};

export const actions = {
  async login({ commit, dispatch }, { email, password }) {
    // make an API call to login the user with an email address and password
    console.log("inside login")
    let response = null;
    try {
      response = await this.$axios.post("token/", { email, password });
      if (response.status == 200) {
        commit(AUTH_MUTATIONS.SET_PAYLOAD, {
          access: response.data.access,
          refresh: response.data.refresh,
          user: {
            email: email,
          }
        }
        );
        this.$toast.show("Logged In Successfully", {
          theme: "toasted-primary",
          position: "bottom-center",
          duration: 2000,
          type: "success",
          iconPack: "material",
          icon: "login",
        });
      }

    }
    catch (error) {
      this.$toast.show(error.response.data.detail, {
        theme: "toasted-primary",
        position: "bottom-center",
        duration: 2000,
        type: "error",
        iconPack: "material",
        icon: "login",
      });
      throw error;
    }
  },

  async register({ commit }, { username, phone_number, email, password }) {
    let first_name = username.split(" ")[0];
    let last_name = username.split(" ")[1];
    try {
      const response = await this.$axios.post("accounts/", {
        first_name,
        last_name,
        phone_number,
        email,
        password,
      });
      if (response.status == 201 || response.status == 200) {
        this.$toast.show("Registered Successfully", {
          theme: "toasted-primary",
          position: "bottom-center",
          duration: 2000,
          type: "success",
          iconPack: "material",
          icon: "login",
        });
      }
    }
    catch (error) {
      this.$toast.show(error.response.data.detail, {
        theme: "toasted-primary",
        position: "bottom-center",
        duration: 2000,
        type: "error",
        iconPack: "material",
        icon: "login",
      });
      throw error;
    }
    if (process.env.NODE_ENV == "production") {
      console.log(response);
    }
  },

  // given the current refresh token, refresh the user's access token to prevent expiry
  async refresh({ commit, state }) {
    const { refresh } = state;

    // make an API call using the refresh token to generate a new access token
    const { data } = await this.$axios.post("token/refresh", { refresh });

    commit(AUTH_MUTATIONS.SET_PAYLOAD, payload);
  },

  // logout the user
  logout({ commit, state }) {
    commit(AUTH_MUTATIONS.LOGOUT);
  },
};

export const getters = {
  // determine if the user is authenticated based on the presence of the access token
  isAuthenticated: (state) => {
    return state.access && state.access !== "";
  },
  userEmail: (state) => {
    return state.user ? state.user.email : null;
  },
};
