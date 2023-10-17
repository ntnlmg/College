public class Main {
    public static void main(String[] args) {
        Cuboid<Double> c1 = new Cuboid<>(1.3, 2.2, 2.0);
        Cuboid<Integer> c2 = new Cuboid<>(1, 2, 3);

        System.out.println(c1.getVolume());
        System.out.println(c1.toString());
        System.out.println(c2.toString());

    }
}