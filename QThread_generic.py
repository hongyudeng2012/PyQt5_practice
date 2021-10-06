# -*- coding: utf-8 -*-
"""
Created on Wed Oct  6 17:52:55 2021

@author: Deng
"""

from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import requests
import time


class WorkerSignals(QObject):
    '''
    Defines the signals available from a running woker thread.
    
    Supported signals are:
        
    finihsed 
        No data
    
    error 
        'tuple' (exctype,value,traceback.format_exc())
    
    result
        'object' data returned from processing,anything
        
    progress
        'int' indicating % progress
    '''
    finished = pyqtSignal()
    error = pyqtSignal(tuple)
    result = pyqtSignal(object)
    progress = pyqtSignal(int)

class Worker (QRunnable):
    '''''
    worker thread
    inherits from QRunnable to handler worker thread setup, signals and wrap-up.

    :param callback: the funtion callback to run on this worker
    :thread. Suplied args and kwargs will be pass through to the runner
    
    :type callback: function
    
    :param args :Arguments to pass to the callback function
    
    :params kwargs : Keywards to pass 
    :
    '''
    def __init__(self,fn,*args,**kwargs):
        super(Worker,self).__init__()
        # store constructor arguments (re-used for processing )
        self.fn = fn
        self.args = args
        self.kwargs = kwargs
        self.signals = WorkerSignals()
        
        # add the callback to our kwargs
        kwargs['progress_callback'] = self.signals.progress 
    
    def run(self):
        '''
        initial the runner function with passed args and kwargs
        '''
        print("execute once")
        try:
            result = self.fn(*self.args,**self.kwargs)
        except:
            traceback.print_exc()
            exctype,value = sys.exc_info()[:2]
            self.signals.error.emit((exctype,value,traceback.format_exc()))
        else:
            self.signals.result.emit(result)#return the result of the process
        finally:
            self.signals.finished.emit()# done
    
    
class MainWindow(QMainWindow):
    def __init__(self, *arg, **kwargs):

        super(MainWindow,self).__init__(*arg,**kwargs)
        
    
        self.counter = 0
        
        layout = QVBoxLayout()
        
        self.l = QLabel("start")
        
        b = QPushButton("danger")
        b.pressed.connect(self.oh_no)
        
    
        layout.addWidget(self.l)
        layout.addWidget(b)
        
        w = QWidget()
        w.setLayout(layout)
        self.setCentralWidget(w)
        self.show()
        
        self.threadpool = QThreadPool()
        print(f"mulithreading with maximul {self.threadpool.maxThreadCount()} threads ")
        
        self.timer = QTimer()
        self.timer.setInterval(1000)
        self.timer.timeout.connect(self.recurring_timer)
        self.timer.start()
    
    def progress_fn(self,n):
        print(f"{n} done")
        
    def execute_fn(self,progress_callback):
        for n in range(0,5):
            time.sleep(1)
            progress_callback.emit(n*100/4)
        return "Done"
    def print_output(self,s):
        print(s)
    def thread_complete(self):
        print("Thread complete")
    
    def oh_no(self):
        # pass the function to execute
        worker = Worker (self.execute_fn)# any other args, kwargs are passed to the run function
        worker.signals.result.connect(self.print_output)
        worker.signals.finished.connect(self.thread_complete)
        worker.signals.progress.connect(self.progress_fn)
        # execute
        self.threadpool.start(worker)
        
        
    def recurring_timer(self):
        self.counter +=1
        self.l.setText(f"counter: {self.counter}")
app = QApplication([])
window = MainWindow()
app.exec_()