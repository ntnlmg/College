public class Lecturer {
    private int id;
    private String name;
    private String[] teach;

    public int getId() {
        return id;
    }

    public String getName() {
        return name;
    }

    public String[] getTeach() {
        return teach;
    }

    public void setId(int id) {
        this.id = id;
    }

    public void setName(String name) {
        this.name = name;
    }

    public void setTeach(String... teach) {
        this.teach = teach;
    }
}
