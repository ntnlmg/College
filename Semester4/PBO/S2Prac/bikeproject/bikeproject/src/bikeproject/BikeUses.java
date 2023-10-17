package bikeproject;

public enum BikeUses {
    OFFROAD("Off-road"),
    TRACK("Tracks"),
    ROAD("Road"),
    DOWNHILL("Downhill"),
    TRAIL("Trail");

    private String info;

    private BikeUses(String s) {
        info = s;
    }

    public String getInfo() {
        return info;
    }
}
