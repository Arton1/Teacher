from evolutional_algorithm.population import Population
from sys import argv

population = Population([15, 4, 6, 7, 7, 6, 4, 8, 8, 8, 9, 10, 11, 1, 15, 20, 1, 1, 4])
# population.print_information()
population.evolve(int(argv[1]))
# population.print_information()
# population.print_best_solution()
