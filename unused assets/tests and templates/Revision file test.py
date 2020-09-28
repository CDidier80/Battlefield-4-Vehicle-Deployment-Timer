# BF4 Deployment Timer Main Excecutable

from PyQt5 import QtWidgets, QtMultimediaWidgets, QtMultimedia, QtCore, QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys
from threading import Timer

sys.path.append('C:\\Users\\Owner\\PycharmProjects\\BF4 Deployment Timer\\sound\\friendly timers\\friendly AA r')



class MyWindow(QMainWindow):

    counter = 90

    def __init__(self):
        super(MyWindow, self).__init__()
        self.setGeometry(0, 0, 1920, 1080)
        self.setWindowTitle("BF4 Deployment Timer")


                             # Video Background

        self.videoWidget = QtMultimediaWidgets.QVideoWidget()
        self.setCentralWidget(self.videoWidget)

        self.mediaPlayer = QtMultimedia.QMediaPlayer(None, QtMultimedia.QMediaPlayer.VideoSurface)
        self.mediaPlayer.setVideoOutput(self.videoWidget)


        local = QtCore.QUrl.fromLocalFile('C:/Users/Owner/PycharmProjects/BF4 Deployment Timer/vidbackground2.mov')
        media = QtMultimedia.QMediaContent(local)
        self.mediaPlayer.setMedia(media)
        self.mediaPlayer.play()

        self.initUI()



    def initUI(self):

    #                                     INITIALIZATION STEP 1: CREATE TIMER WIDGET

        # self.timerwidget = QtWidgets.QWidget(self)
        # # self.timerwidget.setObjectName("timerwidget")
        # #
        self.timer_label = QtWidgets.QLabel(self)   #self.timerwidget
        self.timer_label.setGeometry(QtCore.QRect(1380, 720, 431, 271))
        self.timer_label.setStyleSheet("border-image: url('C:/Users/Owner/PycharmProjects/BF4 Deployment Timer/black timer background rev.jpg'); color: rgb(136, 204, 241)")

        font2 = QtGui.QFont()
        font2.setFamily("Agency FB")
        font2.setPointSize(38)

        self.timer_label.setFont(font2)
        self.timer_label.setTextFormat(QtCore.Qt.AutoText)
        self.timer_label.setObjectName("timerlabel")
        self.timer_label.setText('Awaiting Orders')
        self.timer_label.setAlignment(QtCore.Qt.AlignCenter)
        self.timer_label.setLayoutDirection(QtCore.Qt.RightToLeft)



        # timer_layout = QtWidgets.QVBoxLayout()
        # timer_layout.addWidget(self.timer_label)
        # self.setLayout(timer_layout)




        #                                 INITIALIZATION STEP 2: LOAD AUDIO FILES

        self.url_AA1 = QtCore.QUrl.fromLocalFile('C:\\Users\\Owner\\PycharmProjects\\BF4 Deployment Timer\\sound\\friendly timers\\friendly AA r\\friendly aa pt1.mp3')
        self.AA1 = QtMultimedia.QMediaContent(self.url_AA1)
        self.AA1_player = QtMultimedia.QMediaPlayer()
        self.AA1_player.setMedia(self.AA1)


        self.url_AA2 = QtCore.QUrl.fromLocalFile('C:\\Users\\Owner\\PycharmProjects\\BF4 Deployment Timer\\sound\\friendly timers\\friendly AA r\\friendly aa pt2.mp3')
        self.AA2 = QtMultimedia.QMediaContent(self.url_AA2)
        self.AA2_player = QtMultimedia.QMediaPlayer()
        self.AA2_player.setMedia(self.AA2)

        self.url_AA3 = QtCore.QUrl.fromLocalFile(
            'C:\\Users\\Owner\\PycharmProjects\\BF4 Deployment Timer\\sound\\friendly timers\\friendly AA r\\friendly aa pt3.mp3')
        self.AA3 = QtMultimedia.QMediaContent(self.url_AA3)
        self.AA3_player = QtMultimedia.QMediaPlayer()
        self.AA3_player.setMedia(self.AA3)

        self.url_AA4 = QtCore.QUrl.fromLocalFile(
            'C:\\Users\\Owner\\PycharmProjects\\BF4 Deployment Timer\\sound\\friendly timers\\friendly AA r\\friendly aa pt4.mp3')
        self.AA4 = QtMultimedia.QMediaContent(self.url_AA4)
        self.AA4_player = QtMultimedia.QMediaPlayer()
        self.AA4_player.setMedia(self.AA4)









        #                             INITIALIZATION STEP 3: CREATE VEHICLE BUTTONS

        self.AA_button = QtWidgets.QPushButton(self)                         # create AA button
        self.AA_button.setGeometry(QtCore.QRect(1500, 300, 154, 93))         # create size of icon
        AA_icon = QtGui.QIcon()                                              # create an icon object
        AA_icon.addPixmap(QtGui.QPixmap("vehicle icons/AA.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)  # give object a picture attribute
        self.AA_button.setIcon(AA_icon)                                      # assign the icon object (with pic) to the button's attribute property
        self.AA_button.setIconSize(QtCore.QSize(300, 300))                   # set size of the button
        self.AA_button.setObjectName("AA_Icon")                              # name the button
        # self.AA_button.toggle()
        self.AA_button.clicked.connect(self.AA_click)                        # connect the button to the reaction event
        self.AA_button.clicked.connect(self.timer_start)









        #                               INITIALIZATION STEP 4: CREATE 'TIMER' OBJECT
        self.countdown = QtCore.QTimer()
        self.countdown.timeout.connect(self.print_timer)
        self.countdown.timeout.connect(self.AA_click)


    #                                METHODS NEEDED FOR WIDGET FUNCTIONALITY
    def timer_start(self):
        self.countdown.start(1000)

    def print_timer(self):
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(88)

        font2 = QtGui.QFont()
        font2.setFamily("Agency FB")
        font2.setPointSize(38)

        self.timer_label.setFont(font)
        self.timer_label.setText(str(MyWindow.counter))
        MyWindow.counter -= 1
        if MyWindow.counter == 1:
            pass
        if MyWindow.counter in range(-4, 0):
            self.timer_label.setFont(font2)
            self.timer_label.setText('Ready to Deploy')
        if MyWindow.counter == -4:
            self.countdown.stop()
            MyWindow.counter = 90
            self.timer_label.setText('Awaiting Orders')




    def AA_click(self):

            if MyWindow.counter == 89:
                self.AA1_player.play()
            if MyWindow.counter == 65:
                self.AA2_player.play()
            if MyWindow.counter == 31:
                self.AA3_player.play()
            if MyWindow.counter == 12:
                self.AA4_player.play()








def run_app():
    created_app = QApplication(sys.argv)
    application = MyWindow()
    application.show()
    sys.exit(created_app.exec_())



# part 4 -- last step -- call the run_app function to launch the application

run_app()