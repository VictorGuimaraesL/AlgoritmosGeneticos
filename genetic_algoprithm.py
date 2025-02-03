from random import random
from individual import Individual
from population import Population
import numpy as np


class GeneticAlgorithm:
    
    def __init__(self, population_size, mutation_rate, crossover_rate, elitism_count, weight, profit, capacity):
        self.population_size = population_size
        self.mutation_rate = mutation_rate
        self.crossover_rate = crossover_rate
        self.elitism_count = elitism_count
        self.weight = weight
        self.profit = profit
        self.capacity = capacity
        
    def baglist(self):
        print('Lista:')
        print('Item  Peso  Lucro')
        item = np.arange(1,25)
        for i in range(self.weight.shape[0]):
            print('{0}      {1}      {2}\n'.format(item[i], self.weight[i], self.profit[i]))
    
    def total_weight_profit(self, population):
        item = np.arange(1,25)
        f =np.array( population.get_fittest().chromosome).reshape(24, 1)
        for i in range(len(item)):
            TW = sum(np.multiply(self.weight,f))
            TP = sum(np.multiply(self.profit,f))
        print(f'Total Weight:{TW}')
        print(f'Total Profit:{TP}')
        
    def init_population(self, chromosome_size):
        return Population(self.population_size, chromosome_size)
        
    def calculate_fitness(self, individual):
        aux = np.array(individual.chromosome).reshape(24,1)
        for i in range(individual.chromosome_size):
            if sum(np.multiply(self.weight,aux)) <= self.capacity:
                individual.fitness = sum(np.multiply(self.profit,aux))
            else:
                individual.fitness = 0
        return individual.fitness
        
    def evaluate_population(self, population):
        population_fitness = 0
        for i in range(population.size):
            population_fitness += self.calculate_fitness(population.individuals[i])
            
        population.fitness = population_fitness
        
    def is_terminate_condition_met(self, population):
        for i in range(population.size):
            if population.generation == 100:
                return True
            else:
                return False
        
    def select_parent(self, population):
        roulette_whell_position = random() * population.fitness
        spin_whell = 0
        for i in range(population.size):
            spin_whell += population.get_fittest(i).fitness
            if spin_whell >= roulette_whell_position:
                return population.get_fittest(i)
            
        return population.get_fittest(-1)
        
    def crossover_population(self, population):
        new_population = Population(population.size, population.chromosome_size)
        
        for i in range(population.size):
            parent1 = population.get_fittest(i)
            
            if self.crossover_rate > random() and i >= self.elitism_count:
                parent2 = self.select_parent(population)
                offspring = Individual(population.chromosome_size)
                
                cut_index = int(random() * parent1.chromosome_size)
                for j in range(parent1.chromosome_size):
                    if j <= cut_index:
                        offspring.chromosome[j] = parent1.chromosome[j]
                    else:
                        offspring.chromosome[j] = parent2.chromosome[j]
                        
                new_population.individuals[i] = offspring
                
            else:
                new_population.individuals[i] = parent1
                
        return new_population
    
    def mutate_population(self, population):
        new_population = Population(population.size, population.chromosome_size)
        
        for i in range(population.size):
            individual = population.individuals[i]
            
            for j in range(individual.chromosome_size):
                if self.mutation_rate > random():
                    if individual.chromosome[j] == 1:
                        individual.chromosome[j] = 0
                    else:
                        individual.chromosome[j] = 1
                        
            new_population.individuals[i] = individual
        
        return new_population
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        