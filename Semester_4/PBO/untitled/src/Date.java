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

    public void set(int d, int m, int y) {
        // Memeriksa kevalidan tanggal, bulan, dan tahun
        if (y >= 1900 && y <= 2023) {
            boolean isLeapYear = (y % 4 == 0 && y % 100 != 0) || (y % 400 == 0);

            if (m >= 1 && m <= 12) {
                int maxDay;

                if (m == 2) {
                    maxDay = isLeapYear ? 29 : 28;
                } else if (m == 4 || m == 6 || m == 9 || m == 11) {
                    maxDay = 30;
                } else {
                    maxDay = 31;
                }

                if (d >= 1 && d <= maxDay) {
                    day = d;
                    month = m;
                    year = y;
                } else {
                    System.out.println("Invalid day for the given month and year.");
                }
            } else {
                System.out.println("Invalid month.");
            }
        } else {
            System.out.println("Invalid year.");
        }
    }

    public String toString() {
        return String.format("%02d/%02d/%04d", day, month, year);
    }
}
