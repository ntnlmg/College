package Barang;

public class PenjualanTester {
    public static void main(String[] args) {
        Barang b = new Barang(0, "Panci", 14000, 20);
        Barang b1 = new Barang(1, "Spons", 2000, 100);

        Penjualan p = new Penjualan();

        p.tambahBarang(b);
        p.tambahBarang(b1);
        p.listBarang();

        double total_harga = p.hitungTotalHarga();
        System.out.println(total_harga);

    }
}
