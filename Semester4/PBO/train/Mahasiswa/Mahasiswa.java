package Mahasiswa;

public class Mahasiswa {
    private String nama;
    private double nilai;

    // constructor
    public Mahasiswa(String nama, double nilai) {
        this.nama = nama;
        this.nilai = nilai;
    }

    // getter setter

    public String getNama() {
        return nama;
    }

    public double getNilai() {
        return nilai;
    }

    public void setNama(String nama) {
        this.nama = nama;
    }

    public void setNilai(double nilai) {
        this.nilai = nilai;
    }

    @Override
    public String toString() {
        return "Mahasiswa [nama=" + nama + ", nilai=" + nilai + "]";
    }

    // toString()

}
