from genetic_algorithm import GeneticAlgorithm
import pandas as pd

dataset = pd.read_csv(r"C:\Users\USUARIO\Documents\Algoritmos Geneticos\database\P08-cwp.csv")
Weights = dataset.iloc[:, 1:2].values
Profits = dataset.iloc[:, 2:3].values

generation = 0
ga = GeneticAlgorithm(10, 0.01, 0.97, 2, Weights, Profits, 6404180)

population = ga.init_population(24)
population.generation = generation
ga.evaluate_population(population)

print(f'{ga.baglist()}')

while not ga.is_terminate_condition_met(population):

    print(f'Best solution: {population.get_fittest().chromosome}')
    
    generation += 1
    population = ga.crossover_population(population)
    population = ga.mutate_population(population)
    ga.evaluate_population(population)
    
    population.generation = generation
    
    
print(f'Found solution in {generation} generations')
print(f'The best solution: {population.get_fittest().chromosome}')
print(f'{ga.total_weight_profit(population)}')
print('Capacity: 6404180')
