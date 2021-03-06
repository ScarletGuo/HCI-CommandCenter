from PyQt5.QtWidgets import *
import device
from subprocess import call
import os
import sys


class ControlCenter(QWidget):

    def __init__(self):
        super().__init__()
        self.outputStr = 1000
        self.allOut = ""
        self.curDevice = ""
        self.kinect_1_str = "Switch to kinect 1 tab. \nEnter 'help' to get command lists.\n"
        self.ros_1_str = "Switch to ros 1 tab.\nEnter 'help' to get command lists.\n"
        self.kinect = device.Device
        self.ros = device.Device

        self.initUI()

    def buttonClicked(self):
        sender = self.sender()
        if sender.text() == 'Kinect':
            self.kinect = device.Kinect();
            self.kinect_1_str += 'A new kinect device is established with default setting. \n'
            self.kinect_1_str += self.kinect.get_status()


        if sender.text() == 'ROS':
            self.ros = device.Ros();
            self.ros_1_str += "A new ROS device is estabilished with default setting. \n"
            self.ros_1_str += self.ros.get_status()

        if sender.text() == 'EyeTrack':
            eye_track = device.EyeTracker();
            self.curDeviceStatus.setText(sender.text() + ': a new Eye Tracking device is estabilished with default setting. \n');

        if sender.text() == 'Dialog':
            dialog = device.Dialogue();
            self.curDeviceStatus.setText(sender.text() + ': a new System Dialog device is estabilished with default setting. \n');



        self.outputStr += 1
        
        print(self.outputStr)


    def tab_clicked(self):
        # update status window string
        sender = self.sender()
        if sender.text() == 'Kinect_1':
            self.kinect_1.setDefault(False)
            self.ros_1.setDefault(False)
            sender.setDefault(True)

            self.curDevice = 'Kinect_1'
            self.curDeviceStatus.setText(self.kinect_1_str)
        elif sender.text() == 'ROS_1':
            self.kinect_1.setDefault(False)
            self.ros_1.setDefault(False)
            sender.setDefault(True)
            
            self.curDevice = 'ROS_1'
            self.curDeviceStatus.setText(self.ros_1_str)

    def deviceSettingBox(self):
        self.gridGroupBox = QGroupBox("Devices")

        layout = QGridLayout()

        # kinect btn
        self.kinect = QPushButton("Kinect")
        self.kinect.clicked.connect(self.buttonClicked)  
        layout.addWidget(self.kinect, 0, 0, 1, 1)
        # ROS btn
        self.ros = QPushButton("ROS")
        self.ros.clicked.connect(self.buttonClicked) 
        layout.addWidget(self.ros, 1, 0, 1, 1)
        # eye track btn
        self.eye_track = QPushButton("EyeTrack")
        self.eye_track.clicked.connect(self.buttonClicked) 
        layout.addWidget(self.eye_track, 2, 0, 1, 1)
        # Dialog btn
        self.ros = QPushButton("Dialog")
        layout.addWidget(self.ros, 3, 0, 1, 1)
        self.ros.clicked.connect(self.buttonClicked) 

        self.gridGroupBox.setLayout(layout)

    def statusWindow(self):
        self.statusBox = QGroupBox("Status Window")
        layout = QGridLayout()
        # kinect 1
        self.kinect_1 = QPushButton("Kinect_1")
        self.kinect_1.clicked.connect(self.tab_clicked)  
        layout.addWidget(self.kinect_1, 0, 0, 1, 1)
        # ros 1
        self.ros_1 = QPushButton("ROS_1")
        self.ros_1.clicked.connect(self.tab_clicked)  
        layout.addWidget(self.ros_1, 0, 1, 1, 1)

        layout.addWidget(QPushButton("Dialog_1"), 0, 2, 1, 1)
        layout.addWidget(QPushButton("Kinect_2"), 0, 3, 1, 1)

        self.curDeviceStatus = QTextEdit()
        self.curDeviceStatus.setPlainText("Current device status will be displayed here.\nPlease use buttons on the left side to create new devices.\nPlease use button at top to view the status of specific device.")
        layout.addWidget(self.curDeviceStatus, 1, 0, 1, 4)

        self.cmd_line = QLineEdit()
        layout.addWidget(self.cmd_line, 2, 0, 1, 3)
        self.submit = QPushButton("Submit")
        self.submit.clicked.connect(self.submit_clicked) 
        self.cmd_line.returnPressed.connect(self.submit.click) 
        layout.addWidget(self.submit, 2, 3, 1, 1)

        self.statusBox.setLayout(layout)

    def submit_clicked(self):
        sender = self.sender()
        instruction = self.cmd_line.text()
        print (instruction)

        # if current tab is Kinect_!
        if self.curDevice == 'Kinect_1':
            kinect_mannul = "1.getStatus\n2.setPort N\n3.setHost N\n"
            self.kinect_1_str += '>> '
            self.kinect_1_str += instruction
            self.kinect_1_str += '\n'
            if instruction == 'help':
                self.kinect_1_str += kinect_mannul

            if instruction == 'getStatus':
                self.kinect_1_str += self.kinect.get_status()

            if 'setPort' in instruction:
                portNum = 123
                self.kinect_1_str += self.kinect.set_port(portNum)

            if 'setHost' in instruction:
                hostNum = 345
                self.kinect_1_str += self.kinect.set_host(hostNum)

            self.curDeviceStatus.setText(self.kinect_1_str)


        # if current tab is ROS_1
        elif self.curDevice == 'ROS_1':

            ros_mannual = "1.getStatus\n3.move\n4.sitDown\n5.simpleWalk N\n6.moveHead\n2.moveArm\n"
            self.ros_1_str += '>> '
            self.ros_1_str += instruction
            self.ros_1_str += '\n'

            if instruction == 'help':
                self.ros_1_str += ros_mannual

            elif instruction == 'getStatus':
                self.ros_1_str += self.ros.get_status()

            # check if the output exists
            # if not, create one with specific commands
            # if yes, return busy message
            elif instruction == 'stand':
                try:
                    if not os.path.exists('robot_control/output'):
                        file = open("robot_control/output","w") 
                        file.write(instruction) 
                        file.close() 
                        self.ros_1_str += self.ros.stand();
                    else:
                        self.ros_1_str += "Other command is in process"
                except FileNotFoundError:
                    self.ros_1_str += "Directory: robot_control not detected\n"

            elif instruction == 'simpleWalk':
                try:
                    if not os.path.exists('robot_control/output'):
                        file = open("robot_control/output","w") 
                        file.write(instruction) 
                        file.close() 
                        self.ros_1_str += self.ros.simpleWalk();
                    else:
                        self.ros_1_str += "Other command is in process"
                except FileNotFoundError:
                    self.ros_1_str += "Directory: robot_control not detected\n"

            elif instruction == 'sitDown':
                try:
                    if not os.path.exists('robot_control/output'):
                        file = open("robot_control/output","w") 
                        file.write(instruction) 
                        file.close() 
                        self.ros_1_str += self.ros.standby();
                    else:
                        self.ros_1_str += "Other command is in process"
                except FileNotFoundError:
                    self.ros_1_str += "Directory: robot_control not detected\n"

            elif instruction == 'moveHead':
                try:
                    if not os.path.exists('robot_control/output'):
                        file = open("robot_control/output","w") 
                        file.write(instruction) 
                        file.close() 
                        self.ros_1_str += self.ros.moveHead();
                    else:
                        self.ros_1_str += "Other command is in process"
                except FileNotFoundError:
                    self.ros_1_str += "Directory: robot_control not detected\n"

            elif instruction == 'moveArm':
                try:
                    if not os.path.exists('robot_control/output'):
                        file = open("robot_control/output","w") 
                        file.write(instruction) 
                        file.close() 
                        self.ros_1_str += self.ros.moveArm();
                    else:
                        self.ros_1_str += "Other command is in process"
                except FileNotFoundError:
                    self.ros_1_str += "Directory: robot_control not detected\n"
                
            else:
                self.ros_1_str += "No command matches\n"


            # set the print text to ros_1_str
            self.curDeviceStatus.setText(self.ros_1_str)

        self.cmd_line.clear();


    def initUI(self):
        self.setGeometry(200, 100, 1100, 800)
        self.setWindowTitle("Control Center")

        self.deviceSettingBox()
        self.statusWindow()
        mainLayout = QGridLayout()
        mainLayout.addWidget(self.gridGroupBox, 0, 0)
        mainLayout.addWidget(self.statusBox, 0, 1, 1, 5)
        self.setLayout(mainLayout)

        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    cc = ControlCenter()
    sys.exit(app.exec_())