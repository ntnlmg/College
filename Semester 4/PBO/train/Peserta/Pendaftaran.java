public class Pendaftaran {
    private int nomor;
    private String tanggal;
    private Peserta peserta;
    private Kursus kursus;
    private static int counter = 0;

    // Generate
    public Pendaftaran() {

    }

    public int getNomor() {
        return nomor;
    }

    public void setNomor(int nomor) {
        this.nomor = nomor;
    }

    public String getTanggal() {
        return tanggal;
    }

    public void setTanggal(String tanggal) {
        this.tanggal = tanggal;
    }

    public Peserta getPeserta() {
        return peserta;
    }

    public void setPeserta(Peserta peserta) {
        this.peserta = peserta;
    }

    public Kursus getKursus() {
        return kursus;
    }

    public void setKursus(Kursus kursus) {
        this.kursus = kursus;
    }

    public void getInfo(int nomor) {
        for (int i = 0; i < counter; i++) {

        }
    }

    public void tambahPendaftar(String tanggal, Peserta p, Kursus k) {
        peserta = p;
        kursus = k;
        nomor = counter++;
        this.tanggal = tanggal;
        k.tambahPeserta(p);

    }

    public String toString() {
        return peserta.getNama() + " registered to " + kursus.getNama();
    }

}
