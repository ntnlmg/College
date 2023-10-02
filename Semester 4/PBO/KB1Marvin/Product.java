package KB1Marvin;

public class Product {
    private String name;
    private int price;

    Product(String name, int price) {
        this.name = name;
        this.price = price;
        System.out.println(this.name + " ADDED");
    }

    public String getName() {
        return name;
    }

    public int getPrice() {
        return price;
    }

}