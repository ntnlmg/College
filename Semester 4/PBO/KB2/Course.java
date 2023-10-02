public class Course {
    private static int count = 1;
    private int id;
    private String name;
    private String Schedule;
    private Lecturer Lec;

    // Constructor
    public Course(String name, String schedule) {
        this.id = count++;
        this.name = name;
        Schedule = schedule;

    }

    // getter
    public int getId() {
        return id;
    }

    public String getName() {
        return name;
    }

    public String getSchedule() {
        return Schedule;
    }

    public Lecturer getLec() {
        return Lec;
    }

    // setter
    public void setId(int id) {
        this.id = id;
    }

    public void setName(String name) {
        this.name = name;
    }

    public void setSchedule(String schedule) {
        Schedule = schedule;
    }

    public void setLec(Lecturer lec) {
        Lec = lec;
    }

    // Functional methods
    public String getCourseData() {
        return getName() + " on " + getSchedule();
    }

    public void setLecturer(Lecturer lec) {
        this.Lec = lec;
    }

    public void deductCourse(String name) {
        name = " ";
        this.name = name;
    }

    @Override
    public String toString() {
        return "00" + getId() + " " + getName() + " on " + getSchedule() + " | " + getLec();
    }

}
