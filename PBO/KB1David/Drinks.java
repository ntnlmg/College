package KB1David;

public class Drinks {
  private String name;
  private int price, stock;

  public Drinks(String p1, int p2) {
    name = p1;
    price = p2;
    stock = 0;
  }

  public void setStock(int pAmount) {
    stock += pAmount;
  }

  public void setPrice(int i) {
    price = i;
  }

  public int getPrice() {
    return price;
  }

  public String getName() {
    return name;
  }

  public int getStock() {
    return stock;
  }

}
