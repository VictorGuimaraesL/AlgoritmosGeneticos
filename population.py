from individual import Individual


class Population:
    
    def __init__(self, population_size, chromosome_size=15):
        self.size = population_size
        self.chromosome_size = chromosome_size
        self.fitness = 0
        self.generation = 0
        self.individuals = [ Individual(chromosome_size) for i in range(population_size) ]
    
        
    def get_fittest(self, offset=0):
        return sorted(self.individuals, key=lambda individual: individual.fitness, reverse=True)[offset]