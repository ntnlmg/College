import java.util.Scanner;

public class productTest {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);

        Product[] products = new Product;

        for (int i = 0; i < products.length; i++) {
            System.out.print("itemNum: ");
            int itemNumber = in.nextInt();

            System.out.print("name: ");
            String name = in.next();

            System.out.print("price: ");
            double price = in.nextDouble();

            System.out.print("qtt: ");
            int qty = in.nextInt();

            products[i] = new Product(itemNumber, name, price, qty);
            System.out.println(products[i].toString());
        }

        int counter = 0;

        while (true) {
            System.out.print("item num: ");

            int itemNumber = in.nextInt();

            if (itemNumber == -1) {
                break;
            }
            System.out.print("name: ");
            String name = in.next();

            System.out.print("price: ");
            double price = in.nextDouble();

            System.out.print("qtt: ");
            int qty = in.nextInt();

            products[counter] = new Product(itemNumber, name, price, qty);
            System.out.println(products[counter].toString());
            counter++;
        }
    }
}