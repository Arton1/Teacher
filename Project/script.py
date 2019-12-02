"""
Autorstwo:
Artur Wyrozębski
Mateusz Szczepkowski

Sposób korzystania z programu:
python3.7 script.py [liczba generacji]

Wartości ocen proszę przypisywać jako listę do zmiennej oceny
"""
from evolutional_algorithm.population import Population
from sys import argv
import cProfile

pr = cProfile.Profile()
oceny = [4, 8, 8, 8, 9, 10, 7, 6, 6, 6, 6, 2, 3, 4, 10, 10, 3, 10, 10, 5, 4, 3, 3, 3, 3, 3, 2]
# oceny = [7, 5, 3, 4, 9, 1]
# oceny = [7, 4, 6, 2, 1, 7, 9, 10, 10, 10, 2, 1]
# oceny = [7, 4, 6, 2, 1, 7, 9]
pr.enable()
population = Population(oceny)
population.evolve(int(argv[1]))
pr.disable()
population.print_solution()
# pr.print_stats(sort="cumulative")