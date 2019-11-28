from random import randint
from statistics import mean


class Individual:
    _MUTATIONS_RATIO = 2/10  # percentage of genes that get changed

    def __init__(self, solution):
        self._solution = solution

    def evaluate_fitness(self):
        pass

    def create_child(self, other_individual):
        child_solution = [mean(first_gene, second_gene) for first_gene, second_gene in zip(self._solution, other_individual._solution)]
        return Individual(child_solution)

    def mutate(self, min_score, max_score):
        solution_length = len(self._solution)
        amount_of_mutations = self.MUTATIONS_RATIO*solution_length
        for mutation in range(amount_of_mutations):
            self._solution[randint(0, solution_length)] = randint(min_score, max_score)

    def get_information(self):
        text = ""
        for value in self._solution:
            text += f"{value} "
        return text[0:-1]
