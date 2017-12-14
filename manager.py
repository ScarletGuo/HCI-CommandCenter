import device
import os

class manager(object):
    def __init__(self):
        self.devices = {}

    def addDevice(self, dev):
        if dev == "Ros":
            ros = device.Ros()
            self.devices["{}_{}".format(dev, ros.ID)] = ros
            ros.msg.append('A new ros device is established with default setting. \n')
            ros.msg.append(ros.get_status())
            return ros
        elif dev == "Kinect":
            kin = device.Kinect()
            self.devices["{}_{}".format(dev, kin.ID)] = kin
            kin.msg += 'A new Kinect device is established with default setting. \n'
            kin.msg += kin.get_status()
            return kin
        elif dev == "EyeTracker":
            eye = device.EyeTracker()
            self.devices["{}_{}".format(dev, eye.ID)] = eye
            eye.msg += 'A new Eye Tracker device is established with default setting. \n'
            eye.msg += eye.get_status()
            return eye
        elif dev == "Dialogue":
            dia = device.Dialogue()
            self.devices["{}_{}".format(dev, dia.ID)] = dia
            dia.msg += 'A new Dialogue device is established with default setting. \n'
            dia.msg += dia.get_status()
            return dia

    def action(self, dev, action):
        if "Ros" in dev:
            self.handleRos(dev, action)

    def handleRos(self, dev, action):
        if not os.path.exists('robot_control/output'):
            file = open("robot_control/output","w") 
            file.write(action) 
            file.close() 
            self.devices[dev].msg += self.devices[dev].send(dev, action);
        else:
            self.devices[dev].msg+= self.devices[dev].fail(dev, action);

