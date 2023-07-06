package Class2Class;

public class main {
    public static void main(String[] args) {

    }

    public static Staff cast(Stu obj1, Staff obj2) {
        // values changing
        obj2.id = obj1.id;
        obj2.phone = null;
        return obj2;
    }
}
