public class Student {
    private static int countID = 1;
    public static String isStatus;
    int countLearn = 0;
    private int id;
    private String name;
    private Course[] learn = new Course[Byte.MAX_VALUE];
    private boolean status;

    // Constructor
    public Student(String name) {
        this.id = countID++;
        this.name = name;
        this.status = true;
    }

    // Getter
    public int getId() {
        return id;
    }

    public String getName() {
        return name;
    }

    public boolean getStatus() {
        return status;
    }

    public Course[] getLearn() {
        return learn;
    }

    public Course getLearnIndex(int index) {
        return learn[index];
    }

    public int getLearnCount() {

        for (int i = 0; i < learn.length; i++) {
            if (learn[i] == null) {
                break;
            } else {
                countLearn = i;
                countLearn++;
            }
        }
        return countLearn;
    }

    // Setter
    public void setId(int id) {
        this.id = id;
    }

    public void setName(String name) {
        this.name = name;
    }

    public void setStatus(boolean status) {
        this.status = status;
    }

    public void setLearn(Course l) {
        learn[getLearnCount()] = l;
    }

    // Functional methods
    public void removeLearn(int courseId) {
        for (int i = 0; i < learn.length; i++) {
            if (learn[i].getId() == courseId) {
                learn[i] = null;
                countLearn--;
                break;
            } else {
            }
        }
    }

    @Override
    public String toString() {
        isStatus = getStatus() ? "Active" : "Non-active";
        return "00" + getId() + " " + getName() + " (" + getLearnCount() + ") " + isStatus;
    }
}
