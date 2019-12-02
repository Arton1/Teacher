from evolutional_algorithm.population import Population
from evolutional_algorithm.individual import Individual
from sys import argv
import cProfile

pr = cProfile.Profile()
tab = [4, 8, 8, 8, 9, 10, 7, 6, 6, 6, 6, 2, 3, 4, 10, 10, 3, 10, 10, 5, 4, 3, 3, 3, 3, 3, 2]
pr.enable()
population = Population(tab)
population.evolve(int(argv[1]))
pr.disable()
pr.print_stats(sort="cumulative")