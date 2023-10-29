const scriptURL = "https://script.google.com/macros/s/AKfycbzjgOvgVHO3bU-R51fDrhBN7tEYCyWw3QBHLJTwkEPcJBMbdLd9cXNTd5g_A1lDtFyWkg/exec";
const form = document.forms["contact-form"];
const btnSub = document.querySelector(".btn-submit");
const btnLoad = document.querySelector(".btn-loading");
const alertSuc = document.querySelector(".alert-success");
const alertWar = document.querySelector(".alert-warning");

form.addEventListener("submit", (e) => {
  e.preventDefault();
  btnSub.classList.toggle("d-none");
  btnLoad.classList.toggle("d-none");

  fetch(scriptURL, { method: "POST", body: new FormData(form) })
    .then((response) => {
      btnSub.classList.toggle("d-none");
      btnLoad.classList.toggle("d-none");
      alertSuc.classList.toggle("d-none");
      form.reset();
      console.log("Success!", response);
    })
    .catch((error) => {
      alertWar.classList.toggle("d-none");
      console.error("Error!", error.message);
    });
});
