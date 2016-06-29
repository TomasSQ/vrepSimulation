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

DEBUG = False

GENOME = [-0.18532508327941266, -0.39377839520630287, 0.2544114205720458, -0.20660291084641602, 0.04304821950072735, -0.2291248929985723, -0.2617618447795159, 0.34137323903475236, 0.07368537299935063, -0.3667244112493151, 0.08027249462917274, 0.037899668700874245, 0.3620183301416051, -0.20336018992231342, -0.18942987046061732, -0.29621325036397694, 0.2006988401263613, -0.05110159605552467, -0.023574927522250988, -0.28921640488469746, -0.33650670319740417, -0.325089075236195, -0.3960155939540082, 0.16451829213582025, 0.4577281864467505, 0.11637454796531355, 0.4246244034851724, -0.11136995896762258, 0.26572636431535346, -0.3741868391682418, 0.0879232222445182, 0.173736085715557, 0.39711610376445916, 0.17035836965330797, -0.15936938344340212, -0.05931181278608155, -0.49622691435393784, 0.25890063549177933, -0.11736996360695062, -0.13126745864806277, 0.05028807520936307, 0.31902978537750126, -0.22197985339266812, -0.3245914288983681, 0.12628743630170602, 0.012192775008681767, 0.09222766006533478, 0.07812510929253391, -0.497838341274243, -0.13275211704955103, -0.025244973157201422, 0.33057349391649415, -0.2714748237678877, -0.05209652759767536, 0.2229177917291325, 0.28577801122761193, 0.3666308332255561, -0.03492975431085954, -0.4139659506623221, -0.1446150388526697, -0.3625374019400769, -0.13401975026277024, -0.18037134006789846, 0.11601477455171916, 0.028932169431598154, -0.3892435149677812, -0.29373713061930906, -0.4571120252315213, -0.28802479507621703, 0.29595846117287994, -0.4380989948175018, -0.48151130287758637, 0.460890411698204, 0.4066819398836823, -0.31344149306161717, 0.25516337511622333, -0.08935157814915506, 0.1625784073818679, -0.33251289975889975, 0.4671940188765894, 0.4644818666945797, -0.22054572967732344, -0.02443578422345105, -0.45937615846308677, -0.376093805741782, -0.22613012194261262, -0.3127372965854135, 0.03971380552691406, -0.33153556301956666, -0.26030510448223687, 0.48351777052988953, 0.09536384674285692, 0.02149909834822361, -0.4538117908257744, 0.37184112999905916, -0.2095726304841663, 0.27003075029045365, -0.2546003780226249, 0.26682668895026307, 0.4626730238833697, 0.2950807354348657, -0.3629890436312394, 0.4735490754412218, 0.1866752984082285, -0.32434436053141724, 0.49883370488709633, 0.12920151932561585, -0.10170971570258036, 0.3070243786888658, 0.3353735651838361, 0.020132441331004003, -0.17441575168548484, 0.3502337282080099, 0.2662928314303029, -0.3595432056876703, 0.3539903743216064, -0.02878867352205261, -0.27527313041726453, -0.07709298806007991, 0.02140975524743227, -0.25848151333998703, 0.17641317984998328, -0.23036663691580028, -0.07348675246184366, -0.3970065555673551, 0.302359425551329, -0.47759200101996624, -0.2643927276661081, 0.15454229567213684, 0.3657935277748072, 0.16771160231129667, 0.18813074333048851, -0.4185273695082423, -0.10403396617999938, 0.48233605367015864, 0.42534881556830395, 0.3993046058955235, -0.018051327363096337, -0.09445440063611255, -0.4865593918181291, -0.36396011122085536, -0.1359510373669628, 0.30582555104361064, 0.4929119524124711, 0.26082674092731584, 0.021673167224745993, 0.13128419208878095, -0.4999932298985662, -0.10068504892203578, -0.02033376058188896, 0.029279218572086485, -0.21659750432276437, -0.4546575815850439, -0.24534520729921627, -0.16928938628589285, -0.38707375611916583, 0.03576450279051635, 0.005660030085889778, -0.0912879087444336, 0.2309015045841849, -0.4561147482836061, -0.47788815391761885, 0.47839845260913694, -0.2140258458139337, 0.4397006483159197, -0.024859101624531976, -0.3511614478699472, 0.13454229419707575, 0.10908227576924134, 0.31747911159247555, 0.29224208362008963, 0.48707361638211943, 0.29959527050581636, -0.2439132797145347, -0.0982903025239461, -0.11820372806759616, 0.44028285019346125, -0.023179373164665673, -0.2358010419096409, -0.35709362365483766, -0.2227485337878875, -0.36913978636291767, -0.10427431698875855, -0.11963895941479963, 0.4854682225550192, 0.40892161134825145, -0.2758926161929217, 0.32236836689486437, -0.019314715993913212, 0.005467448471417002, 0.25132971563483075, 0.17397577152903243, 0.2890036010425756, -0.12539795624524896, -0.4928408892632693, -0.11236678055027893, -0.08551385354998164, 0.42898661502249646, 0.45566328150116253, 0.2181529437849471, 0.2983415091504388, 0.13366509239070512, 0.2957248776671102, -0.2207253385604152, -0.22648024974932202, 0.3198552909705027, -0.3152689907206324, -0.21997004756871774, -0.4777214692662527, 0.4271742049700904, -0.4189799513388922, -0.00843131043809009, -0.25230213405560287, 0.1997323506516555, -0.27194498474343265, -0.1268181850378871, -0.31693921745433995, -0.19772193643702962, -0.315850888161066, -0.48266867060276675, -0.28399728559656234, 0.4235914538740253, -0.025518246829356106, -0.10561304645915759, 0.025129431477411646, 0.3427127250827535, 0.3769243094486253, 0.4854051318823226, -0.2322920306845403, 0.2504268499448804, 0.3042141873502614, 0.38008796146376067, -0.095535361451347, 0.1531787287249523, -0.33865470497536143, -0.1640207842778898, -0.24350064521954962, 0.4733054675448607, 0.38229901060622096, 0.019089604626691292, 0.2683176044770803, 0.38344356514755285, -0.465191672007806, -0.20783737788079037, 0.49627705672045486, -0.36626272568891793, -0.38284112524802283, -0.3748253816190832, 0.2610145545506196, -0.48577905104849206, -0.42462459992440693, -0.25218393293478736, -0.139007556939706, 0.2929862258051026, 0.4098702822625149, -0.3434172606061092, 0.2755637886694906, -0.4510056490044133, 0.39455354471238346, 0.23617425371436662, 0.08064558628652285, -0.12387567039636915, -0.3159211051032137, -0.4497403365801351, -0.2395629506722884, -0.19113171108862115, 0.040815890559229184, 0.41267588452929216, -0.46490779144831507, 0.11467704864734218, 0.22082162675283412, 0.2936825645044454, 0.2011398556114723, -0.40802544532301965, -0.33193850220845733, 0.1286390519523677, 0.056670144772524855, -0.4837497979752515, -0.41579238294986975, 0.10374417874073916, -0.37981293270379224, -0.31150569808331174, -0.08826331953559663, 0.3259504631469772, -0.48973217151037074, -0.46390897805548736, -0.018875221771957662, 0.05982590977098934, -0.26603613385165614, -0.4479061684822908, -0.04985594731963083, -0.03540284490732837, 0.3022525235957009, 0.46418144339571443, -0.4956970280281562, -0.46348513396490143, 0.3362067916514744, 0.26837366471895185, 0.06342007544309358, -0.4966438076453631, 0.35816982888922466, 0.4334213865732034, 0.2311500732560644, 0.18227220628559626, -0.05525014191068245, -0.11376288904976473, -0.08064055795379077, -0.23589699564757616, -0.31282152481545233, -0.22981512328176812, -0.32524499611330115, 0.06464056491967196, 0.31308970291360727, 0.4864329511454992, -0.04973138430467472, -0.45813119219863885, -0.3745345612978658, -0.43925511073014323, 0.2970093546136202, -0.44047997337456535, 0.05099157724021064, -0.009746088786070972, -0.23467225818131665, -0.1450133747456931, -0.23120783524066701, 0.025892025404818053, -0.333564706911353, -0.02738653463067242, 0.16901304191566358, 0.4053452232009457, 0.3922236512072095, 0.19075839607888023, -0.29591802599857886, -0.48854200189366725, -0.4237042229115284, -0.23181575828556034]
N_COEF = 5
JOINT_SIZE = 2 * N_COEF + 2
INTERVAL = 0.05 #50ms

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
    dt = 0

    while True:
        joint_movements = []

        for i in xrange(len(Body)):
            coefs = individual[i * JOINT_SIZE:(i + 1) * JOINT_SIZE]
            joint_movements.append(truncated_Fourier(coefs, dt)*control_joints[i])

        JointControl2(clientID, 0, Body, joint_movements)

        time.sleep(INTERVAL)
        dt += INTERVAL

def main():
    reset_simulation(clientID)
    move_robot(GENOME)

    print("   The Walker: %s"% tools.selBest(pop, k = 1))

if __name__ == "__main__":
    main()
