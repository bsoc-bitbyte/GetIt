export default function ({ store, route, redirect }) {
  // Check if the user is signed in
  console.log(route,store.getters['auth/isAuthenticated']);
  if (route.name ==="Signin"){
    return 
  }
  else if (route.name!=='Signup' && !store.getters['auth/isAuthenticated']  ) {
    // Redirect to the sign-in page if not signed in
    return redirect('/signin');
  }
}
