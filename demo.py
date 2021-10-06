# -*- coding: utf-8 -*-
"""
Created on Wed Oct  6 10:15:25 2021

@author: Deng
"""

from PyQt5 import QtWidgets
from PyQt5 import QtCore
from PyQt5 import QtGui
#  only needed for access to command line arguments
import sys

#  subclass QMainWindow to customize application's main window
class MyMainWindow(QtWidgets.QMainWindow):
    def __init__(self, *arg,**kwargs):
        super(MyMainWindow, self).__init__(*arg,**kwargs)
        
        self.setWindowTitle("My first PyQt5 App")
        
        label = QtWidgets.QLabel("what is Qlable?")
        
        # the 'Qt' namespace from QtCore has a lot of attributes to customise 
        # and control widgets, see Http:// doc.qt.io/qt-5/qt.html
        label.setAlignment(QtCore.Qt.AlignCenter)
        
        #set the center wdiget of the window. widget will expand 
        # to take up all the space in the window by default
        self.setCentralWidget(label)
        
#  you need one and only one QApplication instance per application. it is act as event scheduler
#  pass in sys.argv to allow command line arguments for your app
app = QtWidgets.QApplication (sys.argv)

window = MyMainWindow()
window.show()# IMPORTANT !!! windows are hidden by default
# start the event loop
app.exec_()

#  your application won't reach here until you exit and the event loop has stopped