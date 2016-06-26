import vrep
import time
import random
import math

from manage_joints import *

from deap import base
from deap import creator
from deap import tools

def JointControl2(clientID,i,Body, commandAngles):

    vrep.simxSetJointTargetPosition(clientID,Body[0][i],commandAngles[0],vrep.simx_opmode_streaming)
    vrep.simxSetJointTargetPosition(clientID,Body[1][i],commandAngles[1],vrep.simx_opmode_streaming)
    #Left Leg
    vrep.simxSetJointTargetPosition(clientID,Body[2][i],commandAngles[2],vrep.simx_opmode_streaming)
    vrep.simxSetJointTargetPosition(clientID,Body[3][i],commandAngles[3],vrep.simx_opmode_streaming)
    vrep.simxSetJointTargetPosition(clientID,Body[4][i],commandAngles[4],vrep.simx_opmode_streaming)
    vrep.simxSetJointTargetPosition(clientID,Body[5][i],commandAngles[5],vrep.simx_opmode_streaming)
    vrep.simxSetJointTargetPosition(clientID,Body[6][i],commandAngles[6],vrep.simx_opmode_streaming)
    vrep.simxSetJointTargetPosition(clientID,Body[7][i],commandAngles[7],vrep.simx_opmode_streaming)
    #Right Leg
    vrep.simxSetJointTargetPosition(clientID,Body[8][i],commandAngles[8],vrep.simx_opmode_streaming)
    vrep.simxSetJointTargetPosition(clientID,Body[9][i],commandAngles[9],vrep.simx_opmode_streaming)
    vrep.simxSetJointTargetPosition(clientID,Body[10][i],commandAngles[10],vrep.simx_opmode_streaming)
    vrep.simxSetJointTargetPosition(clientID,Body[11][i],commandAngles[11],vrep.simx_opmode_streaming)
    vrep.simxSetJointTargetPosition(clientID,Body[12][i],commandAngles[12],vrep.simx_opmode_streaming)
    vrep.simxSetJointTargetPosition(clientID,Body[13][i],commandAngles[13],vrep.simx_opmode_streaming)
    #Left Arm
    vrep.simxSetJointTargetPosition(clientID,Body[14][i],commandAngles[14],vrep.simx_opmode_streaming)
    vrep.simxSetJointTargetPosition(clientID,Body[15][i],commandAngles[15],vrep.simx_opmode_streaming)
    vrep.simxSetJointTargetPosition(clientID,Body[16][i],commandAngles[16],vrep.simx_opmode_streaming)
    vrep.simxSetJointTargetPosition(clientID,Body[17][i],commandAngles[17],vrep.simx_opmode_streaming)
    vrep.simxSetJointTargetPosition(clientID,Body[18][i],commandAngles[18],vrep.simx_opmode_streaming)
    #Right Arm
    vrep.simxSetJointTargetPosition(clientID,Body[19][i],commandAngles[19],vrep.simx_opmode_streaming)
    vrep.simxSetJointTargetPosition(clientID,Body[20][i],commandAngles[20],vrep.simx_opmode_streaming)
    vrep.simxSetJointTargetPosition(clientID,Body[21][i],commandAngles[21],vrep.simx_opmode_streaming)
    vrep.simxSetJointTargetPosition(clientID,Body[22][i],commandAngles[22],vrep.simx_opmode_streaming)
    vrep.simxSetJointTargetPosition(clientID,Body[23][i],commandAngles[23],vrep.simx_opmode_streaming)
    #Left Fingers
    vrep.simxSetJointTargetPosition(clientID,Body[25][i][0],1.0-commandAngles[25],vrep.simx_opmode_streaming)
    vrep.simxSetJointTargetPosition(clientID,Body[25][i][1],1.0-commandAngles[25],vrep.simx_opmode_streaming)
    vrep.simxSetJointTargetPosition(clientID,Body[25][i][2],1.0-commandAngles[25],vrep.simx_opmode_streaming)
    vrep.simxSetJointTargetPosition(clientID,Body[25][i][3],1.0-commandAngles[25],vrep.simx_opmode_streaming)
    vrep.simxSetJointTargetPosition(clientID,Body[25][i][4],1.0-commandAngles[25],vrep.simx_opmode_streaming)
    vrep.simxSetJointTargetPosition(clientID,Body[25][i][5],1.0-commandAngles[25],vrep.simx_opmode_streaming)
    vrep.simxSetJointTargetPosition(clientID,Body[25][i][6],1.0-commandAngles[25],vrep.simx_opmode_streaming)
    vrep.simxSetJointTargetPosition(clientID,Body[25][i][7],1.0-commandAngles[25],vrep.simx_opmode_streaming)
    #Right Fingers
    vrep.simxSetJointTargetPosition(clientID,Body[27][i][0],1.0-commandAngles[27],vrep.simx_opmode_streaming)
    vrep.simxSetJointTargetPosition(clientID,Body[27][i][1],1.0-commandAngles[27],vrep.simx_opmode_streaming)
    vrep.simxSetJointTargetPosition(clientID,Body[27][i][2],1.0-commandAngles[27],vrep.simx_opmode_streaming)
    vrep.simxSetJointTargetPosition(clientID,Body[27][i][3],1.0-commandAngles[27],vrep.simx_opmode_streaming)
    vrep.simxSetJointTargetPosition(clientID,Body[27][i][4],1.0-commandAngles[27],vrep.simx_opmode_streaming)
    vrep.simxSetJointTargetPosition(clientID,Body[27][i][5],1.0-commandAngles[27],vrep.simx_opmode_streaming)
    vrep.simxSetJointTargetPosition(clientID,Body[27][i][6],1.0-commandAngles[27],vrep.simx_opmode_streaming)
    vrep.simxSetJointTargetPosition(clientID,Body[27][i][7],1.0-commandAngles[27],vrep.simx_opmode_streaming)

