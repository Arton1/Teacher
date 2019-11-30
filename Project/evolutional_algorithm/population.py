from .individual import Individual
from random import randint, random, sample
from math import ceil


class Population:
    _AMOUNT_OF_CANDIDATES = 200
    _AMOUNT_OF_CHILDREN = 40
    _TOURNAMENT_SIZE = 4/50

    def __init__(self,
                 problem,
                 candidates_amount=_AMOUNT_OF_CANDIDATES,
                 children_amount=_AMOUNT_OF_CHILDREN,
                 ):
        self._problem = problem
        self._candidates = []
        self._generation = 0
        self._children_amount = children_amount
        self._tournament_size = ceil(candidates_amount*self._TOURNAMENT_SIZE)
        if self._tournament_size % 2 == 1:
            self._tournament_size -= 1
        self._maximum_gene = max(self._problem)
        if len(self._problem) < self._maximum_gene:
            self._maximum_gene = len(self._problem)
        for i in range(candidates_amount):
            solution = [randint(1, self._maximum_gene)
                        for child in problem
                        ]
            self._candidates.append(Individual(solution))
        self._best_solution = max(self._candidates, key=lambda x: x.evaluate_fitness(self._problem))

    def _set_best(self):
        best = self._best_solution
        best_fitness = best.evaluate_fitness(self._problem)
        for individual in self._candidates:
            individual_fitness = individual.evaluate_fitness(self._problem)
            if best_fitness > individual_fitness:
                best = individual
                best_fitness = individual_fitness
        self._best_solution = best

    def print_best_solution(self):
        print(f"{self._best_solution.get_information()} : {self._best_solution.evaluate_fitness(self._problem)}")

    def roulette_select_individual(self, candidates_with_fitness):
        fitness_sum = sum(1/fitness for candidate, fitness in candidates_with_fitness)
        spin = random()
        probability_sum = 0
        for potential_parent, fitness in candidates_with_fitness:
            probability = 1 / (fitness*fitness_sum)
            probability_sum += probability
            if probability_sum > spin:
                return potential_parent

    def tournament_select_individual(self, candidates_with_fitness):
        tournament_candidates = sample(candidates_with_fitness, self._tournament_size)
        return min(tournament_candidates, key=lambda x: x[1])[0]

    def ranking_select_individual(self, candidates_with_fitness):
        # to do
        candidates_with_fitness.sort(key=lambda x: x[1], reversed=True)

    def _select_pair_of_parents(self):
        candidates_with_fitness = [(individual, individual.evaluate_fitness(self._problem)) for individual in self._candidates]
        first_parent = self.tournament_select_individual(candidates_with_fitness)
        candidates_without_first_parent = [(individual, fitness) for individual, fitness in candidates_with_fitness if individual != first_parent]
        del candidates_with_fitness
        second_parent = self.tournament_select_individual(candidates_without_first_parent)
        return first_parent, second_parent

    def _create_children(self):
        children = []
        for child_index in range(self._children_amount):
            first_parent, second_parent = self._select_pair_of_parents()
            child = Individual.create_child(first_parent, second_parent)
            child.mutate(1, self._maximum_gene)
            children.append(child)
        return children

    def _update_population(self, children):
        candidates_with_fitness = [(individual, individual.evaluate_fitness(self._problem)) for individual in self._candidates]
        for individual in children:
            candidates_with_fitness.append((individual, individual.evaluate_fitness(self._problem)))
        candidates_with_fitness.sort(key=lambda x: x[1])
        self._candidates = list(map(lambda x: x[0], candidates_with_fitness[:len(self._candidates)]))

    def evolve(self, amount_of_iterations=1):
        for i in range(amount_of_iterations):
            children = self._create_children()
            self._update_population(children)
            # self._set_best()
            self._generation += 1

    def print_information(self):
        print(f"Generacja: {self._generation}")
        for index, individual in enumerate(sorted(self._candidates, key=lambda x: x.evaluate_fitness(self._problem))):
            print(f"{index+1}: {individual.get_information()} : {individual.evaluate_fitness(self._problem)}")