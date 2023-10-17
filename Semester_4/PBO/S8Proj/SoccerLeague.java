import java.util.ArrayList;
import java.util.InputMismatchException;
import java.util.List;
import java.util.Scanner;

public class SoccerLeague {
    public static void main(String[] args) {
        List<Team> teams = new ArrayList<>();
        teams.add(new Team("Team 1"));
        teams.add(new Team("Team 2"));
        teams.add(new Team("Team 3"));
        teams.add(new Team("Team 4"));

        Scheduler scheduler = new Scheduler(teams);
        Scanner scanner = new Scanner(System.in);

        int temperature = 0;
        boolean stopInput = false;
        while (!scheduler.isSeasonOver()) {
            if (!stopInput) {
                try {
                    System.out.print("Enter temperature (-1 to quit): ");
                    temperature = scanner.nextInt();
                    if (temperature == -1) {
                        stopInput = true;
                        continue;
                    }
                    scheduler.scheduleGames(temperature);
                } catch (InputMismatchException e) {
                    System.out.println("Invalid temperature input. Please enter an integer value.");
                    scanner.nextLine(); // Clear the input buffer
                }
            } else {
                scheduler.scheduleGames(temperature);
            }
        }

        System.out.println("Season is over");
        scheduler.printStatistics();

        scanner.close();
    }
}
