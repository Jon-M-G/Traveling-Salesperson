import random
import math

StartXvalues = [1,5,5,3,7,8,4,2,9]
StartYvalues = [1,4,8,5,6,7,8,4,2]
cities = []
for i in range(len(StartXvalues)):
    cities.append(str(StartXvalues[i])+','+str(StartYvalues[i]))
print(cities)
# crossover functinos for randomness
def crossover(tour1, tour2):
    start = random.randint(0,len(tour1)-1)
    end = random.randint(0, len(tour1) - 1)
    NewTour = tour1[start:end]
    for i in range(len(tour2)):
        if tour2[i] not in NewTour:
            NewTour.append(tour2[i])

    return NewTour

class Tour:


    def __init__(self,cities):
        self.tour = cities

    def fitness(self):
        Xvalues = []
        Yvalues = []
        total = 0
        for i in range(len(self.tour)):
            Xvalues.append(int(self.tour[i].split(',')[0]))
            Yvalues.append(int(self.tour[i].split(',')[1]))
        for i in range(len(Xvalues) - 1):
            total += math.sqrt(math.pow(Xvalues[i + 1] - Xvalues[i], 2) + math.pow(Yvalues[i + 1] - Yvalues[i], 2))
        return total
# create random individual
    def generateIndividual(self):
        return random.sample(self.tour, len(self.tour))
# create a population for genetic algorithm
def generatePopulation(n,cities):
    population =[]
    for i in range(n):
        tour = Tour(cities)
        population.append(tour.generateIndividual())
    return population
#random mutation by picking two random cities and swapping them
def mutate(tour):
    pos1 = random.randint(0,len(tour)-1)
    pos2 = random.randint(0,len(tour)-1)
    while pos2 == pos1:
        pos2 = random.randint(0, len(tour) - 1)
    t = tour[pos1]
    tour[pos1] = tour[pos2]
    tour[pos2] = t




pop = generatePopulation(3,cities)
print(pop)
print(pop[0])