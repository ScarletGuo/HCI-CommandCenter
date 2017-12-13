# -*- encoding: UTF-8 -*- 

''' Whole Body Motion: Head orientation control '''

import sys
import time
import math
from naoqi import ALProxy


def StiffnessOn(proxy):
    # We use the "Body" name to signify the collection of all joints
    pNames = "Body"
    pStiffnessLists = 1.0
    pTimeLists = 1.0
    proxy.stiffnessInterpolation(pNames, pStiffnessLists, pTimeLists)


def main():
    ''' Example of a whole body head orientation control
        Warning: Needs a PoseInit before executing
                 Whole body balancer must be inactivated at the end of the script
    '''
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
    StiffnessOn(motionProxy)

    # Send NAO to Pose Init
    postureProxy.goToPosture("StandInit", 0.5)

   


if __name__ == "__main__":
    robotIp = "192.168.1.201"

    if len(sys.argv) <= 1:
        print "Usage python motion_wbEffectorControlHead.py robotIP (optional default: 127.0.0.1)"
    else:
        robotIp = sys.argv[1]

    main()

