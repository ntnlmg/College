package bikeproject;

public interface RoadParts extends BikeParts {
    // constant declaration
    public final String TERRAIN = "track_racing";

    // required methods after implementation
    public int getPostHeight();

    public void setPostHeight(int newValue);

    public int getTyreWidth();

    public void setTyreWidth(int newValue);
}
