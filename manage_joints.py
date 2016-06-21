# -*- coding: utf-8 -*-
"""
Created on Tue Jul  7 14:09:03 2015

@author: Pierre Jacquot
"""

import vrep

#Get the handles of all NAO in the scene
def get_all_handles(nbrOfNao,clientID,Body):
    print '-> Head for NAO : '+ str(1)
    Body[0].append(vrep.simxGetObjectHandle(clientID,'HeadYaw#',vrep.simx_opmode_oneshot_wait)[1])
    Body[1].append(vrep.simxGetObjectHandle(clientID,'HeadPitch#',vrep.simx_opmode_oneshot_wait)[1])
    #Left Leg
    print '-> Left Leg for NAO : ' + str(1)
    Body[2].append(vrep.simxGetObjectHandle(clientID,'LHipYawPitch3#',vrep.simx_opmode_oneshot_wait)[1])
    Body[3].append(vrep.simxGetObjectHandle(clientID,'LHipRoll3#',vrep.simx_opmode_oneshot_wait)[1])
    Body[4].append(vrep.simxGetObjectHandle(clientID,'LHipPitch3#',vrep.simx_opmode_oneshot_wait)[1])
    Body[5].append(vrep.simxGetObjectHandle(clientID,'LKneePitch3#',vrep.simx_opmode_oneshot_wait)[1])
    Body[6].append(vrep.simxGetObjectHandle(clientID,'LAnklePitch3#',vrep.simx_opmode_oneshot_wait)[1])
    Body[7].append(vrep.simxGetObjectHandle(clientID,'LAnkleRoll3#',vrep.simx_opmode_oneshot_wait)[1])
    #Right Leg
    print '-> Right Leg for NAO : ' + str(1)
    Body[8].append(vrep.simxGetObjectHandle(clientID,'RHipYawPitch3#',vrep.simx_opmode_oneshot_wait)[1])
    Body[9].append(vrep.simxGetObjectHandle(clientID,'RHipRoll3#',vrep.simx_opmode_oneshot_wait)[1])
    Body[10].append(vrep.simxGetObjectHandle(clientID,'RHipPitch3#',vrep.simx_opmode_oneshot_wait)[1])
    Body[11].append(vrep.simxGetObjectHandle(clientID,'RKneePitch3#',vrep.simx_opmode_oneshot_wait)[1])
    Body[12].append(vrep.simxGetObjectHandle(clientID,'RAnklePitch3#',vrep.simx_opmode_oneshot_wait)[1])
    Body[13].append(vrep.simxGetObjectHandle(clientID,'RAnkleRoll3#',vrep.simx_opmode_oneshot_wait)[1])
    #Left Arm
    print '-> Left Arm for NAO : ' + str(1)
    Body[14].append(vrep.simxGetObjectHandle(clientID,'LShoulderPitch3#',vrep.simx_opmode_oneshot_wait)[1])
    Body[15].append(vrep.simxGetObjectHandle(clientID,'LShoulderRoll3#',vrep.simx_opmode_oneshot_wait)[1])
    Body[16].append(vrep.simxGetObjectHandle(clientID,'LElbowYaw3#',vrep.simx_opmode_oneshot_wait)[1])
    Body[17].append(vrep.simxGetObjectHandle(clientID,'LElbowRoll3#',vrep.simx_opmode_oneshot_wait)[1])
    Body[18].append(vrep.simxGetObjectHandle(clientID,'LWristYaw3#',vrep.simx_opmode_oneshot_wait)[1])
    #Right Arm
    print '-> Right Arm for NAO : ' + str(1)
    Body[19].append(vrep.simxGetObjectHandle(clientID,'RShoulderPitch3#',vrep.simx_opmode_oneshot_wait)[1])
    Body[20].append(vrep.simxGetObjectHandle(clientID,'RShoulderRoll3#',vrep.simx_opmode_oneshot_wait)[1])
    Body[21].append(vrep.simxGetObjectHandle(clientID,'RElbowYaw3#',vrep.simx_opmode_oneshot_wait)[1])
    Body[22].append(vrep.simxGetObjectHandle(clientID,'RElbowRoll3#',vrep.simx_opmode_oneshot_wait)[1])
    Body[23].append(vrep.simxGetObjectHandle(clientID,'RWristYaw3#',vrep.simx_opmode_oneshot_wait)[1])
    #Left fingers
    print '-> Left Fingers for NAO : ' + str(1)
    Body[24].append(vrep.simxGetObjectHandle(clientID,'NAO_LThumbBase#',vrep.simx_opmode_oneshot_wait)[1])
    Body[24].append(vrep.simxGetObjectHandle(clientID,'Revolute_joint8#',vrep.simx_opmode_oneshot_wait)[1])
    Body[24].append(vrep.simxGetObjectHandle(clientID,'NAO_LLFingerBase#',vrep.simx_opmode_oneshot_wait)[1])
    Body[24].append(vrep.simxGetObjectHandle(clientID,'Revolute_joint12#',vrep.simx_opmode_oneshot_wait)[1])
    Body[24].append(vrep.simxGetObjectHandle(clientID,'Revolute_joint14#',vrep.simx_opmode_oneshot_wait)[1])
    Body[24].append(vrep.simxGetObjectHandle(clientID,'NAO_LRFinger_Base#',vrep.simx_opmode_oneshot_wait)[1])
    Body[24].append(vrep.simxGetObjectHandle(clientID,'Revolute_joint11#',vrep.simx_opmode_oneshot_wait)[1])
    Body[24].append(vrep.simxGetObjectHandle(clientID,'Revolute_joint13#',vrep.simx_opmode_oneshot_wait)[1])
    Body[25].append(Body[24][0:8])
    #Right Fingers
    print '-> Right Fingers for NAO : ' + str(1)
    Body[26].append(vrep.simxGetObjectHandle(clientID,'NAO_RThumbBase#',vrep.simx_opmode_oneshot_wait)[1])
    Body[26].append(vrep.simxGetObjectHandle(clientID,'Revolute_joint0#',vrep.simx_opmode_oneshot_wait)[1])
    Body[26].append(vrep.simxGetObjectHandle(clientID,'NAO_RLFingerBase#',vrep.simx_opmode_oneshot_wait)[1])
    Body[26].append(vrep.simxGetObjectHandle(clientID,'Revolute_joint5#',vrep.simx_opmode_oneshot_wait)[1])
    Body[26].append(vrep.simxGetObjectHandle(clientID,'Revolute_joint6#',vrep.simx_opmode_oneshot_wait)[1])
    Body[26].append(vrep.simxGetObjectHandle(clientID,'NAO_RRFinger_Base#',vrep.simx_opmode_oneshot_wait)[1])
    Body[26].append(vrep.simxGetObjectHandle(clientID,'Revolute_joint2#',vrep.simx_opmode_oneshot_wait)[1])
    Body[26].append(vrep.simxGetObjectHandle(clientID,'Revolute_joint3#',vrep.simx_opmode_oneshot_wait)[1])
    Body[27].append(Body[26][0:8])
    for i in range(0, nbrOfNao-1):
        print '-> Head for NAO : '+ str(i+2)
        Body[0].append(vrep.simxGetObjectHandle(clientID,'HeadYaw#'+str(i),vrep.simx_opmode_oneshot_wait)[1])
        Body[1].append(vrep.simxGetObjectHandle(clientID,'HeadPitch#'+str(i),vrep.simx_opmode_oneshot_wait)[1])
        #Left Leg
        print '-> Left Leg for NAO : ' + str(i+2)
        Body[2].append(vrep.simxGetObjectHandle(clientID,'LHipYawPitch3#'+str(i),vrep.simx_opmode_oneshot_wait)[1])
        Body[3].append(vrep.simxGetObjectHandle(clientID,'LHipRoll3#'+str(i),vrep.simx_opmode_oneshot_wait)[1])
        Body[4].append(vrep.simxGetObjectHandle(clientID,'LHipPitch3#'+str(i),vrep.simx_opmode_oneshot_wait)[1])
        Body[5].append(vrep.simxGetObjectHandle(clientID,'LKneePitch3#'+str(i),vrep.simx_opmode_oneshot_wait)[1])
        Body[6].append(vrep.simxGetObjectHandle(clientID,'LAnklePitch3#'+str(i),vrep.simx_opmode_oneshot_wait)[1])
        Body[7].append(vrep.simxGetObjectHandle(clientID,'LAnkleRoll3#'+str(i),vrep.simx_opmode_oneshot_wait)[1])
        #Right Leg
        print '-> Right Leg for NAO : ' + str(i+2)
        Body[8].append(vrep.simxGetObjectHandle(clientID,'RHipYawPitch3#'+str(i),vrep.simx_opmode_oneshot_wait)[1])
        Body[9].append(vrep.simxGetObjectHandle(clientID,'RHipRoll3#'+str(i),vrep.simx_opmode_oneshot_wait)[1])
        Body[10].append(vrep.simxGetObjectHandle(clientID,'RHipPitch3#'+str(i),vrep.simx_opmode_oneshot_wait)[1])
        Body[11].append(vrep.simxGetObjectHandle(clientID,'RKneePitch3#'+str(i),vrep.simx_opmode_oneshot_wait)[1])
        Body[12].append(vrep.simxGetObjectHandle(clientID,'RAnklePitch3#'+str(i),vrep.simx_opmode_oneshot_wait)[1])
        Body[13].append(vrep.simxGetObjectHandle(clientID,'RAnkleRoll3#'+str(i),vrep.simx_opmode_oneshot_wait)[1])
        #Left Arm
        print '-> Left Arm for NAO : ' + str(i+2)
        Body[14].append(vrep.simxGetObjectHandle(clientID,'LShoulderPitch3#'+str(i),vrep.simx_opmode_oneshot_wait)[1])
        Body[15].append(vrep.simxGetObjectHandle(clientID,'LShoulderRoll3#'+str(i),vrep.simx_opmode_oneshot_wait)[1])
        Body[16].append(vrep.simxGetObjectHandle(clientID,'LElbowYaw3#'+str(i),vrep.simx_opmode_oneshot_wait)[1])
        Body[17].append(vrep.simxGetObjectHandle(clientID,'LElbowRoll3#'+str(i),vrep.simx_opmode_oneshot_wait)[1])
        Body[18].append(vrep.simxGetObjectHandle(clientID,'LWristYaw3#'+str(i),vrep.simx_opmode_oneshot_wait)[1])
        #Right Arm
        print '-> Right Arm for NAO : ' + str(i+2)
        Body[19].append(vrep.simxGetObjectHandle(clientID,'RShoulderPitch3#'+str(i),vrep.simx_opmode_oneshot_wait)[1])
        Body[20].append(vrep.simxGetObjectHandle(clientID,'RShoulderRoll3#'+str(i),vrep.simx_opmode_oneshot_wait)[1])
        Body[21].append(vrep.simxGetObjectHandle(clientID,'RElbowYaw3#'+str(i),vrep.simx_opmode_oneshot_wait)[1])
        Body[22].append(vrep.simxGetObjectHandle(clientID,'RElbowRoll3#'+str(i),vrep.simx_opmode_oneshot_wait)[1])
        Body[23].append(vrep.simxGetObjectHandle(clientID,'RWristYaw3#'+str(i),vrep.simx_opmode_oneshot_wait)[1])
        #Left fingers
        print '-> Left Fingers for NAO : ' + str(i+2)
        Body[24].append(vrep.simxGetObjectHandle(clientID,'NAO_LThumbBase#'+str(i),vrep.simx_opmode_oneshot_wait)[1])
        Body[24].append(vrep.simxGetObjectHandle(clientID,'Revolute_joint8#'+str(i),vrep.simx_opmode_oneshot_wait)[1])
        Body[24].append(vrep.simxGetObjectHandle(clientID,'NAO_LLFingerBase#'+str(i),vrep.simx_opmode_oneshot_wait)[1])
        Body[24].append(vrep.simxGetObjectHandle(clientID,'Revolute_joint12#'+str(i),vrep.simx_opmode_oneshot_wait)[1])
        Body[24].append(vrep.simxGetObjectHandle(clientID,'Revolute_joint14#'+str(i),vrep.simx_opmode_oneshot_wait)[1])
        Body[24].append(vrep.simxGetObjectHandle(clientID,'NAO_LRFinger_Base#'+str(i),vrep.simx_opmode_oneshot_wait)[1])
        Body[24].append(vrep.simxGetObjectHandle(clientID,'Revolute_joint11#'+str(i),vrep.simx_opmode_oneshot_wait)[1])
        Body[24].append(vrep.simxGetObjectHandle(clientID,'Revolute_joint13#'+str(i),vrep.simx_opmode_oneshot_wait)[1])
        Body[25].append(Body[24][i*8:(i+1)*8])
        #Right Fingers
        print '-> Right Fingers for NAO : ' + str(i+2)
        Body[26].append(vrep.simxGetObjectHandle(clientID,'NAO_RThumbBase#'+str(i),vrep.simx_opmode_oneshot_wait)[1])
        Body[26].append(vrep.simxGetObjectHandle(clientID,'Revolute_joint0#'+str(i),vrep.simx_opmode_oneshot_wait)[1])
        Body[26].append(vrep.simxGetObjectHandle(clientID,'NAO_RLFingerBase#'+str(i),vrep.simx_opmode_oneshot_wait)[1])
        Body[26].append(vrep.simxGetObjectHandle(clientID,'Revolute_joint5#'+str(i),vrep.simx_opmode_oneshot_wait)[1])
        Body[26].append(vrep.simxGetObjectHandle(clientID,'Revolute_joint6#'+str(i),vrep.simx_opmode_oneshot_wait)[1])
        Body[26].append(vrep.simxGetObjectHandle(clientID,'NAO_RRFinger_Base#'+str(i),vrep.simx_opmode_oneshot_wait)[1])
        Body[26].append(vrep.simxGetObjectHandle(clientID,'Revolute_joint2#'+str(i),vrep.simx_opmode_oneshot_wait)[1])
        Body[26].append(vrep.simxGetObjectHandle(clientID,'Revolute_joint3#'+str(i),vrep.simx_opmode_oneshot_wait)[1])
        Body[27].append(Body[26][i*8:(i+1)*8])

