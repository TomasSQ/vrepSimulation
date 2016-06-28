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

GENOME = [-0.45469889240437633, -0.48111314464607546, -0.15823706598520015, 0.047587962290808306, -0.18673917482919333, -0.038815289668724606, 0.11979915403910635, -0.28443213412524904, 0.44586699110964356, -0.22930045625513107, -0.2786187498389444, -0.03126335994257945, -0.03101942679853409, 0.1473680381984772, 0.2746235978387427, -0.2858079536872734, 0.26377469579270774, 0.4614844486388999, -0.25005431754489815, 0.4140169031866302, 0.15612741085777704, 0.1938443426113543, -0.11229687705877323, -0.07183322804119907, -0.3746608404630589, -0.0274925096561085, -0.3966231610573364, 0.3356172769744964, -0.0686996885228639, 0.42051144326162104, 0.014202428677485224, -0.19376753992672036, -0.08148678658173292, 0.12402561129981116, -0.3424998956552199, 0.4174132625627114, 0.40432774295790064, 0.10447739094621, -0.25789576615600884, -0.3197517170497859, 0.1549639752683949, 0.15982749043724476, 0.3923193311161908, 0.3660624011584467, -0.24653234820721803, -0.4773433977499365, -0.45312419942004645, 0.15154168420243586, 0.2185173195370954, 0.1387693398359514, -0.11255541364184363, -0.03977893047435266, -0.266497512613321, 0.3720631992073993, 0.09353741118500924, 0.15285713913295496]
N_COEF = 0
JOINT_SIZE = 2 * N_COEF + 2
INTERVAL = 0.05 #50ms

#Serie de Fourier Truncada
def truncated_Fourier(coeficients, time, stable):
    value = stable and coeficients[0] / 2.0 or 0.0

    for i in xrange(N_COEF):
        if stable: value += coeficients[2 * i + 2] * math.cos((i + 1) * time)
        if not stable: value += coeficients[2 * i + 3] * math.sin((i + 1) * time)

    return value

#Conexao com o vrep
vrep.simxFinish(-1) # just in case, close all opened connections
clientID = vrep.simxStart('127.0.0.1',19997,True,True,5000,5) # Conecta com o VREP. Por padrao ele ja abre essa porta.
if clientID == -1:
    exit (10)



#Juntas do NAO
Head_Yaw=[];Head_Pitch=[];
L_Hip_Yaw_Pitch=[];L_Hip_Roll=[];L_Hip_Pitch=[];L_Knee_Pitch=[];L_Ankle_Pitch=[];L_Ankle_Roll=[];
R_Hip_Yaw_Pitch=[];R_Hip_Roll=[];R_Hip_Pitch=[];R_Knee_Pitch=[];R_Ankle_Pitch=[];R_Ankle_Roll=[];
L_Shoulder_Pitch=[];L_Shoulder_Roll=[];L_Elbow_Yaw=[];L_Elbow_Roll=[];L_Wrist_Yaw=[]
R_Shoulder_Pitch=[];R_Shoulder_Roll=[];R_Elbow_Yaw=[];R_Elbow_Roll=[];R_Wrist_Yaw=[]
R_H=[];L_H=[];R_Hand=[];L_Hand=[];
Body = [Head_Yaw,Head_Pitch,L_Hip_Yaw_Pitch,L_Hip_Roll,L_Hip_Pitch,L_Knee_Pitch,L_Ankle_Pitch,L_Ankle_Roll,R_Hip_Yaw_Pitch,R_Hip_Roll,R_Hip_Pitch,R_Knee_Pitch,R_Ankle_Pitch,R_Ankle_Roll,L_Shoulder_Pitch,L_Shoulder_Roll,L_Elbow_Yaw,L_Elbow_Roll,L_Wrist_Yaw,R_Shoulder_Pitch,R_Shoulder_Roll,R_Elbow_Yaw,R_Elbow_Roll,R_Wrist_Yaw,L_H,L_Hand,R_H,R_Hand]

#Multiplicador das juntas do NAO
Head_Yaw=1.0;Head_Pitch=1.0;
L_Hip_Yaw_Pitch=1.0;L_Hip_Roll=1.0;L_Hip_Pitch=1.0;L_Knee_Pitch=1.0;L_Ankle_Pitch=1.0;L_Ankle_Roll=1.0;
R_Hip_Yaw_Pitch=1.0;R_Hip_Roll=1.0;R_Hip_Pitch=1.0;R_Knee_Pitch=1.0;R_Ankle_Pitch=1.0;R_Ankle_Roll=1.0;
L_Shoulder_Pitch=1.0;L_Shoulder_Roll=1.0;L_Elbow_Yaw=1.0;L_Elbow_Roll=1.0;L_Wrist_Yaw=1.0
R_Shoulder_Pitch=1.0;R_Shoulder_Roll=1.0;R_Elbow_Yaw=1.0;R_Elbow_Roll=1.0;R_Wrist_Yaw=1.0
R_H=1.0;L_H=1.0;R_Hand=1.0;L_Hand=1.0;
control_joints = [Head_Yaw,Head_Pitch,L_Hip_Yaw_Pitch,L_Hip_Roll,L_Hip_Pitch,L_Knee_Pitch,L_Ankle_Pitch,L_Ankle_Roll,R_Hip_Yaw_Pitch,R_Hip_Roll,R_Hip_Pitch,R_Knee_Pitch,R_Ankle_Pitch,R_Ankle_Roll,L_Shoulder_Pitch,L_Shoulder_Roll,L_Elbow_Yaw,L_Elbow_Roll,L_Wrist_Yaw,R_Shoulder_Pitch,R_Shoulder_Roll,R_Elbow_Yaw,R_Elbow_Roll,R_Wrist_Yaw,L_H,L_Hand,R_H,R_Hand]

get_all_handles(3, clientID,Body)
f = file('start_moviment_ga.txt')

startMoves = []
for line in f:
    split_line = line.split(' ')
    startMoves += [[float(x) for x in split_line[1:]]]

#Reset da simulacao
def reset_simulation(clientID):
    vrep.simxStopSimulation(clientID, vrep.simx_opmode_oneshot)
    time.sleep(1) # um pequeno sleep entre o stop e o start
    vrep.simxStartSimulation(clientID, vrep.simx_opmode_oneshot)
    for move in startMoves:
        JointControl(clientID, 0, Body, move)
        time.sleep(0.1)

def move_robot(individual):
    stable = True
    scycles = 0
    stcmax = 10
    dt = 0

    while True:
        joint_movements = []

        for i in xrange(len(Body)):
            coefs = individual[i * JOINT_SIZE:(i + 1) * JOINT_SIZE]
            joint_movements.append(truncated_Fourier(coefs, dt, stable)*control_joints[i])

        JointControl2(clientID, 0, Body, joint_movements)

        time.sleep(INTERVAL)
        dt += INTERVAL
        scycles += 1
        if scycles >= stcmax:
            scycles = 0
            stable = not stable

def main():
    reset_simulation(clientID)
    move_robot(GENOME)

if __name__ == "__main__":
    main()
