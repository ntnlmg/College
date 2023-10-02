package KB1Marvin;

import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);

        VendingMachine vendingMachine = new VendingMachine();
        MobilePhone mobilePhone = new MobilePhone();

        Flazzcard card1 = new Flazzcard("Lockey Irawan", "BCA");
        Flazzcard card2 = new Flazzcard("Marvin Adinata", "BNI");

        Product cola = new Product("cola", 2500);
        Product fanta = new Product("fanta", 5000);
        Product sprite = new Product("sprite", 4500);

        vendingMachine.addproducts(cola, fanta, sprite);
        System.out.println();

        vendingMachine.restock("cola", 1);
        vendingMachine.restock("fanta", 2);
        vendingMachine.restock("sprite", 5);

        vendingMachine.checkStock();
        System.out.println();

        mobilePhone.topup(card1, 50_000);

        mobilePhone.checkBalance(card1);
        System.out.println();
        // // output:
        // // [nama] [bank source] [balance] [point rewards]
        // Lockey Irawan BCA 50000 0

        vendingMachine.get(card1, "cola");
        System.out.println();
        // // output:
        // Enjoy your cola !
        // balance remains 47500.00
        // point rewards 250.00

        vendingMachine.get(card2, "cola");
        System.out.println();
        // // output:
        // Sorry, not enough money !

        vendingMachine.get(card1, "cola");
        System.out.println();

        mobilePhone.redeem(card1);
        System.out.println();
        // // output:
        // Sorry, you need 9750.00 more points !

        // // lakukan transaksi hingga mencapai 10_000 point atau lebih dan lakukan
        // redeem lagi
        // card1.addPoint(10000);
        mobilePhone.redeem(card1);
        System.out.println();

        in.close();
    }
}