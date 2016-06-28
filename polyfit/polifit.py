import vrep
import time
from manage_joints import *
import numpy as np

vrep.simxFinish(-1) # just in case, close all opened connections
clientID = vrep.simxStart('127.0.0.1',19997,True,True,5000,5) # Connecta com o VREP. Por padrao ele ja abre essa porta.
if clientID == -1:
    exit (10)

def reset_simulation(clientID):
    vrep.simxStopSimulation(clientID, vrep.simx_opmode_oneshot)
    time.sleep(1) # um pequeno sleep entre o stop e o start
    vrep.simxStartSimulation(clientID, vrep.simx_opmode_oneshot)

Head_Yaw=[];Head_Pitch=[];
L_Hip_Yaw_Pitch=[];L_Hip_Roll=[];L_Hip_Pitch=[];L_Knee_Pitch=[];L_Ankle_Pitch=[];L_Ankle_Roll=[];
R_Hip_Yaw_Pitch=[];R_Hip_Roll=[];R_Hip_Pitch=[];R_Knee_Pitch=[];R_Ankle_Pitch=[];R_Ankle_Roll=[];
L_Shoulder_Pitch=[];L_Shoulder_Roll=[];L_Elbow_Yaw=[];L_Elbow_Roll=[];L_Wrist_Yaw=[]
R_Shoulder_Pitch=[];R_Shoulder_Roll=[];R_Elbow_Yaw=[];R_Elbow_Roll=[];R_Wrist_Yaw=[]
R_H=[];L_H=[];R_Hand=[];L_Hand=[];
Body = [Head_Yaw,Head_Pitch,L_Hip_Yaw_Pitch,L_Hip_Roll,L_Hip_Pitch,L_Knee_Pitch,L_Ankle_Pitch,L_Ankle_Roll,R_Hip_Yaw_Pitch,R_Hip_Roll,R_Hip_Pitch,R_Knee_Pitch,R_Ankle_Pitch,R_Ankle_Roll,L_Shoulder_Pitch,L_Shoulder_Roll,L_Elbow_Yaw,L_Elbow_Roll,L_Wrist_Yaw,R_Shoulder_Pitch,R_Shoulder_Roll,R_Elbow_Yaw,R_Elbow_Roll,R_Wrist_Yaw,L_H,L_Hand,R_H,R_Hand]

get_all_handles(3, clientID,Body)
def startPosition():
    f = file('start_moviment.txt')

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
            JointControl(clientID, 0, Body, move)
            time.sleep(0.007)

reset_simulation(clientID)
startPosition()
walk()
