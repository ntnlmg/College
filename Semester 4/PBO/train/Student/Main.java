
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        StudentManager sm = new StudentManager();

        System.out.print("Enter how many student data you want to input:");
        int many_student = in.nextInt();
        // for (int i = 0; i == many_student; i++) {
        int stu_count = 0;
        while (stu_count < many_student) {
            System.out.print("Nick-name, Age, and Score: ");
            String name = in.next();
            int age = in.nextInt();
            double score = in.nextDouble();
            in.nextLine(); // Clear the newline character

            Studentttt s = new Studentttt(name, age, score);
            sm.add_student(s);
            stu_count++;
        }
        System.out.println();
        System.out.println("Average score: " + sm.average_score());
        sm.show_student_lists();

        Studentttt hs = sm.get_highest_score();
        if (hs != null) {
            System.out.println("Student with highest score: " + hs);
        } else {
            System.out.println("No students found.");
        }
        in.close();
    }
}
