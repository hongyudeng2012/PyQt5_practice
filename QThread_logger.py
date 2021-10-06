# -*- coding: utf-8 -*-
"""
Created on Wed Oct  6 15:50:58 2021

@author: Deng
"""

# Qthread need to be deleted after usage.If a lot of threads are used, it is better to use threadpool 
# https://realpython.com/python-pyqt-qthread/#reusing-threads-qrunnable-and-qthreadpool
#  example of a logger

from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import requests



class WorkerSignals(QObject):
    '''
    Defines the signals available from a running woker thread.
    
    data
        tuple of (identifier, data)
    '''
    data = pyqtSignal(tuple)

class Worker(QRunnable)    :
    '''
    worker thread
    inherits from QRunnable to handler worker thread setup, signals and wrap-up.
    
    :param id : the id for this worker
    :param url: the url to retrieve
    
    '''
    
    def __init__(self,id,url):
        super(Worker,self).__init__()
        self.id = id
        self.url = url
        self.signals = WorkerSignals()
        
    def run(self):
        r = requests.get(self.url)
        for line in r.text.splitlines():
            self.signals.data.emit((self.id,line))

class MainWindow(QMainWindow):
    def __init__(self, *args,**kwargs):
        super (MainWindow,self).__init__(*args,**kwargs)
        self.urls = [
            'http://www.google.com',
            'http://www.google.com',
            'http://www.google.com',
            'http://www.udemy.com/create-simple-gui-applications-with-python-and-qt',
            'http://www.google.com']
        layout = QVBoxLayout()
        self.text = QPlainTextEdit()
        self.text.setReadOnly(True)
        
        button = QPushButton("go get em")
        button.pressed.connect(self.excecute)
        layout.addWidget(self.text)
        layout.addWidget(button)
        
        w= QWidget()
        w.setLayout(layout)
        
        self.setCentralWidget(w)
        
        self.show()
        self.threadpool = QThreadPool()
        print(f"mulithreading with maximul {self.threadpool.maxThreadCount()} threads ")
    def excecute(self):
        for n, url in enumerate (self.urls):
            worker = Worker(n,url)
            worker.signals.data.connect(self.display_output)
            
            #  EXECUTE
            self.threadpool.start(worker)
    def display_output(self,data):
        id,s = data
        self.text.appendPlainText(f"WORKER {id} : {s}")

app = QApplication([])
window = MainWindow()
app.exec_()
