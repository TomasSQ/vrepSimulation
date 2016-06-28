# Executa um arquivo de entrada enviando comandos para as juntas
# o arquivo eh esperado no formato gerado pelo arquivo obtain_training_data.py
import vrep
import time

from manage_joints import *
import argparse

# Valores default
DEFAULT_VREP_HOST = ['127.0.0.1']
DEFAULT_VREP_PORT = [19997]
DEFAULT_FILE = ["training_data.txt"]

# Parser dos comandos
parser = argparse.ArgumentParser(description='Movimenta o robo de acordo com os dados de duas redes neurais')
parser.add_argument('--file', '-F', nargs = 1, default = DEFAULT_FILE,
                    help='Arquivo com os movimentos para o robo executar')
parser.add_argument('--host', '-H', nargs = 1, default = DEFAULT_VREP_HOST,
                    help='Host VREP')
parser.add_argument('--port', '-P', nargs = 1, default = DEFAULT_VREP_PORT,
                    help='Porta VREP')






if __name__ == '__main__':
    args = parser.parse_args()
    [file_name] = args.file
    host = args.host[0]
    port = args.port[0]


    vrep.simxFinish(-1)

    clientID = vrep.simxStart(host,port,True,True,5000,5) # Connecta com o VREP. Por padrao ele ja abre essa porta.
    if clientID == -1:
        print "Could not connect on VREP"
        exit (10)



    Head_Yaw=[];Head_Pitch=[];
    L_Hip_Yaw_Pitch=[];L_Hip_Roll=[];L_Hip_Pitch=[];L_Knee_Pitch=[];L_Ankle_Pitch=[];L_Ankle_Roll=[];
    R_Hip_Yaw_Pitch=[];R_Hip_Roll=[];R_Hip_Pitch=[];R_Knee_Pitch=[];R_Ankle_Pitch=[];R_Ankle_Roll=[];
    L_Shoulder_Pitch=[];L_Shoulder_Roll=[];L_Elbow_Yaw=[];L_Elbow_Roll=[];L_Wrist_Yaw=[]
    R_Shoulder_Pitch=[];R_Shoulder_Roll=[];R_Elbow_Yaw=[];R_Elbow_Roll=[];R_Wrist_Yaw=[]
    R_H=[];L_H=[];R_Hand=[];L_Hand=[];
    Body = [Head_Yaw,Head_Pitch,L_Hip_Yaw_Pitch,L_Hip_Roll,L_Hip_Pitch,L_Knee_Pitch,L_Ankle_Pitch,L_Ankle_Roll,R_Hip_Yaw_Pitch,R_Hip_Roll,R_Hip_Pitch,R_Knee_Pitch,R_Ankle_Pitch,R_Ankle_Roll,L_Shoulder_Pitch,L_Shoulder_Roll,L_Elbow_Yaw,L_Elbow_Roll,L_Wrist_Yaw,R_Shoulder_Pitch,R_Shoulder_Roll,R_Elbow_Yaw,R_Elbow_Roll,R_Wrist_Yaw,L_H,L_Hand,R_H,R_Hand]

    get_all_handles(3, clientID,Body)


    f = file(file_name)

    time.sleep(10) # tempo para gravar :)

    print "Starting simulation..."
    for line in f:
        split_line = line.split(' ')
        to_float = [float(x) for x in split_line[1:]]
        JointControl(clientID, 0, Body, to_float)
        time.sleep(0.1)


    f.close()
