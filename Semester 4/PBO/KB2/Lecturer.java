public class Lecturer {
    private static int count = 1;
    int countTeach = 0;
    private int id;
    private String name;
    private Course[] teach = new Course[5];

    // Constructor
    public Lecturer(String name) {
        this.id = count++;
        this.name = name;
    }

    // Getters
    public int getId() {
        return id;
    }

    public String getName() {
        return name;
    }

    public Course[] getTeach() {
        return teach;
    }

    public Course getTeachIndex(int index) {
        return teach[index];
    }

    public int getTeachCount() {

        for (int i = 0; i < teach.length; i++) {
            if (teach[i] == null) {
                break;
            } else {
                countTeach = i;
                countTeach++;
            }
        }
        return countTeach;
    }

    public String getAllTeach() {
        String str = " ";
        for (int i = 0; i < teach.length; i++) {
            if (teach[i] == null) {

            } else {
                str += teach[i].getName() + "|";
            }
        }
        return str;
    }

    // Setters
    public void setId(int id) {
        this.id = id;
    }

    public void setName(String name) {
        this.name = name;
    }

    public void setTeach(Course t) {
        teach[getTeachCount()] = t;
    }

    // Functional methods

    @Override
    public String toString() {
        return "00" + getId() + " " + getName() + " (" + getTeachCount() + ") " + getAllTeach();
    }
}
