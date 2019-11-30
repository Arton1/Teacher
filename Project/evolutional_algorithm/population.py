from .individual import Individual
from random import randint, random


class Population:
    _AMOUNT_OF_CANDIDATES = 50
    _AMOUNT_OF_CHILDREN = 10
    _AMOUNT_OF_GENES = 7
    _MIN_GENE = 1
    _MAX_GENE = 10

    def __init__(self,
                 problem,
                 candidates_amount=_AMOUNT_OF_CANDIDATES,
                 children_amount=_AMOUNT_OF_CHILDREN,
                 minimum_gene=_MIN_GENE,
                 maximum_gene=_MAX_GENE,
                 ):
        self._problem = problem
        self._candidates = []
        self._generation = 0
        self._children_amount = children_amount
        self._minimum_gene = minimum_gene
        self._maximum_gene = maximum_gene
        for i in range(candidates_amount):
            solution = [randint(minimum_gene, maximum_gene)
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

    def roulette_select_individual(self, candidates_with_fitness):
        fitness_sum = sum(1/candidate[1] for candidate in candidates_with_fitness)
        spin = random()
        probability_sum = 0
        for potential_parent, fitness in candidates_with_fitness:
            probability = 1 / (fitness*fitness_sum)
            probability_sum += probability
            if probability_sum > spin:
                return potential_parent

    def _select_pair_of_parents(self):
        candidates_with_fitness = [(individual, individual.evaluate_fitness(self._problem)) for individual in self._candidates]
        first_parent = self.roulette_select_individual(candidates_with_fitness)
        candidates_without_first_parent = [(individual, fitness) for individual, fitness in candidates_with_fitness if individual != first_parent]
        del candidates_with_fitness
        second_parent = self.roulette_select_individual(candidates_without_first_parent)
        return first_parent, second_parent

    def _create_children(self):
        children = []
        # for child_index in range(self._children_amount):
        first_parent, second_parent = self._select_pair_of_parents()
        child = Individual.create_child(first_parent, second_parent)
        if(random() < 0.2):
            child.mutate(self._minimum_gene, self._maximum_gene)
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
            self._set_best()
            self._generation += 1

    def print_information(self):
        print(f"Generacja: {self._generation}")
        for index, individual in zip(range(self._AMOUNT_OF_CANDIDATES), sorted(self._candidates, key=lambda x: x.evaluate_fitness(self._problem))):
            print(f"{index+1}: {individual.get_information()} : {individual.evaluate_fitness(self._problem)}")
        # for index, individual in zip(range(self._AMOUNT_OF_CANDIDATES), self._candidates):
            # print(f"{index+1}: {individual.get_information()} : {individual.evaluate_fitness(self._problem)}")