#Get the Handles of all NAOs except the first one
def get_new_nao_handles(nbrOfNao,clientID,Body):
    for i in range(0, nbrOfNao-1):
        print '-> Head for NAO : '+ str(i+2)
        Body[0].append(vrep.simxGetObjectHandle(clientID,'HeadYaw#'+str(i),vrep.simx_opmode_oneshot_wait)[1])
        Body[1].append(vrep.simxGetObjectHandle(clientID,'HeadPitch#'+str(i),vrep.simx_opmode_oneshot_wait)[1])
        #Left Leg
        print '-> Left Leg for NAO : ' + str(i+2)
        Body[2].append(vrep.simxGetObjectHandle(clientID,'LHipYawPitch3#'+str(i),vrep.simx_opmode_oneshot_wait)[1])
        Body[3].append(vrep.simxGetObjectHandle(clientID,'LHipRoll3#'+str(i),vrep.simx_opmode_oneshot_wait)[1])
        Body[4].append(vrep.simxGetObjectHandle(clientID,'LHipPitch3#'+str(i),vrep.simx_opmode_oneshot_wait)[1])
        Body[5].append(vrep.simxGetObjectHandle(clientID,'LKneePitch3#'+str(i),vrep.simx_opmode_oneshot_wait)[1])
        Body[6].append(vrep.simxGetObjectHandle(clientID,'LAnklePitch3#'+str(i),vrep.simx_opmode_oneshot_wait)[1])
        Body[7].append(vrep.simxGetObjectHandle(clientID,'LAnkleRoll3#'+str(i),vrep.simx_opmode_oneshot_wait)[1])
        #Right Leg
        print '-> Right Leg for NAO : ' + str(i+2)
        Body[8].append(vrep.simxGetObjectHandle(clientID,'RHipYawPitch3#'+str(i),vrep.simx_opmode_oneshot_wait)[1])
        Body[9].append(vrep.simxGetObjectHandle(clientID,'RHipRoll3#'+str(i),vrep.simx_opmode_oneshot_wait)[1])
        Body[10].append(vrep.simxGetObjectHandle(clientID,'RHipPitch3#'+str(i),vrep.simx_opmode_oneshot_wait)[1])
        Body[11].append(vrep.simxGetObjectHandle(clientID,'RKneePitch3#'+str(i),vrep.simx_opmode_oneshot_wait)[1])
        Body[12].append(vrep.simxGetObjectHandle(clientID,'RAnklePitch3#'+str(i),vrep.simx_opmode_oneshot_wait)[1])
        Body[13].append(vrep.simxGetObjectHandle(clientID,'RAnkleRoll3#'+str(i),vrep.simx_opmode_oneshot_wait)[1])
        #Left Arm
        print '-> Left Arm for NAO : ' + str(i+2)
        Body[14].append(vrep.simxGetObjectHandle(clientID,'LShoulderPitch3#'+str(i),vrep.simx_opmode_oneshot_wait)[1])
        Body[15].append(vrep.simxGetObjectHandle(clientID,'LShoulderRoll3#'+str(i),vrep.simx_opmode_oneshot_wait)[1])
        Body[16].append(vrep.simxGetObjectHandle(clientID,'LElbowYaw3#'+str(i),vrep.simx_opmode_oneshot_wait)[1])
        Body[17].append(vrep.simxGetObjectHandle(clientID,'LElbowRoll3#'+str(i),vrep.simx_opmode_oneshot_wait)[1])
        Body[18].append(vrep.simxGetObjectHandle(clientID,'LWristYaw3#'+str(i),vrep.simx_opmode_oneshot_wait)[1])
        #Right Arm
        print '-> Right Arm for NAO : ' + str(i+2)
        Body[19].append(vrep.simxGetObjectHandle(clientID,'RShoulderPitch3#'+str(i),vrep.simx_opmode_oneshot_wait)[1])
        Body[20].append(vrep.simxGetObjectHandle(clientID,'RShoulderRoll3#'+str(i),vrep.simx_opmode_oneshot_wait)[1])
        Body[21].append(vrep.simxGetObjectHandle(clientID,'RElbowYaw3#'+str(i),vrep.simx_opmode_oneshot_wait)[1])
        Body[22].append(vrep.simxGetObjectHandle(clientID,'RElbowRoll3#'+str(i),vrep.simx_opmode_oneshot_wait)[1])
        Body[23].append(vrep.simxGetObjectHandle(clientID,'RWristYaw3#'+str(i),vrep.simx_opmode_oneshot_wait)[1])
        #Left fingers
        print '-> Left Fingers for NAO : ' + str(i+2)
        Body[24].append(vrep.simxGetObjectHandle(clientID,'NAO_LThumbBase#'+str(i),vrep.simx_opmode_oneshot_wait)[1])
        Body[24].append(vrep.simxGetObjectHandle(clientID,'Revolute_joint8#'+str(i),vrep.simx_opmode_oneshot_wait)[1])
        Body[24].append(vrep.simxGetObjectHandle(clientID,'NAO_LLFingerBase#'+str(i),vrep.simx_opmode_oneshot_wait)[1])
        Body[24].append(vrep.simxGetObjectHandle(clientID,'Revolute_joint12#'+str(i),vrep.simx_opmode_oneshot_wait)[1])
        Body[24].append(vrep.simxGetObjectHandle(clientID,'Revolute_joint14#'+str(i),vrep.simx_opmode_oneshot_wait)[1])
        Body[24].append(vrep.simxGetObjectHandle(clientID,'NAO_LRFinger_Base#'+str(i),vrep.simx_opmode_oneshot_wait)[1])
        Body[24].append(vrep.simxGetObjectHandle(clientID,'Revolute_joint11#'+str(i),vrep.simx_opmode_oneshot_wait)[1])
        Body[24].append(vrep.simxGetObjectHandle(clientID,'Revolute_joint13#'+str(i),vrep.simx_opmode_oneshot_wait)[1])
        Body[25].append(Body[24][i*8:(i+1)*8])
        #Right Fingers
        print '-> Right Fingers for NAO : ' + str(i+2)
        Body[26].append(vrep.simxGetObjectHandle(clientID,'NAO_RThumbBase#'+str(i),vrep.simx_opmode_oneshot_wait)[1])
        Body[26].append(vrep.simxGetObjectHandle(clientID,'Revolute_joint0#'+str(i),vrep.simx_opmode_oneshot_wait)[1])
        Body[26].append(vrep.simxGetObjectHandle(clientID,'NAO_RLFingerBase#'+str(i),vrep.simx_opmode_oneshot_wait)[1])
        Body[26].append(vrep.simxGetObjectHandle(clientID,'Revolute_joint5#'+str(i),vrep.simx_opmode_oneshot_wait)[1])
        Body[26].append(vrep.simxGetObjectHandle(clientID,'Revolute_joint6#'+str(i),vrep.simx_opmode_oneshot_wait)[1])
        Body[26].append(vrep.simxGetObjectHandle(clientID,'NAO_RRFinger_Base#'+str(i),vrep.simx_opmode_oneshot_wait)[1])
        Body[26].append(vrep.simxGetObjectHandle(clientID,'Revolute_joint2#'+str(i),vrep.simx_opmode_oneshot_wait)[1])
        Body[26].append(vrep.simxGetObjectHandle(clientID,'Revolute_joint3#'+str(i),vrep.simx_opmode_oneshot_wait)[1])
        Body[27].append(Body[26][(i+1)*8:(i+2)*8])


