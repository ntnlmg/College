package KB1Marvin;

public class VendingMachine {
    final int MAX_DRINKS = 3;
    private Product drinks[] = new Product[MAX_DRINKS];
    private int stock[] = new int[MAX_DRINKS];

    public void addproducts(Product... product) {
        for (int i = 0; i < product.length; i++) {
            drinks[i] = product[i];
        }
    }

    public void restock(String name, int ammount) {
        for (int i = 0; i < drinks.length; i++) {
            if (name.equals(drinks[i].getName())) {
                stock[i] += ammount;
            }
        }
    }

    public void checkStock() {
        for (int i = 0; i < drinks.length; i++) {
            System.out.println(drinks[i].getName() + " " + stock[i]);
        }
    }

    public void get(Flazzcard card, String product_name) {
        int i = 0;
        for (i = 0; i < drinks.length; i++) {
            if (product_name.equals(drinks[i].getName())) {
                break;
            } else {
                System.out.println("Noproduct found");
            }
        }
        if (card.getSaldo() >= drinks[i].getPrice() && stock[i] >= 1) {
            stock[i]--;
            double point_reward = drinks[i].getPrice() * 0.1;
            card.setSaldo(card.getSaldo() - drinks[i].getPrice());
            card.setPoint(card.getPoin() + point_reward);

            System.out.println("Enjoy your " + drinks[i].getName());
            System.out.println("balance remains " + card.getSaldo());
            System.out.println("point rewards " + card.getPoin());
        } else if (card.getSaldo() < drinks[i].getPrice()) {
            System.out.println("Sorry, not enough money !");
        } else {
            System.out.println("Sorry, cola is not available !");
            System.out.println("balance remains " + card.getSaldo());
            System.out.println("point rewards " + card.getPoin());
        }
    }

}