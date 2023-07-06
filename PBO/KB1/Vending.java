public class Vending {
    private String forsale;
    private Drinks[] D = new Drinks[3];

    public void addproducts(Drinks product) {

    }

    public void restock() {

    }

    public void checkStock() {
        for (int j = 0; j < D.length; j++) {
            System.out.println(D[j].getName());
        }

    }

    // public void get(flazzCard card, String product) {
    // if(card.getBalance() >=)
    // }

}
