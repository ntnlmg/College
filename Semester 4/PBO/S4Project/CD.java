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

}
