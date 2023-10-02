import java.util.ArrayList;
import java.util.List;

public class tst {
    public static void main(String[] args) {
        // int d = 0;
        // if (d >= 1 && d <= 31) {
        // System.out.println("benar");
        // } else {
        // System.out.println("salah");
        // }
        // LoIr23011988
        // Irawan:23/01/1988
        // String a = "Lockey";
        // String b = "Irawan";
        // String c = a.substring(0, 2);
        // String d = b.substring(0, 2);
        // System.out.println(c + d);

        int tahun = 2001;
        boolean check_kabisat = false;
        if (tahun % 4 == 0) {
            if (tahun % 100 == 0) {
                if (tahun % 400 == 0) {
                    check_kabisat = true;
                }
            } else {
                check_kabisat = true;
            }
        }

        if (check_kabisat) {
            System.out.println(tahun + " adalah tahun kabisat.");
        } else {
            System.out.println(tahun + " bukan tahun kabisat.");
        }

        int a = 1;
        String b = "0" + a;
        String mm = (a < 10) ? "0" : "" + a;
        String c = mm + a;
        System.out.println(b);
        System.out.println(c);

        // Date d = new Date();
        // d.set(23, 1, 1988);
        // System.out.println(d.toString());

    }
}
