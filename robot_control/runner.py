import rospy
from naoqi import ALProxy
from std_msgs.msg import String
    
def talker():
	pub = rospy.Publisher('chatter', String, queue_size=10)
	rospy.init_node('talker', anonymous=True)
	rate = rospy.Rate(10) # 10hz
	tts = ALProxy("ALTextToSpeech", "192.168.1.201", 9559)
	tts.setLanguage("English")
	tts.say("Hello World")


	while not rospy.is_shutdown():
		hello_str = "hello world %s" % rospy.get_time()
		rospy.loginfo(hello_str)
		pub.publish(hello_str)
		rate.sleep()

if __name__ == '__main__':
	try:
		talker()
	except rospy.ROSInterruptException:
		pass
	
