



#    template for adding a video to PYQT5




from PyQt5 import QtWidgets, QtMultimediaWidgets,QtMultimedia, QtGui, QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys


# part 1: set up main window of app

class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.setGeometry(0, 0, 1000, 500)
        self.setWindowTitle("BF4 Deployment Timer")
        self.initGUI()




    def initGUI(self):

        self.videoWidget = QtMultimediaWidgets.QVideoWidget()
        self.setCentralWidget(self.videoWidget)



        self.mediaPlayer = QtMultimedia.QMediaPlayer(None, QtMultimedia.QMediaPlayer.VideoSurface)
        self.mediaPlayer.setVideoOutput(self.videoWidget)



        local = QtCore.QUrl.fromLocalFile('C:/Users/Owner/PycharmProjects/BF4 Deployment Timer/vidbackground2.mov')
        media = QtMultimedia.QMediaContent(local)
        self.mediaPlayer.setMedia(media)

        print('state: ' + str(self.mediaPlayer.state()))
        print('mediaStatus: ' + str(self.mediaPlayer.mediaStatus()))
        print('error: ' + str(self.mediaPlayer.error()))

        self.mediaPlayer.play()

        print('state: ' + str(self.mediaPlayer.state()))
        print('mediaStatus: ' + str(self.mediaPlayer.mediaStatus()))
        print('error: ' + str(self.mediaPlayer.error()))

def run_app():
    created_app = QApplication(sys.argv)
    application = MyWindow()
    application.show()
    sys.exit(created_app.exec_())



run_app()