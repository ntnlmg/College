package S7Prac;

public class Terminal {
    private Prize[] prizes = new Prize[3];

    public Terminal(Prize a, Prize b, Prize c) {
        prizes[0] = a;
        prizes[1] = b;
        prizes[2] = c;
    }

    // Methods
    public void setCreditBalance(Card a, int money) {
        int cb = money * 2;
        a.setCreditBalance(cb);
    }

    public void transferCredit(Card a, Card b, int creds) {
        if (a.getCreditBalance() >= creds) {
            System.out.println("Transfered");
            a.setUsedCreditBalance(creds);
            b.setCreditBalance(creds);
        } else {
            System.out.println("Insufficient credits");
        }
    }

    public void transferTicket(Card a, Card b, int ticks) {
        if (a.getCreditBalance() >= ticks) {
            System.out.println("Transfered");
            a.setUsedTicketBalance(ticks);
            b.setTicketBalance(ticks);
        } else {
            System.out.println("Insufficient tickets");
        }
    }

    public void redeemPrize(Card a, int option) {
        if (option == 0 || option > 3) {
            System.out.println("Because prize option is only 1-3");
        } else {
            if (prizes[option - 1].getRemain() > 0) {
                if (a.getTicketBalance() >= prizes[option - 1].getTicketRequire()) {
                    System.out.println("Congratulations, You choose " + prizes[option - 1].getName());
                    a.setUsedTicketBalance(prizes[option - 1].getTicketRequire());
                    prizes[option - 1].setUsedRemain();
                    System.out.println("Remaining ticket: " + a.getTicketBalance());
                } else {
                    System.out.println("Insufficient Tickets");
                }
            } else {
                System.out.println("Prize Empty!");
            }
        }
    }

}