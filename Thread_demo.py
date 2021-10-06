# -*- coding: utf-8 -*-
"""
Created on Wed Oct  6 16:01:36 2021

@author: Deng
"""
# the code demonstrate the problem of thread issue
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

import time


class Worker(QRunnable):
    '''''
    worker thread
    '''
    # @pyqtslot()
    def __init__(self,fn,*args,**kwargs):
        super(Worker,self).__init__()
        self.fn = fn
        self.args = args
        self.kwargs = kwargs
        
    def run(self):
        '''
        execute the runner function with passed self.args,self.kwargs
        '''
        # print(f"args is { type(self.args)} ")
        # print(f"kwargs is {self.kwargs} ")
        if self.args ==() and self.kwargs == {} : 
            self.fn()
        print("start a thread with {fn}")


class MainWindow(QMainWindow):
    def __init__(self, *arg, **kwargs):
        super(MainWindow,self).__init__(*arg,**kwargs)
        self.threadpool = QThreadPool()
        print(f"mulithreading with maximul {self.threadpool.maxThreadCount()} threads ")
        self.counter = 0
        layout = QVBoxLayout()
        self.l = QLabel("start")
        b = QPushButton("danger")
        b.pressed.connect(self.oh_no)
        
        c = QPushButton("?")
        c.pressed.connect(self.change_message)
        
        layout.addWidget(self.l)
        layout.addWidget(b)
        layout.addWidget(c)
        
        w = QWidget()
        w.setLayout(layout)
        self.setCentralWidget(w)
        self.show()
        
    def change_message(self):
        self.message = "pressed"
        worker =  Worker((lambda : time.sleep(3)))
        self.threadpool.start(worker)
    def hello_print(self):
        print("no danger, nothing happened")
    def  oh_no(self):
        # self.message = "pressed"
        worker =  Worker(self.hello_print)
        self.threadpool.start(worker)

            

    
app = QApplication([])
window = MainWindow()
app.exec_()