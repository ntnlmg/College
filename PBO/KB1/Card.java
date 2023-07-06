public class Card {
    private String name;
    private String bank;
    private double balance;
    private double point;

    public Card(String name, String bank) {
        this.name = name;
        this.bank = bank;
    }

    // setter
    public void setBalance(double balance) {
        this.balance = balance;
    }

    public void setName(String name) {
        this.name = name;
    }

    public void setPoint(double pnt) {
        this.point = pnt;
    }

    public void setBank(String bank) {
        this.bank = bank;
    }

    // getter
    public String getBank() {
        return bank;
    }

    public double getPoint() {
        return point;
    }

    public String getName() {
        return name;
    }

    public double getBalance() {
        return balance;
    }

}
