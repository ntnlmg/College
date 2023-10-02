import javax.swing.Spring;

public class Main {
    public static void main(String[] args) {
        // Flazzcard
        Card card1 = new Card("Lockey Irawan", "BCA");
        Card card2 = new Card("Natan", "Mandiri");
        Phone mobilePhone = new Phone();
        Vending vendingMachine = new Vending();

        Drinks cola = new Drinks("Cola", 2500);
        Drinks fanta = new Drinks("Fanta", 5000);
        Drinks sprite = new Drinks("Sprite", 4500);

        vendingMachine.addproducts(cola);
        vendingMachine.addproducts(fanta);
        vendingMachine.addproducts(sprite);

        vendingMachine.checkStock();

        mobilePhone.topup(card1, 50000);

        mobilePhone.checkBalance(card1);

        mobilePhone.redeem(card1);

    }

}
