from PyQt5.QtWidgets import *
import device
from subprocess import call
import sys
from manager import manager

kid = 0
eid = 0
did = 0
rid = 0

class ControlCenter(QWidget):

    def __init__(self, app):
        super().__init__()
        self.app = app
        self.manager = manager()
        self.outputStr = 1000
        self.allOut = ""
        self.curDevice = ""
        # self.kinect_1_str = "Switch to kinect 1 tab. \nEnter 'help' to get command lists.\n"
        # self.ros_1_str = "Switch to ros 1 tab.\nEnter 'help' to get command lists.\n"
        self.kinect = device.Device
        self.ros = device.Device

        self.initUI()

    def buttonClicked(self):
        sender = self.sender()
        new = self.manager.addDevice(sender.text())
        self.updateStatus(new, sender.text())
        # self.outputStr += 1

    def add_kinect_btn(self):
        # a pop up window requires host and port, after clicking "saving" 
        pass


    def tab_clicked(self):
        # update status window string
        sender = self.sender()
        txt = sender.text()
        self.curDevice = sender.text()
        self.curDeviceStatus.setText(''.join(self.manager.devices[txt].msg))
        # if "Kinect" in txt:
        #     self.kinect_1.setDefault(False)
        #     self.ros_1.setDefault(False)
        #     sender.setDefault(True)

        # elif sender.text() == 'ROS_1':
        #     self.kinect_1.setDefault(False)
        #     self.ros_1.setDefault(False)
        #     sender.setDefault(True)
            
        #     self.curDevice = 'ROS_1'
            

    def deviceSettingBox(self):
        self.gridGroupBox = QGroupBox("Devices")

        layout = QGridLayout()

        # kinect btn
        self.kinect = QPushButton("Kinect")
        self.kinect.clicked.connect(self.buttonClicked)  
        layout.addWidget(self.kinect, 0, 0, 1, 1)
        # ROS btn
        self.ros = QPushButton("Ros")
        self.ros.clicked.connect(self.buttonClicked) 
        layout.addWidget(self.ros, 1, 0, 1, 1)
        # eye track btn
        self.eye_track = QPushButton("EyeTracker")
        self.eye_track.clicked.connect(self.buttonClicked) 
        layout.addWidget(self.eye_track, 2, 0, 1, 1)
        # Dialog btn
        self.ros = QPushButton("Dialogue")
        layout.addWidget(self.ros, 3, 0, 1, 1)
        self.ros.clicked.connect(self.buttonClicked) 

        self.gridGroupBox.setLayout(layout)

    def initStatus(self):
        self.statusBar = QHBoxLayout()
        if len(self.manager.devices) != 0:
            for d in self.manager.devices.values():
                if type(d) is device.Kinect:
                    self.kinect = QPushButton("Kinect_{}".format(d.ID))
                    self.kinect.clicked.connect(self.tab_clicked)
                    self.statusBar.addWidget(self.kinect) 
                elif type(d) == device.Ros:
                    self.ros = QPushButton("Ros_{}".format(d.ID))
                    self.ros.clicked.connect(self.tab_clicked)
                    self.statusBar.addWidget(self.ros) 
                elif type(d) == device.EyeTracker:
                    self.eyetracker = QPushButton("EyeTracker_{}".format(d.ID))
                    self.eyetracker.clicked.connect(self.tab_clicked)
                    self.statusBar.addWidget(self.eyetracker) 
                elif type(d) == device.Dialogue:
                    self.dialog = QPushButton("Dialogue_{}".format(d.ID))
                    self.dialog.clicked.connect(self.tab_clicked)
                    self.statusBar.addWidget(self.dialog)
                else:
                    print("Error: does not support the device")
        self.layout.addLayout(self.statusBar, 0, 0)
        self.statusBox.setLayout(self.layout)
        self.statusBox.show()
        self.app.processEvents()

    def updateStatus(self, d, dtype):
        btn = QPushButton("{}_{}".format(dtype, d.ID))
        btn.clicked.connect(self.tab_clicked)
        self.statusBar.addWidget(btn)

    def statusWindow(self):
        self.statusBox = QWidget()
        self.statusBox.setWindowTitle("Status Window")
        self.layout = QGridLayout()

        # self.statusBar = QHBoxLayout()

        # if len(self.manager.devices) != 0:
        #     for d in manager.devices:
        #         if type(d) is Kindect:
        #             self.kinect = QPushButton("Kinect_{}".format(d.ID))
        #             self.kinect.clicked.connect(self.tab_clicked)
        #             self.statusBar.addWidget(self.kinect) 
        #         elif type(d) == ROS:
        #             self.ros = QPushButton("ROS_{}".format(d.ID))
        #             self.ros.clicked.connect(self.tab_clicked)
        #             self.statusBar.addWidget(self.ros) 
        #         elif type(d) == EyeTracker:
        #             self.eyetracker = QPushButton("EyeTracker_{}".format(d.ID))
        #             self.eyetracker.clicked.connect(self.tab_clicked)
        #             self.statusBar.addWidget(self.eyetracker) 
        #         elif type(d) == Dialogue:
        #             self.dialog = QPushButton("Dialogue_{}".format(d.ID))
        #             self.dialog.clicked.connect(self.tab_clicked)
        #             self.statusBar.addWidget(self.dialog)

        # self.layout.addLayout(self.statusBar, 0, 0)
        self.initStatus()

        self.curDeviceStatus = QTextEdit()
        self.curDeviceStatus.setPlainText("Current device status will be displayed here.\nPlease use buttons on the left side to create new devices.\nPlease use button at top to view the status of specific device.")
        self.layout.addWidget(self.curDeviceStatus, 1, 0)

        self.cmd_line = QLineEdit()
        self.layout.addWidget(self.cmd_line, 2, 0)
        self.submit = QPushButton("Submit")
        self.submit.clicked.connect(self.submit_clicked) 
        self.cmd_line.returnPressed.connect(self.submit.click) 
        self.layout.addWidget(self.submit, 3, 1)

        self.statusBox.setLayout(self.layout)

    def submit_clicked(self):
        sender = self.sender()
        instruction = self.cmd_line.text()
        print (instruction)
        d = self.manager.devices[self.curDevice]
        d.msg += '>> '
        d.msg += instruction
        d.msg += '\n'
        self.manager.action(self.curDevice, instruction)
        self.cmd_line.clear();
        self.curDeviceStatus.setText(''.join(d.msg))


    def initUI(self):
        self.setGeometry(200, 100, 1100, 800)
        self.setWindowTitle("Control Center")

        self.statusWindow()
        self.deviceSettingBox()
        mainLayout = QGridLayout()
        mainLayout.addWidget(self.gridGroupBox, 0, 0)
        mainLayout.addWidget(self.statusBox, 0, 1, 1, 5)
        self.setLayout(mainLayout)

        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    cc = ControlCenter(app)
    sys.exit(app.exec_())