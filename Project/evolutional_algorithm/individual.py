from random import randint
from statistics import mean
from math import ceil


class Individual:
    _MUTATIONS_RATIO = 2/10  # percentage of genes that get changed

    def __init__(self, solution):
        self._solution = solution

    def evaluate_fitness(self, received_points):
        amount_of_cookies = sum(self._solution)
        penalty = 0
        for left_child, left_cookies, right_child, right_cookies in zip(received_points[:-1], self._solution[:-1], received_points[1:], self._solution[1:]):
            if left_child < right_child and not left_cookies < right_cookies:
                penalty += right_child - left_child + (left_cookies - right_cookies) + 1
            else:
                if left_child > right_child and not left_cookies > right_cookies:
                    penalty += left_child - right_child + (right_cookies - left_cookies) + 1
        return amount_of_cookies + penalty

    def create_child(self, other_individual):
        if other_individual is None:
            print("WTF")
        child_solution = [ceil(mean((first_gene, second_gene))) for first_gene, second_gene in zip(self._solution, other_individual._solution)]
        return Individual(child_solution)

    def mutate(self, min_score, max_score):
        solution_length = len(self._solution)
        amount_of_mutations = self._MUTATIONS_RATIO*solution_length
        for mutation in range(ceil(amount_of_mutations)):
            self._solution[randint(0, solution_length-1)] = randint(min_score, max_score)

    def get_information(self):
        text = ""
        for value in self._solution:
            text += f"{value} "
        return text[0:-1]
