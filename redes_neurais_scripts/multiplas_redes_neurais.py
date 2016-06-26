# Usa duas redes neurais para movimentar o robo
#
import numpy as np
import cPickle as pickle
import vrep
import time

from manage_joints import *
import argparse

# Valores default
DEFAULT_COMMANDS_PER_NEURAL_NETWORK = [15, 10000]
DEFAULT_VREP_HOST = ['127.0.0.1']
DEFAULT_VREP_PORT = [19997]
DEFAULT_FILES = ['model_1_training_data_1_500_sample_01_random.txt_3_hidden_600_epochs_without_i.pkl', 'model_1_training_data_1_2999_sample_01_random.txt_10_hidden_600_epochs_without_i.pkl']

# Parser dos comandos
parser = argparse.ArgumentParser(description='Movimenta o robo de acordo com os dados de duas redes neurais')
parser.add_argument('--files', '-T', nargs = 2, default = DEFAULT_FILES,
                    help='Arquivos com as redes neurais serializadas')
parser.add_argument('--commands-per-neural-network', '-C',  nargs = 2, type  = int, default = DEFAULT_COMMANDS_PER_NEURAL_NETWORK,
                    help='Quantidade de comandos dados usando cada uma das redes neurais')
parser.add_argument('--host', '-H', nargs = 1, default = DEFAULT_VREP_HOST,
                    help='Host VREP')
parser.add_argument('--port', '-P', nargs = 1, default = DEFAULT_VREP_PORT,
                    help='Porta VREP')




if __name__ == '__main__':
    args = parser.parse_args()
    [first_file, second_file] = args.files
    # Deserializa as redes neurais
    first_net = pickle.load(open(first_file,'rb'))
    second_net = pickle.load(open(second_file,'rb'))

    host = args.host[0]
    port = args.port[0]
    [first_net_moves, second_net_moves] = args.commands_per_neural_network


    vrep.simxFinish(-1)

    clientID = vrep.simxStart(host,port,True,True,5000,5) # Connecta com o VREP. Por padrao ele ja abre essa porta.
    if clientID == -1:
        print "Could not connect on VREP"
        exit (10)


    # Obtem os handlers
    Head_Yaw=[];Head_Pitch=[];
    L_Hip_Yaw_Pitch=[];L_Hip_Roll=[];L_Hip_Pitch=[];L_Knee_Pitch=[];L_Ankle_Pitch=[];L_Ankle_Roll=[];
    R_Hip_Yaw_Pitch=[];R_Hip_Roll=[];R_Hip_Pitch=[];R_Knee_Pitch=[];R_Ankle_Pitch=[];R_Ankle_Roll=[];
    L_Shoulder_Pitch=[];L_Shoulder_Roll=[];L_Elbow_Yaw=[];L_Elbow_Roll=[];L_Wrist_Yaw=[]
    R_Shoulder_Pitch=[];R_Shoulder_Roll=[];R_Elbow_Yaw=[];R_Elbow_Roll=[];R_Wrist_Yaw=[]
    R_H=[];L_H=[];R_Hand=[];L_Hand=[];
    Body = [Head_Yaw,Head_Pitch,L_Hip_Yaw_Pitch,L_Hip_Roll,L_Hip_Pitch,L_Knee_Pitch,L_Ankle_Pitch,L_Ankle_Roll,R_Hip_Yaw_Pitch,R_Hip_Roll,R_Hip_Pitch,R_Knee_Pitch,R_Ankle_Pitch,R_Ankle_Roll,L_Shoulder_Pitch,L_Shoulder_Roll,L_Elbow_Yaw,L_Elbow_Roll,L_Wrist_Yaw,R_Shoulder_Pitch,R_Shoulder_Roll,R_Elbow_Yaw,R_Elbow_Roll,R_Wrist_Yaw,L_H,L_Hand,R_H,R_Hand]

    get_all_handles(3, clientID,Body)

    # Um pequeno intervalo para comecar
    time.sleep(10)

    print "Starting simulation..."

    # Executa os primeiros comandos utilizando a primeira rede lida
    for i in range(first_net_moves):
        sensors =  get_joint_values(clientID,Body)
        sensors += [0.0] * (26 - len(sensors))
        mov = first_net.activate(sensors)

        JointControl(clientID, 0, Body, mov)
        time.sleep(0.01)

    #executa os proximos comandos coma segunda rede
    for i in range(second_net_moves):
        sensors =  get_joint_values(clientID,Body)
        sensors += [0.0] * (26 - len(sensors))
        mov = second_net.activate(sensors)

        JointControl(clientID, 0, Body, mov)
        time.sleep(0.01)
