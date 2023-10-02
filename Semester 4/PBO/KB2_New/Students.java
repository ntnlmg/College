public class Students {
    private int id;
    private static int counter = 1;
    private String name;
    private String learn[];
    private boolean status;

    public Students() {
        id = counter++;
        name = " ";
        status = true;
    }

    public int getId() {
        return id;
    }

    public String getName() {
        return name;
    }

    public boolean getStatus() {
        return status;
    }

    public void setName(String name) {
        this.name = name;
    }

    public void setLearn(String... learn) {
        this.learn = learn;
    }

    public void setStatus(boolean status) {
        this.status = status;
    }
}
