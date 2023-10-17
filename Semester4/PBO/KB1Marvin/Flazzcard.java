package KB1Marvin;

public class Flazzcard {
    private String name;
    private String bank_name;
    private double saldo;
    private double point;

    Flazzcard(String name, String bank_name) {
        this.name = name;
        this.bank_name = bank_name;
    }

    public String getName() {
        return name;
    }

    public String getBankName() {
        return bank_name;
    }

    public double getSaldo() {
        return saldo;
    }

    public double getPoin() {
        return point;
    }

    public void setSaldo(double saldo) {
        this.saldo = saldo;
    }

    public void setPoint(double point) {
        this.point = point;
    }
}