class Main {
    public static void main(String[] args) {

        // input :
        Students stu = new Students("Lockey", "Irawan", 23, 1, 1988, Major.IT);
        Students stu1 = new Students("Clara", "Disha", 16, 9, 2003, Major.IS);

        // output :
        // LoIr23011988:Lockey Irawan:23/01/1988:Information Technology
        System.out.println(stu);
        System.out.println(stu1);

    }
}