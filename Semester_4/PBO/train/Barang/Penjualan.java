package Barang;

public class Penjualan {
    private String tanggal;
    private Barang daftarBarang[];

    private static int counter = 0;

    public Penjualan() {
        tanggal = "00-00-00";
        daftarBarang = new Barang[Short.MAX_VALUE];
    }

    public String getTanggal() {
        return tanggal;
    }

    public void setTanggal(String tanggal) {
        this.tanggal = tanggal;
    }

    public Barang[] getDaftarBarang() {
        return daftarBarang;
    }

    public void setDaftarBarang(Barang[] daftarBarang) {
        this.daftarBarang = daftarBarang;
    }

    // functional method
    public void tambahBarang(Barang barang) {
        if (counter <= Short.MAX_VALUE) {
            daftarBarang[counter] = barang;
            counter++;
        } else {
            System.out.println("errr: penuh!!");
        }

    }

    public double hitungTotalHarga() {
        double total = .0;

        for (int i = 0; i < counter; i++) {
            total += daftarBarang[i].getHarga();
        }

        return total;
    }

    public void listBarang() {
        for (Barang barang : daftarBarang) {
            if (barang != null) {
                System.out.print(barang.toString());
            } else {
                continue;
            }

        }
    }

}
