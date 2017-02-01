app.directive('login', function() {
  return {
    restrict: 'E',
    replace: true,
    templateUrl: 'js/directives/login.html',
    link: function startApp() {
      gapi.load('auth2', function() {
        gapi.client.load('plus','v1').then(function() {
          gapi.signin2.render('signin-button', {
              scope: 'https://www.googleapis.com/auth/plus.login',
              fetch_basic_profile: false });
          gapi.auth2.init({fetch_basic_profile: false,
              scope:'https://www.googleapis.com/auth/plus.login'}).then(
                function (){
                  console.log('init');
                  auth2 = gapi.auth2.getAuthInstance();
                  auth2.isSignedIn.listen(updateSignIn);
                  auth2.then(updateSignIn);
                });
        });
      });
    }
  }
});