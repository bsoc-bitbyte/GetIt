import VuexPersistence from 'vuex-persist'
import * as Cookies from 'js-cookie'
import Vuex from 'vuex'

export default ({ store, req, isDev }) => {
    new VuexPersistence({
    key: 'authentication-cookie',
    paths: ['auth.access', 'auth.refresh'],
    storage: {
      getItem: key => process.client ? JSON.parse(Cookies.get(key) || '{}') || '' : null,
      setItem: (key, value) => Cookies.set(key, value, { expires: 14, secure: !isDev }),
      removeItem: key => Cookies.remove(key),
    },
  }).plugin(store);
}
