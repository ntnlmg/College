import java.util.Scanner;

public class Main {
    static int countLec, countStu, countCourses = 0;

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        Lecturer[] lec = new Lecturer[Byte.MAX_VALUE];
        Student[] stu = new Student[Byte.MAX_VALUE];
        Course[] courses = new Course[Byte.MAX_VALUE];
        int cursor;

        do {
            cursor = Menu(in);
            menuProgram(cursor, lec, courses, stu, in);
        } while (cursor != 0);

    }

    public static int Menu(Scanner in) {
        int cursor = -1;

        System.out.println("1. Add Lecturer");
        System.out.println("2. Add Student");
        System.out.println("3. Add Course");
        System.out.println("4. Set Course | Show All Lecturer | Show All Course");
        System.out.println("5. Take Course | Show All Student | Show All Course");
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

    public static void menuProgram(int cursor, Lecturer[] lec, Course[] courses, Student[] stu, Scanner in) {
        switch (cursor) {
            case 0:
                break;
            case 1:
                addLecturer(lec, in);
                break;
            case 2:
                addStudent(stu, in);
                break;
            case 3:
                addCourse(courses, in);
                break;
            case 4:
                setCourse(courses, lec, in);
                break;
            case 5:
                takeCourse(stu, courses, in);
                break;
            case 6:
                removeCourse(stu, courses, in);
                break;
            case 7:
                detailStudents(stu);
                setStudentState(stu, in);
                detailStudents(stu);
                break;
            case 8:
                detailLecturers(lec);
                break;
            case 9:
                detailStudents(stu);
                break;
            case 10:
                detailCourses(courses);
                break;
        }
    }

    private static void addLecturer(Lecturer[] lec, Scanner in) {
        String tempName;
        Lecturer tempLec;

        System.out.println("Please enter the lecturer name: ");
        in.nextLine();
        tempName = in.nextLine();

        try {
            tempLec = new Lecturer(tempName);
            lec[countLec++] = tempLec;
        } catch (Exception e) {
            // TODO: handle exception
            System.out.println("Sorry, Lecturer list is full: " + e);
        }
        System.out.println();
    }

    private static void addStudent(Student[] stu, Scanner in) {
        String tempName;
        Student tempStu;

        System.out.println("Please enter the student name: ");
        in.nextLine();
        tempName = in.nextLine();

        try {
            tempStu = new Student(tempName);
            stu[countStu++] = tempStu;
        } catch (Exception e) {
            // TODO: handle exception
            System.out.println("Sorry, Student list is full: " + e);
        }
        System.out.println();
    }

    private static void addCourse(Course[] courses, Scanner in) {
        String tempName;
        String tempSchedule;
        Course tempCourse;

        System.out.println("Please enter the Course name: ");
        in.nextLine();
        tempName = in.nextLine();

        System.out.println("Please enter the schedule (day, time): ");
        tempSchedule = in.nextLine();

        try {
            tempCourse = new Course(tempName, tempSchedule);
            courses[countCourses++] = tempCourse;
        } catch (Exception e) {
            // TODO: handle exception
            System.out.println("Sorry, Course list is full: " + e);
        }
        System.out.println();
    }

    private static void setCourse(Course[] courses, Lecturer[] lec, Scanner in) {
        int courseId;
        int lecturerId;

        System.out.println("Daftar Lecturer: ");
        for (int i = 0; i < lec.length && lec[i] != null; i++) {
            System.out.println((i + 1) + ". " + lec[i].getName());
        }

        System.out.println();

        System.out.println("Daftar Course:");
        for (int j = 0; j < courses.length && courses[j] != null; j++) {
            System.out.println((j + 1) + ". " + courses[j].getCourseData());
        }

        do {
            System.out.print("Pilih lecturer berdasarkan ID: ");
            lecturerId = in.nextInt() - 1;
            in.nextLine();
            // System.out.println("lecturerID" + lecturerId);
        } while (lecturerId < 0 || lecturerId >= lec.length || lec[lecturerId] == null);

        do {
            System.out.print("Pilih course berdasarkan ID: ");
            courseId = in.nextInt() - 1;
            in.nextLine();
            // System.out.println("courseID" + courseId);

        } while (courseId < 0 || courseId >= courses.length || courses[courseId] == null);

        courses[courseId].setLec(lec[lecturerId]);
        lec[lecturerId].setTeach(courses[courseId]);
        System.out.println();

    }

    private static void takeCourse(Student[] stu, Course[] courses, Scanner in) {
        int courseId;
        int stuId;

        System.out.println("Daftar Student: ");
        for (int i = 0; i < stu.length && stu[i] != null; i++) {
            System.out.println((i + 1) + ". " + stu[i].getName());
        }

        System.out.println();

        System.out.println("Daftar Course:");
        for (int j = 0; j < courses.length && courses[j] != null; j++) {
            System.out.println((j + 1) + ". " + courses[j].getCourseData());
        }

        do {
            System.out.print("Pilih Student berdasarkan ID: ");
            stuId = in.nextInt() - 1;
            in.nextLine();
            // System.out.println("StudentID" + stuId);
        } while (stuId < 0 || stuId >= stu.length || stu[stuId] == null);

        do {
            System.out.print("Pilih course berdasarkan ID: ");
            courseId = in.nextInt() - 1;
            in.nextLine();
            // System.out.println("courseID" + courseId);

        } while (courseId < 0 || courseId >= courses.length || courses[courseId] == null);

        if (stu[stuId].getStatus() == true) {
            stu[stuId].setLearn(courses[courseId]);
            System.out.println();
        } else {
            System.out.println("Sorry, " + stu[stuId].getName() + " can't take this course because "
                    + stu[stuId].getName() + " is" + (stu[stuId].getStatus() ? "Active" : "Non-active"));
            System.out.println();
        }

    }

    private static void removeCourse(Student[] stu, Course[] courses, Scanner in) {
        int courseId;
        int stuId;

        System.out.println("Daftar Student: ");
        for (int i = 0; i < stu.length && stu[i] != null; i++) {
            System.out.println((i + 1) + ". " + stu[i].getName());
        }

        System.out.println();

        System.out.println("Daftar Course:");
        for (int j = 0; j < courses.length && courses[j] != null; j++) {
            System.out.println((j + 1) + ". " + courses[j].getCourseData());
        }

        do {
            System.out.print("Pilih Student berdasarkan ID: ");
            stuId = in.nextInt() - 1;
            in.nextLine();
            // System.out.println("StudentID" + stuId);
        } while (stuId < 0 || stuId >= stu.length || stu[stuId] == null);

        do {
            System.out.print("Pilih Course berdasarkan ID: ");
            courseId = in.nextInt() - 1;
            in.nextLine();
            // System.out.println("courseID" + courseId);

        } while (courseId < 0 || courseId >= courses.length || courses[courseId] == null);

        stu[stuId].removeLearn(courses[courseId].getId());
        System.out.println();
    }

    private static void setStudentState(Student[] stu, Scanner in) {
        int Choice = -1;
        System.out.println("1: Activate");
        System.out.println("2: Deactivate");

        while (true) {
            try {
                System.out.print("Please enter your choice: ");
                Choice = in.nextInt();
                in.nextLine();
            } catch (Exception e) {
                System.out.println("Err" + e);
                in.nextLine();
            }

            if (Choice >= 0 && Choice <= 2) {
                break;
            } else {
                System.out.println("Only number 1 and 2 is allowed");
            }

        }

        switch (Choice) {
            case 1:
                activateStatus(stu, in);
                System.out.println();
                break;

            case 2:
                deactivateStatus(stu, in);
                break;
        }
    }

    public static void activateStatus(Student[] stu, Scanner in) {
        int cursor = getStudentNumber(stu, in);

        stu[cursor].setStatus(true);
    }

    public static void deactivateStatus(Student[] stu, Scanner in) {
        int cursor = getStudentNumber(stu, in);

        stu[cursor].setStatus(false);
        System.out.println(stu[cursor].getName() + " is " + stu[cursor].getStatus());
    }

    private static void detailLecturers(Lecturer[] lec) {
        for (Lecturer lect : lec) {
            if (lect == null) {

            } else {
                System.out.println(lect);
            }
        }
        System.out.println();
    }

    private static void detailStudents(Student[] stu) {
        for (Student stud : stu) {
            if (stud == null) {

            } else {
                System.out.println(stud);
            }
        }
        System.out.println();

    }

    public static void detailCourses(Course[] courses) {
        for (Course course : courses) {
            if (course == null) {

            } else {
                System.out.println(course);
            }
        }
        System.out.println();

    }

    public static int getLecturerNumber(Lecturer[] lec, Scanner in) {
        int count = -1;

        if (lec[0] == null) {
            return -1;
        }
        for (Lecturer lect : lec) {
            System.out.println(lect);
        }
        System.out.println();

        while (true) {
            System.out.print("Input Lecturer ID: ");
            try {
                count = in.nextInt();
            } catch (Exception e) {
                System.out.println("Err" + e);
                in.nextLine();
            }
            if (count >= 0 && count <= lec.length - 1) {
                return count;
            }
        }
    }

    public static int getStudentNumber(Student[] stu, Scanner in) {
        int count = -1;

        if (stu[0] == null) {
            return -1;
        }

        for (Student stud : stu) {
            if (stud == null) {

            } else {
                System.out.println(stud);
            }
        }

        while (true) {
            System.out.print("Input Student ID: ");
            try {
                count = in.nextInt() - 1;
            } catch (Exception e) {
                System.out.println("Err" + e);
                in.nextLine();
            }
            if (count >= 0 && count <= stu.length) {
                return count;
            }
        }
    }

    public static int getCourseNumber(Course[] courses, Scanner in) {
        int count = -1;

        if (courses[0] == null) {
            return -1;
        }

        for (Course course : courses) {
            System.out.println(course);
        }

        while (true) {
            System.out.print("Input Course ID: ");
            try {
                count = in.nextInt();
            } catch (Exception e) {
                System.out.println("Err" + e);
                in.nextLine();
            }
            if (count >= 0 && count <= courses.length - 1) {
                return count;
            }
        }
    }

    // how many input we want
    // public static int getNumInput(Scanner in) {
    // while (true) {
    // System.out.print("Enter number of input you wanna have (0 or greater): ");
    // try {
    // maxSize = in.nextInt();
    // } catch (Exception e) {
    // System.out.println("Beep-Beep wrong input: " + e);
    // in.nextLine();
    // }

    // if (maxSize >= 0) {
    // return maxSize;
    // }
    // }
    // }

}
