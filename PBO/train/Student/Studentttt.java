public class Studentttt {
    private static int stu_id = 1;
    private String name;
    private int age;
    private double score;

    public Studentttt(String name, int age, double score) {
        stu_id++;
        this.name = name;
        this.age = age;
        this.score = score;
    }

    public static int getStu_id() {
        return stu_id;
    }

    public static void setStu_id() {
        stu_id++;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public int getAge() {
        return age;
    }

    public void setAge(int age) {
        this.age = age;
    }

    public double getScore() {
        return score;
    }

    public void setScore(double score) {
        this.score = score;
    }

    @Override
    public String toString() {
        return name + "\t\t" + age + "\t" + score;
    }

}
