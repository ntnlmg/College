package bikeproject;

public interface MountainParts extends BikeParts {
    // constant declaration
    public final String TERRAIN = "off_road";

    // required methods after implementation

    public String getSuspension();

    public void setSuspension(String newValue);

    public String getType();

    public void setType(String newValue);
}