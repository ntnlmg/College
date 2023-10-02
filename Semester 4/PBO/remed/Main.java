package remed;

public class Main {
  public static void main(String[] args) {
    Ferry fer = new Ferry();

    Cars mobil1 = new Cars();
    mobil1.setPerson(4);
    Cars mobil2 = new Cars();
    mobil2.setPerson(1);
    Cars mobil3 = new Cars();
    mobil3.setPerson(4);

    Bikes motor1 = new Bikes();
    motor1.setPerson(2);
    Bikes motor2 = new Bikes();
    motor2.setPerson(1);
    Bikes motor3 = new Bikes();
    motor3.setPerson(3);

    fer.addPerson(4);

    fer.addCars(mobil1, mobil2, mobil3);
    fer.addBikes(motor1, motor2, motor3);

    System.out.println(fer);

    // SOUT berapa penumpang, mobil, motor, orgMotor, orgMobil
  }
}