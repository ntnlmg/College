package LastProject;

public class DVD extends Product {
    // fields
    private int length;
    private int rating;
    private String studio;

    // constructor
    public DVD(int itemNumber, String Name, Double Price, int Quantity, int movieLength, int ageRating,
            String filmStudio) {
        super(itemNumber, Name, Price, Quantity);
        this.length = movieLength;
        this.rating = ageRating;
        this.studio = filmStudio;
    }

    public int getlength() {
        return length;
    }

    public void setlength(int length) {
        this.length = length;
    }

    public int getRating() {
        return rating;
    }

    public void setRating(int rating) {
        this.rating = rating;
    }

    public String getStudio() {
        return studio;
    }

    public void setStudio(String studio) {
        this.studio = studio;
    }

    public String toString() {
        String isStatus = isstatus() ? "Active" : "Discontinued";
        String s = "Item Number\t\t: "
                + getitemNumber() + '\n'
                + "Name\t\t\t: "
                + getName() + '\n'
                + "Movie length\t\t: "
                + getlength() + '\n'
                + "Age Rating\t\t: "
                + getRating() + '\n'
                + "Film Studio\t\t: "
                + getStudio() + '\n'
                + "Quantity in stock\t: "
                + getQty() + '\n'
                + "Price\t\t\t: $"
                + getPrice() + '\n'
                + "Stock value\t\t: $"
                + getValue() + '\n' + "Product Status\t\t: "
                + isStatus + '\n';
        return s;

    }

}
