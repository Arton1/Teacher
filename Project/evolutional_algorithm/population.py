from .individual import Individual
from random import randint, random, sample
from math import ceil


class Population:
    _AMOUNT_OF_CANDIDATES = 200
    _AMOUNT_OF_CHILDREN = 150 
    _TOURNAMENT_SIZE = 30/100

    def __init__(self,
                 problem,
                 candidates_amount=_AMOUNT_OF_CANDIDATES,
                 children_amount=_AMOUNT_OF_CHILDREN,
                 ):
        self._problem = problem
        self._candidates_with_fitness = []
        self._generation = 0
        self._children_amount = children_amount
        self._tournament_size = ceil(candidates_amount*self._TOURNAMENT_SIZE)
        if self._tournament_size % 2 == 1:
            self._tournament_size -= 1
        self._maximum_gene = len(set(self._problem))
        if len(self._problem) < self._maximum_gene:
            self._maximum_gene = len(self._problem)
        for i in range(candidates_amount):
            solution = [randint(1, self._maximum_gene) for child in problem]
            individual = Individual(solution)
            fitness = individual.evaluate_fitness(problem)
            self._candidates_with_fitness.append((individual, fitness))
        self._best_solution = max(self._candidates_with_fitness, key=lambda x: x[1])

    def _set_best(self):
        best, best_fitness = self._best_solution
        for individual, fitness in self._candidates_with_fitness:
            if best_fitness > fitness:
                best = individual
                best_fitness = fitness
        self._best_solution = (best, best_fitness)

    def print_best_solution(self):
        individual, fitness = self._best_solution
        print(f"{individual.get_information()} : {fitness}")

    def print_best_solution_from_generation(self):
        best, best_fitness = self._candidates_with_fitness[0]
        for individual, fitness in self._candidates_with_fitness[1:]:
            if best_fitness > fitness:
                best = individual
                best_fitness = fitness
        print(f"Generacja: {self._generation} : {best.get_information()} : {best_fitness}")

    def print_information(self):
        print(f"Generacja: {self._generation}")
        for index, (individual, fitness) in enumerate(sorted(self._candidates, key=lambda x: x[1])):
            print(f"{index+1}: {individual.get_information()} : {fitness}")

    def _roulette_select_individual(self, candidates_with_fitness):
        fitness_sum = sum(1/fitness for candidate, fitness in candidates_with_fitness)
        spin = random()
        probability_sum = 0
        for potential_parent, fitness in candidates_with_fitness:
            probability = 1 / (fitness*fitness_sum)
            probability_sum += probability
            if probability_sum > spin:
                return potential_parent, fitness

    def _tournament_select_individual(self, candidates_with_fitness):
        tournament_candidates = sample(candidates_with_fitness, self._tournament_size)
        return min(tournament_candidates, key=lambda x: x[1])

    def _ranking_select_individual(self, candidates_with_fitness):
        candidates_with_fitness.sort(key=lambda x: x[1], reverse=True)
        rank_sum = (len(candidates_with_fitness)+1)*len(candidates_with_fitness)/2
        spin = randint(0, rank_sum)
        index_sum = 0
        for index, (candidate, fitness) in enumerate(candidates_with_fitness, start=1):
            if spin <= index_sum + index:
                return candidate, fitness
            index_sum += index

    def _best_select_individual(self, candidates_with_fitness):
        return min(candidates_with_fitness, key=lambda x: x[1])

    def _select_pair_of_parents(self):
        first_parent_with_fitness = self._tournament_select_individual(self._candidates_with_fitness)
        self._candidates_with_fitness.remove(first_parent_with_fitness)
        second_parent_with_fitness = self._tournament_select_individual(self._candidates_with_fitness)
        self._candidates_with_fitness.append(first_parent_with_fitness)
        return first_parent_with_fitness, second_parent_with_fitness

    def _create_children(self):
        children_with_fitness = []
        for pair in range(0, self._children_amount, 2):
            (first_parent, first_parent_fitness), (second_parent, second_parent_fitness) = self._select_pair_of_parents()
            pair_of_children = Individual.create_pair_by_multipoints(first_parent, second_parent)
            for child in pair_of_children:
                child.mutate(1, self._maximum_gene)
                children_with_fitness.append((child, child.evaluate_fitness(self._problem)))
        return children_with_fitness

    def _update_population(self, children_with_fitness):
        candidates = self._candidates_with_fitness
        candidates.extend(children_with_fitness)
        candidates.sort(key=lambda x: x[1])
        self._candidates_with_fitness = candidates[:len(candidates)]

    def evolve(self, amount_of_iterations=1):
        self.print_best_solution_from_generation()
        for i in range(amount_of_iterations):
            children_with_fitness = self._create_children()
            self._update_population(children_with_fitness)
            self._generation += 1
            self.print_best_solution_from_generation()
        self._set_best()

    def print_solution(self):
        print(f"Rozwiązanie: {self._best_solution[1]}")