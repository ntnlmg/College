package remed;

public class Ferry {
  private Person personCount = new Person();
  private Bikes bikesCount = new Bikes();
  private Cars carsCount = new Cars();

  public void addPerson(int i) {
    personCount.add(i);
  }

  public void addBikes(Bikes... paramBikes) {
    bikesCount.add(paramBikes.length);
  }

  public void addCars(Cars... paramCars) {
    carsCount.add(paramCars.length);
  }

  public String toString() {
    int totalPersons = personCount.getAmount() + bikesCount.getPersons() + carsCount.getPersons();
    String res = "";
    res += "Penumpang: " + personCount.getAmount() + "\nJumlah Mobil: " + carsCount.getAmount() + "\nJumlah Motor: "
        + bikesCount.getAmount() + "\nPenumpang Mobil: " + carsCount.getPersons() + "\nPenumpang Motor: "
        + bikesCount.getPersons() + "\nTotal Penumpang: " + totalPersons;
    return res;
  }
  // SOUT berapa penumpang, mobil, motor, orgMotor, orgMobil
}