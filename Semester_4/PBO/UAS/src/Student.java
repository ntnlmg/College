// date : Monday, 3rd July 2023
// name : Natanael Missionday Gloryant

public class Student extends Person {
    private Date bornDate = new Date();
    private String id;
    private Major major;

    // id = 2 chars fname + 2 chars lname + dd + mm + yy + major
    // score = 10
    public Student(String fn, String ln, int d, int m, int y, Major mj) {
        super(fn, ln);
        bornDate = setDate(d, m, y);
        major = mj;
        String dd = (d < 10) ? "0" : "";
        String mm = (m < 10) ? "0" : "";
        dd = dd + d;
        mm = mm + m;

        id = fn.substring(0, 2) + ln.substring(0, 2) + dd + mm + y;
    }

    // called in constructor
    // score = 20
    public Date setDate(int d, int m, int y) {
        bornDate.set(d, m, y);
        return bornDate;
    }

    // will output = id + ":" + first name + last name + ":" + bornDate + ":" +
    // major
    // LoIr23011988:Lockey Irawan:23/01/1988:Information Technology
    // score : 20

    public String toString() {
        return id + ":" + super.toString() + ":" + bornDate + ":" + major.standsFor();
        //
    }
}
