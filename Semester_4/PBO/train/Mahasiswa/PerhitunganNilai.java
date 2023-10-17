package Mahasiswa;

public class PerhitunganNilai {
    public static double hitungRatarata(Mahasiswa... arr) {
        double rata = .0;
        double sum = .0;

        for (int i = 0; i < arr.length; i++) {
            sum += arr[i].getNilai();
        }

        rata = sum / arr.length;

        return rata;
    }
}