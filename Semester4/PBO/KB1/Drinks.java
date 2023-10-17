public class Drinks {
    private String name;
    private int price;

    public Drinks(String product, int price) {
        this.name = product;
        this.price = price;

        System.out.println(this.name + " added");
    }

    // setter
    public void setName(String product) {
        this.name = product;
    }

    public void setPrice(int x) {
        this.price = price;
    }

    public String getName() {
        return name;
    }

    public int getPrice() {
        return price;
    }

}
