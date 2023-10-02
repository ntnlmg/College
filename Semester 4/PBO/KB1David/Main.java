package KB1David;

public class Main {
  public static void main(String[] args) {
    MobilePhone mobilePhone = new MobilePhone();
    VendingMachine vendingMachine = new VendingMachine();
    FlazzCard card1 = new FlazzCard("Lockey Irawan", "BCA");
    FlazzCard card2 = new FlazzCard("David Yusaku", "BCA");

    Drinks cola = new Drinks("cola", 2500);
    Drinks fanta = new Drinks("fanta", 5000);
    Drinks sprite = new Drinks("sprite", 4500);

    vendingMachine.addproducts(cola, fanta, sprite);

    vendingMachine.restock("cola", 1);
    vendingMachine.restock("fanta", 2);
    vendingMachine.restock("sprite", 5);

    vendingMachine.checkStock();

    mobilePhone.topup(card1, 50_000);
    mobilePhone.checkBalance(card1);

    vendingMachine.get(card1, "cola");

    vendingMachine.get(card2, "cola");
    vendingMachine.get(card1, "cola");

    mobilePhone.redeem(card1);
    mobilePhone.topup(card1, 200000);

    vendingMachine.restock("fanta", 100);
    for (int i = 0; i < 30; i++) {
      vendingMachine.get(card1, "fanta");
    }

    vendingMachine.checkStock();
    mobilePhone.redeem(card1);
  }
}
