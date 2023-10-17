public class Course {
    private int id;
    private static int counter = 1;
    private String name;
    private String schedule;
    private Lecturer lecturer;

    public int getId() {
        return id;
    }

    public String getName() {
        return name;
    }

    public String getSchedule() {
        return schedule;
    }

    public String getLecturer() {
        return lecturer.getName();
    }

    public void setName(String name) {
        this.name = name;
    }

    public void setSchedule(String schedule) {
        this.schedule = schedule;
    }

    public void setLecturer(Lecturer lecturer) {
        this.lecturer = lecturer;
    }

    public String getCourseData() {
        return getName() + " | " + getSchedule();
    }
}
