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

        self.music_file = QUrl.fromLocalFile('./media/audio/music/deadline.mp3')
        self.background_music_playlist = QMediaPlaylist()
        self.background_music_playlist.setPlaybackMode(QMediaPlaylist.Loop)
        self.background_music_playlist.addMedia(QMediaContent(self.music_file))

        self.backgroundMusic_player = QMediaPlayer(None, QMediaPlayer.LowLatency)
        self.backgroundMusic_player.setPlaylist(self.background_music_playlist)
        self.backgroundMusic_player.setVolume(100)
        self.backgroundMusic_player.play()

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

