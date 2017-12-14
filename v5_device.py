'''
Get all information from specifice device and log them for future referencesdf
'''

from time import gmtime, strftime

class Device:
    def __init__(self):
        self.msg = "default constructor"
        # print("Connection established")
        pass

    def __init__(self, input_name):
        self.msg = "Customize constructor for " + input_name
        self.name = input_name
        self.counter = 0

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

    '''
    get name of current device
    '''
    def get_name(self):
        return self.name

    '''
    display device information and status
    '''
    def get_status(self):
        return self.msg

    '''
    prepend device information and status
    '''
    def add_status(self, newCommand):
        self.msg = str(self.counter) + " " + newCommand + "\n" + self.msg
        self.counter += 1

class Ros(Device):
    def __init__(self):
        super().__init__()
        pass

    def __init__(self, input_name):
        super().__init__(input_name)

    def get_status(self):
        return super().get_status()
        

class Kinect(Device):
    def __init__(self):
        super().__init__()

    def __init__(self, input_name):
        super().__init__(input_name)

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
