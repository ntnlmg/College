package Mahasiswa;

public class MahasiswaTest {
    public static void main(String[] args) {
        Mahasiswa[] arr = {
                new Mahasiswa("Joni", 100),
                new Mahasiswa("Toni", 75),
                new Mahasiswa("Joko", 50)

        };

        // PerhitunganNilai app = new PerhitunganNilai();
        // double rata = app.hitungRatarata(null);
        // System.out.println(rata);

        double rata = PerhitunganNilai.hitungRatarata(arr);
        System.out.println(rata);
    }

}
