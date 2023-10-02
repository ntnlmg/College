package PN;

public class Mobil {
    private final int max_penumpang = 4;
    private static int car_counter = 0;
    private Penumpang orang = new Penumpang(max_penumpang);

    public Mobil(int jumlah_penumpang) {
        car_counter++;
        orang.setJumlah_penumpang(jumlah_penumpang);
    }

    public static int getCar_counter() {
        return car_counter;
    }

    public int get_penumpang_mobil() {
        return orang.get_jumlah_penumpang();
    }

}
