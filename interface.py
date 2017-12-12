'''
@copyright: Andrew Schoen


'''

# TODO: cleaning unnecessary imports
import os
from threading import Thread, Lock
from multiprocessing import Process, Pipe
import json
import pandas as pd
import numpy as np
import time
from itertools import count
import sys
from utility import *
import random
import string
import re

class Interface(object):
    "A generic interface object"

    def __init__(self, write=None):
        # if read == None:
        #     self.read_loc = None
        # else:
        #     self.read_loc = self.clean_path(read)

        if write == None:
            self.write_loc = None
        else:
            self.write_loc = self.clean_path(write)

    @staticmethod
    def clean_path(path):
        if path.startswith("~"):
            path = os.path.expanduser(path)
        realpath = os.path.realpath(path)
        return realpath

class KinectInterface(Interface):
    """
    Sets up the connection to the kinect and allows for easy access to new data.
    """

    def __init__(self, connection):
        """
        connection - A Connection object.
        """
        Interface.__init__(self)
        self.connection = connection
        if self.connection.status != "open":
            try:
                self.connection.open()
            except:
                raise IOError

        # Set up the kinect interface as a thread
        self.data = None
        # set to True if data has not yet been used by the algorithm
        self.new_data = False
        self.lock = Lock()
        self.thread = Thread(target=self.receiveData)
        self.running = True
        self.thread.start()

    # thread function: constantly polls the connection for new data and
    # updates self.new_data and self.data as needed
    def receiveData(self):
        while self.running:
            try:
                data = self.connection.receive()
            except:
                data = False
            if data:
                self.lock.acquire()
                self.data = data
                self.new_data = True
                self.lock.release()

    # checks to see if there is new data, returns (success (0/1), data) for
    # use in algorithm
    def checkForData(self):
        self.lock.acquire()
        if self.new_data:
            # print 'Checking.'
            result = (1, json.loads(self.data))
            self.new_data = False
        else:
            result = (0, 0)
        self.lock.release()
        return result

    def checkForCalibrationData(self):
        self.lock.acquire()
        if self.new_data:
            raw = json.loads(self.data)
            result = (1, [raw["quaternion_X"], raw["quaternion_Y"],
                          raw["quaternion_Z"], raw["quaternion_W"]])
            self.new_data = False
        else:
            result = (0, 0)
        self.lock.release()
        return result

    def stop(self):
        self.running = False
        self.connection.close()