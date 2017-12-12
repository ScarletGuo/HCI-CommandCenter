import os


'''
this class managed all the data storage. each device has an instance
@param device: a string specifying device type
@param log: a list to all the notifications
'''

class Container(object):

    def __init__(self, session, device):
    	self.device = device
        self.data_loc = session.write_loc + device + "-data.csv"
        self.log_loc = session.write_loc + device + "-log.txt"
        self.log = []

    def error(message):
    	self.log.append("ERROR: %s" % message)
    	self.commandWindow.print(device, "ERROR: %s" % message)

    def notification(message):
    	self.log.append("%s" % message)
    	self.commandWindow.print(device, "%s" % message)

    ''' 
    save the data to file, return true if success
    TODO
    '''
    def save():
    	pass


'''
this class stores static information for this session
@param write_loc: subject folder for data storage
@param subid: subject indentifier
@param startT: starting time
'''
class Session(object):

	def __init__(self, devices, subid = "000", write = None):
		self.devices = devices
		self.id = subid
		# folder 
		if write == None:
            self.write_loc = None
        else:
            self.write_loc = self.clean_path(write)
        self.devices = devices
        self.containerLists = {}

'''
reformat input path
'''
    @staticmethod
    def clean_path(path):
        if path.startswith("~"):
            path = os.path.expanduser(path)
        realpath = os.path.realpath(path)
        if not path.endswith("/"):
        	realpath = realpath + "/"
        return realpath