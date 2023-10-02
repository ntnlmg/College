public class Kursus {
    private String nama;
    private int sesi;
    private double biaya;
    private Peserta daftarPeserta[];
    public static int counter = 0;

    // Generate
    public Kursus(String nama, int sesi, double biaya) {
        this.nama = nama;
        this.sesi = sesi;
        this.biaya = biaya;
        daftarPeserta = new Peserta[Short.MAX_VALUE];
    }

    public String getNama() {
        return nama;
    }

    public void setNama(String nama) {
        this.nama = nama;
    }

    public int getSesi() {
        return sesi;
    }

    public void setSesi(int sesi) {
        this.sesi = sesi;
    }

    public double getBiaya() {
        return biaya;
    }

    public void setBiaya(double biaya) {
        this.biaya = biaya;
    }

    public Peserta[] getDaftarPeserta() {
        return daftarPeserta;
    }

    public void setDaftarPeserta(Peserta[] daftarPeserta) {
        this.daftarPeserta = daftarPeserta;
    }

    public void tambahPeserta(Peserta p) {
        daftarPeserta[counter++] = p;
    }

    public void listPeserta() {
        for (int i = 0; i < counter; i++) {
            System.out.print(daftarPeserta[i].toString());
        }
    }

    public double hitungTotalPendapatan() {
        double total = biaya * counter;
        return total;
    }
}
