<template>

<body>
  <div class="content-box">
    <div class="catch-line-outer">
        <div class="catch-line-inner">
            <p>"Gear Up, Sign Up, Shop Now!"</p>
        </div>
    </div>
    <div class="username">
      <p>Username</p>
      <input type="text" name=""  placeholder="Enter your name"/>
    </div>
    <div class="email">
      <p>Email</p>
      <input type="email" name="" placeholder="Enter your email"/>
    </div>
    <div class="password">
      <p>Password</p>
      <input type="password" name="" placeholder="*************"/>
    </div>
    <div class="sign-up">
      <a href="#">
        <button type="submit" id="Sign-up">
          <p>Sign up</p>
        </button>
      </a>
    </div>
    <div class="sign-up-google">
      <button type="submit" id="submit-google">
        <div class="google-img">
        </div>
        <a href="#">Sign up with Google</a>
      </button>
    </div>
    <div class="optional-sign-in">
      <p>
        <span class="account-text">Dont have an account?</span>
        <a href="#">Sign in</a>
      </p>
    </div>
  </div>
  <div class="img-box-outer">
      <div class="img-box-inner">
          <img src="../assets/images/37. order-delivered-3.png" alt="" />
      </div>
  </div>
</body>
</template>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Poppins:ital,wght@0,300;0,400;0,500;1,500&display=swap');

* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
  font-family: 'Poppins', sans-serif;
}

body {
  position: absolute;
  width: 100%;
  height: 100%;
  display: flex; 
  /* background: lightblue; */
  background: #F8F8F8;
}

.img-box-outer {

  position: absolute;
  left: 42.15%;
  right: 1.32%;
  top: 10.57%;
  bottom: 1.26%;
}
.img-box-outer .img-box-inner{
  position: absolute;
  width: 517px;
  height: 429px;
  left: 148px;
  top: 108px;
}

section .img-box-outer .img-box-inner img {
  position: absolute;
  width: 457px;
  height: 422px;
  left: -30px;
  top: -90px
}

.content-box{
  display: flex;
  flex-direction: column;
  align-items: center;
  padding: 72px 7px;
  gap: 21px;

  position: absolute;
  left: 14.38%;
  right: 59.31%;
  top: 1.09%;
  bottom: 0%;
  width: 400px;
}

.catch-line-outer{
  display: flex;
  flex-direction: row;
  align-items: flex-start;
  padding: 10px;
  gap: 10px;
  position: absolute;
  left: 10px;
  width: 365px;
  height: 46px;
}
.catch-line-outer .catch-line-inner{
  display: flex;
  flex-direction: row;
  align-items: flex-start;
  padding: 7px 0px;
  gap: 10px;
  width: 217px;
  height: 36px;
}
.catch-line-outer .catch-line-inner p{
  width: 217px;
  height: 22px;
  font-family: 'Poppins';
  font-style: normal;
  font-weight: 400;
  font-size: 14px;
  line-height: 22px;
  text-align: center;
  letter-spacing: 0.03em;
  color: #636364;
}


.username{
  width: 324.35px;
  height: 81.23px;
  position: absolute;
  top: 150px;
  left: 26px;
}

.username p{
  width: 84.6px;
  height: 25.46px;
  font-family: 'Poppins';
  font-style: normal;
  font-weight: 500;
  font-size: 14px;
  line-height: 21px;
  text-align: center;
  letter-spacing: 0.03em;

  color: #181818;
}
.username input[type=text]{
  box-sizing: border-box;
  width: 323.29px;
  height: 48.49px;
  padding: 10px;
  border: 1px solid rgba(0, 0, 0, 0.25);
  /* filter: drop-shadow(0px 4px 10px rgba(0, 0, 0, 0.25)); */
  border-radius: 12px;
}
.username input[type=text]::placeholder{
  position: absolute;
  left: 10px;
}

.email{
  width: 324.35px;
  height: 81.23px;
  position: absolute;
  top: 250px;
  left: 26px;
}

