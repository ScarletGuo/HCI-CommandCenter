
import argparse
from naoqi import ALProxy

def main():
    motionProxy  = ALProxy("ALMotion", "192.168.1.201", 9559)
    postureProxy = ALProxy("ALRobotPosture", "192.168.1.201", 9559)

    # Wake up robot
    motionProxy.wakeUp()

    # Send robot to Pose Init
    postureProxy.goToPosture("StandInit", 0.5)

    # Go to rest position
    motionProxy.rest()

    # print motion state
    print motionProxy.getSummary()


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--ip", type=str, default="192.168.1.201",
                        help="Robot ip address")
    parser.add_argument("--port", type=int, default=9559,
                        help="Robot port number")

    args = parser.parse_args()
    main(args.ip, args.port)
