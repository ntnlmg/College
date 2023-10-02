package Barang;

public class Barang {
    private int kode;
    private String nama;
    private double harga;
    private int jumlah;

    public Barang(int kode, String nama, double harga, int jumlah) {
        this.kode = kode;
        this.nama = nama;
        this.harga = harga;
        this.jumlah = jumlah;
    }

    public int getKode() {
        return kode;
    }

    public void setKode(int kode) {
        this.kode = kode;
    }

    public String getNama() {
        return nama;
    }

    public void setNama(String nama) {
        this.nama = nama;
    }

    public double getHarga() {
        return harga;
    }

    public void setHarga(double harga) {
        this.harga = harga;
    }

    public int getJumlah() {
        return jumlah;
    }

    public void setJumlah(int jumlah) {
        this.jumlah = jumlah;
    }

    public String toString() {
        String s = getKode() + " " + getNama() + " " + getJumlah() + " " + getHarga() + '\n';
        return s;
    }

}