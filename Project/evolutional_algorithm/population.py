from solution.py import Individual

AMOUNT_OF_CANDIDATES = 12
AMOUNT_OF_CHILDREN = 6


class Population:
    def __init__(self):
        _candidates = []
        _generation = 0
        for i in range(AMOUNT_OF_CANDIDATES):
            _candidates.append(Individual())

    def get_best(self):
        best = self._candidates[0]
        best_fitness = best.evaluate_fitness()
        for individual in self._candidates[1:]:
            individual_fitness = individual.evaluate_fitness()
            if best_fitness < individual_fitness:
                best = individual
                best_fitness = individual_fitness
        return best

    def _select_parents(self):
        pass

    def _create_children(self, parents):
        children = []
        for first_parent, second_parent in zip(parents[::2], parents[1::2]:
            children.append(Individual.create_child(first_parent, second_parent))
        return children

    def _update_population(self):
        pass

    def evolve(self, amount_of_iterations):
        for i in range(amount_of_iterations):
            parents = self._select_parents()
            children = self._create_children(parents)
            self._update_population(children)

    def print_information(self):
        print(f"Generacja: {self._generation}\n")
        for index, individual in zip(range(AMOUNT_OF_CANDIDATES), self._candidates):
            print(f"{index}: {individual.get_information()} : {individual.evaluate_fitness()}\n)
