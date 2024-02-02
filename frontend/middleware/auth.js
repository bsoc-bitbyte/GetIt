export default function ({ store, route, redirect }) {
  // Check if the user is signed in
  if (route.name==='checkOut' && !store.getters['auth/isAuthenticated']  ) {
    // Redirect to the sign-in page if not signed in
    return redirect('/signin');
  }
}
