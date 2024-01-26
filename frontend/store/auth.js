// reusable aliases for mutations
export const AUTH_MUTATIONS = {
  SET_USER: 'SET_USER',
  SET_PAYLOAD: 'SET_PAYLOAD',
  LOGOUT: 'LOGOUT',
}

export const state = () => ({
  access: null, // JWT access token
  refresh: null, // JWT refresh token
})

export const mutations = {
  // store new or updated token fields in the state
  [AUTH_MUTATIONS.SET_PAYLOAD] (state, { access, refresh = null }) {
    state.access = access

    // refresh token is optional, only set it if present
    if (refresh) {
      state.refresh = refresh
    }
  },

  // clear our the state, essentially logging out the user
  [AUTH_MUTATIONS.LOGOUT] (state) {
    state.access = null
    state.refresh = null
  },
}

export const actions = {
  async login ({ commit, dispatch }, { email, password }) {
    // make an API call to login the user with an email address and password
    const { data } = await this.$axios.post(
      'token/',
      { email, password }
    )

    // commit the user and tokens to the state
    commit(AUTH_MUTATIONS.SET_PAYLOAD, data)
  },

  async register ({ commit }, { username, email, password }) {
    let first_name = username, last_name = username
    const response = await this.$axios.post(
      'accounts/',
      { first_name, last_name, email, password }
    )
    if (process.env.NODE_ENV == 'production') {
      console.log(response)
    }
  },

  // given the current refresh token, refresh the user's access token to prevent expiry
  async refresh ({ commit, state }) {
    const { refresh } = state

    // make an API call using the refresh token to generate a new access token
    const { data } = await this.$axios.post(
      'token/refresh',
      { refresh }
    )

    commit(AUTH_MUTATIONS.SET_PAYLOAD, payload)
  },

  // logout the user
  logout ({ commit, state }) {
    commit(AUTH_MUTATIONS.LOGOUT)
  },
}

export const getters = {
  // determine if the user is authenticated based on the presence of the access token
  isAuthenticated: (state) => {
    return state.access && state.access !== ''
  },
}
