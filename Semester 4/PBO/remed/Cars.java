package remed;

public class Cars {
  private final int MAXDATA = 4;
  private static int personCount = 0;
  private static int carsCount = 0;

  public void setPerson(int i) {
    if (i > MAXDATA) {
      System.out.println("Invalid Amount!!");
    } else {
      personCount += i;
    }
  }

  public void add(int i) {
    carsCount += i;
  }

  public int getAmount() {
    return carsCount;
  }

  public int getPersons() {
    return personCount;
  }
}