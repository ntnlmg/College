package Lainnya;

import java.util.Scanner;

public class strintdoubleeks {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);

        String n = in.next();

        try {
            System.out.println(Integer.parseInt(n));

            System.out.println(Double.parseDouble(n));

            System.out.println(String.format("%e", Double.parseDouble(n)));
        } catch (NumberFormatException e) {
            System.out.println("Bukan Angka");
        }
    }
}
