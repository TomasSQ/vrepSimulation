from deap import base
from deap import creator
from deap import tools
import random
import math

import matplotlib.pyplot as plt
import numpy as np

N_COEF = 5
NGEN = 10
POPULATION_SIZE = 100
CXPB = 0.9
MUTPB = 0.1
BEGIN = 0
END = BEGIN + 6000

INTERVAL = 0.001

def truncated_Fourier(coeficients, time):
    value = coeficients[0]

    for i in xrange(N_COEF):
        value += coeficients[2 * i + 2] * math.cos((i + 1) * coeficients[1] * time)
        value += coeficients[2 * i + 3] * math.sin((i + 1) * coeficients[1] * time)

    return value

def createEval(function):
    def evalFit(individual):
        fit = 0
        for t in xrange(END - BEGIN):
            fit += abs(function[t] - truncated_Fourier(individual, t * INTERVAL) / 4)

        if fit > 100 and individual[1] == 0:
            fit *= 1000
        return fit,
    return evalFit

def mutate(individual):
    return [(random.random() * 10 - 10 / 2.0) for x in individual if random.random() < 0.1]

def initGA(function):
    creator.create("FitnessMin", base.Fitness, weights=(-1.0,))
    creator.create("Individual", list, fitness=creator.FitnessMin)
    toolbox = base.Toolbox()
    toolbox.register("attr_coef", random.uniform, -10, 10)
    toolbox.register("individual", tools.initRepeat, creator.Individual, toolbox.attr_coef, 2 * N_COEF + 2)
    toolbox.register("population", tools.initRepeat, list, toolbox.individual)

    toolbox.register("evaluate", createEval(function))
    toolbox.register("mate", tools.cxTwoPoint)
    toolbox.register("mutate", mutate)
    toolbox.register("elite",tools.selBest, k = 2)
    toolbox.register("select", tools.selTournament, tournsize = 3)

    return toolbox

def evolve(toolbox):
    pop = toolbox.population(n = POPULATION_SIZE)
    fitnesses = list(map(toolbox.evaluate, pop))
    for ind, fit in zip(pop, fitnesses):
        ind.fitness.values = fit

    for g in range(NGEN):
        print("-- Generation %i --" % g)

        elite = toolbox.elite(pop)
        elite = list(map(toolbox.clone, elite))
        offspring = toolbox.select(pop, POPULATION_SIZE-2)
        offspring = list(map(toolbox.clone, offspring))

        for child1, child2 in zip(offspring[::2],offspring[1::2]):
            if random.random() < CXPB:
                toolbox.mate(child1, child2)
                del child1.fitness.values
                del child2.fitness.values


        for mutant in offspring:
            if random.random() < MUTPB:
                toolbox.mutate(mutant)
                del mutant.fitness.values

        offspring = elite + offspring

        # Evaluate the individuals with an invalid fitness
        invalid_ind = [ind for ind in offspring if not ind.fitness.valid]
        fitnesses = map(toolbox.evaluate, invalid_ind)
        for ind, fit in zip(invalid_ind, fitnesses):
            ind.fitness.values = fit

        if len(offspring) > 0:
            pop[:] = offspring

        # Gather all the fitnesses in one list and print the stats
        fits = [ind.fitness.values[0] for ind in pop]

        length = len(pop)
        mean = sum(fits) / length

        print("  Min %s" % min(fits))
        print("  Max %s" % max(fits))
        print("  Avg %s" % mean)

        if min(fits) < 2:
            break

    return tools.selBest(pop, k = 1)[0]

def aproximate(function):
    toolbox = initGA(function)
    return evolve(toolbox)

f = file('training_data2.txt')

functions = []

for i in xrange(27):
    functions += [[]]

for line in f:
    split_line = line.split(' ')
    if float(split_line[0]) < BEGIN:
        continue
    if float(split_line[0]) > END:
        break
    to_float = [float(x) for x in split_line[1:]]
    for i in xrange(len(to_float)):
        functions[i] += [to_float[i]]

for function in functions[2:]:
    x = np.arange(0, len(function) * INTERVAL, INTERVAL)
    plt.plot(x, function)

    print "Aproximation"
    #coeficients = aproximate(function)
    #print coeficients
    #aproximation = []
    #for t in xrange(len(function)):
    #    aproximation += [truncated_Fourier(coeficients, t * INTERVAL)]

    #plt.plot(x, np.array(aproximation) / 4)
    p = np.poly1d(np.polyfit(x, function, 150))
    aproximation = []
    for t in xrange(len(function)):
        aproximation += [p(t * INTERVAL)]
    plt.plot(x, aproximation)

    plt.show()
