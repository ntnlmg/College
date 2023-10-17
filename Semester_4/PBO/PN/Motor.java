package PN;

public class Motor {
    private final int max_penumpang = 2;
    private static int bike_counter = 0;
    private Penumpang orang = new Penumpang(max_penumpang);

    public Motor(int jumlah_penumpang) {
        bike_counter++;
        orang.setJumlah_penumpang(jumlah_penumpang);
    }

    public static int getBike_counter() {
        return bike_counter;
    }

    public int get_penumpang_motor() {
        return orang.get_jumlah_penumpang();
    }

}
