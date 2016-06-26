# Obtem a posicao das juntas do robo nao
from naoqi import ALProxy
import time

from manage_joints import *


DEFAULT_FILE_TO_WRITE = "robot_training_data"
DEFAULT_QTD_OF_MOVEMENTS = 10000

naoIP = '127.0.0.1'
naoPort = 59193
motionProxy = ALProxy("ALMotion",naoIP, naoPort)
postureProxy = ALProxy("ALRobotPosture", naoIP, naoPort)
posture = 'StandZero'



postureProxy.goToPosture(posture,1.0)

f = file(DEFAULT_FILE_TO_WRITE, 'w')
motionProxy.moveToward(1,0,0)

for i in range(0, DEFAULT_QTD_OF_MOVEMENTS):
    angles = motionProxy.getAngles('Body', False)
    line = ' '.join(str(x) for x in [i] + angles) + '\n'
    time.sleep(0.1)
    f.write(line)
    print line

f.close()
