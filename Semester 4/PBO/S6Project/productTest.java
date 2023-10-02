import java.util.Scanner;

public class productTest {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);

        int maxSize = -1;

        while (true) {
            System.out.print("Enter num of product (0 or greater): ");
            try {
                maxSize = in.nextInt();
            } catch (Exception e) {
                System.out.println("Incorrect data type entered!" + e);
                in.nextLine();
            }

            if (maxSize >= 0) {
                break;
            }
        }

        if (maxSize == 0) {
            System.out.println("No products require!");
        } else {
            product products[] = new product[maxSize];

            int count = 0;
            int tempNum;
            String tempName;
            int tempQty;
            double tempPrice;

            product product;

            while (true) {
                if (count == maxSize) {
                    break;
                }

                System.out.print("ItemNum, Name, Quantity, Price: ");
                tempNum = in.nextInt();
                tempName = in.next();
                tempQty = in.nextInt();
                tempPrice = in.nextDouble();

                // products[count] = new product(tempNum, tempName, tempPrice, tempQty);
                // System.out.println();
                // System.out.println(products[count].toString());
                // count++;

                product = new product(tempNum, tempName, tempPrice, tempQty);
                products[count++] = product;

            }

            for (product producte : products) {
                System.out.println(producte);
            }
        }

    }
}
