package remed;

public class Bikes {
  private final int MAXDATA = 2;
  private static int personCount = 0;
  private static int bikesCount = 0;

  public void setPerson(int i) {
    if (i > MAXDATA) {
      System.out.println("Invalid Amount!!");
    } else {
      personCount += i;
    }
  }

  public void add(int i) {
    bikesCount += i;
  }

  public int getAmount() {
    return bikesCount;
  }

  public int getPersons() {
    return personCount;
  }
}