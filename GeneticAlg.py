import numpy as np
import random


def count_adaptation(chromosome, c):
    counter = 0
    translation = int(chromosome.shape[0] / 2) + 1
    for i in range(chromosome.shape[0]):
        for j in range(chromosome.shape[1]):
            z = c - (j - translation) ** 2 - (-i + translation) ** 2
            counter += (z - chromosome[i][j]) ** 2
    return counter


def count_probabilities(adaptations):
    sum_adp = sum(adaptations)
    probabilities = []
    for adaptation in adaptations:
        probabilities.append(sum_adp / adaptation)
    norm_factor = 1 / sum(probabilities)
    normalised = []
    for probability in probabilities:
        normalised.append(norm_factor * probability)
    return normalised


def choose_parents(population, adaptations, no_pop):
    choice = np.random.choice(adaptations, no_pop, p=count_probabilities(adaptations))
    # print("wybór rodziców:", choice)
    parents = []
    parents_indexes = []
    for value in choice:
        parents_indexes.append(adaptations.index(value))
    # print("indexy w popualcji: ", parents_indexes)
    for index in parents_indexes:
        parents.append(population[index])
    return parents


def crossing1(parents, n, no_pop):  # wymiana 4 ćwiartki
    offspring = []
    available_parents = list(range(no_pop))
    for i in range(no_pop):
        if i % 2 == 0:
            cross_range = np.random.randint(n, size=2)
        else:
            mother_idx = random.choice(available_parents)
            available_parents.remove(mother_idx)
            father_idx = random.choice(available_parents)
            available_parents.remove(father_idx)
            mother, father = parents[mother_idx].copy(), parents[father_idx].copy()
            buff = father[cross_range[0]:, cross_range[1]:].copy()
            father[cross_range[0]:, cross_range[1]:] = mother[cross_range[0]:, cross_range[1]:].copy()
            mother[cross_range[0]:, cross_range[1]:] = buff.copy()
            offspring.append(father.copy())
            offspring.append(mother.copy())
    return offspring


def crossing2(parents, n, no_pop):  # wymiana losowych prostokatow
    offspring = []
    available_parents = list(range(no_pop))
    for i in range(no_pop):
        if i % 2 == 0:
            cross_place = np.random.randint(n, size=2)
            cross_box_x = cross_place[0] + np.random.randint(n - cross_place[0])
            cross_box_y = cross_place[1] + np.random.randint(n - cross_place[1])
        else:
            mother_idx = random.choice(available_parents)
            available_parents.remove(mother_idx)
            father_idx = random.choice(available_parents)
            available_parents.remove(father_idx)
            mother, father = parents[mother_idx].copy(), parents[father_idx].copy()
            buff = father[cross_place[0]:cross_box_x, cross_place[1]:cross_box_y].copy()
            father[cross_place[0]:cross_box_x, cross_place[1]:cross_box_y] = \
                mother[cross_place[0]:cross_box_x, cross_place[1]:cross_box_y].copy()
            mother[cross_place[0]:cross_box_x, cross_place[1]:cross_box_y] = buff.copy()
            offspring.append(father.copy())
            offspring.append(mother.copy())
    return offspring


def crossing3(parents, n, no_pop):  # wymiana losowych cwiartek
    offspring = []
    available_parents = list(range(no_pop))
    for i in range(no_pop):
        if i % 2 == 0:
            cross_place = np.random.randint(n, size=2)
            choose_quarter = np.random.randint(1, 5)
        else:
            mother_idx = random.choice(available_parents)
            available_parents.remove(mother_idx)
            father_idx = random.choice(available_parents)
            available_parents.remove(father_idx)
            mother, father = parents[mother_idx].copy(), parents[father_idx].copy()
            if choose_quarter == 1:
                buff = father[:cross_place[0], :cross_place[1]].copy()
                father[:cross_place[0], :cross_place[1]] = mother[:cross_place[0], :cross_place[1]].copy()
                mother[:cross_place[0], :cross_place[1]] = buff.copy()
            elif choose_quarter == 2:
                buff = father[:cross_place[0], cross_place[1]:].copy()
                father[:cross_place[0], cross_place[1]:] = mother[:cross_place[0], cross_place[1]:].copy()
                mother[:cross_place[0], cross_place[1]:] = buff.copy()
            elif choose_quarter == 3:
                buff = father[cross_place[0]:, :cross_place[1]].copy()
                father[cross_place[0]:, :cross_place[1]] = mother[cross_place[0]:, :cross_place[1]].copy()
                mother[cross_place[0]:, :cross_place[1]] = buff.copy()
            elif choose_quarter == 4:
                buff = father[cross_place[0]:, cross_place[1]:].copy()
                father[cross_place[0]:, cross_place[1]:] = mother[cross_place[0]:, cross_place[1]:].copy()
                mother[cross_place[0]:, cross_place[1]:] = buff.copy()
            offspring.append(father.copy())
            offspring.append(mother.copy())
    return offspring


def crossing4(parents, n, no_pop):  # wymiana losowych komorek
    offspring = []
    available_parents = list(range(no_pop))
    cross_place = []
    for i in range(no_pop):
        if i % 2 == 0:
            no_corssing = np.random.randint(50)
            for j in range(no_corssing):
                cross_place.append(np.random.randint(n, size=2))
        else:
            mother_idx = random.choice(available_parents)
            available_parents.remove(mother_idx)
            father_idx = random.choice(available_parents)
            available_parents.remove(father_idx)
            mother, father = parents[mother_idx].copy(), parents[father_idx].copy()
            for j in range(no_corssing):
                buff = father[cross_place[j][0], cross_place[j][1]]
                father[cross_place[j][0], cross_place[j][1]] = mother[cross_place[j][0], cross_place[j][1]]
                mother[cross_place[j][0], cross_place[j][1]] = buff
            offspring.append(father.copy())
            offspring.append(mother.copy())
    return offspring


def mutation(offspring, c, n):
    for chromosome in offspring:
        for i in range(n):
            for j in range(n):
                if random.uniform(0, 100) < 0.01:
                    chromosome[i][j] = np.random.randint(1, c)
                    # print("mutation")
    return offspring
