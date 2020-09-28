from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtMultimedia import *
from PyQt5.QtMultimediaWidgets import *

class VideoPlayer(QWidget):
    def __init__(self, parent=None):
        super(VideoPlayer, self).__init__(parent)
        self.setGeometry(0,0,1000,500)

        videoWidget = QVideoWidget()           #create videowidet object


        layout = QVBoxLayout()                 # create layout for videowidget to be placed in
        layout.addWidget(videoWidget)          # place the videowidget object onto the layout object
        self.setLayout(layout)                 # put the layout object on the main window


        self.mediaPlayer = QMediaPlayer(None, QMediaPlayer.VideoSurface)    # create qmediaplayer object with video surface
        self.mediaPlayer.setVideoOutput(videoWidget)                        # assign the videowidget to the qmediaplayer object





    def keyPressEvent(self, e):
        print('state: ' + str(self.mediaPlayer.state()))
        print('mediaStatus: ' + str(self.mediaPlayer.mediaStatus()))
        print('error: ' + str(self.mediaPlayer.error()))
        if e.key() == Qt.Key_L:
            print('loading')
            self.load()
        if e.key() == Qt.Key_P:
            print('playing')
            self.mediaPlayer.play()

    def load(self):
        local = QUrl.fromLocalFile('C:/Users/Owner/PycharmProjects/BF4 Deployment Timer/vidbackground2.mov')
        media = QMediaContent(local)



        self.mediaPlayer.setMedia(media)

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    player = VideoPlayer()
    player.show()
    sys.exit(app.exec_())