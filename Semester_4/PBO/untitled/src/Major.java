public enum Major {
    IS("Information System"),
    IT("Information Technology"),
    Design("Visual and Communication Design");

    private String fullName;

    Major(String i) {
        fullName = i;
    }

    public String getFullName() {
        return fullName;
    }
}
