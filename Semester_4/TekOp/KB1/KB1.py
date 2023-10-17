import numpy as np


class Ant:
    def __init__(self, start_city):
        self.start_city = start_city
        self.current_city = start_city
        self.tabu_list = [start_city]
        self.total_distance = 0

    def get_candidate_cities(self, pheromone, distances):
        candidate_cities = []
        for i in range(len(distances[self.current_city])):
            if i not in self.tabu_list and i != self.current_city:
                candidate_cities.append(i)
        return candidate_cities

    def calculate_probabilities(self, candidate_cities, pheromone, distances, alpha, beta):
        attractiveness = []
        for i in candidate_cities:
            tau = pheromone[self.current_city][i]
            if distances[self.current_city][i] == 0:
                attract = 1e-10
            else:
                attract = (tau ** alpha) * \
                    ((1 / distances[self.current_city][i]) ** beta)
            attractiveness.append(attract)
        total = sum(attractiveness)
        return [x / total for x in attractiveness]

    def select_next_city(self, pheromone, distances, alpha, beta):
        candidate_cities = self.get_candidate_cities(pheromone, distances)
        if not candidate_cities:
            return None

        probabilities = self.calculate_probabilities(
            candidate_cities, pheromone, distances, alpha, beta)
        next_city = self.choose_next_city(candidate_cities, probabilities)
        self.tabu_list.append(next_city)
        self.total_distance += distances[self.current_city][next_city]
        self.current_city = next_city
        # calculate the attractiveness of each neighboring city
        attractiveness = []
        for i in range(len(distances)):
            print("i in attrac ", i)
            if i not in self.tabu_list:
                print("i in tabu ", i, self.tabu_list)
                # check if distance is not zero
                if distances[self.current_city][i] != 0:
                    tau = pheromone[self.current_city][i]
                    print("tau", tau)
                    print("c, cur, i", self.current_city,
                          distances[self.current_city][i])
                    # calculate attractiveness using formula
                    attract = (tau ** alpha) * \
                        ((1 / distances[self.current_city][i]) ** beta)
                    print("att ", attract)
                    attractiveness.append((i, attract))
                    print("attractiveness", attractiveness, '\n')

        if not attractiveness:
            return None

        # select the next city probabilistically
        probabilities = np.array([x[1] for x in attractiveness])
        print("prob ", probabilities, '\n')

        sum_probabilities = np.sum(probabilities)
        print("sum.prob ", sum_probabilities, '\n')

        probabilities = probabilities / sum_probabilities
        print("new prob ", probabilities, '\n')

        selected_index = np.random.choice(
            range(len(attractiveness)), p=probabilities)
        print("s.index ", selected_index)
        selected_city = attractiveness[selected_index][0]
        print("s.city ", selected_city,
              attractiveness[selected_index][0], '\n')

        # update the ant's tabu list, total distance, and current city
        self.tabu_list.append(selected_city)
        print("new tabu ", self.tabu_list,)
        self.total_distance += distances[self.current_city][selected_city]
        print("total d ", distances[self.current_city][selected_city])
        print("real total d ", self.total_distance, '\n')
        self.current_city = selected_city
        print("cur, selected", self.current_city, "=", selected_city)

    def choose_next_city(self, candidate_cities, probabilities):
        rand = np.random.choice(candidate_cities, p=probabilities)
        print(rand)
        return rand

    def reset(self):
        self.current_city = self.start_city
        print("after reset ", self.current_city)
        self.tabu_list = [self.start_city]
        print("after reset ", self.tabu_list)
        self.total_distance = 0
        print("t.distances after reset", self.total_distance, '\n')


class ACO:
    def __init__(self, distances, n_ants, n_iterations, pheromone_deposit, pheromone_decay, alpha, beta):
        self.distances = distances
        self.n_ants = n_ants
        self.n_iterations = n_iterations
        self.pheromone_deposit = pheromone_deposit
        self.pheromone_decay = pheromone_decay
        self.alpha = alpha
        self.beta = beta
        self.ants = [Ant(i) for i in range(len(distances))]
        self.pheromone = np.ones((len(distances), len(distances)))

    def update_pheromone_trails(self, ant):
        for i in range(len(ant.tabu_list) - 1):
            current_city = ant.tabu_list[i]
            next_city = ant.tabu_list[i + 1]
            self.pheromone[current_city][next_city] += self.pheromone_deposit / \
                ant.total_distance
            self.pheromone[next_city][current_city] = self.pheromone[current_city][next_city]

    def update_pheromone_levels(self, ant):
        for i in range(len(ant.tabu_list) - 1):
            curr_city = ant.tabu_list[i]
            next_city = ant.tabu_list[i+1]
            self.pheromone[curr_city][next_city] += self.pheromone_deposit / \
                ant.total_distance
            self.pheromone[next_city][curr_city] = self.pheromone[curr_city][next_city]
        self.pheromone *= self.pheromone_decay

    def solve(self):
        best_tour = None
        best_distance = float('inf')

        for it in range(self.n_iterations):
            print("iteration", it)
            for ant in self.ants:
                for i in range(len(self.distances) - 1):
                    print("self i ", i)
                    ant.select_next_city(
                        self.pheromone, self.distances, self.alpha, self.beta)

                # add distance from last city back to starting city
                ant.total_distance += self.distances[ant.current_city][ant.start_city]
                # print("ant total distance ", self.distances[ant.current_city][ant.start_city])

                # update best tour and distance
                if ant.total_distance < best_distance:
                    best_tour = ant.tabu_list.copy()
                    best_distance = ant.total_distance

                # update pheromone trails
                self.update_pheromone_trails(ant)
                print("update pheromone trails", self.update_pheromone_trails)

            # update pheromone trails globally
            self.pheromone *= (1 - self.pheromone_decay)
            print("Pheromone after decay", self.pheromone)
            self.pheromone += self.pheromone_deposit / best_distance
            print("New pheromone", self.pheromone)

        return best_tour, best_distance


distances = np.array([[0, 6, 0, 0, 3, 5],
                      [6, 0, 5, 0, 0, 4],
                      [0, 5, 0, 8, 0, 8],
                      [0, 0, 8, 0, 9, 2],
                      [3, 0, 0, 9, 0, 7],
                      [5, 4, 8, 2, 7, 0]])

#distances, n_ants, n_iterations, pheromone_deposit, pheromone_decay, alpha, beta
aco = ACO(distances, 10, 100, 1, 0.05, 1, 2)
best_tour, best_distance = aco.solve()
print("Best tour found:", best_tour)
print("Distance of best tour:", best_distance)
