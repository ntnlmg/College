package KB1David;

public class MobilePhone {

  public void topup(FlazzCard card1, int i) {
    card1.setBalance(i);
  }

  public void checkBalance(FlazzCard card) {
    System.out.println(card.getUser() + " " + card.getBank() + " " + card.getBalance() + " " + card.getPoint());
  }

  public void redeem(FlazzCard card) {
    int rewards;
    if (card.getPoint() < 10000) {
      System.out.println("Sorry, you need " + (10000 - card.getPoint()) + " more points !");
    } else {
      rewards = (int) card.getPoint() / 10000;
      System.out.println("You got " + (rewards * 1000) + " from your point rewards");
      card.setBalance(rewards * 1000);
      System.out.println("Balance remains " + card.getBalance());
      card.setPoint(-(rewards * 10000));
      System.out.println("Point rewards " + card.getPoint());
    }
  }

}
