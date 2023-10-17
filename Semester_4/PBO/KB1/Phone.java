public class Phone {

    public void topup(Card card, double nominal) {
        card.setBalance(card.getBalance() + nominal);
    }

    public void checkBalance(Card card) {
        System.out.println(card.getName() + " " + card.getBank() + " "
                + card.getBalance() + " " + card.getPoint());
    }

    public void redeem(Card card) {
        if (card.getPoint() >= 10000) {
            int reward = (int) (card.getPoint() / 10000) * 1000;
            card.setBalance((card.getBalance() + reward));
            card.setPoint(card.getPoint() - reward * 10);

            System.out.println("You got " + reward + " from your point rewards");
            System.out.println("Balance remains: " + card.getBalance());
            System.out.println("Point remains: " + card.getPoint());
        } else {
            System.out.println("Sorry, you need" + (10000 - card.getPoint()) + "more points!");
        }
    }

}
