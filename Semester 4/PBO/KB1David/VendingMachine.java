package KB1David;

public class VendingMachine {
  private int MAXDRINKS = 3;
  private Drinks[] drinks = new Drinks[MAXDRINKS];

  public void addproducts(Drinks... param) {
    for (int i = 0; i < param.length; i++) {
      drinks[i] = new Drinks(param[i].getName(),
          param[i].getPrice());
    }
  }

  public void restock(String pName, int pAmount) {
    if (pAmount < 0) {
      System.out.println("Input tidak boleh negatif");
    } else {
      for (int i = 0; i < drinks.length; i++) {
        if (pName.equalsIgnoreCase(drinks[i].getName())) {
          drinks[i].setStock(pAmount);
        }
      }
    }
  }

  public void checkStock() {
    for (int i = 0; i < drinks.length; i++) {
      System.out.println(drinks[i].getName() + " " + drinks[i].getStock());
    }
  }

  public void get(FlazzCard card, String drink) {
    for (int i = 0; i < drinks.length; i++) {
      if (card.getBalance() < drinks[i].getPrice()) {
        System.out.println("Sorry, not enough money!");
        break;
      } else {
        if (drinks[i].getName().equalsIgnoreCase(drink)) {
          if (drinks[i].getStock() == 0) {
            System.out.println("Sorry, " + drinks[i].getName() + " is not available !");
            System.out.println("Balance remains " + card.getBalance());
            System.out.println("Point rewards " + card.getPoint());
          } else {
            drinks[i].setStock(-1);
            System.out.println("Enjoy your " + drinks[i].getName() + " !");
            card.setBalance(-drinks[i].getPrice());
            System.out.println("Balance remains " + card.getBalance());
            card.setPoint(drinks[i].getPrice() * 0.1);
            System.out.println("Point rewards " + card.getPoint());
          }
        }
      }
    }
  }

}
