from PyQt5 import QtMultimediaWidgets, QtMultimedia, QtCore
from PyQt5.QtCore import QUrl, QRect, Qt
from PyQt5.QtGui import QFont
from PyQt5.QtMultimedia import QMediaContent, QMediaPlaylist, QMediaPlayer
from PyQt5.QtMultimediaWidgets import QVideoWidget
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QFrame
import sys
import os


class MyWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setGeometry(0,0,1920,1080)
        self.setWindowTitle('PyQt5 Test')
        self.initialize_content()
        self.initialize_interactive_methods()

    def initialize_content(self):


        self.blacktile_default_style = "border-image: url('./media/images/backgrounds/control console.png');"
        self.logo_label_default_style = "border-image: url('./media/images/backgrounds/title background.png'); " \
                                        "background-color:black; color: rgb(136, 204, 241)"
        self.timer_label_default_style = "border-image: url('./media/images/backgrounds/tile background.jpg'); color:" \
                                         "rgb(136, 204, 241) "
        self.timer_label_10sec_style = "border-image: url('./media/images/backgrounds/tile background.jpg'); color: red;"
        self.timer_label_deploy_style = "border-image: url('./media/images/backgrounds/tile background.jpg'); color: rgb(" \
                                    "98, 255, 0); "
        self.blacktile_label = QLabel(self)
        self.blacktile_label.setGeometry(QRect(1313, 0, 601, 1080))
        self.blacktile_label.setFrameShadow(QFrame.Raised)
        self.blacktile_label.setStyleSheet(self.blacktile_default_style)
        self.blacktile_label.show()

    def initialize_interactive_methods(self):
        """All widget functions activated by user interaction are defined in this method. The UCAnalysisGUI class 
        calls this method during the execution of it's __init__ method"""
        pass


# Run Application
def launch_GUI():
    app_configuration = QApplication(sys.argv)   # Creates a QApplication that configures the PyQt5 program
    application = MyWindow()                     # Instantiates our GUI class
    application.show()                           # Show the application on local machine's screen
    sys.exit(app_configuration.exec_())          # Instructs program to terminate when user closes the GUI


launch_GUI()                                     # Run the program

