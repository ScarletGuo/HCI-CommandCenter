import rospy
from std_msgs.msg import String
from naoqi import ALProxy
import sys
import motion
import time
def StiffnessOn(proxy):
    # We use the "Body" name to signify the collection of all joints
    pNames =  "Body"
    pStiffnessLists = 1.0
    pTimeLists = 1.0
    proxy.stiffnessInterpolation(pNames, pStiffnessLists, pTimeLists)


def main(steps):
	robotIP = "192.168.1.201"
   	try:
	        motionProxy = ALProxy("ALMotion", robotIP, 9559)
   	except Exception, e:
        	print "Could not create proxy to ALMotion"
        	print "Error was: ", e

	try:
        	postureProxy = ALProxy("ALRobotPosture", robotIP, 9559)
    	except Exception, e:
        	print "Could not create proxy to ALRobotPosture"
        	print "Error was: ", e

	counter = 0
	while counter < steps:
		# Set NAO in Stiffness On
		StiffnessOn(motionProxy)

	    	# Send NAO to Pose Init
		postureProxy.goToPosture("StandInit", 0.5)

	  	#####################
	    	## Enable arms control by Walk algorithm
	    	#####################
	    	motionProxy.setWalkArmsEnabled(True, True)
	    	#~ motionProxy.setWalkArmsEnabled(False, False)

		#####################	
		## FOOT CONTACT PROTECTION
		#####################
		#~ motionProxy.setMotionConfig([["ENABLE_FOOT_CONTACT_PROTECTION", False]])
		motionProxy.setMotionConfig([["ENABLE_FOOT_CONTACT_PROTECTION", True]])

		#TARGET VELOCITY
		X = -0.5  #backward
		Y = 0.0
		Theta = 0.0
		Frequency =0.0 # low speed
		motionProxy.setWalkTargetVelocity(X, Y, Theta, Frequency)

		time.sleep(4.0)

		#TARGET VELOCITY
		X = 0.8
		Y = 0.0
		Theta = 0.0
		Frequency =1.0 # max speed
		motionProxy.setWalkTargetVelocity(X, Y, Theta, Frequency)

		time.sleep(4.0)

		#TARGET VELOCITY
		X = 0.2
		Y = -0.5
		Theta = 0.2
		Frequency =1.0
		motionProxy.setWalkTargetVelocity(X, Y, Theta, Frequency)

		time.sleep(2.0)

	
		#####################
		## End Walk
		#####################
		#TARGET VELOCITY
		X = 0.0
		Y = 0.0
		Theta = 0.0
		motionProxy.setWalkTargetVelocity(X, Y, Theta, Frequency)	
		time.sleep(2.0)
		counter += 1
