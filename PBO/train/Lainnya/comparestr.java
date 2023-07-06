package Lainnya;

public class comparestr {
    public static void main(String[] args) {
        boolean isSame = compare(new String("The String"), new String("The not String"));
        System.out.println(isSame);
    }

    private static boolean compare(String str, String str0) {
        return str.equalsIgnoreCase(str0);
    }
}
