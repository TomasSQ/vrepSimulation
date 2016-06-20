from naoqi import ALProxy
import time

from manage_joints import *


naoIP = '127.0.0.1'
naoPort = 55830
motionProxy = ALProxy("ALMotion",naoIP, naoPort)
postureProxy = ALProxy("ALRobotPosture", naoIP, naoPort)
posture = 'StandZero'



postureProxy.goToPosture(posture,1.0)

f = file('training_data2.txt', 'w')
motionProxy.moveToward(1,0,0)

for i in range(0, 50000):
    angles = motionProxy.getAngles('Body', False)
    line = ' '.join(str(x) for x in [i] + angles) + '\n'
    f.write(line)
    print line

f.close()
