import VuexPersistence from 'vuex-persist'
import * as Cookies from 'js-cookie'

export default ({ store, req, isDev }) => {
  new VuexPersistence({
    key: 'authentication-cookie',
    modules: ['auth'], // Specify only 'auth' module to persist
    storage: {
      getItem: key => process.client ? JSON.parse(Cookies.get(key) || '{}') || '' : null,
      setItem: (key, value) => Cookies.set(key, value, { expires: 14, secure: !isDev }),
      removeItem: key => Cookies.remove(key),
    },
  }).plugin(store);

  // Since you want to persist only the 'auth' module, you don't need to persist 'cart' separately
}
