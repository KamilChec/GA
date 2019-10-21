import numpy as np
import GeneticAlg as ga

n = 11  # only odd numbers
c = 50
no_pop = 50  # only even
population = []
adaptation = []
offspring = []
mutated_offspring = []
for chromosome in range(no_pop):
    population.append(np.random.randint(1, c, size=(n, n)))
    adaptation.append(ga.count_adaptation(population[chromosome], c))
parents = ga.choose_parents(population, adaptation, no_pop).copy()
offspring = ga.crossing2(parents, n, no_pop).copy()
mutated_offspring = ga.mutation(offspring, c, n).copy()
population.clear()
population = mutated_offspring.copy()
mutated_offspring.clear()
index_min = np.argmin(adaptation)
first_series = adaptation[index_min]
for i in range(10000):
    parents.clear()
    offspring.clear()
    adaptation.clear()
    for chromosome in range(no_pop):
        adaptation.append(ga.count_adaptation(population[chromosome], c))
    parents = ga.choose_parents(population, adaptation, no_pop).copy()
    offspring = ga.crossing2(parents, n, no_pop).copy()
    population.clear()
    mutated_offspring = ga.mutation(offspring, c, n).copy()
    population = mutated_offspring.copy()
    mutated_offspring.clear()
last_series = adaptation[index_min]
print(int((last_series/(first_series-last_series))*100))
index_min = np.argmin(adaptation)
print(population[index_min])
