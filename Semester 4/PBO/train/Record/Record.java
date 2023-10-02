import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

public class Record<T extends Comparable<T>> {
    private List<T> value;

    public Record() {
        value = new ArrayList<>();

    }

    public void add(T in) {
        value.add(in);
    }

    public void sort() { // bubble sort
        System.out.println("Before sort: " + value);
        Collections.sort(value);
        System.out.println("After sort" + value);
        System.out.println();
    }
}