#Allow the joint to move in the VRep Simulation
def JointControl(clientID,i,Body, commandAngles):

    vrep.simxSetJointTargetPosition(clientID,Body[0][i],commandAngles[0],vrep.simx_opmode_streaming)
    vrep.simxSetJointTargetPosition(clientID,Body[1][i],commandAngles[1],vrep.simx_opmode_streaming)
    #Left Leg
    vrep.simxSetJointTargetPosition(clientID,Body[2][i],commandAngles[8],vrep.simx_opmode_streaming)
    vrep.simxSetJointTargetPosition(clientID,Body[3][i],commandAngles[9],vrep.simx_opmode_streaming)
    vrep.simxSetJointTargetPosition(clientID,Body[4][i],commandAngles[10],vrep.simx_opmode_streaming)
    vrep.simxSetJointTargetPosition(clientID,Body[5][i],commandAngles[11],vrep.simx_opmode_streaming)
    vrep.simxSetJointTargetPosition(clientID,Body[6][i],commandAngles[12],vrep.simx_opmode_streaming)
    vrep.simxSetJointTargetPosition(clientID,Body[7][i],commandAngles[13],vrep.simx_opmode_streaming)
    #Right Leg
    vrep.simxSetJointTargetPosition(clientID,Body[8][i],commandAngles[14],vrep.simx_opmode_streaming)
    vrep.simxSetJointTargetPosition(clientID,Body[9][i],commandAngles[15],vrep.simx_opmode_streaming)
    vrep.simxSetJointTargetPosition(clientID,Body[10][i],commandAngles[16],vrep.simx_opmode_streaming)
    vrep.simxSetJointTargetPosition(clientID,Body[11][i],commandAngles[17],vrep.simx_opmode_streaming)
    vrep.simxSetJointTargetPosition(clientID,Body[12][i],commandAngles[18],vrep.simx_opmode_streaming)
    vrep.simxSetJointTargetPosition(clientID,Body[13][i],commandAngles[19],vrep.simx_opmode_streaming)
    #Left Arm
    vrep.simxSetJointTargetPosition(clientID,Body[14][i],commandAngles[2],vrep.simx_opmode_streaming)
    vrep.simxSetJointTargetPosition(clientID,Body[15][i],commandAngles[3],vrep.simx_opmode_streaming)
    vrep.simxSetJointTargetPosition(clientID,Body[16][i],commandAngles[4],vrep.simx_opmode_streaming)
    vrep.simxSetJointTargetPosition(clientID,Body[17][i],commandAngles[5],vrep.simx_opmode_streaming)
    vrep.simxSetJointTargetPosition(clientID,Body[18][i],commandAngles[6],vrep.simx_opmode_streaming)
    #Right Arm
    vrep.simxSetJointTargetPosition(clientID,Body[19][i],commandAngles[20],vrep.simx_opmode_streaming)
    vrep.simxSetJointTargetPosition(clientID,Body[20][i],commandAngles[21],vrep.simx_opmode_streaming)
    vrep.simxSetJointTargetPosition(clientID,Body[21][i],commandAngles[22],vrep.simx_opmode_streaming)
    vrep.simxSetJointTargetPosition(clientID,Body[22][i],commandAngles[23],vrep.simx_opmode_streaming)
    vrep.simxSetJointTargetPosition(clientID,Body[23][i],commandAngles[24],vrep.simx_opmode_streaming)
    #Left Fingers
    vrep.simxSetJointTargetPosition(clientID,Body[25][i][0],1.0-commandAngles[7],vrep.simx_opmode_streaming)
    vrep.simxSetJointTargetPosition(clientID,Body[25][i][1],1.0-commandAngles[7],vrep.simx_opmode_streaming)
    vrep.simxSetJointTargetPosition(clientID,Body[25][i][2],1.0-commandAngles[7],vrep.simx_opmode_streaming)
    vrep.simxSetJointTargetPosition(clientID,Body[25][i][3],1.0-commandAngles[7],vrep.simx_opmode_streaming)
    vrep.simxSetJointTargetPosition(clientID,Body[25][i][4],1.0-commandAngles[7],vrep.simx_opmode_streaming)
    vrep.simxSetJointTargetPosition(clientID,Body[25][i][5],1.0-commandAngles[7],vrep.simx_opmode_streaming)
    vrep.simxSetJointTargetPosition(clientID,Body[25][i][6],1.0-commandAngles[7],vrep.simx_opmode_streaming)
    vrep.simxSetJointTargetPosition(clientID,Body[25][i][7],1.0-commandAngles[7],vrep.simx_opmode_streaming)
    #Right Fingers
    vrep.simxSetJointTargetPosition(clientID,Body[27][i][0],1.0-commandAngles[25],vrep.simx_opmode_streaming)
    vrep.simxSetJointTargetPosition(clientID,Body[27][i][1],1.0-commandAngles[25],vrep.simx_opmode_streaming)
    vrep.simxSetJointTargetPosition(clientID,Body[27][i][2],1.0-commandAngles[25],vrep.simx_opmode_streaming)
    vrep.simxSetJointTargetPosition(clientID,Body[27][i][3],1.0-commandAngles[25],vrep.simx_opmode_streaming)
    vrep.simxSetJointTargetPosition(clientID,Body[27][i][4],1.0-commandAngles[25],vrep.simx_opmode_streaming)
    vrep.simxSetJointTargetPosition(clientID,Body[27][i][5],1.0-commandAngles[25],vrep.simx_opmode_streaming)
    vrep.simxSetJointTargetPosition(clientID,Body[27][i][6],1.0-commandAngles[25],vrep.simx_opmode_streaming)
    vrep.simxSetJointTargetPosition(clientID,Body[27][i][7],1.0-commandAngles[25],vrep.simx_opmode_streaming)


