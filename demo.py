# -*- coding: utf-8 -*-
"""
Created on Wed Oct  6 10:15:25 2021

@author: Deng
"""

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
#  only needed for access to command line arguments
import sys


#  you need one and only one QApplication instance per application. it is act as event scheduler
#  pass in sys.argv to allow command line arguments for your app
app = QApplication (sys.argv)

window = QMainWindow()
window.show()# IMPORTANT !!! windows are hidden by default
# start the event loop
app.exec_()

#  your application won't reach here until you exit and the event loop has stopped