package S7Prac;

public class Prize {
    // Properties
    private String name;
    private int ticketRequire;
    private int remain;

    public Prize(String a, int b, int c) {
        this.name = a;
        this.ticketRequire = b;
        this.remain = c;
    }

    public void setUsedRemain() {
        --remain;
    }

    public int getRemain() {
        return remain;
    }

    public int getTicketRequire() {
        return ticketRequire;
    }

    public String getName() {
        return name;
    }

}
