'''
@author Scarlet Guo
main.py
'''

from docopt import docopt
from console import Console, Notice, Progress
from guiwindow import commandWindow, Session

__version__ = "0.1"
__doc__ = """HCI-ComandCenter v{0}
Usage:
     main.py [options] [ --model <path>... ]
Options:
     -h --help                            Show this screen. [default: False]
     -v --version                         Show the current version. [default: False]
     -s <str> --subid <str>               Subject identifier. [default: 000]
     -w <folder> --write <folder>         Save data to a folder. [default: None]
     --host <hostname>                    Specify host. [default: 192.168.0.2]
     --port <port>                        Specify port. [default: 5005]
     --buffer <buffersize>                Specify buffer size. [default: 4096]
""".format(__version__)

'''
let user choose their devices
'''
def initDevice(args):
	self.devices = self.initDevice().devices

'''
initialize data storage
'''
def initdata(args):
	self.session = Session(self.devices, args["--subid"], args["--write"])

'''
init main gui window
'''
def initGUI(args):
	self.commandWindow = commandWindow(self.session)

'''
send error message
'''
class Error(object):
	def __init__(self, message):
		self.container.error(message)

'''
send notification
'''
class Notification:
	def __init__(self, message):
		self.container.notification(message)

if __name__ == '__main__':
	args = docopt(__doc__, version='CM v{0}'.format(__version__))
    print(args)
    # TODO: start an QApplication
    initdata(args)
    initGUI(args)




