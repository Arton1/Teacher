from evolutional_algorithm.population import Population
from evolutional_algorithm.individual import Individual
from sys import argv
# solution = [1 for x in range(7)]
# print(solution)
# individual = Individual(solution)
# print(individual.evaluate_fitness([1, 5, 4, 7, 1, 2, 8]))


population = Population([7, 4, 6, 2, 1, 4, 7])
population.print_information()
population.evolve(int(argv[1]))
population.print_information()
population.print_best_solution()