import rospy
from std_msgs.msg import String
from naoqi import ALProxy
import tts
import simpleWalk
import moveHead
import standby
import stand 
import moveArm
def callback(data):
	tokens = data.data.split(' ')
	if tokens[0] == "tts":
		tts.main(tokens[1]) 
	elif tokens[0] == "simpleWalk": 
		simpleWalk.main(int(tokens[1]))
	elif tokens[0] == "moveHead":
		moveHead.main(tokens[1],tokens[2],tokens[3])
	elif tokens[0] == "standby":
		standby.main()
	elif tokens[0] == "stand":
		stand.main()
	elif tokens[0] == "moveArm":
		moveArm.main(tokens[1],tokens[2],tokens[3], tokens[4],tokens[5])
		
		

def listener():

	# In ROS, nodes are uniquely named. If two nodes with the same
	# node are launched, the previous one is kicked off. The
	# anonymous=True flag means that rospy will choose a unique
	# name for our 'listener' node so that multiple listeners can
	# run simultaneously.
	rospy.init_node('listener', anonymous=True)

	rospy.Subscriber("robot_control", String, callback)

	# spin() simply keeps python from exiting until this node is stopped
	rospy.spin()

if __name__ == '__main__':
	listener()
