from evolutional_algorithm.population import Population
from evolutional_algorithm.individual import Individual
from sys import argv

tab = [4, 8, 8, 8, 9, 10, 7]
population = Population(tab)
# invidual = Individual([2, 1, 2, 1, 1, 2, 3])
# print(invidual.evaluate_fitness(tab))
# population.print_information()
population.evolve(int(argv[1]))
# population.print_information()
# population.print_best_solution()