DEBUG = True

POPULATION_SIZE = 20
COEF_RANGE = 1.0
N_COEF = 5
JOINT_SIZE = 2 * N_COEF + 2
DELTA_TIME = 3.0
INTERVAL = 0.05 #50ms
ANGLE_THRESHOLD = 15.0 * (math.pi)/180

#Serie de Fourier Truncada
def truncated_Fourier(coeficients, time):
    value = coeficients[0] / 2.0

    for i in xrange(N_COEF):
        value += coeficients[2 * i + 2] * math.cos((i + 1) * coeficients[1] * time)
        value += coeficients[2 * i + 3] * math.sin((i + 1) * coeficients[1] * time)

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

#Multiplicador das juntas do NAO
Head_Yaw=0;Head_Pitch=0;
L_Hip_Yaw_Pitch=1.0;L_Hip_Roll=1.0;L_Hip_Pitch=1.0;L_Knee_Pitch=1.0;L_Ankle_Pitch=1.0;L_Ankle_Roll=0.0;
R_Hip_Yaw_Pitch=1.0;R_Hip_Roll=1.0;R_Hip_Pitch=1.0;R_Knee_Pitch=1.0;R_Ankle_Pitch=1.0;R_Ankle_Roll=0.0;
L_Shoulder_Pitch=1.0;L_Shoulder_Roll=1.0;L_Elbow_Yaw=1.0;L_Elbow_Roll=1.0;L_Wrist_Yaw=0.0
R_Shoulder_Pitch=1.0;R_Shoulder_Roll=1.0;R_Elbow_Yaw=1.0;R_Elbow_Roll=1.0;R_Wrist_Yaw=0.0
R_H=0.0;L_H=0.0;R_Hand=0.0;L_Hand=0.0;
control_joints = [Head_Yaw,Head_Pitch,L_Hip_Yaw_Pitch,L_Hip_Roll,L_Hip_Pitch,L_Knee_Pitch,L_Ankle_Pitch,L_Ankle_Roll,R_Hip_Yaw_Pitch,R_Hip_Roll,R_Hip_Pitch,R_Knee_Pitch,R_Ankle_Pitch,R_Ankle_Roll,L_Shoulder_Pitch,L_Shoulder_Roll,L_Elbow_Yaw,L_Elbow_Roll,L_Wrist_Yaw,R_Shoulder_Pitch,R_Shoulder_Roll,R_Elbow_Yaw,R_Elbow_Roll,R_Wrist_Yaw,L_H,L_Hand,R_H,R_Hand]
[Head_Yaw,Head_Pitch,]

get_all_handles(3, clientID,Body)

ret, NAO = vrep.simxGetObjectHandle(clientID, "NAO", vrep.simx_opmode_blocking)
ret, NAO_Head = vrep.simxGetObjectHandle(clientID, "HeadYaw", vrep.simx_opmode_blocking)

#Funcoes de GA
creator.create("FitnessMax", base.Fitness, weights=(1.0,))
creator.create("Individual", list, fitness = creator.FitnessMax)

