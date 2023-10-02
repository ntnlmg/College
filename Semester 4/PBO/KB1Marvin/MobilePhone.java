package KB1Marvin;

public class MobilePhone {

    public void topup(Flazzcard card, double ammount) {
        card.setSaldo(card.getSaldo() + ammount);
    }

    public void checkBalance(Flazzcard card) {
        System.out.println("[nama] [bank source] [balance] [point rewards]");
        System.out.println(card.getName() + " " + card.getBankName() + " "
                + card.getSaldo() + " " + card.getPoin());
    }

    public void redeem(Flazzcard card) {
        if (card.getPoin() >= 10000) {
            int balance_reward = (int) (card.getPoin() / 10000) * 1000;
            card.setSaldo(card.getSaldo() + balance_reward);
            card.setPoint(card.getPoin() - balance_reward * 10);

            System.out.println("You got " + balance_reward + " from your point rewards.");
            System.out.println("balance remains " + card.getSaldo());
            System.out.println("point rewards " + card.getPoin());
        } else {
            System.out.println("Sorry, you need " + (10000 - card.getPoin()) + " more points !");
        }
    }

}