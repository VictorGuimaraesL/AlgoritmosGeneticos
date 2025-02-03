from random import random


class Individual:
    
    def __init__(self, chromosome_size):
        self.chromosome_size = chromosome_size
        self.fitness = 0
        self.chromosome = [ 1 if random() > 0.5 else 0 for i in range(chromosome_size) ]