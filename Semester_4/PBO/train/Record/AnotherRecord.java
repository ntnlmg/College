import java.util.ArrayList;
import java.util.List;

public class AnotherRecord<T extends Comparable<T>> {
    private List<T> value;

    public AnotherRecord() {
        value = new ArrayList<>();

    }

    public void add(T in) {
        value.add(in);
    }

    public void sort() { // bubble sort
        int size = value.size();
        for (int i = 0; i < size - 1; i++) {
            for (int j = 0; j < size - i - 1; j++) {
                T current = value.get(j);
                T next = value.get(j + 1);
                if (current.compareTo(next) > 0) {
                    // Swap elements
                    value.set(j, next);
                    value.set(j + 1, current);
                }
            }
        }
        System.out.println(value);
    }
}
