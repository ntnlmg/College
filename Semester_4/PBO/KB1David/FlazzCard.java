package KB1David;

public class FlazzCard {
  private String name, bank_source;
  private double balance, point_rewards;

  public FlazzCard(String p1, String p2) {
    name = p1;
    bank_source = p2;
    balance = 0;
    point_rewards = 0;
  }

  public void setBalance(int i) {
    balance += i;
  }

  public void setPoint(double d) {
    point_rewards += d;
  }

  public String getUser() {
    return name;
  }

  public String getBank() {
    return bank_source;
  }

  public double getBalance() {
    return balance;
  }

  public double getPoint() {
    return point_rewards;
  }

}
