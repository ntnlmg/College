package S7Prac;

public class Arcade {
    public static void main(String[] args) {

        Card one = new Card();
        Card two = new Card();

        Prize a = new Prize("Candy", 10, 10);
        Prize b = new Prize("Rice Cooker", 200, 10);
        Prize c = new Prize("Xbox Game Pass", 800, 1);

        Terminal t = new Terminal(a, b, c);
        Games g = new Games(2);

        t.setCreditBalance(one, 50);
        t.setCreditBalance(two, 25);

        g.play(one);
        g.play(one);
        g.play(one);
        g.play(one);
        g.play(two);

        one.data();
        two.data();

        t.redeemPrize(one, 1);

    }
}
