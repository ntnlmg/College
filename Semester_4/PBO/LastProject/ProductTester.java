package LastProject;

import java.util.Scanner;

public class ProductTester {
    static int count = 0;
    static int maxSize = -1;

    public static void main(String[] args) {

        Scanner in = new Scanner(System.in);
        int maxSize, menuChoice;

        maxSize = getNumProducts(in);
        if (maxSize == 0) {
            System.out.println("No products required!");
        } else {
            Product[] products = new Product[maxSize];

            for (int i = 0; i < maxSize; i++) {
                addToInventory(products, in);
            }

            do {
                menuChoice = getMenuOption(in);
                executeMenuChoice(menuChoice, products, in);
            } while (menuChoice != 0);
        }

    }

    // to choose menu
    public static int getMenuOption(Scanner in) {
        int option = -1;

        System.out.println("1. View Inventory");
        System.out.println("2. Add Stock");
        System.out.println("3. Deduct Stock");
        System.out.println("4. Discontinue Product");
        System.out.println("5. Continue Product");
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

    // menu program
    public static void executeMenuChoice(int menuChoice, Product[] products, Scanner in) {
        switch (menuChoice) {
            case 0:
                break;
            case 1:
                displayInventory(products);
                break;
            case 2:
                addStock(products, in);
                break;
            case 3:
                deductStock(products, in);
                break;
            case 4:
                discontinueInventory(products, in);
                break;
            case 5:
                continueInventory(products, in);
                break;
        }
    }

    // to select product in inventory
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

    // to determine how many product that we want to have in inventory
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

    public static void deductStock(Product[] products, Scanner in) {
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

    public static void addStock(Product[] products, Scanner in) {
        int productChoice = getProductNumber(products, in);
        int updateValue = -1;

        if (products[productChoice].getStatus() == true) {
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
        } else {
            System.out.println("The products is discontinued!");
        }
    }

    public static void addCDInventory(Product[] products, Scanner in) {
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

    public static void addDVDInventory(Product[] products, Scanner in) {
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
        int stockChoice = -1;
        System.out.println("1: CD");
        System.out.println("2: DVD");

        while (true) {
            try {
                System.out.print("Please enter option (0-1): ");
                stockChoice = in.nextInt();
                in.nextLine();
            } catch (Exception e) {
                System.out.println("Err" + e);
                in.nextLine();
            }

            if (stockChoice >= 0 && stockChoice <= 2) {
                break;
            } else {
                System.out.println("Only number 1 and 2 is allowed");
            }

        }

        switch (stockChoice) {
            case 1:
                addCDToInventory(products, in);
                break;

            case 2:
                addDVDToInventory(products, in);
                break;
        }

    }

    public static void addDVDToInventory(Product[] products, Scanner in) {

        int tempNum;
        String tempName;
        int tempQty;
        double tempPrice;
        int tempLength;
        int tempRating;
        String tempStudio;

        Product tempProduct;

        System.out.print("Please enter the DVD name: ");
        tempName = in.nextLine();

        System.out.print("Please enter the film studio name: ");
        tempStudio = in.nextLine();

        System.out.print("Please enter the age rating: ");
        tempRating = in.nextInt();

        in.nextLine();

        System.out.print("Please enter the movie length in minutes: ");
        tempLength = in.nextInt();

        in.nextLine();

        System.out.print("Please enter the quantity of stock for this product: ");
        tempQty = in.nextInt();

        System.out.print("Please enter the price for this product: ");
        tempPrice = in.nextDouble();

        System.out.print("Please enter the item number: ");
        tempNum = in.nextInt();

        in.nextLine();

        // products[count] = new Product(tempNum, tempName, tempPrice, tempQty);
        // System.out.println();
        // System.out.println(products[count].toString());
        // count++;

        tempProduct = new DVD(tempNum, tempName, tempPrice, tempQty, tempLength, tempRating, tempStudio);
        products[count++] = tempProduct;
        System.out.println();
    }

    public static void addCDToInventory(Product[] products, Scanner in) {

        int tempNum;
        String tempName;
        int tempQty;
        double tempPrice;
        String tempArt;
        int tempNumOfSongs;
        String tempLabel;

        Product tempProduct;

        System.out.print("Please enter the CD name: ");
        tempName = in.nextLine();

        System.out.print("Please enter the artist name: ");
        tempArt = in.nextLine();

        System.out.print("Please enter the record label name: ");
        tempLabel = in.nextLine();

        System.out.print("Please enter the number of songs: ");
        tempNumOfSongs = in.nextInt();

        in.nextLine();

        System.out.print("Please enter the quantity of stock for this product: ");
        tempQty = in.nextInt();

        System.out.print("Please enter the price for this product: ");
        tempPrice = in.nextDouble();

        System.out.print("Please enter the item number: ");
        tempNum = in.nextInt();

        in.nextLine();

        tempProduct = new CD(tempNum, tempName, tempPrice, tempQty, tempArt, tempNumOfSongs, tempLabel);
        products[count++] = tempProduct;
        System.out.println();
    }

    public static void discontinueInventory(Product[] products, Scanner in) {
        int productChoice = getProductNumber(products, in);

        products[productChoice].setStatus(false);
    }

    public static void displayInventory(Product[] products) {
        for (Product product : products) {
            System.out.println(product);
        }
    }

}

// addToInventory Origin
// public static void addToInventory(Product[] products, Scanner in) {

// int count = 0;
// int tempNum;
// String tempName;
// int tempQty;
// double tempPrice;

// Product TempProduct;

// while (true) {
// if (count == maxSize) {
// break;
// }

// System.out.print("Input product ID: ");
// tempNum = in.nextInt();

// in.nextLine();

// System.out.print("Input product name: ");
// tempName = in.nextLine();

// System.out.print("Input product quantity: ");
// tempQty = in.nextInt();

// System.out.print("Input product price: ");
// tempPrice = in.nextDouble();

// // products[count] = new Product(tempNum, tempName, tempPrice, tempQty);
// // System.out.println();
// // System.out.println(products[count].toString());
// // count++;

// TempProduct = new Product(tempNum, tempName, tempPrice, tempQty);
// products[count++] = TempProduct;
// System.out.println();
// }
// }

// addStock Origin
// public static void addStock(Product[] products, Scanner in) {
// int productChoice = getProductNumber(products, in);
// int updateValue = -1;
// System.out.print("How many products do you want to add? :");

// while (true) {
// try {
// updateValue = in.nextInt();
// } catch (Exception e) {
// System.out.println("Err" + e);
// in.nextLine();
// }

// if (updateValue > 0) {
// break;
// }
// }

// products[productChoice].addToInventory(updateValue);

// }

// To update the discontinued to continue
// public static void continueInventory(Product[] products, Scanner in) {
// int productChoice = getProductNumber(products, in);

// products[productChoice].setstatus(true);
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
