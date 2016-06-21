import vrep
import time

from manage_joints import *

vrep.simxFinish(-1) # just in case, close all opened connections
clientID = vrep.simxStart('127.0.0.1',19997,True,True,5000,5) # Connecta com o VREP. Por padrao ele ja abre essa porta.
if clientID == -1:
    exit (10)


Head_Yaw=[];Head_Pitch=[];
L_Hip_Yaw_Pitch=[];L_Hip_Roll=[];L_Hip_Pitch=[];L_Knee_Pitch=[];L_Ankle_Pitch=[];L_Ankle_Roll=[];
R_Hip_Yaw_Pitch=[];R_Hip_Roll=[];R_Hip_Pitch=[];R_Knee_Pitch=[];R_Ankle_Pitch=[];R_Ankle_Roll=[];
L_Shoulder_Pitch=[];L_Shoulder_Roll=[];L_Elbow_Yaw=[];L_Elbow_Roll=[];L_Wrist_Yaw=[]
R_Shoulder_Pitch=[];R_Shoulder_Roll=[];R_Elbow_Yaw=[];R_Elbow_Roll=[];R_Wrist_Yaw=[]
R_H=[];L_H=[];R_Hand=[];L_Hand=[];
Body = [Head_Yaw,Head_Pitch,L_Hip_Yaw_Pitch,L_Hip_Roll,L_Hip_Pitch,L_Knee_Pitch,L_Ankle_Pitch,L_Ankle_Roll,R_Hip_Yaw_Pitch,R_Hip_Roll,R_Hip_Pitch,R_Knee_Pitch,R_Ankle_Pitch,R_Ankle_Roll,L_Shoulder_Pitch,L_Shoulder_Roll,L_Elbow_Yaw,L_Elbow_Roll,L_Wrist_Yaw,R_Shoulder_Pitch,R_Shoulder_Roll,R_Elbow_Yaw,R_Elbow_Roll,R_Wrist_Yaw,L_H,L_Hand,R_H,R_Hand]

get_all_handles(3, clientID,Body)

MENOR_DISTANCIA = 0.0001
MAXIMO_CICLOS_PARADOS = 100

def moveRobo(chromosome):
	#move cada articulacao de acordo com as constantes do chromosome

def deltaX(p1, p2):
	return 0

def fitness (chromosome):
	p0 = vrep.simxGetObjectPosition(clientID, nao, -1, vrep.simx_opmode_blocking)
	pf = []
	while True:
		p1 = vrep.simxGetObjectPosition(clientID, nao, -1, vrep.simx_opmode_blocking)
		moveRobo(chromosome)
		time.sleep(0.001)
		pf = vrep.simxGetObjectPosition(clientID, nao, -1, vrep.simx_opmode_blocking)
		delta = deltaX(p2, p1.x)
		if delta < MENOR_DISTANCIA:
			ciclosParados += 1
		if ciclosParados >= MAXIMO_CICLOS_PARADOS:
			break

	return deltaX(pf, p0)

#faz algoritmo genetico
