from random import randint, random, sample
from statistics import mean
from math import ceil, floor


class Individual:
    _MUTATIONS_CHANCE = 1/5  # percentage of individuals that get changed
    _MUTATION_POINTS_AMOUNT = 1/30
    _AMOUNT_OF_CROSSOVER_POINTS = 1/5

    def __init__(self, solution):
        self._solution = solution

    def evaluate_fitness(self, problem):
        amount_of_cookies = sum(self._solution)
        penalty = 0
        solution = self._solution
        left_index = 0
        right_index = 1
        while right_index < len(problem):
            if problem[left_index] < problem[right_index] and not solution[left_index] < solution[right_index]:
                penalty += solution[left_index] - solution[right_index] + 2
                if left_index == right_index - 1 or (problem[left_index] < problem[left_index+1] and right_index != left_index+1):  # do propagation of penalty
                    propagation_index = right_index + 1
                    while propagation_index < len(problem) and problem[propagation_index-1] <= problem[propagation_index]:  # propagate to the right
                        penalty += solution[left_index] - solution[right_index] + 2
                        propagation_index += 1
            if problem[left_index] > problem[right_index] and not solution[left_index] > solution[right_index]:
                penalty += solution[right_index] - solution[left_index] + 2
                if left_index == right_index - 1 or (problem[right_index-1] > problem[right_index] and right_index != left_index+1):  # do propagation of penalty
                    propagation_index = left_index - 1
                    while propagation_index >= 0 and problem[propagation_index+1] <= problem[propagation_index]:  # propagate to the left
                        penalty += solution[right_index] - solution[left_index] + 2
                        propagation_index -= 1
            if left_index == right_index-1 or problem[right_index-1] == problem[right_index]:
                right_index += 1
            if right_index < len(problem) and problem[right_index-1] != problem[right_index]:
                left_index += 1
        return amount_of_cookies + penalty

    def create_child_by_mean(self, other_individual):
        child_solution = [floor(mean((first_gene, second_gene))) for first_gene, second_gene in zip(self._solution, other_individual._solution)]
        return Individual(child_solution),

    def create_pair_by_multipoints(self, other_individual):
        indexes = sorted(sample(range(0, len(self._solution)-1), ceil(len(self._solution)*self._AMOUNT_OF_CROSSOVER_POINTS)))
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
            for mutation in range(ceil(len(self._solution)*self._MUTATION_POINTS_AMOUNT)):
                self._solution[randint(0, len(self._solution)-1)] = randint(min_score, max_score)

    def get_information(self):
        text = ""
        for value in self._solution:
            text += f"{value} "
        return text[0:-1]
