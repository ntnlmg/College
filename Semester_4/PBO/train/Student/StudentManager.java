import java.util.ArrayList;
import java.util.List;

public class StudentManager {
    private List<Studentttt> stu;

    public StudentManager() {
        stu = new ArrayList<>();
    }

    public void add_student(Studentttt student) {
        stu.add(student);
    }

    public double average_score() {

        if (stu.isEmpty()) {
            return .0;
        }

        double total_score = .0;
        for (Studentttt Student : stu) {
            total_score += Student.getScore();
        }
        return total_score / stu.size();
    }

    public void show_student_lists() {
        System.out.println("Student name\tage\tscore");
        for (Studentttt Student : stu) {
            System.out.println(Student);
        }
        System.out.println();
    }

    public Studentttt get_highest_score() {
        if (stu.isEmpty()) {
            return null;
        }

        Studentttt highest_score_student = stu.get(0);
        for (Studentttt Student : stu) {
            if (Student.getScore() > highest_score_student.getScore()) {
                highest_score_student = Student;
            }
        }
        return highest_score_student;
    }

}