#Get the Handle of only one NAO
def get_first_handles(clientID,Body):
    print '-> Head for NAO : '+ str(1)
    Body[0].append(vrep.simxGetObjectHandle(clientID,'HeadYaw#',vrep.simx_opmode_oneshot_wait)[1])
    Body[1].append(vrep.simxGetObjectHandle(clientID,'HeadPitch#',vrep.simx_opmode_oneshot_wait)[1])
    #Left Leg
    print '-> Left Leg for NAO : ' + str(1)
    Body[2].append(vrep.simxGetObjectHandle(clientID,'LHipYawPitch3#',vrep.simx_opmode_oneshot_wait)[1])
    Body[3].append(vrep.simxGetObjectHandle(clientID,'LHipRoll3#',vrep.simx_opmode_oneshot_wait)[1])
    Body[4].append(vrep.simxGetObjectHandle(clientID,'LHipPitch3#',vrep.simx_opmode_oneshot_wait)[1])
    Body[5].append(vrep.simxGetObjectHandle(clientID,'LKneePitch3#',vrep.simx_opmode_oneshot_wait)[1])
    Body[6].append(vrep.simxGetObjectHandle(clientID,'LAnklePitch3#',vrep.simx_opmode_oneshot_wait)[1])
    Body[7].append(vrep.simxGetObjectHandle(clientID,'LAnkleRoll3#',vrep.simx_opmode_oneshot_wait)[1])
    #Right Leg
    print '-> Right Leg for NAO : ' + str(1)
    Body[8].append(vrep.simxGetObjectHandle(clientID,'RHipYawPitch3#',vrep.simx_opmode_oneshot_wait)[1])
    Body[9].append(vrep.simxGetObjectHandle(clientID,'RHipRoll3#',vrep.simx_opmode_oneshot_wait)[1])
    Body[10].append(vrep.simxGetObjectHandle(clientID,'RHipPitch3#',vrep.simx_opmode_oneshot_wait)[1])
    Body[11].append(vrep.simxGetObjectHandle(clientID,'RKneePitch3#',vrep.simx_opmode_oneshot_wait)[1])
    Body[12].append(vrep.simxGetObjectHandle(clientID,'RAnklePitch3#',vrep.simx_opmode_oneshot_wait)[1])
    Body[13].append(vrep.simxGetObjectHandle(clientID,'RAnkleRoll3#',vrep.simx_opmode_oneshot_wait)[1])
    #Left Arm
    print '-> Left Arm for NAO : ' + str(1)
    Body[14].append(vrep.simxGetObjectHandle(clientID,'LShoulderPitch3#',vrep.simx_opmode_oneshot_wait)[1])
    Body[15].append(vrep.simxGetObjectHandle(clientID,'LShoulderRoll3#',vrep.simx_opmode_oneshot_wait)[1])
    Body[16].append(vrep.simxGetObjectHandle(clientID,'LElbowYaw3#',vrep.simx_opmode_oneshot_wait)[1])
    Body[17].append(vrep.simxGetObjectHandle(clientID,'LElbowRoll3#',vrep.simx_opmode_oneshot_wait)[1])
    Body[18].append(vrep.simxGetObjectHandle(clientID,'LWristYaw3#',vrep.simx_opmode_oneshot_wait)[1])
    #Right Arm
    print '-> Right Arm for NAO : ' + str(1)
    Body[19].append(vrep.simxGetObjectHandle(clientID,'RShoulderPitch3#',vrep.simx_opmode_oneshot_wait)[1])
    Body[20].append(vrep.simxGetObjectHandle(clientID,'RShoulderRoll3#',vrep.simx_opmode_oneshot_wait)[1])
    Body[21].append(vrep.simxGetObjectHandle(clientID,'RElbowYaw3#',vrep.simx_opmode_oneshot_wait)[1])
    Body[22].append(vrep.simxGetObjectHandle(clientID,'RElbowRoll3#',vrep.simx_opmode_oneshot_wait)[1])
    Body[23].append(vrep.simxGetObjectHandle(clientID,'RWristYaw3#',vrep.simx_opmode_oneshot_wait)[1])
    #Left fingers
    print '-> Left Fingers for NAO : ' + str(1)
    Body[24].append(vrep.simxGetObjectHandle(clientID,'NAO_LThumbBase#',vrep.simx_opmode_oneshot_wait)[1])
    Body[24].append(vrep.simxGetObjectHandle(clientID,'Revolute_joint8#',vrep.simx_opmode_oneshot_wait)[1])
    Body[24].append(vrep.simxGetObjectHandle(clientID,'NAO_LLFingerBase#',vrep.simx_opmode_oneshot_wait)[1])
    Body[24].append(vrep.simxGetObjectHandle(clientID,'Revolute_joint12#',vrep.simx_opmode_oneshot_wait)[1])
    Body[24].append(vrep.simxGetObjectHandle(clientID,'Revolute_joint14#',vrep.simx_opmode_oneshot_wait)[1])
    Body[24].append(vrep.simxGetObjectHandle(clientID,'NAO_LRFinger_Base#',vrep.simx_opmode_oneshot_wait)[1])
    Body[24].append(vrep.simxGetObjectHandle(clientID,'Revolute_joint11#',vrep.simx_opmode_oneshot_wait)[1])
    Body[24].append(vrep.simxGetObjectHandle(clientID,'Revolute_joint13#',vrep.simx_opmode_oneshot_wait)[1])
    Body[25].append(Body[24][0:8])
    #Right Fingers
    print '-> Right Fingers for NAO : ' + str(1)
    Body[26].append(vrep.simxGetObjectHandle(clientID,'NAO_RThumbBase#',vrep.simx_opmode_oneshot_wait)[1])
    Body[26].append(vrep.simxGetObjectHandle(clientID,'Revolute_joint0#',vrep.simx_opmode_oneshot_wait)[1])
    Body[26].append(vrep.simxGetObjectHandle(clientID,'NAO_RLFingerBase#',vrep.simx_opmode_oneshot_wait)[1])
    Body[26].append(vrep.simxGetObjectHandle(clientID,'Revolute_joint5#',vrep.simx_opmode_oneshot_wait)[1])
    Body[26].append(vrep.simxGetObjectHandle(clientID,'Revolute_joint6#',vrep.simx_opmode_oneshot_wait)[1])
    Body[26].append(vrep.simxGetObjectHandle(clientID,'NAO_RRFinger_Base#',vrep.simx_opmode_oneshot_wait)[1])
    Body[26].append(vrep.simxGetObjectHandle(clientID,'Revolute_joint2#',vrep.simx_opmode_oneshot_wait)[1])
    Body[26].append(vrep.simxGetObjectHandle(clientID,'Revolute_joint3#',vrep.simx_opmode_oneshot_wait)[1])
    Body[27].append(Body[26][0:8])



