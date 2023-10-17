// nim : 312110010
// date : Monday, 3rd July 2023

public class Date {
    private int day;
    private int month;
    private int year;

    public int getDay() {
        return day;
    }

    public int getMonth() {
        return month;
    }

    public int getYear() {
        return year;
    }

    // getter and setter as needed
    // day = 1 .. 28,29,30,31 according to month and year -> (> 0 and < 32)
    // month = 1 .. 12 -> (>0 and < 12)
    // year = 1900 - 2023 -> (check y kabisat dan >= 1900 and <= 2023)
    // score = 20
    public void set(int d, int m, int y) {
        boolean check_kabisat = false;
        if (d >= 1 && d <= 31 && m >= 1 && m <= 12 && y >= 1900 && y <= 2023) {
            if (y % 4 == 0) {
                if (y % 100 == 0) {
                    if (y % 400 == 0) {
                        check_kabisat = true;
                    }
                } else {
                    check_kabisat = true;
                }
            }
            if (check_kabisat) {
                day = 00;
                month = 00;
                year = 00;
            } else {
                day = d;
                month = m;
                year = y;
            }

        } else {
            day = 00;
            month = 00;
            year = 00;
        }

    }

    // return format = dd/mm/yyyy
    public String toString() {
        String dd = (day < 10) ? "0" : "";
        String mm = (month < 10) ? "0" : "";
        return dd + "/" + mm + "/" + year;
    }
    // public String toString() {
    // return new String();
    // }

}
