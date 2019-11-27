class Individual:
    def __init__(self):
        self._solution = []
        pass

    def evaluate_fitness(self):
        pass

    def create_child(self, other_individual):
        pass

    def mutate(self):
        pass

    def get_information(self):
        text = ""
        for value in self._solution:
            text += f"{value} "
        return text[0:-1]
