# -*- coding: utf-8 -*-
"""
Created on Wed Oct  6 14:11:10 2021

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
        # windowTitleChanged is a SIGNAL of Qt Widget
        # the connected function will be called whenever the window title is changed
        # new title will be passed to the function
        
        # self.windowTitleChanged.connect(self.onWindowTitleChange)
        
        # SIGNAL: The connected function will be called wheever the window title is changed
        #  new title is discarded in the lambda and the function is called without parameters
        #  lambda create an enclosure,connect to self prevent garbage collector
        # https://newbedev.com/using-lambda-expression-to-connect-slots-in-pyqt
        # self.windowTitleChanged.connect(lambda x:self.my_custom_fn())

        # SIGNAL: The connected function will be called wheever the window title is changed
        # the new title is passed to the function and replaced the default parameter. extra
        # data is passed from within the lambda
        self.windowTitleChanged.connect(lambda x:self.my_custom_fn(x,10))

        self.setWindowTitle("My first PyQt5 App")
        
        label = QtWidgets.QLabel("AWESOME LABEL")
        
        # the 'Qt' namespace from QtCore has a lot of attributes to customise 
        # and control widgets, see Http:// doc.qt.io/qt-5/qt.html
        label.setAlignment(QtCore.Qt.AlignCenter)
        
        #set the center wdiget of the window. widget will expand 
        # to take up all the space in the window by default
        self.setCentralWidget(label)
    def onWindowTitleChange(self,s):
        print(s)
    def my_custom_fn(self, a = "hello", b =5):
        print (a,b)
        
#  you need one and only one QApplication instance per application. it is act as event scheduler
#  pass in sys.argv to allow command line arguments for your app
app = QtWidgets.QApplication (sys.argv)

window = MyMainWindow()
window.show()# IMPORTANT !!! windows are hidden by default
# start the event loop
app.exec_()