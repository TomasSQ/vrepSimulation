import vrep
import time

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
