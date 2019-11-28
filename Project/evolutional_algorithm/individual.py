from random import randint
from statistics import mean


class Individual:
    CHILDREN_AMOUNT = 7
    MAX_SCORE = 10
    MIN_SCORE = 0
    _MUTATIONS_RATIO = 2/10  # percentage of genes that get changed

    def __init__(self, solution_from_parents=None):
        if solution_from_parents is not None:
            self._solution = solution_from_parents
        else:
            self._solution = [randint(self.MIN_SCORE, self.MAX_SCORE)
                              for child in range(self.CHILDREN_AMOUNT)
                              ]

    def evaluate_fitness(self):
        pass

    def create_child(self, other_individual):
        child_solution = [mean(first_gene, second_gene) for first_gene, second_gene in zip(self._solution, other_individual._solution)]
        return Individual(child_solution)

    def mutate(self):
        solution_length = len(self._solution)
        amount_of_mutations = self.MUTATIONS_RATIO*solution_length
        for mutation in range(amount_of_mutations):
            self._solution[randint(0, solution_length)] = randint(0, self._maximum_score)

    def get_information(self):
        text = ""
        for value in self._solution:
            text += f"{value} "
        return text[0:-1]
