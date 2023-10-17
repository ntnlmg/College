package PN;

public class KapalFerry {
    Mobil car;
    Motor bike;
    Penumpang people;

    public KapalFerry(Mobil car, Motor bike, Penumpang people) {
        this.car = car;
        this.bike = bike;
        this.people = people;
    }

    public int jumlah_mobil() {
        return car.getCar_counter();
    }

    public int jumlah_motor() {
        return bike.getBike_counter();
    }

    public int total_penumpang() {
        return car.get_penumpang_mobil() + bike.get_penumpang_motor() + people.get_jumlah_penumpang();
    }

}
