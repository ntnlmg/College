public class RecordTester {

    public static void main(String[] args) {
        Record<Double> records = new Record<>();
        records.add(99.1);
        records.add(-1.23);
        records.add(7.41);
        records.sort();

        Record<String> records2 = new Record<>();
        records2.add("C");
        records2.add("Z");
        records2.add("A");
        records2.sort();
    }
}
