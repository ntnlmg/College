
// Mendapatkan elemen form-container
var formContainer = document.getElementById('login-form');

// Fungsi untuk mengubah tema
function changeTheme(theme) {
  if (theme === 'light') {
    formContainer.style.setProperty('--cust-bg-color', 'white');
  } else if (theme === 'dark') {
    formContainer.style.setProperty('--cust-bg-color', 'black');
  }

  // Simpan tema ke localStorage
  localStorage.setItem('theme', theme);

  // Trigger event theme-changed
  document.dispatchEvent(new CustomEvent('theme-changed', { detail: { theme: theme } }));
}

// Menambahkan event listener untuk tombol Light
document.getElementById('refresh-light').addEventListener('click', function () {
    changeTheme('light'); // Panggil fungsi dengan tema 'light'
});

// Menambahkan event listener untuk tombol Dark
document.getElementById('refresh-dark').addEventListener('click', function () {
    changeTheme('dark'); // Panggil fungsi dengan tema 'dark'
});

// Mendengarkan perubahan tema
document.addEventListener('theme-changed', function (event) {
  var currentTheme = event.detail.theme;
  changeTheme(currentTheme);
});
// Memeriksa apakah tema tersimpan di localStorage saat halaman dimuat
var storedTheme = localStorage.getItem('theme');
if (storedTheme) {
  // Jika tema tersimpan, gunakan tema tersebut
  changeTheme(storedTheme);
} else {
  // Jika tidak, gunakan tema default (misalnya, 'auto' atau tema lain yang Anda tentukan)
  changeTheme('auto');
}

// Menggunakan JavaScript untuk menyembunyikan form pop-up saat halaman dimuat
document.addEventListener("DOMContentLoaded", function() {
var form = document.getElementById("myForm");
form.style.display = "none";
});

function toggleForm() {
var form = document.getElementById("myForm");
if (form.style.display === "flex") {
  form.style.display = "none";
} else {
  form.style.display = "flex";
}
}

// Menambahkan event listener ke tombol
document.getElementById('refresh').addEventListener('click', function() {
// Melakukan reload halaman
location.reload();
});
