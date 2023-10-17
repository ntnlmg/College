package PN;

public class Pelabuhan {
    public static void main(String[] args) {
        Mobil a1 = new Mobil(4);
        
        Motor b1 = new Motor(2);

        Penumpang c1 = new Penumpang(20);

        KapalFerry titanic = new KapalFerry(a1, b1, c1);

        System.out.println(titanic.jumlah_mobil());
        System.out.println(titanic.jumlah_motor());
        System.out.println(titanic.total_penumpang());
    }
}