.email p{
  width: 43.6px;
  height: 25.46px;

  font-family: 'Poppins';
  font-style: normal;
  font-weight: 500;
  font-size: 14px;
  line-height: 21px;
  text-align: center;
  letter-spacing: 0.03em;

color: #181818;
}

.email input[type=email]{
  box-sizing: border-box;

  width: 323.29px;
  height: 48.49px;
  padding: 10px;
  border: 1px solid rgba(0, 0, 0, 0.25);
  /* filter: drop-shadow(0px 4px 10px rgba(0, 0, 0, 0.25)); */
  border-radius: 12px;
}
.email input[type=email]::placeholder{
  position: absolute;
  left: 10px;
}

.password{
  width: 323.01px;
  height: 81.23px;
  position: absolute;
  top: 350px;
  left: 26px;
}

.password p{
  width: 76.5px;
  height: 25.46px;

  font-family: 'Poppins';
  font-style: normal;
  font-weight: 500;
  font-size: 14px;
  line-height: 21px;
  text-align: center;
  letter-spacing: 0.03em;

  color: #181818;
}

.password input[type=password]{
  box-sizing: border-box;
  width: 323.01px;
  height: 48.49px;
  padding: 10px;
  border: 1px solid rgba(0, 0, 0, 0.25);
  /* filter: drop-shadow(0px 4px 10px rgba(0, 0, 0, 0.25)); */
  border-radius: 12px;
}
.password input[type=password]::placeholder{
  position: absolute;
  left: 10px;
  top: 15px;
  font-size: 1rem;
}
.signup-button{
  width: 320.01px;
  height: 48.49px;
}

.sign-up{
  width: 320.01px;
  height: 48.49px;
  position: absolute;
  top: 450px;
  left: 26px;
}

#Sign-up{
  width: 320.01px;
  height: 48.49px;
  
  background: #EA454C;
  box-shadow: 0px 4px 10px rgba(233, 68, 75, 0.25);
  border-radius: 12px;
  cursor: pointer;
  padding: 12px;
}

#Sign-up p{
width: 100%;
height: 100%;
font-family: 'Poppins';
font-style: normal;
font-weight: 500;
font-size: 14px;
line-height: 21px;
text-align: center;
letter-spacing: 0.03em;
color: #FFFFFf;
}

.sign-up-google{
  width: 320.01px;
  height: 48.49px;
  position: absolute;
  top: 520px;
  left: 26px;
}

#submit-google{
  box-sizing: border-box;

  width: 320.01px;
  height: 48.49px;

  border: 1px solid rgba(0, 0, 0, 0.25);
  filter: drop-shadow(0px 4px 10px rgba(0, 0, 0, 0.25));
  border-radius: 12px;
}

.google-img{
  position: absolute;
  width: 29.47px;
  height: 33.95px;
  left: 36.86px;
  top: 6.45px;

background: url(../assets/images/google-icon.png);
}

.optional-sign-in{
  position: absolute;
  left: 50px;
  width: 280.6px;
  padding: 10px;
  top: 570px;
}
.optional-sign-in p > span{

  font-family: 'Poppins';
  font-style: normal;
  font-weight: 500;
  font-size: 12px;
  line-height: 15px;
  text-align: center;
  letter-spacing: 0.03em;

  color: #595959;
}

.optional-sign-in p > a{
  font-family: 'Poppins';
  font-style: normal;
  font-weight: 500;
  font-size: 12px;
  line-height: 15px;
  text-align: center;
  letter-spacing: 0.03em;
  color: #EA454C;
  cursor: pointer;
}

.optional-sign-in span{
  display: inline;
}

/* Media Queries */

@media only screen and (max-width: 360px) {
  .img-box-outer{
    display: none;
  }
  body{
    width: 1vh;
    height: 1vh;
  }
}

@media only screen and (min-width: 360px) and (max-width: 768px) {
  body{
    margin: 0;
    padding: 0;
  }

  .content-box{
    left: 53.38%;
    top: 10.09%;
    width: 348px;
  }

  .img-box-outer{
    display: none;
  }
}

@media only screen and (width= 480px){
  .content-box{
    left:10.38%;
    top: 1.09%;
  }
}
</style>