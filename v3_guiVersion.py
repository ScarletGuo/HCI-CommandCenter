import sys
from PyQt5.QtWidgets import *


class ControlCenter(QWidget):
    def __init__(self):
        super().__init__()
        self.outputStr = 1000
        self.allOut = "All devices status: \n" + "ERROR: [Kinect] is not open\n" + "[Eyetracker] has finished caliberation\n" +  "[ROS] right arm moves to [102, 39, 38]\n"

        self.initUI()
    def buttonClicked(self):
        sender = self.sender()
        self.kinect.setDefault(False)
        self.eye_track.setDefault(False)
        self.ros.setDefault(False)
        sender.setDefault(True)

        self.outputStr += 1
        self.curDeviceStatus.setText(sender.text() + ': status')
        self.allOut += 'Switch to ' + sender.text() + '\n'
        self.allStatus.setText(self.allOut)
        print(self.outputStr)

    def deviceSettingBox(self):
        self.gridGroupBox = QGroupBox("Device Setting")

        layout = QGridLayout()

        layout.addWidget(QPushButton("+"), 0, 0)
        layout.addWidget(QPushButton("-"), 1, 0)

        # kinect setting
        self.kinect = QPushButton("Kinect")
        # self.kinect.setDefault(True)
        self.kinect.clicked.connect(self.buttonClicked)  
        layout.addWidget(self.kinect, 2, 0)

        self.eye_track = QPushButton("EysTrack")
        layout.addWidget(self.eye_track, 3, 0)
        self.eye_track.clicked.connect(self.buttonClicked) 

        self.ros = QPushButton("ROS")
        layout.addWidget(self.ros, 4, 0)
        self.ros.clicked.connect(self.buttonClicked) 

        layout.addWidget(QLabel("Host:"), 0, 2)
        layout.addWidget(QLineEdit(), 0, 3)

        layout.addWidget(QLabel("Port:"), 1, 2)
        layout.addWidget(QLineEdit(), 1, 3)

        # EysTrack setting
        # ROS setting

        layout.addWidget(QPushButton("Save"), 0, 4, 2, 1)

        self.curDeviceStatus = QTextEdit()
        self.curDeviceStatus.setPlainText("Current device status will be displayed here.\n")
        layout.addWidget(self.curDeviceStatus, 2, 2, 3, 3)

        self.gridGroupBox.setLayout(layout)

    def createStatusWindow(self):
        self.statudWindow = QGroupBox("All Device Status")
        self.allStatus = QTextEdit()
        self.allStatus.setPlainText(self.allOut)

        layout = QGridLayout()
        layout.addWidget(self.allStatus)

        self.statudWindow.setLayout(layout)

    def createCmdBox(self):
        self.cmdBox = QGroupBox("Command Line")
        layout = QHBoxLayout()

        layout.addWidget(QLineEdit())
        layout.addWidget(QPushButton("Submit"))

        self.cmdBox.setLayout(layout)

    def initUI(self):
        self.setGeometry(893, 70, 700, 800)
        self.setWindowTitle("Contro Center")

        self.deviceSettingBox()
        self.createStatusWindow()
        self.createCmdBox()
        mainLayout = QVBoxLayout()
        mainLayout.addWidget(self.gridGroupBox)
        mainLayout.addWidget(self.statudWindow)
        mainLayout.addWidget(self.cmdBox)
        self.setLayout(mainLayout)

        self.show()


if __name__ == '__main__':

    app = QApplication(sys.argv)
    cc = ControlCenter()
    sys.exit(app.exec_())
