import java.util.Scanner;

public class ProductTester {
    static int maxSize = -1;

    public static void main(String[] args) {

        Scanner in = new Scanner(System.in);
        int maxSize, menuChoice;

        maxSize = getNumProducts(in);
        if (maxSize == 0) {
            System.out.println("No products required!");
        } else {
            Product[] products = new Product[maxSize];
            addToInventory(products, in);
            do {
                menuChoice = getMenuOption(in);
                executeMenuChoice(menuChoice, products, in);
            } while (menuChoice != 0);
        }

    }

    public static int getMenuOption(Scanner in) {
        int option = -1;

        System.out.println("1. View Inventory");
        System.out.println("2. Add Stock");
        System.out.println("3. Deduct Stock");
        System.out.println("4. Continue Product");
        System.out.println("5. Discontinue Product");
        System.out.println("0. Exit");

        while (true) {
            try {
                System.out.print("Please enter option (0-4): ");
                option = in.nextInt();
            } catch (Exception e) {
                System.out.println("Err" + e);
                in.nextLine();
            }

            if (option >= 0 && option <= 5) {
                break;
            }
        }
        return option;
    }

    public static void executeMenuChoice(int menuChoice, Product[] products, Scanner in) {
        switch (menuChoice) {
            case 0:
                break;
            case 1:
                displayInventory(products);
                break;
            case 2:
                addInventory(products, in);
                break;
            case 3:
                deductInventory(products, in);
                break;
            case 4:
                continueInventory(products, in);
                break;
            case 5:
                discontinueInventory(products, in);
                break;
        }
    }

    public static int getProductNumber(Product[] products, Scanner in) {
        int productChoice = -1;

        if (products[0] == null) {
            return -1;
        }

        for (Product product : products) {
            System.out.println(product);
        }

        while (true) {
            System.out.print("Input product ID (0-" + (products.length - 1) + "):");
            try {
                productChoice = in.nextInt();
            } catch (Exception e) {
                System.out.println("Err" + e);
                in.nextLine();
            }
            if (productChoice >= 0 && productChoice <= products.length - 1) {
                return productChoice;
            }
        }
    }

    public static int getNumProducts(Scanner in) {
        while (true) {
            System.out.print("Enter num of product (0 or greater): ");
            try {
                maxSize = in.nextInt();
            } catch (Exception e) {
                System.out.println("Incorrect data type entered!" + e);
                in.nextLine();
            }

            if (maxSize >= 0) {
                return maxSize;
            }
        }
    }

    public static void deductInventory(Product[] products, Scanner in) {
        int productChoice = getProductNumber(products, in);
        int updateValue = -1;
        System.out.print("How many products do you want to remove? :");

        while (true) {
            try {
                updateValue = in.nextInt();
            } catch (Exception e) {
                System.out.println("Err" + e);
                in.nextLine();
            }

            if (updateValue > 0) {
                break;
            }
        }

        products[productChoice].deductFromInventory(updateValue);

    }

    public static void addInventory(Product[] products, Scanner in) {
        int productChoice = getProductNumber(products, in);
        int updateValue = -1;
        System.out.print("How many products do you want to add? :");

        while (true) {
            try {
                updateValue = in.nextInt();
            } catch (Exception e) {
                System.out.println("Err" + e);
                in.nextLine();
            }

            if (updateValue > 0) {
                break;
            }
        }

        products[productChoice].addToInventory(updateValue);

    }

    public static void addToInventory(Product[] products, Scanner in) {

        int count = 0;
        int tempNum;
        String tempName;
        int tempQty;
        double tempPrice;

        Product TempProduct;

        while (true) {
            if (count == maxSize) {
                break;
            }

            System.out.print("Input product ID: ");
            tempNum = in.nextInt();

            in.nextLine();

            System.out.print("Input product name: ");
            tempName = in.nextLine();

            System.out.print("Input product quantity: ");
            tempQty = in.nextInt();

            System.out.print("Input product price: ");
            tempPrice = in.nextDouble();

            // products[count] = new Product(tempNum, tempName, tempPrice, tempQty);
            // System.out.println();
            // System.out.println(products[count].toString());
            // count++;

            TempProduct = new Product(tempNum, tempName, tempPrice, tempQty);
            products[count++] = TempProduct;
            System.out.println();
        }
    }

    public static void continueInventory(Product[] products, Scanner in) {
        int productChoice = getProductNumber(products, in);

        products[productChoice].setstatus(true);
    }

    public static void discontinueInventory(Product[] products, Scanner in) {
        int productChoice = getProductNumber(products, in);

        products[productChoice].setstatus(false);
    }

    public static void displayInventory(Product[] products) {
        for (Product product : products) {
            System.out.println(product);
        }
    }

}

// Section 6

// int maxSize = -1;

// while (true) {
// System.out.print("Enter num of product (0 or greater): ");
// try {
// maxSize = in.nextInt();
// } catch (Exception e) {
// System.out.println("Incorrect data type entered!" + e);
// in.nextLine();
// }

// if (maxSize >= 0) {
// break;
// }
// }

// if (maxSize == 0) {
// System.out.println("No products require!");
// } else {
// Product products[] = new Product[maxSize];

// int count = 0;
// int tempNum;
// String tempName;
// int tempQty;
// double tempPrice;

// Product product;

// while (true) {
// if (count == maxSize) {
// break;
// }

// tempNum = in.nextInt();

// in.nextLine();

// tempName = in.nextLine();
// tempQty = in.nextInt();
// tempPrice = in.nextDouble();

// // products[count] = new Product(tempNum, tempName, tempPrice, tempQty);
// // System.out.println();
// // System.out.println(products[count].toString());
// // count++;

// product = new Product(tempNum, tempName, tempPrice, tempQty);
// products[count++] = product;

// }

// for (Product producte : products) {
// System.out.println(producte);
// }
// }

// Section 5
// for (int i = 0; i < products.length; i++) {
// System.out.print("itemNum: ");
// int itemNumber = in.nextInt();

// System.out.print("name: ");
// String name = in.next();

// System.out.print("price: ");
// double price = in.nextDouble();

// System.out.print("qtt: ");
// int qty = in.nextInt();

// products[i] = new Product(itemNumber, name, price, qty);
// System.out.println(products[i].toString());
// }

// ============================================================
// int counter = 0;

// while (true) {
// System.out.print("item num: ");

// int itemNumber = in.nextInt();

// if (itemNumber == -1) {
// break;
// }
// System.out.print("name: ");
// String name = in.next();

// System.out.print("price: ");
// double price = in.nextDouble();

// System.out.print("qtt: ");
// int qty = in.nextInt();

// products[counter] = new Product(itemNumber, name, price, qty);
// System.out.println(products[counter].toString());
// counter++;
// }

// Section 4
// Product musicCD = new Product(11, "Greatest Hits", 9.99, 25);
// Product DVD = new Product(21, "Fast and Furious", 13.99, 10);
// Product officeSupplies = new Product();
// Product software = new Product();

// officeSupplies.setitemNumber(1);
// officeSupplies.setName("Paper");
// officeSupplies.setPrice(0.99);
// officeSupplies.setQty(50000);

// software.setitemNumber(31);
// software.setName("Adobe Premiere");
// software.setPrice(299.99);
// software.setQty(15);

// System.out.println(musicCD.toString());
// System.out.println(DVD.toString());
// System.out.println(officeSupplies.toString());
// System.out.println(software.toString());
