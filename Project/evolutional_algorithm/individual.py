from random import randint, random, sample
from statistics import mean
from math import ceil, floor


class Individual:
    _MUTATIONS_CHANCE = 1/5  # percentage of genes that get changed
    _MUTATIONS_AMOUNT = 1/15
    _AMOUNT_OF_POINTS = 1/5

    def __init__(self, solution):
        self._solution = solution

    def evaluate_fitness(self, problem):
        amount_of_cookies = sum(self._solution)
        penalty = 0
        for (index, left_child), left_cookies, right_child, right_cookies in zip(enumerate(problem[:-1]), self._solution[:-1], problem[1:], self._solution[1:]):
            const_penalty = 2
            if left_child < right_child and not left_cookies < right_cookies:
                while True:
                    penalty += left_cookies - right_cookies + const_penalty
                    if not (index < len(problem)-1 and problem[index+1] >= problem[index]):
                        break
                    if(self._solution[index+1] == self._solution[index]):
                            const_penalty += 1
                    index += 1
            elif left_child > right_child and not left_cookies > right_cookies:
                while True:
                    penalty += right_cookies - left_cookies + const_penalty
                    if not (index > 0 and problem[index-1] >= problem[index]):
                        break
                    if(self._solution[index-1] == self._solution[index]):
                        const_penalty += 1
                    index -= 1
            elif left_child == right_child and not left_cookies == right_cookies:
                if left_cookies < right_cookies:
                    while True:
                        penalty += right_cookies - left_cookies + 2
                        if not (index > 0 and problem[index-1] >= problem[index]):
                            break
                        if(self._solution[index-1] == self._solution[index]):
                            const_penalty += 1
                        index -= 1
                elif left_cookies > right_cookies:
                    while True:
                        penalty += left_cookies - right_cookies + 2
                        if not (index < len(problem)-1 and problem[index+1] >= problem[index]):
                            break
                        if(self._solution[index+1] == self._solution[index]):
                            const_penalty += 1
                        index += 1
        return amount_of_cookies + penalty

    def create_child_by_mean(self, other_individual):
        child_solution = [floor(mean((first_gene, second_gene))) for first_gene, second_gene in zip(self._solution, other_individual._solution)]
        return Individual(child_solution),

    def create_pair_by_multipoints(self, other_individual):
        indexes = sorted(sample(range(0, len(self._solution)-1), ceil(len(self._solution)*self._AMOUNT_OF_POINTS)))
        first_child_solution = []
        second_child_solution = []
        indexes_index = 0
        switched = False
        for (index, first_parent_gene), second_parent_gene in zip(enumerate(self._solution), other_individual._solution):
            if(switched):
                first_child_solution.append(second_parent_gene)
                second_child_solution.append(first_parent_gene)
            else:
                first_child_solution.append(first_parent_gene)
                second_child_solution.append(second_parent_gene)
            if(indexes_index < len(indexes) and index == indexes[indexes_index]):
                indexes_index += 1
                switched = not switched
        return Individual(first_child_solution), Individual(second_child_solution)

    def mutate(self, min_score, max_score):
        while random() < self._MUTATIONS_CHANCE:
            for mutation in range(ceil(len(self._solution)*self._MUTATIONS_AMOUNT)):
                self._solution[randint(0, len(self._solution)-1)] = randint(min_score, max_score)

    def get_information(self):
        text = ""
        for value in self._solution:
            text += f"{value} "
        return text[0:-1]
