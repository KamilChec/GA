import numpy as np
import GeneticAlg as ga

n = 11  # only odd numbers
c = 50
no_pop = 50  # only even
population = []
adaptation = []
for chromosome in range(no_pop):
    population.append(np.random.randint(1, c, size=(n, n)))
    adaptation.append(ga.count_adaptation(population[chromosome], c))
pierwsza_seria = sum(adaptation)
# print("funkcja celu: ",adaptation)
# print("prawdopodobienstwo: ",ga.count_probabilities(adaptation))
parents = ga.choose_parents(population, adaptation, no_pop)
offspring = ga.crossing2(parents, n, no_pop)
offspring = ga.mutation(offspring, c, n)
for i in range(1000):
    new_population = offspring.copy()
    adaptation.clear()
    for chromosome in range(no_pop):
        adaptation.append(ga.count_adaptation(new_population[chromosome], c))
    # print(adaptation)
    parents = ga.choose_parents(population, adaptation, no_pop)
    offspring = ga.crossing2(parents, n, no_pop)
    offspring = ga.mutation(offspring, c, n)
ostatnia_seria = sum(adaptation)
print(pierwsza_seria-ostatnia_seria)
# print(offspring[:5])

