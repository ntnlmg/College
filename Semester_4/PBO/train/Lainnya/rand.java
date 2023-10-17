package Lainnya;

import java.util.Random;

public class rand {
    public static void main(String[] args) {
        // with random class
        Random r = new Random();
        int a = r.nextInt(11);
        int b = r.nextInt(11);

        System.out.println(a);
        System.out.println(b);

        // with math random
        int c = (int) (1 + Math.random() * 10);
        int d = (int) (1 + Math.random() * 10);

        System.out.println(c);
        System.out.println(d);
    }

}