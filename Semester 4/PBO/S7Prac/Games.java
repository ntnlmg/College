package S7Prac;

import java.util.Random;

public class Games {
    // Properties
    private int creditRequire;

    // Behaviours
    public Games(int cr) {
        creditRequire = cr;
    }

    public void play(Card a) {
        if (a.getCreditBalance() >= creditRequire) {
            // play
            a.setUsedCreditBalance(creditRequire);
            System.out.println("Enjoy the game");

            // random tickets
            Random rand = new Random();
            int r = rand.nextInt(500);
            a.setTicketBalance(r);
            System.out.println("You've got " + r + " tickets");

        } else {
            System.out.println("Insufficient credits");
        }
    }
}
