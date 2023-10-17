import java.util.Scanner;

public class Main {
    static int countLec = 0, countStu = 0, countCour = 0;
    static String tempName;
    static int tempLec, tempStu, tempCour;

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        Lecturer[] lecturers = new Lecturer[Byte.MAX_VALUE];
        Students[] students = new Students[Byte.MAX_VALUE];
        Course[] courses = new Course[Byte.MAX_VALUE];

        int cursor;

        do {
            cursor = Menu(in);
            menuProgram(cursor, lecturers, courses, students, in);
        } while (cursor != 0);

    }

    public static int Menu(Scanner in) {
        int cursor = -1;

        System.out.println("1. Add Lecturer");
        System.out.println("2. Add Student");
        System.out.println("3. Add Course");
        System.out.println("4. Set Course | Show All Student | Show All Course");
        System.out.println("5. Take Course");
        System.out.println("6. Remove Course | Show All Student | Show All Course Corresponding");
        System.out.println("7. Set Status | Show All Student");
        System.out.println("8. Detail Lecturer");
        System.out.println("9. Detail Student");
        System.out.println("10. Detail Course");
        System.out.println("0. Exit");

        while (true) {
            try {
                System.out.print("Please enter your choice (0-10): ");
                cursor = in.nextInt();
            } catch (Exception e) {
                // TODO: handle exception
                System.out.println("Beep-Beep wrong input: " + e);
                in.nextLine();
            }

            if (cursor >= 0 && cursor <= 10) {
                break;
            }
        }

        System.out.println();
        return cursor;

    }

    public static void menuProgram(int cursor, Lecturer[] lecturers, Course[] courses, Students[] students,
            Scanner in) {

        switch (cursor) {
            case 0:
                break;
            case 1: // addLecturer
                System.out.println("Please enter the lecturer name: ");
                in.nextLine();
                tempName = in.nextLine();
                addLecturer(lecturers[countLec++], tempName);
                break;

            case 2: // addStudent
                System.out.println("Please enter the student name: ");
                in.nextLine();
                tempName = in.nextLine();
                addStudent(students[countStu++], tempName);
                break;

            case 3: // addCourse
                System.out.println("Please enter the Course name: ");
                in.nextLine();
                tempName = in.nextLine();

                System.out.println("Please enter the schedule (day, time): ");
                String tempSchedule = in.nextLine();
                addCourse(courses[countCour++], tempName, tempSchedule);
                break;

            case 4: // setCourse
                System.out.println("Daftar Lecturer: ");
                for (int i = 1; i < countLec + 1; i++) {
                    if (lecturers[i] == null) {

                    } else {
                        System.out.println("00" + i + " " + lecturers[i - 1].getName());
                    }
                }

                System.out.println();

                System.out.println("Daftar Course:");
                for (int j = 1; j < countCour + 1; j++) {
                    System.out.println("00" + j + " " + courses[j - 1].getCourseData());
                }

                System.out.print("Pilih Lecturer berdasarkan ID: ");
                tempLec = in.nextInt();
                System.out.print("Pilih Course berdasarkan ID: ");
                tempCour = in.nextInt();

                setCourse(courses[tempCour - 1], lecturers[tempLec - 1]);
                break;

            // case 5:
            // takeCourse(students, courses);
            // break;

            // case 6:
            // removeCourse(stu, cour, in);
            // break;

            // case 7:
            // detailStudents(stu);
            // setStudentState(stu, in);
            // break;

            case 8:
                detailLecturers(lecturers);
                break;

            // case 9:
            // detailStudents(stu);
            // break;

            // case 10:
            // detailCourses(cour);
            // break;
        }
    }

    public static Lecturer addLecturer(Lecturer lec, String name) {
        lec = new Lecturer();
        lec.setName(name);
        return lec;
    }

    public static Students addStudent(Students stu, String name) {
        stu = new Students();
        stu.setName(name);
        return stu;
    }

    public static Course addCourse(Course cour, String name, String schedule) {
        cour = new Course();
        cour.setName(name);
        cour.setSchedule(schedule);
        return cour;
    }

    public static void setCourse(Course cour, Lecturer lec) {
        cour.setLecturer(lec);
        lec.setTeach(cour.getName());
    }

    public static void detailLecturers(Lecturer[] lecturers) {
        for (int i = 1; i < countLec + 1; i++) {
            System.out.println("00" + i + " " + lecturers[i - 1].getName());

        }
    }
}