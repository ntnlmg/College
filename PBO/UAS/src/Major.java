// date : Monday, 3rd July 2023
// name : Natanael Missionday Gloryant

public enum Major {
    IS("Information System"),
    IT("Information Technology"),
    Design("Visual and Communication Design");

    private String standsFor;

    // modified constructor
    // score = 20
    Major(String i) {
        this.standsFor = i;
        // IS for Information System
        // IT for Information technology
        // Design for Visual and Communication Design
    }

    // getter
    public String standsFor() {
        return standsFor;
    }
}
