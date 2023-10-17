public class Product {

    static int count = 0;
    // field : private
    private String name;
    private Double price;
    private int itemNumber;
    private int qty;
    private boolean status;

    // constructor : public
    public Product() {
        this.name = " ";
        this.price = .0;
        this.itemNumber = -1;
        this.qty = 0;
        this.status = true;
    }

    public Product(int itemNumber, String Name, Double Price, int Quantity) {
        this.itemNumber = itemNumber;
        this.name = Name;
        this.price = Price;
        this.qty = Quantity;
        this.status = true;
    }

    // getter
    public String getName() {
        return name;
    }

    public Double getPrice() {
        return price;
    }

    public int getitemNumber() {
        return itemNumber;
    }

    public int getQty() {
        return qty;
    }

    public boolean isstatus() {
        return status;
    }

    // setter
    public void setName(String name) {
        this.name = name;
    }

    public void setPrice(Double price) {
        this.price = price;
    }

    public void setitemNumber(int itemNumber) {
        this.itemNumber = itemNumber;
    }

    public void setQty(int qty) {
        this.qty = qty;
    }

    public void setstatus(boolean status) {
        this.status = status;
    }

    public boolean getStatus() {
        return status;
    }

    // functional methods
    public double getValue() {
        return getPrice() * getQty();
    }

    public String toString() {
        String isStatus = isstatus() ? "Active" : "Discontinued";
        String s = "Item Number\t\t: " + getitemNumber() + '\n' + "Name\t\t\t: " + getName() + '\n'
                + "Quantity in stock\t: "
                + getQty() + '\n'
                + "Price\t\t\t: $"
                + getPrice() + '\n'
                + "Stock value\t\t: $"
                + getValue() + '\n' + "Product Status\t\t: "
                + isStatus + '\n';
        return s;
        // return "Product [name=" + name + ", price=" + price + ", itemNumber=" +
        // itemNumber + ",
        // qty=" + qty + "]";
    }

    public void addToInventory(int Quantity) {
        qty += Quantity;
    }

    public void deductFromInventory(int Quantity) {
        qty = qty - Quantity > -1 ? qty - Quantity : 0;
    }

}