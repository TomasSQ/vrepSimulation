import vrep
import time
import random
import math

from manage_joints import *

from deap import base
from deap import creator
from deap import tools

N_COEF = 5
INDIVIDUAL_SIZE=2 * N_COEF + 2
INTERVAL=0.05 #50ms

#Serie de Fourier Truncada
def truncated_Fourier(coeficients, time):
    value = coeficients[0] / 2.0

    for i in xrange(N_COEF):
        value += coeficients[2 * i + 2] * math.cos(coeficients[1] * time)
        value += coeficients[2 * i + 3] * math.sin(coeficients[1] * time)

    return value

#Conexao com o vrep
vrep.simxFinish(-1) # just in case, close all opened connections
clientID = vrep.simxStart('127.0.0.1',19997,True,True,5000,5) # Conecta com o VREP. Por padrao ele ja abre essa porta.
if clientID == -1:
    exit (10)

#Reset da simulacao
def reset_simulation(clientID):
    vrep.simxStopSimulation(clientID, vrep.simx_opmode_oneshot)
    time.sleep(1) # um pequeno sleep entre o stop e o start
    vrep.simxStartSimulation(clientID, vrep.simx_opmode_oneshot)


#Juntas do NAO
Head_Yaw=[];Head_Pitch=[];
L_Hip_Yaw_Pitch=[];L_Hip_Roll=[];L_Hip_Pitch=[];L_Knee_Pitch=[];L_Ankle_Pitch=[];L_Ankle_Roll=[];
R_Hip_Yaw_Pitch=[];R_Hip_Roll=[];R_Hip_Pitch=[];R_Knee_Pitch=[];R_Ankle_Pitch=[];R_Ankle_Roll=[];
L_Shoulder_Pitch=[];L_Shoulder_Roll=[];L_Elbow_Yaw=[];L_Elbow_Roll=[];L_Wrist_Yaw=[]
R_Shoulder_Pitch=[];R_Shoulder_Roll=[];R_Elbow_Yaw=[];R_Elbow_Roll=[];R_Wrist_Yaw=[]
R_H=[];L_H=[];R_Hand=[];L_Hand=[];
Body = [Head_Yaw,Head_Pitch,L_Hip_Yaw_Pitch,L_Hip_Roll,L_Hip_Pitch,L_Knee_Pitch,L_Ankle_Pitch,L_Ankle_Roll,R_Hip_Yaw_Pitch,R_Hip_Roll,R_Hip_Pitch,R_Knee_Pitch,R_Ankle_Pitch,R_Ankle_Roll,L_Shoulder_Pitch,L_Shoulder_Roll,L_Elbow_Yaw,L_Elbow_Roll,L_Wrist_Yaw,R_Shoulder_Pitch,R_Shoulder_Roll,R_Elbow_Yaw,R_Elbow_Roll,R_Wrist_Yaw,L_H,L_Hand,R_H,R_Hand]

get_all_handles(3, clientID,Body)

ret, NAO = vrep.simxGetObjectHandle(clientID, "NAO", vrep.simx_opmode_blocking)
ret, NAO_Head = vrep.simxGetObjectHandle(clientID, "HeadYaw", vrep.simx_opmode_blocking)

#Funcoes de GA
creator.create("FitnessMax", base.Fitness, weights=(1.0,))
creator.create("Individual", list, fitness = creator.FitnessMax)

toolbox = base.Toolbox()
toolbox.register("attr_coef", lambda: (random.random() * 1 - 0.5))
toolbox.register("individual", tools.initRepeat, creator.Individual, toolbox.attr_coef, len(Body) * INDIVIDUAL_SIZE)
toolbox.register("population", tools.initRepeat, list, toolbox.individual)

def evalRobot(individual):
    reset_simulation(clientID)
    dt = 0
    shead = 0
    h = vrep.simxGetObjectPosition(clientID, NAO_Head, -1, vrep.simx_opmode_blocking)[1][2] - 0.1

    while dt < 1:
        joint_movements = []

        for i in xrange(len(Body)):
            coefs = individual[i * INDIVIDUAL_SIZE:(i + 1) * INDIVIDUAL_SIZE]
            joint_movements.append(truncated_Fourier(coefs, dt))
        JointControl(clientID, 0, Body, joint_movements)
        hn = vrep.simxGetObjectPosition(clientID, NAO_Head, -1, vrep.simx_opmode_blocking)[1][2] - 0.1
        shead += (hn-h)
        h = hn
        time.sleep(INTERVAL)
        dt += INTERVAL

    ret, robot_position = vrep.simxGetObjectPosition(clientID, NAO, -1, vrep.simx_opmode_blocking)
    ret, head_position = vrep.simxGetObjectPosition(clientID, NAO_Head, -1, vrep.simx_opmode_blocking)
    #xfactor consiste na posicao x que o NAO andou
    x_factor = robot_position[0]
    fit = (shead*x_factor)
    print(fit)
    return fit,

def mutate(individual):
    return [(random.random() * 1 - 0.5) for x in individual if random.random() < 0.05]

toolbox.register("evaluate", evalRobot)
toolbox.register("mate", tools.cxTwoPoint)
toolbox.register("mutate", mutate)
toolbox.register("select",tools.selTournament, tournsize = 3)

def main():
    pop = toolbox.population(n = 20)

    CXPB, MUTPB, NGEN = 0.6, 0.2, 40

    fitnesses = list(map(toolbox.evaluate, pop))
    for ind, fit in zip(pop, fitnesses):
        ind.fitness.values = fit

    for g in xrange(NGEN):
        print("-- Generation %i --" % g)

        offspring = toolbox.select(pop, len(pop))
        offspring = list(map(toolbox.clone, offspring))

        for child1, child2 in zip(offspring[::2],offspring[1::2]):
            if random.random() < CXPB:
                toolbox.mate(child1, child2)
                del child1.fitness.values
                del child2.fitness.values

        for mutant in offspring:
            if random.random()<MUTPB:
                toolbox.mutate(mutant)
                del mutant.fitness.values

        invalid_ind = [ind for ind in offspring if not ind.fitness.valid]
        fitnesses = map(toolbox.evaluate,invalid_ind)

        for ind, fit in zip(invalid_ind, fitnesses):
            ind.fitness.values = fit

        fits = [ind.fitness.values[0] for ind in pop]
        length = len(pop)
        mean = sum(fits) / length
        sum2 = sum(x*x for x in fits)
        std = abs(sum2/length - mean**2)**0.5

        print("  Min %s" % min(fits))
        print("  Max %s" % max(fits))
        print("  Avg %s" % mean)
        print("  Std %s" % std)
        #TODO escrever melhor cromossomo print tools.selBest(pop, k=1)

        pop[:] = offspring

if __name__ == "__main__":
    main()
