import vrep
import time
from manage_joints import *
import numpy as np

#para rodar, coloque na mesma pasta do vrep.
#instrucoes em http://www.coppeliarobotics.com/helpFiles/en/remoteApiClientSide.htm
print ('Program started')

vrep.simxFinish(-1) # just in case, close all opened connections
clientID = vrep.simxStart('127.0.0.1',19997,True,True,5000,5) # Connecta com o VREP. Por padrao ele ja abre essa porta.
if clientID == -1:
    exit (10)

print ('Connected to remote API server')


def reset_simulation(clientID):
    vrep.simxStopSimulation(clientID, vrep.simx_opmode_oneshot)
    time.sleep(1) # um pequeno sleep entre o stop e o start
    vrep.simxStartSimulation(clientID, vrep.simx_opmode_oneshot)

def simple():
    # obtem os handlers. Um Handler eh um numero que identifica um componente, como, por exemplo, uma junta
    res, nao = vrep.simxGetObjectHandle(clientID, "NAO", vrep.simx_opmode_blocking)
    res, shL = vrep.simxGetObjectHandle(clientID, "LShoulderPitch3", vrep.simx_opmode_blocking)
    res, shR = vrep.simxGetObjectHandle(clientID, "RShoulderPitch3", vrep.simx_opmode_blocking)
    res, kneeR = vrep.simxGetObjectHandle(clientID, "RKneePitch3", vrep.simx_opmode_blocking)
    res, kneeL = vrep.simxGetObjectHandle(clientID, "LKneePitch3", vrep.simx_opmode_blocking)
    res, hipPitchL = vrep.simxGetObjectHandle(clientID, "LHipPitch3", vrep.simx_opmode_blocking)
    res, hipPitchR = vrep.simxGetObjectHandle(clientID, "RHipPitch3", vrep.simx_opmode_blocking)
    res, hipYawPitchL = vrep.simxGetObjectHandle(clientID, "LHipYawPitch3", vrep.simx_opmode_blocking)
    res, hipYawPitchR = vrep.simxGetObjectHandle(clientID, "RHipYawPitch3", vrep.simx_opmode_blocking)
    res, anklePitchL = vrep.simxGetObjectHandle(clientID, "LAnklePitch3", vrep.simx_opmode_blocking)
    res, anklePitchR = vrep.simxGetObjectHandle(clientID, "RAnklePitch3", vrep.simx_opmode_blocking)


    while True:
    	# Envia comandos para as juntas
    	vrep.simxSetJointTargetPosition(clientID, kneeR, 1.2,vrep.simx_opmode_oneshot)
    	vrep.simxSetJointTargetPosition(clientID, anklePitchR, 0.4,vrep.simx_opmode_oneshot)

    	time.sleep(1)
    	vrep.simxSetJointTargetPosition(clientID, hipYawPitchL, -0.3,vrep.simx_opmode_oneshot)

    	vrep.simxSetJointTargetPosition(clientID, hipPitchR, -0.1,vrep.simx_opmode_oneshot)
    	vrep.simxSetJointTargetPosition(clientID, hipYawPitchR, -0.3,vrep.simx_opmode_oneshot)
    	vrep.simxSetJointTargetPosition(clientID, kneeR, -0.1,vrep.simx_opmode_oneshot)
    	vrep.simxSetJointTargetPosition(clientID, anklePitchR, 0,vrep.simx_opmode_oneshot)

    	print vrep.simxGetObjectPosition(clientID, nao, -1, vrep.simx_opmode_blocking)
    	reset_simulation(clientID)

    #time.sleep(3)
    #vrep.simxSetJointTargetPosition(clientID, hipPitchL, -0.5,vrep.simx_opmode_oneshot)
    #vrep.simxSetJointTargetPosition(clientID, kneeL, -0.5,vrep.simx_opmode_oneshot)
    #vrep.simxSetJointTargetPosition(clientID, anklePitchL, 0.5,vrep.simx_opmode_oneshot)


Head_Yaw=[];Head_Pitch=[];
L_Hip_Yaw_Pitch=[];L_Hip_Roll=[];L_Hip_Pitch=[];L_Knee_Pitch=[];L_Ankle_Pitch=[];L_Ankle_Roll=[];
R_Hip_Yaw_Pitch=[];R_Hip_Roll=[];R_Hip_Pitch=[];R_Knee_Pitch=[];R_Ankle_Pitch=[];R_Ankle_Roll=[];
L_Shoulder_Pitch=[];L_Shoulder_Roll=[];L_Elbow_Yaw=[];L_Elbow_Roll=[];L_Wrist_Yaw=[]
R_Shoulder_Pitch=[];R_Shoulder_Roll=[];R_Elbow_Yaw=[];R_Elbow_Roll=[];R_Wrist_Yaw=[]
R_H=[];L_H=[];R_Hand=[];L_Hand=[];
Body = [Head_Yaw,Head_Pitch,L_Hip_Yaw_Pitch,L_Hip_Roll,L_Hip_Pitch,L_Knee_Pitch,L_Ankle_Pitch,L_Ankle_Roll,R_Hip_Yaw_Pitch,R_Hip_Roll,R_Hip_Pitch,R_Knee_Pitch,R_Ankle_Pitch,R_Ankle_Roll,L_Shoulder_Pitch,L_Shoulder_Roll,L_Elbow_Yaw,L_Elbow_Roll,L_Wrist_Yaw,R_Shoulder_Pitch,R_Shoulder_Roll,R_Elbow_Yaw,R_Elbow_Roll,R_Wrist_Yaw,L_H,L_Hand,R_H,R_Hand]

get_all_handles(3, clientID,Body)
def startPosition():

    f = file('start_moviment_ga.txt')

    startMoves = []
    for line in f:
        split_line = line.split(' ')
        startMoves += [[float(x) for x in split_line[1:]]]
    for move in startMoves:
        JointControl(clientID, 0, Body, move)
        time.sleep(0.1)

BEGIN = 4210
END = BEGIN + 3000

INTERVAL = 0.001


def walk():
    f = file('training_data2.txt')

    functions = []
    aproximations = []

    for i in xrange(26):
        functions += [[]]
        aproximations += [[]]

    for line in f:
        split_line = line.split(' ')
        if float(split_line[0]) < BEGIN:
            continue
        if float(split_line[0]) > END:
            break
        to_float = [float(x) for x in split_line[1:]]
        for i in xrange(len(to_float)):
            functions[i] += [to_float[i]]

    i = 0
    for f in xrange(len(functions)):
        print i
        i += 1
        x = np.arange(0, len(functions[f]) * INTERVAL, INTERVAL)
        p = np.poly1d(np.polyfit(x, functions[f], 150))
        for t in xrange(len(functions[f])):
            aproximations[f] += [p(t * INTERVAL)]

    while True:
        for t in xrange(len(aproximations[0])):
            move = []
            for aproximation in aproximations:
                move += [aproximation[t]]
            print t
            JointControl(clientID, 0, Body, move)
            time.sleep(0.007)

reset_simulation(clientID)
startPosition()
walk()
