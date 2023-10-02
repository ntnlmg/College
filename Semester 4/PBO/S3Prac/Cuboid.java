public class Cuboid<T extends Number> {
    private T length;
    private T breadth;
    private T height;

    public Cuboid(T l, T b, T h) {
        this.length = l;
        this.breadth = b;
        this.height = h;
    }

    public double getVolume() {
        double l = length.doubleValue();
        double b = breadth.doubleValue();
        double h = height.doubleValue();
        return l * b * h;
    }

    public String toString() {
        String s = length + " - " + breadth + " - " + height;
        return s;
    }
}
