public class Kumon {
    public static void main(String[] args) {
        Peserta p1 = new Peserta("joko", 15, "Malang", "SMA");
        Peserta p2 = new Peserta("tjakra", 15, "Jogja", "SMA");
        Kursus k = new Kursus("Coding", 11, 500_000);

        // Pendaftaran regist = new Pendaftaran();

        Pendaftaran regist[] = {
                new Pendaftaran(),
                new Pendaftaran()
        };

        regist[0].tambahPendaftar("17/08/23", p1, k);
        regist[1].tambahPendaftar("16/04/23", p2, k);
        k.listPeserta();
        System.out.println(regist[0].toString());

        double omset = k.hitungTotalPendapatan();

        System.out.println(omset);
    }
}
