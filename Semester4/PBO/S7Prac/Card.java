package S7Prac;

public class Card {
    // Properties
    private int creditBalance;
    private int ticketBalance;
    private int cardNumber;

    // Static counter
    private static int c = 0;

    // Methods or Behaviours
    public Card() {
        this.creditBalance = 0;
        this.ticketBalance = 0;
        this.cardNumber = ++c;
    }

    // setter
    public void setCreditBalance(int creds) {
        this.creditBalance = creditBalance + creds;
    }

    public void setUsedCreditBalance(int creds) {
        this.creditBalance = creditBalance - creds;
    }

    public void setTicketBalance(int ticks) {
        this.ticketBalance = ticketBalance + ticks;
    }

    public void setUsedTicketBalance(int ticks) {
        this.ticketBalance = ticketBalance - ticks;
    }

    public void setCardNumber(int cardID) {
        this.cardNumber = cardID;
    }

    // getter
    public int getCreditBalance() {
        return creditBalance;
    }

    public int getTicketBalance() {
        return ticketBalance;
    }

    public int getCardNumber() {
        return cardNumber;
    }

    public void data() {
        System.out.println("Credit: " + creditBalance + ", Ticket: " + ticketBalance + ", Card number: " + cardNumber);
    }

}
