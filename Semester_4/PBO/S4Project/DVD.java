public class DVD extends Product {
    // fields
    int lenght;
    int rating;
    String studio;

    // constructor
    public DVD(int itemNumber, String Name, Double Price, int Quantity, int movieLenght, int ageRating,
            String filmStudio) {
        super(itemNumber, Name, Price, Quantity);
        this.lenght = movieLenght;
        this.rating = ageRating;
        this.studio = filmStudio;
    }

    public int getLenght() {
        return lenght;
    }

    public void setLenght(int lenght) {
        this.lenght = lenght;
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
}
