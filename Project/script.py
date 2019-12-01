from evolutional_algorithm.population import Population
from sys import argv

population = Population([7, 4, 6, 3, 1, 4, 7])
population.print_information()
population.evolve(int(argv[1]))
population.print_information()
population.print_best_solution()