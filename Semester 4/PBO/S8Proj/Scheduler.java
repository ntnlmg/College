
import java.util.ArrayList;
import java.util.List;
import java.util.Random;

public class Scheduler {
    private static final int MAX_GOALS = 10;
    private static final int CONSECUTIVE_FREEZING_WEEKS = 3;

    private List<Team> teams;
    private List<Game> games;
    private int consecutiveFreezingWeeks;

    public Scheduler(List<Team> teams) {
        this.teams = teams;
        this.games = new ArrayList<>();
        this.consecutiveFreezingWeeks = 0;
    }

    public void scheduleGames(int temperature) {
        if (temperature <= 32) {
            consecutiveFreezingWeeks++;
            System.out.println("Too cold to play.");
        } else {
            consecutiveFreezingWeeks = 0;
            if (teams.size() < 2) {
                System.out.println("Insufficient number of teams to play a game.");
            } else {
                Random random = new Random();
                for (int i = 0; i < 1; i++) {
                    int awayTeamIndex = random.nextInt(teams.size());
                    int homeTeamIndex;
                    do {
                        homeTeamIndex = random.nextInt(teams.size());
                    } while (homeTeamIndex == awayTeamIndex);

                    Team awayTeam = teams.get(awayTeamIndex);
                    Team homeTeam = teams.get(homeTeamIndex);

                    int awayScore = random.nextInt(MAX_GOALS + 1);
                    int homeScore = random.nextInt(MAX_GOALS + 1);

                    Game game = new Game(awayTeam.getName(), homeTeam.getName(), awayScore, homeScore, temperature);
                    games.add(game);

                    updateTeamStatistics(awayTeam, awayScore, homeScore);
                    updateTeamStatistics(homeTeam, homeScore, awayScore);
                }
            }
        }
    }

    private void updateTeamStatistics(Team team, int goalsScored, int goalsAllowed) {
        team.incrementGoalsScored(goalsScored);
        team.incrementGoalsAllowed(goalsAllowed);

        if (goalsScored > goalsAllowed) {
            team.incrementWins();
        } else if (goalsScored < goalsAllowed) {
            team.incrementLosses();
        } else {
            team.incrementTies();
        }
    }

    public boolean isSeasonOver() {
        return consecutiveFreezingWeeks >= CONSECUTIVE_FREEZING_WEEKS;
    }

    public void printStatistics() {
        System.out.println("*********RESULTS*********");
        for (Team team : teams) {
            System.out.println(team);
            System.out.println();
        }

        System.out.println();
        for (Game game : games) {
            System.out.println(game);
            System.out.println();
        }

        int hottestTemp = findHottestTemperature();
        double averageTemp = calculateAverageTemperature();

        System.out.println("Hottest Temp: " + hottestTemp);
        System.out.println("Average Temp: " + averageTemp);
        System.out.println();
    }

    private int findHottestTemperature() {
        int hottestTemp = Integer.MIN_VALUE;
        for (Game game : games) {
            if (game.getTemperature() > hottestTemp) {
                hottestTemp = game.getTemperature();
            }
        }
        return hottestTemp;
    }

    private double calculateAverageTemperature() {
        if (games.isEmpty()) {
            return 0.0;
        }

        int totalTemp = 0;
        for (Game game : games) {
            totalTemp += game.getTemperature();
        }
        return (double) totalTemp / games.size();
    }
}
