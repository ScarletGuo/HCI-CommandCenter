from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from taskDescription import *
from PyQt5 import QtCore, QtWidgets

'''
dialog for selecting devices, can be called at 
'''
class initDevice(QInputDialog):
	def __init__(self):
		# create layout
		# add all devices to layout
		# allow user to choose certain devices [checkboxs in a box set] 
		# tutorial: http://zetcode.com/gui/pyqt5/widgets/
		# self.devices = selected devices

'''
main GUI window
'''
class commandWindow(Object):

	def __init__(self, parent):
		self.parent = parent
		self.mainWindow = QWidget()
		# the upper right window for message output
		self.messageWindow = messageWindow()
		# the upper left window for control buttons
		self.settingWindow = settingWindow()
		# left window for labels of different devices
		self.labelWindow = labelWindow()
		# create layout
		# set layout to main window
		# add each widget class to layout

	def print(self, device, message):
		self.messageWindow.print(device, message)

class messageWindow(QWidget):

	def __init__(self,parent):
		pass

class settingWindow(QWidget):

	def __init__(self, patent):
		pass


class labelWindow(QWidget):

	def __init__(self, parent):
		pass



