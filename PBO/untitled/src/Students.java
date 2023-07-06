public class Students extends Person {
    private Date bornDate;
    private String id;
    private Major major;

    public Students(String fn, String ln, int d, int m, int y, Major mj) {
        super(fn, ln);
        bornDate = setDate(d, m, y);
        major = mj;
        id = generateID(fn, ln);
    }

    public Date setDate(int d, int m, int y) {
        Date date = new Date();
        date.set(d, m, y);
        return date;
    }

    public String generateID(String fn, String ln) {
        String id = fn.substring(0, 2) + ln.substring(0, 2) +
                String.format("%02d%02d%02d", bornDate.getDay(), bornDate.getMonth(), bornDate.getYear());
        return id;
    }

    public String toString() {
        return id + ":" + super.toString() + ":" + bornDate.toString() + ":" + major.getFullName();
    }
}
