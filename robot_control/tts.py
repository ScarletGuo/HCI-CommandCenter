import rospy
from std_msgs.msg import String
from naoqi import ALProxy

def main(data):
	rospy.loginfo(rospy.get_caller_id() + "I heard %s", data)
	tts = ALProxy("ALTextToSpeech", "192.168.1.201", 9559)
	tts.setLanguage("English")
	tts.say(data)
