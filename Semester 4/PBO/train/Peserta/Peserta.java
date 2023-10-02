public class Peserta {
    private String nama;
    private int usia;
    private String alamat;
    private String pendidikan;

    // generate

    public Peserta(String nama, int usia, String alamat, String pendidikan) {
        this.nama = nama;
        this.usia = usia;
        this.alamat = alamat;
        this.pendidikan = pendidikan;
    }

    public String getNama() {
        return nama;
    }

    public void setNama(String nama) {
        this.nama = nama;
    }

    public int getUsia() {
        return usia;
    }

    public void setUsia(int usia) {
        this.usia = usia;
    }

    public String getAlamat() {
        return alamat;
    }

    public void setAlamat(String alamat) {
        this.alamat = alamat;
    }

    public String getPendidikan() {
        return pendidikan;
    }

    public void setPendidikan(String pendidikan) {
        this.pendidikan = pendidikan;
    }

    public String toString() {
        return getNama() + "\t| " + getAlamat() + " | " + getPendidikan() + '\n';
    }
}