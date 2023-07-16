package remed;

public class Person {
  private static int personCount;

  public void add(int i) {
    personCount += i;
  }

  public int getAmount() {
    return personCount;
  }
}
