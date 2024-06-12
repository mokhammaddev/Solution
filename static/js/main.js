const elSignIn = document.querySelector(".js-sign-in");
const elSignUp = document.querySelector(".js-sign-up");
const elModalSignIn = document.getElementById("modal__sign-in");
const elModalSignUp = document.getElementById("modal__sign-up");
const elModalSingInClose = document.querySelector(".js-modal-sign-in-close");
const elModalSingUpClose = document.querySelector(".js-modal-sign-up-close");
const elModalFooterSignUp = document.querySelector(".modal__content-footer-sign-up");
const elModalFooterSignIn = document.querySelector(".modal__content-footer-sign-in");
const elModalSignUpWithEmailLink = document.querySelector(".modal__content-sign-up-email-link");
const elModalSignUpWithEmail = document.getElementById("modal__sign-up-with-email");
const elModalSignUpEmailClose = document.querySelector(".js-modal-sign-up-email-close");
const elModalSignUpGoogle = document.querySelector(".modal__content-sign-up-google-link");
const elModalFooterSignInEmail = document.querySelector(".modal__content-footer-sign-up-email");
const elModalForgotPasswordLink = document.querySelector(".modal__content-forgot-password-link");
const elModalForgotPassword = document.getElementById("modal__forgot-password");
const elModalForgotPasswordClose = document.querySelector(".js-modal-content-forgot-password-close");

elSignIn.addEventListener("click", function () {
  elModalSignIn.classList.add("modal__open");
})

elModalSingInClose.addEventListener("click", function () {
  elModalSignIn.classList.remove("modal__open");
})

elSignUp.addEventListener("click", function () {
  elModalSignUp.classList.add("modal__open");
})

elModalSingUpClose.addEventListener("click", function () {
  elModalSignUp.classList.remove("modal__open");
})

elModalFooterSignUp.addEventListener("click", function () {
  elModalSignIn.classList.remove("modal__open")
  elModalSignUp.classList.add("modal__open")
})

elModalFooterSignIn.addEventListener("click", function () {
  elModalSignUp.classList.remove("modal__open");
  elModalSignIn.classList.add("modal__open");
})

elModalSignUpWithEmailLink.addEventListener("click", function () {
  elModalSignUpWithEmail.classList.add("modal__open")
  elModalSignUp.classList.remove("modal__open")
})

elModalSignUpEmailClose.addEventListener("click", function () {
  elModalSignUpWithEmail.classList.remove("modal__open")
})

elModalSignUpGoogle.addEventListener("click", function () {
  elModalSignUp.classList.add("modal__open")
  elModalSignUpWithEmail.classList.remove("modal__open")
})

elModalFooterSignInEmail.addEventListener("click", function () {
  elModalSignIn.classList.add("modal__open");
  elModalSignUpWithEmail.classList.remove("modal__open")
})

elModalForgotPasswordLink.addEventListener("click", function () {
  elModalForgotPassword.classList.add("modal__open")
  elModalSignIn.classList.remove("modal__open")
})

elModalForgotPasswordClose.addEventListener("click", function () {
  elModalForgotPassword.classList.remove("modal__open")
})