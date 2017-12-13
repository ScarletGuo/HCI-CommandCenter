import sys
from PyQt5.QtWidgets import *
import v5_device


class ControlCenter(QWidget):
    def __init__(self):
        super().__init__()
        self.num_kinect = 0
        self.num_ros = 0

        self.devicesArr = []   
        self.devicesArr.append(device.Kinect("kinect_" + str(self.num_kinect)))
        self.num_kinect += 1

        self.devicesArr.append(device.Kinect("kinect_" + str(self.num_kinect)))
        self.num_kinect += 1

        self.devicesArr.append(device.Ros("ros_" + str(self.num_ros)))   
        self.num_ros += 1

        self.allOut = ""
        self.curDevice = ""
        self.kinect_1_str = "Switch to kinect 1 tab. "
        self.ros_1_str = "Switch to ros 1 tab."

        self.initUI()

    # click to add devices, TODO: updata layout
    def addDevice(self):
        sender = self.sender()
        if sender.text()[0] == 'k': 
            self.devicesArr.append(device.Kinect("kinect_" + str(self.num_kinect)))
            self.num_kinect += 1
            print("kinect btn clicked")
        elif sender.text()[0] == 'r':
            self.devicesArr.append(device.Ros("ros_" + str(self.num_ros)))   
            self.num_ros += 1
            print("ros btn clicked")

    def deviceSettingBox(self):
        self.gridGroupBox = QGroupBox("Devices")
        layout = QGridLayout()

        # kinect btn
        self.kinect = QPushButton("kinect")
        self.kinect.clicked.connect(self.addDevice)  
        layout.addWidget(self.kinect, 0, 0, 1, 1)
        # ROS btn
        self.eye_track = QPushButton("ros")
        layout.addWidget(self.eye_track, 1, 0, 1, 1)
        self.eye_track.clicked.connect(self.addDevice) 
        # eye track btn
        self.ros = QPushButton("eyeTrack")
        layout.addWidget(self.ros, 2, 0, 1, 1)
        self.ros.clicked.connect(self.addDevice) 
        # Dialog btn
        self.ros = QPushButton("dialog")
        layout.addWidget(self.ros, 3, 0, 1, 1)
        self.ros.clicked.connect(self.addDevice) 

        self.gridGroupBox.setLayout(layout)

    # click to change default btn, update current device, set up text
    def tab_clicked(self):
        sender = self.sender()
        # set dafault btn to this sender
        for btn in self.tabs_btn:
            btn.setDefault(False)
        sender.setDefault(True)
        
        # update current device
        for d in self.devicesArr: 
            if d.get_name() == sender.text():
                self.curDevice = d

        self.curDeviceStatus.setText(self.curDevice.get_status())

    def statusWindow(self):
        self.statusBox = QGroupBox("Status Window")
        layout = QGridLayout()

        # create tabs
        self.tabs_btn = []
        for i in range(len(self.devicesArr)):
            deviceBtn = QPushButton(self.devicesArr[i].get_name())
            deviceBtn.clicked.connect(self.tab_clicked)
            self.tabs_btn.append(deviceBtn)
            layout.addWidget(deviceBtn, 0, i, 1, 1) 

        # create output window & command line
        self.curDeviceStatus = QTextEdit()
        self.curDeviceStatus.setPlainText("Current device status will be displayed here.\n")
        layout.addWidget(self.curDeviceStatus, 1, 0, 1, 4)

        self.cmd_line = QLineEdit(">> ")
        layout.addWidget(self.cmd_line, 2, 0, 1, 3)
        self.submit = QPushButton("Submit")
        self.submit.clicked.connect(self.submit_clicked)  
        layout.addWidget(self.submit, 2, 3, 1, 1)

        self.statusBox.setLayout(layout)

    # when submit, get data from cmd
    def submit_clicked(self):
        sender = self.sender()
        instruction = self.cmd_line.text()
        self.cmd_line.setText(">> ")

        # update it's meg
        self.curDevice.add_status(instruction)
        self.curDeviceStatus.setText(self.curDevice.get_status())

        # checking: print instruction to shell
        print(sender.text() + " " + instruction)

    def initUI(self):
        self.setGeometry(200, 100, 1100, 800)
        self.setWindowTitle("Contro Center")

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
