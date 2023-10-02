import random
import math


def fitness(x, y):
    return 21.5 + (x * math.sin(4 * math.pi * x)) + (y * math.sin(20 * math.pi * y))


def generate_population(size, x_bound, y_bound):
    population = []
    for _ in range(size):
        x = random.uniform(*x_bound)
        y = random.uniform(*y_bound)
        population.append((x, y))
    # print("generate population ", population)
    return population


def select_parents(population, num_parents):
    parents = []
    population = sorted(
        population, key=lambda ind: fitness(*ind), reverse=True)
    for i in range(num_parents):
        parents.append(population[i])
        # print(parents)
    return parents


def crossover(parents, num_offsprings):
    offsprings = []
    for _ in range(num_offsprings):
        parent1, parent2 = random.sample(parents, 2)
        x = (parent1[0] + parent2[0]) / 2
        y = (parent1[1] + parent2[1]) / 2
        # print("crossover ", x, " ", y)
        offsprings.append((x, y))
    return offsprings


def mutate(offsprings, mutation_rate, x_bound, y_bound):
    mutated_offsprings = []
    for offspring in offsprings:
        if random.random() < mutation_rate:
            x = random.uniform(*x_bound)
            y = random.uniform(*y_bound)
            # print("mutation ", x, " ", y)
            mutated_offsprings.append((x, y))
        else:
            # print("offspring ", offspring)
            mutated_offsprings.append(offspring)
    return mutated_offsprings


def genetic_algorithm(num_generations, population_size, x_bound, y_bound, num_parents, num_offsprings, mutation_rate):
    population = generate_population(population_size, x_bound, y_bound)
    print("population", population, end="\n")

    for generation in range(num_generations):
        print(generation, "generation", end="\n")

        parents = select_parents(population, num_parents)
        print("parents", parents, end="\n")

        offsprings = crossover(parents, num_offsprings)
        print("offsprings", offsprings, end="\n")

        mutated_offsprings = mutate(
            offsprings, mutation_rate, x_bound, y_bound)
        print("mutated_offspirng", mutated_offsprings, end="\n")

        population = parents + mutated_offsprings
        print("population", population, end="\n")
        print()

    best_individual = max(population, key=lambda ind: fitness(*ind))
    best_fitness = fitness(*best_individual)

    return best_individual, best_fitness


# Example usage
num_generations = 10
population_size = 10
x_bound = (-3.0, 12.1)
y_bound = (4.1, 5.8)
num_parents = 10
num_offsprings = 20
mutation_rate = 0.1

best_individual, best_fitness = genetic_algorithm(
    num_generations, population_size, x_bound, y_bound, num_parents, num_offsprings, mutation_rate)

print(f"Best Individual: {best_individual}")
print(f"Best Fitness: {best_fitness}")
