package LastProject;

public class CD extends Product {
    // fields
    String art;
    int numOfSongs;
    String label;

    // constructor
    public CD(int itemNumber, String Name, Double Price, int Quantity, String Artist, int numberOfSongs,
            String Label) {
        super(itemNumber, Name, Price, Quantity);
        this.art = Artist;
        this.numOfSongs = numberOfSongs;
        this.label = Label;
    }

    public String getArt() {
        return art;
    }

    public void setArt(String art) {
        this.art = art;
    }

    public int getNumOfSongs() {
        return numOfSongs;
    }

    public void setNumOfSongs(int numOfSongs) {
        this.numOfSongs = numOfSongs;
    }

    public String getLabel() {
        return label;
    }

    public void setLabel(String label) {
        this.label = label;
    }

    public String toString() {
        String isStatus = isStatus() ? "Active" : "Discontinued";
        String s = "Item Number\t\t: "
                + getitemNumber() + '\n'
                + "Name\t\t\t: "
                + getName() + '\n'
                + "Artist\t\t\t: "
                + getArt() + '\n'
                + "Songs on Album\t: "
                + getNumOfSongs() + '\n'
                + "Record Label\t\t: "
                + getLabel() + '\n'
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
