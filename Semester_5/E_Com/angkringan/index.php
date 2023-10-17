<?php
session_start();
require_once "function.php";
if (!isset($_SESSION["akun-admin"]) && !isset($_SESSION["akun-user"])) {
    header("Location: login.php");
    exit;
}

if (isset($_GET["transaksi"])) {
    $menu = ambil_data("SELECT * FROM transaksi");
} else if (isset($_GET["pesanan"])) {
    $menu = ambil_data("SELECT p.kode_pesanan, tk.nama_pelanggan, p.kode_menu, p.qty, m.nama
                        FROM pesanan AS p
                        JOIN transaksi AS tk ON (tk.kode_pesanan = p.kode_pesanan)
                        JOIN menu AS m ON (m.kode_menu = p.kode_menu)
                        ORDER BY tk.kode_pesanan
                      ");
} else {
    if (!isset($_GET["search"])) {
        $menu = ambil_data("SELECT * FROM menu ORDER BY kode_menu DESC");
    } else {
        $key_search = $_GET["key-search"];
        $menu = ambil_data("SELECT * FROM menu WHERE nama LIKE '%$key_search%' OR
                            harga LIKE '%$key_search%' OR
                            kategori LIKE '%$key_search%' OR
                            `status` LIKE '%$key_search%'
                            ORDER BY kode_menu DESC
        ");
    }
}

if (isset($_POST["pesan"])) {
    $pesanan = tambah_data_pesanan();
    echo $pesanan > 0
    ? "<script>
    alert('Pesanan Berhasil Dikirim!');
    </script>"
        : "<script>
        alert('Pesanan Gagal Dikirim!');
    </script>";
    if($pesanan > 0){
        header("Location: success.php");
        exit();
    }
}
?>


<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="./src/css/bootstrap-5.2.0/css/bootstrap.min.css">
    <link rel="stylesheet" href="./src/css/bootstrap-icons-1.8.3/bootstrap-icons.css">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.3/css/all.min.css">

    <title>Beranda</title>
<style>
  #goToTop {
    position: fixed;
    bottom: 20px;
    right: 20px;
    z-index: 99;
  }
  /* Add this CSS code to your existing styles or create a new CSS file */
@media (max-width: 576px) {
    /* Adjust the input width for small screens */
    .responsive-input {
        width: 100%;
    }
}

</style>
</head>

<body class="bg-light">
    <!-- Header -->
    <div class="container-fluid position-fixed top-0 bg-dark p-2 d-flex justify-content-between" style="z-index: 2;">
        <div class="text-white h3 d-flex">
            <span id="menu-list" role="button"><i class="bi bi-list"></i></span>
            <a class="text-decoration-none text-white" href="index.php"><span class="mx-3">Angkringan HKY</span></a>
        </div>
        <a class="btn btn-danger fw-bold" href="logout.php" onclick="return confirm('Ingin Logout?')">Logout</a>
    </div>

    <!-- List Menu -->
    <div id="dropdown-menu" class="container-fluid position-fixed float-start bg-dark text-white w-auto vh-100" style="display: none; z-index: 1; top: 50px;">
        <ul>
            <br>
            <li><a class="text-decoration-none p-2 h5 text-light" href="index.php">MENU</a></li><br>
            <?php if (isset($_SESSION["akun-admin"])) { ?>
                <li><a class="text-decoration-none p-2 h5 text-light" href="index.php?pesanan">PESANAN</a></li><br>
                <li><a class="text-decoration-none p-2 h5 text-light" href="index.php?transaksi">TRANSAKSI</a></li>
            <?php } ?>
        </ul>
    </div>

    <!-- Content -->
    <div class="container" style="z-index: -1; margin-top: 60px;">
        <?php
        if (isset($_GET["pesanan"])) include "halaman/pesanan.php";
        else if (isset($_GET["transaksi"])) include "halaman/transaksi.php";
        else include "halaman/beranda.php";
        ?>
    </div>

<button id="goToTop" class="btn btn-primary" onclick="goToTop()">
    <i class="fas fa-arrow-up"></i>
    <!--Go to Top-->
</button>
    <script src="./src/css/bootstrap-5.2.0/js/bootstrap.min.js"></script>
    <script src="https://code.jquery.com/jquery-3.2.1.slim.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/popper.js@1.12.9/umd/popper.min.js"></script>
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js"></script>
    <script src="./src/js/beranda.js"></script>

<script>
function goToTop() {
  window.scrollTo({
    top: 0,
    behavior: "smooth"
  });
}

// // Assuming you have a form element with the id "myForm"
// const form = document.getElementById('myForm');

// form.addEventListener('pesan', function(event) {
//   // Prevent the default form submission
//   event.preventDefault();

//   // Clear the form fields
//   form.reset();
// });
</script>

</body>

</html>