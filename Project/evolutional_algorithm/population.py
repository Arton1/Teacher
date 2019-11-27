from solution.py import Individual

AMOUNT_OF_CANDIDATES = 12
AMOUNT_OF_CHILDREN = 6


class Population:
    def __init__(self):
        _candidates = []
        for i in range(AMOUNT_OF_CANDIDATES):
            _candidates.append(Individual())
        pass

    def get_best(self):
        pass

    def evolve(self):
        pass