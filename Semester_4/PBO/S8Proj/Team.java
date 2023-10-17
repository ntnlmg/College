public class Team {
    private String name;
    private int wins;
    private int losses;
    private int ties;
    private int goalsScored;
    private int goalsAllowed;

    public Team(String name) {
        this.name = name;
        this.wins = 0;
        this.losses = 0;
        this.ties = 0;
        this.goalsScored = 0;
        this.goalsAllowed = 0;
    }

    public String getName() {
        return name;
    }

    public int getWins() {
        return wins;
    }

    public void setWins(int wins) {
        this.wins = wins;
    }

    public int getLosses() {
        return losses;
    }

    public void setLosses(int losses) {
        this.losses = losses;
    }

    public int getTies() {
        return ties;
    }

    public void setTies(int ties) {
        this.ties = ties;
    }

    public int getGoalsScored() {
        return goalsScored;
    }

    public void setGoalsScored(int goalsScored) {
        this.goalsScored = goalsScored;
    }

    public int getGoalsAllowed() {
        return goalsAllowed;
    }

    public void setGoalsAllowed(int goalsAllowed) {
        this.goalsAllowed = goalsAllowed;
    }

    // Other methods

    public void incrementWins() {
        this.wins++;
    }

    public void incrementLosses() {
        this.losses++;
    }

    public void incrementTies() {
        this.ties++;
    }

    public void incrementGoalsScored(int goals) {
        this.goalsScored += goals;
    }

    public void incrementGoalsAllowed(int goals) {
        this.goalsAllowed += goals;
    }

    @Override
    public String toString() {
        return "Team: " + name + "\n" +
                "Wins: " + wins + ", Losses: " + losses + ", Ties: " + ties + "\n" +
                "Points Scored: " + goalsScored + ", Points Allowed: " + goalsAllowed;
    }
}
