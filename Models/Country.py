

class Country:
    def __init__(self, name, cases, population):
        self.name = name
        self.cases = cases
        self.population = population

    def __repr__(self):
        return f"Country {self.name} with {self.cases} cases, population {self.population}"

    def absolute_cases(self):
        return self.cases

    def relative_cases(self):
        return (self.cases / self.population) * 100
