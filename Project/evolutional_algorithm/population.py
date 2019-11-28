from .individual import Individual
from random import rand, randint


class Population:
    _AMOUNT_OF_CANDIDATES = 12
    _AMOUNT_OF_CHILDREN = 6
    _AMOUNT_OF_GENES = 7
    _MIN_GENE = 0
    _MAX_GENE = 10

    def __init__(self,
                 candidates_amount=_AMOUNT_OF_CANDIDATES,
                 children_amount=_AMOUNT_OF_CHILDREN,
                 gene_amount=_AMOUNT_OF_GENES,
                 minimum_gene=_MIN_GENE,
                 maximum_gene=_MAX_GENE,
                 ):
        self._candidates = []
        self._generation = 0
        self._children_amount = children_amount
        self._minimum_gene = minimum_gene
        self._maximum_gene = maximum_gene
        for i in range(candidates_amount):
            solution = [randint(minimum_gene, maximum_gene)
                        for child in range(gene_amount)
                        ]
            self._candidates.append(Individual(solution))

    def get_best(self):
        best = self._candidates[0]
        best_fitness = best.evaluate_fitness()
        for individual in self._candidates[1:]:
            individual_fitness = individual.evaluate_fitness()
            if best_fitness < individual_fitness:
                best = individual
                best_fitness = individual_fitness
        return best.get_information()

    def _get_probabilites_for_roulette_selection(self):
        fitness_list = [individual.evaluate_fitness() for individual in self._candidates]
        fitness_sum = sum(fitness_list)
        probabilities = []
        previous_probability = 0
        for fitness in fitness_list:
            probability = previous_probability + fitness/fitness_sum
            probabilities.append(probability)
            previous_probability = probability
        return probabilities

    def _select_parents(self):
        # needs changing
        parents = []
        probabilities = self._get_probabilites_for_roulette_selection()
        for parent in range(2*self._children_amount):
            spin = rand()
            for potential_parent, bound in zip(self._candidates, probabilities)):
                if spin < bound:
                    parents.append(potential_parent)
                    break
        return parents

    def _create_children(self, parents):
        children = []
        for first_parent, second_parent in zip(parents[::2], parents[1::2]):
            child = Individual.create_child(first_parent, second_parent)
            child.mutate(self._minimum_gene, self._maximum_gene)
            children.append(child)
        return children

    def _update_population(self, children):
        candidates_with_fitness = [individual, individual.evaluate_fitness() for individual in self._candidates]
        for individual in children:
            fitness_list.append((individual, individual.evaluate_fitness()))
        fitness_list.sort(key=lambda x: x[1])
        self._candidates = list(map(lambda x: x[0], fitness_list[:len(self._candidates)]))

    def evolve(self, amount_of_iterations):
        for i in range(amount_of_iterations):
            parents = self._select_parents()
            children = self._create_children(parents)
            self._update_population(children)

    def print_information(self):
        print(f"Generacja: {self._generation}\n")
        for index, individual in zip(range(self._AMOUNT_OF_CANDIDATES), self._candidates):
            print(f"{index+1}: {individual.get_information()} : {individual.evaluate_fitness()}\n")