def get_joint_values(clientID,Body):
    i = 0
    angles = [0] * 25
    angles[0] =  vrep.simxGetJointPosition(clientID,Body[0][i],vrep.simx_opmode_oneshot_wait)[1]
    angles[1] = vrep.simxGetJointPosition(clientID,Body[1][i], vrep.simx_opmode_oneshot_wait)[1]
    #Left Leg
    angles[8] = vrep.simxGetJointPosition(clientID,Body[2][i],vrep.simx_opmode_oneshot_wait)[1]
    angles[9] = vrep.simxGetJointPosition(clientID,Body[3][i],vrep.simx_opmode_oneshot_wait)[1]
    angles[10] = vrep.simxGetJointPosition(clientID,Body[4][i],vrep.simx_opmode_oneshot_wait)[1]
    angles[11] = vrep.simxGetJointPosition(clientID,Body[5][i],vrep.simx_opmode_oneshot_wait)[1]
    angles[12] = vrep.simxGetJointPosition(clientID,Body[6][i],vrep.simx_opmode_oneshot_wait)[1]
    angles[13] = vrep.simxGetJointPosition(clientID,Body[7][i],vrep.simx_opmode_oneshot_wait)[1]
    #Right Leg
    angles[14] = vrep.simxGetJointPosition(clientID,Body[8][i],vrep.simx_opmode_oneshot_wait)[1]
    angles[15] = vrep.simxGetJointPosition(clientID,Body[9][i],vrep.simx_opmode_oneshot_wait)[1]
    angles[16] = vrep.simxGetJointPosition(clientID,Body[10][i],vrep.simx_opmode_oneshot_wait)[1]
    angles[17] = vrep.simxGetJointPosition(clientID,Body[11][i],vrep.simx_opmode_oneshot_wait)[1]
    angles[18] =vrep.simxGetJointPosition(clientID,Body[12][i],vrep.simx_opmode_oneshot_wait)[1]
    angles[19] =vrep.simxGetJointPosition(clientID,Body[13][i],vrep.simx_opmode_oneshot_wait)[1]
    #Left Arm
    angles[2] = vrep.simxGetJointPosition(clientID,Body[14][i],vrep.simx_opmode_oneshot_wait)[1]
    angles[3] =vrep.simxGetJointPosition(clientID,Body[15][i],vrep.simx_opmode_oneshot_wait)[1]
    angles[4] = vrep.simxGetJointPosition(clientID,Body[16][i],vrep.simx_opmode_oneshot_wait)[1]
    angles[5] = vrep.simxGetJointPosition(clientID,Body[17][i],vrep.simx_opmode_oneshot_wait)[1]
    angles[6] =vrep.simxGetJointPosition(clientID,Body[18][i],vrep.simx_opmode_oneshot_wait)[1]
    #Right Arm
    angles[20] = vrep.simxGetJointPosition(clientID,Body[19][i],vrep.simx_opmode_oneshot_wait)[1]
    angles[21] = vrep.simxGetJointPosition(clientID,Body[20][i],vrep.simx_opmode_oneshot_wait)[1]
    angles[22] = vrep.simxGetJointPosition(clientID,Body[21][i],vrep.simx_opmode_oneshot_wait)[1]
    angles[23] = vrep.simxGetJointPosition(clientID,Body[22][i],vrep.simx_opmode_oneshot_wait)[1]
    angles[24] = vrep.simxGetJointPosition(clientID,Body[23][i],vrep.simx_opmode_oneshot_wait)[1]
    #angles[7] = 1.0 - vrep.simxGetJointPosition(clientID,Body[25][i][0],vrep.simx_opmode_oneshot_wait)[1]
    #angles[25] = 1.0 - vrep.simxGetJointPosition(clientID,Body[25][i][0],vrep.simx_opmode_oneshot_wait)[1]


    return angles
