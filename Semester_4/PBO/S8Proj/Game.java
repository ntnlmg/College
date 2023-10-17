public class Game {
    private static int gameId = 1;
    private String awayTeam;
    private String homeTeam;
    private int awayScore;
    private int homeScore;
    private int temperature;

    public Game(String awayTeam, String homeTeam, int awayScore, int homeScore, int temperature) {
        this.awayTeam = awayTeam;
        this.homeTeam = homeTeam;
        this.awayScore = awayScore;
        this.homeScore = homeScore;
        this.temperature = temperature;
    }

    // Getters

    public String getAwayTeam() {
        return awayTeam;
    }

    public String getHomeTeam() {
        return homeTeam;
    }

    public int getAwayScore() {
        return awayScore;
    }

    public int getHomeScore() {
        return homeScore;
    }

    public int getTemperature() {
        return temperature;
    }

    @Override
    public String toString() {
        return "Game #" + gameId++ + "\n" +
                "Temperature: " + temperature + "\n" +
                "Away Team: " + awayTeam + ", " + awayScore + "\n" +
                "Home Team: " + homeTeam + ", " + homeScore;
    }
}
