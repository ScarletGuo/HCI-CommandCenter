'''
Get all information from specifice device and log them for future reference
'''

from time import gmtime, strftime
# from robot_control import standby, simpleWalk, stand, moveHead, moveArm

class Device:
    # host
    # port

    def __init__(self):
        msg = "Connection established"
        self.port = 404
        self.host = 404
        # print("Connection established")
        pass

    '''
    display device information and status
    '''
    def get_status(self):
        msg = "Current status is running. \n"
        # print("General device status")
        return msg


    '''
    set the port of the device
    '''
    def set_port(self, portNum):
        
        self.port = portNum
        msg = 'Set port to ' + str(self.port) + '.\n'

        return msg


    '''
    set the host of the device
    '''
    def set_host(self, hostNum):
        
        self.host = hostNum
        msg = 'Set host to ' + str(self.host) + '.\n'

        return msg

    def get_port(self):

        return self.port

    def get_host(self):

        return self.host

    '''
        Should receive all the messages displayed and store them into a file (called log.txt maybe).
    '''
    def log(log_msg):
        curr_time = strftime("%Y-%m-%d %H:%M:%S\n", gmtime())
        with open('log.txt', 'a') as f:
            f.write('\n' + curr_time)
            f.write(log_msg)

    '''
    get user input, send that command to backend as a string
    '''
    def get_command(self, command):
        return command

class Ros(Device):
    def __init__(self):
        super().__init__()
        pass

    def get_status(self):
        return super().get_status()
    

    def stand():
        #stand.main()
        print("robot standup")
        pass


class Kinect(Device):
    def __init__(self):
        super().__init__()
        pass

    def get_status(self):
        return super().get_status()

class EyeTracker(Device):
    def __init__(self):
        super().__init__()
        pass

    def get_status(self):
        return super().get_status()

class Dialogue(Device):
    def __init__(self):
        super().__init__()
        pass

    def get_status(self):
        return super().get_status()

"""
For test use
"""
if __name__ == '__main__':
    msg = "test\n"
    msg += "test\n"
    print(msg)
    Device.log(msg)
