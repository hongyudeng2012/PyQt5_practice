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

class MainWindow(QMainWindow):
    def __init__(self, *arg, **kwargs):
        super(MainWindow,self).__init__(*arg,**kwargs)
        
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
        self.message = "oh no"
    def  oh_no(self):
        self.message = "pressed"
        for n in range(100):
            time.sleep(0.1)
            self.l.setText(self.message)
            QApplication.processEvents()
            
app = QApplication([])
window = MainWindow()
app.exec_()