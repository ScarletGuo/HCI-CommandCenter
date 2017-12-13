import sys
import time
import math
import motion 
from naoqi import ALProxy



def stiffnessOn(proxy):
    # We use the "Body" name to signify the collection of all joints
    pNames = "Body"
    pStiffnessLists = 1.0
    pTimeLists = 1.0
    proxy.stiffnessInterpolation(pNames, pStiffnessLists, pTimeLists)





def main(side,f,s,t,l):
    # Init proxies.
    try:
        motionProxy = ALProxy("ALMotion", "192.168.1.201", 9559)
    except Exception, e:
        print "Could not create proxy to ALMotion"
        print "Error was: ", e


    try:
        postureProxy = ALProxy("ALRobotPosture", "192.168.1.201", 9559)
    except Exception, e:
        print "Could not create proxy to ALRobotPosture"
        print "Error was: ", e


    # Set NAO in Stiffness On

    stiffnessOn(motionProxy)



    # Send NAO to Pose Init

    postureProxy.goToPosture("StandInit", 0.5)



    leftJointNames = ["LShoulderPitch", "LShoulderRoll", "LElbowYaw", "LElbowRoll"]
    rightJointNames = ["RShoulderPitch", "RShoulderRoll", "RElbowYaw", "RElbowRoll"]


    Arm1 = [float(f), float(s), float(t), float(l)]

    Arm1 = [ x * motion.TO_RAD for x in Arm1] 
    speed = 0.6

    if side == "l" :
  	  motionProxy.angleInterpolationWithSpeed(leftJointNames, Arm1, speed)
    elif side == "r":
	  motionProxy.angleInterpolationWithSpeed(rightJointNames, Arm1, speed)


    time.sleep(2.0)












