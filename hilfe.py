# -*- coding: utf-8 -*-
import sys 

from PyQt4.phonon import Phonon 
from PyQt4 import QtGui, QtCore 
 

import os 

class VPlayer(QtGui.QMainWindow): 
    def __init__(self): 
        QtGui.QMainWindow.__init__(self)
        
        widget = QtGui.QWidget()
        layout = QtGui.QVBoxLayout() 
        widget.setLayout(layout) 

        self.setCentralWidget(widget) 

        self.player = Phonon.VideoPlayer() 
        layout.addWidget(self.player)
        self.player.setMinimumSize(400, 400)

        start = QtGui.QPushButton('Start') 
        stop = QtGui.QPushButton('Stop')
        bye = QtGui.QPushButton('Exit')
        
        start.clicked.connect(self.select_and_play)
        stop.clicked.connect(self.stop_play)
        bye.clicked.connect(self.hastalavista)
       
        layout.addWidget(start)
        layout.addWidget(stop)
        layout.addWidget(bye)
      

        #self.mediaSource = None
        

    def select_and_play(self): 
 
       
        self.mediaSource = Phonon.MediaSource('How_to.avi') 
        self.player.load(self.mediaSource) 
        self.player.play() 
        
    
    def stop_play(self):
        
            self.player.stop()
   
    def hastalavista(self,event):
        self.close()
        



def main():
    
    app = QtGui.QApplication([]) 
    app.setApplicationName('How to..')
    
    tester = VPlayer() 
    tester.show() 
    app.exec_() 
    
    
if __name__ == '__main__':     
 main()
    