toolbox = base.Toolbox()
toolbox.register("attr_coef", lambda: (random.random() * COEF_RANGE - COEF_RANGE / 2.0))
toolbox.register("individual", tools.initRepeat, creator.Individual, toolbox.attr_coef, len(Body) * JOINT_SIZE)
toolbox.register("population", tools.initRepeat, list, toolbox.individual)

def evalRobot(individual):
    reset_simulation(clientID)
    dt = 0

    fit = 0.0

    ox = 0.0
    negative_walk = 0

    while dt < DELTA_TIME:
        joint_movements = []

        for i in xrange(len(Body)):
            coefs = individual[i * JOINT_SIZE:(i + 1) * JOINT_SIZE]
            joint_movements.append(truncated_Fourier(coefs, dt)*control_joints[i])

        JointControl2(clientID, 0, Body, joint_movements)

        x = vrep.simxGetObjectPosition(clientID, NAO, -1, vrep.simx_opmode_blocking)[1][0]
        dx = (x - ox)
        ox = x

        if dx < 0.0:
            negative_walk += 1
        else:
            negative_walk = 0

        ret, orientation = vrep.simxGetObjectOrientation(clientID, NAO, -1, vrep.simx_opmode_blocking)

        orientation_alpha = min(ANGLE_THRESHOLD, max(-ANGLE_THRESHOLD, orientation[0]))
        orientation_beta = min(ANGLE_THRESHOLD, max(-ANGLE_THRESHOLD, orientation[1]))
        orientation_gama = min(ANGLE_THRESHOLD, max(-ANGLE_THRESHOLD, orientation[2]))

        ha = hb = hg = 0
        if orientation_alpha >= 0.0 :
            ha = (- orientation_alpha) / ANGLE_THRESHOLD + 1.0
        else:
            ha = (orientation_alpha + ANGLE_THRESHOLD) / ANGLE_THRESHOLD

        if orientation_beta >= 0.0 :
            hb = (- orientation_beta) / ANGLE_THRESHOLD + 1.0
        else:
            hb = (orientation_beta + ANGLE_THRESHOLD) / ANGLE_THRESHOLD

        if orientation_gama >= 0.0 :
            hg = (- orientation_gama) / (ANGLE_THRESHOLD + 0.1) + 1.0
        else:
            hg = (orientation_gama + (ANGLE_THRESHOLD + 0.1)) / (ANGLE_THRESHOLD + 0.1)

        fit += (ha * hb * hg * dx)

        if (ha * hb * hg < 0.00000001):
            fit -= 2.0

        if negative_walk >= 10:
            fit -= 2.0


        time.sleep(INTERVAL)
        dt += INTERVAL

    if DEBUG: print(fit)
    return fit,

def mutate(individual):
    return [(random.random() * COEF_RANGE - COEF_RANGE / 2.0) for x in individual if random.random() < 0.05]

toolbox.register("evaluate", evalRobot)
toolbox.register("mate", tools.cxTwoPoint)
toolbox.register("mutate", mutate)
toolbox.register("elite",tools.selBest, k = 2)
toolbox.register("select",tools.selTournament, tournsize = 3)

def main():
    pop = toolbox.population(n = POPULATION_SIZE)

    CXPB, MUTPB, NGEN = 0.6, 0.2, 100

    if DEBUG: print("-- Life Span --")
    fitnesses = list(map(toolbox.evaluate, pop))
    for ind, fit in zip(pop, fitnesses):
        ind.fitness.values = fit

    for g in xrange(NGEN):
        print("-- Generation %i --" % (g+1))

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

        if DEBUG: print("-- Calculating fitness for prole --")
        invalid_ind = [ind for ind in offspring if not ind.fitness.valid]
        fitnesses = map(toolbox.evaluate,invalid_ind)

        for ind, fit in zip(invalid_ind, fitnesses):
            ind.fitness.values = fit

        fits = [ind.fitness.values[0] for ind in offspring]
        length = len(pop)
        mean = sum(fits) / length
        sum2 = sum(x*x for x in fits)
        std = abs(sum2/length - mean**2)**0.5

        print("  Min %s" % min(fits))
        print("  Max %s" % max(fits))
        print("  Avg %s" % mean)
        print("  Std %s" % std)

        if DEBUG: print("   Best Chromossome: %s"%tools.selBest(offspring, k = 1))

        pop[:] = offspring

    print("   The Walker: %s"% tools.selBest(pop, k = 1))

if __name__ == "__main__":
    main()
