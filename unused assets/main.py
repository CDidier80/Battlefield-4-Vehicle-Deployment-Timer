# BF4 Deployment Timer Main Excecutable

from PyQt5 import QtWidgets, QtMultimediaWidgets, QtMultimedia, QtCore, QtGui, Qt
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys



class MyWindow(QMainWindow):

    timer_countdown = 90

    def __init__(self):
        super(MyWindow, self).__init__()
        self.setGeometry(0, 0, 1920, 1080)
        self.setWindowTitle("BF4 Deployment Timer")

        self.initUI()

    def initUI(self):

                                             # INITIALIZATION



    #                                     CREATE Video Background

        # create link to movie file
        movie_file = QtCore.QUrl.fromLocalFile('file: C:/Users/Owner/PycharmProjects/BF4 Deployment Timer/'
                                               '3d video background 2.mp4')
        media = QtMultimedia.QMediaContent(movie_file)

        # create video widget
        self.videoWidget = QtMultimediaWidgets.QVideoWidget()
        self.setCentralWidget(self.videoWidget)

        # media player object   (video widget goes in media player)
        self.mediaPlayer = QtMultimedia.QMediaPlayer(None,
                                                     QtMultimedia.QMediaPlayer.VideoSurface)
        self.mediaPlayer.setVideoOutput(self.videoWidget)

        # video_playlist
        self.playlist = QtMultimedia.QMediaPlaylist()
        self.playlist.setCurrentIndex(0)
        self.playlist.setPlaybackMode(QtMultimedia.QMediaPlaylist.Loop)
        self.playlist.addMedia(media)

        # add content to media player
        self.mediaPlayer.setPlaylist(self.playlist)
        self.mediaPlayer.play()



                                         # Load and start background music

        self.music_link = QtCore.QUrl.fromLocalFile(
            'C:\\Users\\Owner\\PycharmProjects\\BF4 Deployment Timer\\sound\\Deadline background music.mp3')

        self.playlist_music = QtMultimedia.QMediaPlaylist()
        self.playlist_music.setPlaybackMode(QtMultimedia.QMediaPlaylist.Loop)

        media2 = QtMultimedia.QMediaContent(self.music_link)
        self.playlist_music.addMedia(media2)

        self.backgroundMusic_player = QtMultimedia.QMediaPlayer()   # create mediaplayer object
        self.backgroundMusic_player.setPlaylist(self.playlist_music)    # set background music as the video_playlist
        self.backgroundMusic_player.setVolume(35)
        self.backgroundMusic_player.play()                            # play it



                                           # make dark panel background

        self.blacktile_label = QtWidgets.QLabel(self)
        self.blacktile_label.setGeometry(QtCore.QRect(1313, 0, 601, 1080))    #(1380, 720, 875, 493))
        self.blacktile_label.setFrameShadow(QtWidgets.QFrame.Raised)
        self.blacktile_label.setObjectName("black panel")
        # self.timer_label.setAutoFillBackground(True)
        self.blacktile_label.setStyleSheet(
            "border-image: url('C:/Users/Owner/PycharmProjects/BF4 Deployment Timer/images/"
            "blue control console vertical.png');")
        self.blacktile_label.show()



                                             # make a label to display BF4 logo

        logo_font = QtGui.QFont()
        logo_font.setFamily("Agency FB")
        logo_font.setPointSize(26)

        self.logo_label = QtWidgets.QLabel(self)
        self.logo_label.setGeometry(QtCore.QRect(1400, 90, 425, 100))
        self.logo_label.setFrameShadow(QtWidgets.QFrame.Raised)
        self.logo_label.setTextFormat(QtCore.Qt.AutoText)
        self.logo_label.setAlignment(QtCore.Qt.AlignCenter)
        self.logo_label.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.logo_label.setText('Reinforcements Available')
        self.logo_label.setFont(logo_font)
        self.logo_label.setStyleSheet(
            "border-image: url('C:/Users/Owner/PycharmProjects/BF4 Deployment Timer/images/"
            "title background 2.png'); background-color:black; color: rgb(136, 204, 241)")
        self.logo_label.show()


                                          # make a label to display timer countdown

        self.timer_label = QtWidgets.QLabel(self)
        self.timer_label.setGeometry(QtCore.QRect(1411, 720, 417, 271))
        self.timer_label.setFrameShadow(QtWidgets.QFrame.Raised)

        self.timer_label.setStyleSheet(
            "border-image: url('C:/Users/Owner/PycharmProjects/BF4 Deployment Timer/images/"
            "blue tile background pic.jpg'); color: rgb(136, 204, 241)")
        self.timer_label.show()

        font2 = QtGui.QFont()
        font2.setFamily("Agency FB")
        font2.setPointSize(38)

        self.timer_label.setFont(font2)
        self.timer_label.setTextFormat(QtCore.Qt.AutoText)
        self.timer_label.setObjectName("timerlabel")
        self.timer_label.setText('Awaiting Orders')
        self.timer_label.setAlignment(QtCore.Qt.AlignCenter)
        self.timer_label.setLayoutDirection(QtCore.Qt.RightToLeft)


                           # Create UP and DOWN arrow buttons to manually adjust timer


        # TIMER DOWN BUTTON
        self.down_button = QtWidgets.QPushButton(self)
        self.down_button.setGeometry(QtCore.QRect(1747, 938, 30, 30))  # create size of icon
        downbutton_icon = QtGui.QIcon()
        downbutton_icon.addPixmap(QtGui.QPixmap(
            'C:/Users/Owner/PycharmProjects/BF4 Deployment Timer/images/down arrow.png'),
            QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.down_button.setIcon(downbutton_icon)
        self.down_button.setIconSize(QtCore.QSize(30, 30))
        self.down_button.setObjectName("down button")
        self.down_button.clicked.connect(self.down_button_click)


        # TIMER UP BUTTON
        self.up_button = QtWidgets.QPushButton(self)
        self.up_button.setGeometry(QtCore.QRect(1777, 938, 30, 30))
        up_button_icon = QtGui.QIcon()
        up_button_icon.addPixmap(QtGui.QPixmap(
            'C:/Users/Owner/PycharmProjects/BF4 Deployment Timer/images/up arrow rev.jpg'),
            QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.up_button.setIcon(up_button_icon)
        self.up_button.setIconSize(QtCore.QSize(30, 30))
        self.up_button.setObjectName("up button")
        self.up_button.clicked.connect(self.up_button_click)




    #                                      Create "Cancel Timer" Button

        cancel_font = QtGui.QFont()
        cancel_font.setFamily("Agency FB")
        cancel_font.setPointSize(12)


        self.cancel_button = QtWidgets.QPushButton(self)
        self.cancel_button.setFont(cancel_font)
        self.cancel_button.setGeometry(QtCore.QRect(1396, 980, 160, 30))
        self.cancel_button.setText('Cancel Orders')
        self.cancel_button.setStyleSheet('color: rgb(136, 204, 241); background-color: black;')
        self.cancel_button.setDisabled(True)
        self.cancel_button.hide()
        self.cancel_button.clicked.connect(self.cancel_clicked)



    #                              CREATE MEDIAPLAYER OBJECTS FOR SOUND EFFECTS (menu clicks)

        # Timer down beep
        self.url_timeDown = QtCore.QUrl.fromLocalFile(
            'C:\\Users\\Owner\\PycharmProjects\\BF4 Deployment Timer\\sound\\sound effects\\timer down.mp3')
        self.timeDown = QtMultimedia.QMediaContent(self.url_timeDown)
        self.timeDown_player = QtMultimedia.QMediaPlayer()
        self.timeDown_player.setMedia(self.timeDown)

        # Timer up beep
        self.url_timeUp = QtCore.QUrl.fromLocalFile(
            'C:\\Users\\Owner\\PycharmProjects\\BF4 Deployment Timer\\sound\\sound effects\\timer up.mp3')
        self.timeUp = QtMultimedia.QMediaContent(self.url_timeUp)
        self.timeUp_player = QtMultimedia.QMediaPlayer()
        self.timeUp_player.setMedia(self.timeUp)

        # error sound
        self.url_error = QtCore.QUrl.fromLocalFile(
            'C:\\Users\\Owner\\PycharmProjects\\BF4 Deployment Timer\\sound\\sound effects\\error sound.mp3')
        self.error = QtMultimedia.QMediaContent(self.url_error)
        self.error_player = QtMultimedia.QMediaPlayer()
        self.error_player.setMedia(self.error)
        self.error_player.setVolume(18)

        # radio beep (button click confirmation)
        self.url_radio = QtCore.QUrl.fromLocalFile(
            'C:\\Users\\Owner\\PycharmProjects\\BF4 Deployment Timer\\sound\\sound effects\\double radio beep.wav')
        self.radio = QtMultimedia.QMediaContent(self.url_radio)
        self.radio_player = QtMultimedia.QMediaPlayer()
        self.radio_player.setMedia(self.radio)
        # self.radio_player.setVolume(100)



                                            # LOAD VEHICLE AUDIO (4 FILES PER VEHICLE)

        #1. Anti-Air

        self.url_AA1 = QtCore.QUrl.fromLocalFile(
            'C:/Users/Owner/PycharmProjects/BF4 Deployment Timer/sound/riendly timers/friendly AA r/'
            'friendly aa pt1.mp3')
        self.AA1 = QtMultimedia.QMediaContent(self.url_AA1)
        self.AA1_player = QtMultimedia.QMediaPlayer()
        self.AA1_player.setMedia(self.AA1)

        self.url_AA2 = QtCore.QUrl.fromLocalFile(
            'C:\\Users\\Owner\\PycharmProjects\\BF4 Deployment Timer\\sound\\friendly timers\\friendly AA r\\'
            'friendly aa pt2.mp3')
        self.AA2 = QtMultimedia.QMediaContent(self.url_AA2)
        self.AA2_player = QtMultimedia.QMediaPlayer()
        self.AA2_player.setMedia(self.AA2)

        self.url_AA3 = QtCore.QUrl.fromLocalFile(
            'C:\\Users\\Owner\\PycharmProjects\\BF4 Deployment Timer\\sound\\friendly timers\\friendly AA r\\'
            'friendly aa pt3.mp3')
        self.AA3 = QtMultimedia.QMediaContent(self.url_AA3)
        self.AA3_player = QtMultimedia.QMediaPlayer()
        self.AA3_player.setMedia(self.AA3)

        self.url_AA4 = QtCore.QUrl.fromLocalFile(
            'C:\\Users\\Owner\\PycharmProjects\\BF4 Deployment Timer\\sound\\friendly timers\\friendly AA r\\'
            'friendly aa pt4.mp3')
        self.AA4 = QtMultimedia.QMediaContent(self.url_AA4)
        self.AA4_player = QtMultimedia.QMediaPlayer()
        self.AA4_player.setMedia(self.AA4)


        #2. Scout Helicopter

        self.url_sh1 = QtCore.QUrl.fromLocalFile(
            'C:\\Users\\Owner\\PycharmProjects\\BF4 Deployment Timer\\sound\\friendly timers\\'
            'friendly scout helicopter\\scout helo pt1 rev.mp3')
        self.sh1 = QtMultimedia.QMediaContent(self.url_sh1)
        self.sh1_player = QtMultimedia.QMediaPlayer()
        self.sh1_player.setMedia(self.sh1)

        self.url_sh2 = QtCore.QUrl.fromLocalFile(
            'C:\\Users\\Owner\\PycharmProjects\\BF4 Deployment Timer\\sound\\friendly timers\\'
            'friendly scout helicopter\\scout helo pt2.wav')
        self.sh2 = QtMultimedia.QMediaContent(self.url_sh2)
        self.sh2_player = QtMultimedia.QMediaPlayer()
        self.sh2_player.setMedia(self.sh2)

        self.url_sh3 = QtCore.QUrl.fromLocalFile(
            'C:\\Users\\Owner\\PycharmProjects\\BF4 Deployment Timer\\sound\\friendly timers\\'
            'friendly scout helicopter\\scout helo pt3.wav')
        self.sh3 = QtMultimedia.QMediaContent(self.url_sh3)
        self.sh3_player = QtMultimedia.QMediaPlayer()
        self.sh3_player.setMedia(self.sh3)

        self.url_sh4 = QtCore.QUrl.fromLocalFile(
            'C:\\Users\\Owner\\PycharmProjects\\BF4 Deployment Timer\\sound\\friendly timers\\'
            'friendly scout helicopter\\scout helo pt4.wav')
        self.sh4 = QtMultimedia.QMediaContent(self.url_sh4)
        self.sh4_player = QtMultimedia.QMediaPlayer()
        self.sh4_player.setMedia(self.sh4)


        #3. attack helicopter
        self.url_ah1 = QtCore.QUrl.fromLocalFile(
            'C:\\Users\\Owner\\PycharmProjects\\BF4 Deployment Timer\\sound\\friendly timers\\'
            'friendly attack helicopter\\attack helo pt1.wav')
        self.ah1 = QtMultimedia.QMediaContent(self.url_ah1)
        self.ah1_player = QtMultimedia.QMediaPlayer()
        self.ah1_player.setMedia(self.ah1)

        self.url_ah2 = QtCore.QUrl.fromLocalFile(
             'C:\\Users\\Owner\\PycharmProjects\\BF4 Deployment Timer\\sound\\friendly timers\\'
             'friendly attack helicopter\\attack helo pt2.wav')
        self.ah2 = QtMultimedia.QMediaContent(self.url_ah2)
        self.ah2_player = QtMultimedia.QMediaPlayer()
        self.ah2_player.setMedia(self.ah2)

        self.url_ah3 = QtCore.QUrl.fromLocalFile(
              'C:\\Users\\Owner\\PycharmProjects\\BF4 Deployment Timer\\sound\\friendly timers\\'
              'friendly attack helicopter\\attack helo pt3.wav')
        self.ah3 = QtMultimedia.QMediaContent(self.url_ah3)
        self.ah3_player = QtMultimedia.QMediaPlayer()
        self.ah3_player.setMedia(self.ah3)

        self.url_ah4 = QtCore.QUrl.fromLocalFile(
                'C:\\Users\\Owner\\PycharmProjects\\BF4 Deployment Timer\\sound\\friendly timers\\'
                'friendly attack helicopter\\attack helo pt4.wav')
        self.ah4 = QtMultimedia.QMediaContent(self.url_ah4)
        self.ah4_player = QtMultimedia.QMediaPlayer()
        self.ah4_player.setMedia(self.ah4)


        #4. Boat
        self.url_b1 = QtCore.QUrl.fromLocalFile(
                'C:\\Users\\Owner\\PycharmProjects\\BF4 Deployment Timer\\sound\\friendly timers\\'
                'friendly attack boat\\boat pt1.wav')
        self.b1 = QtMultimedia.QMediaContent(self.url_b1)
        self.b1_player = QtMultimedia.QMediaPlayer()
        self.b1_player.setMedia(self.b1)

        self.url_b2 = QtCore.QUrl.fromLocalFile(
                'C:\\Users\\Owner\\PycharmProjects\\BF4 Deployment Timer\\sound\\friendly timers\\'
                'friendly attack boat\\boat pt2.wav')
        self.b2 = QtMultimedia.QMediaContent(self.url_b2)
        self.b2_player = QtMultimedia.QMediaPlayer()
        self.b2_player.setMedia(self.b2)

        self.url_b3 = QtCore.QUrl.fromLocalFile(
                'C:\\Users\\Owner\\PycharmProjects\\BF4 Deployment Timer\\sound\\friendly timers\\'
                'friendly attack boat\\boat pt3.wav')
        self.b3 = QtMultimedia.QMediaContent(self.url_b3)
        self.b3_player = QtMultimedia.QMediaPlayer()
        self.b3_player.setMedia(self.b3)

        self.url_b4 = QtCore.QUrl.fromLocalFile(
                'C:\\Users\\Owner\\PycharmProjects\\BF4 Deployment Timer\\sound\\friendly timers\\'
                'friendly attack boat\\boat pt4.wav')
        self.b4 = QtMultimedia.QMediaContent(self.url_b4)
        self.b4_player = QtMultimedia.QMediaPlayer()
        self.b4_player.setMedia(self.b4)

        #5. Tank

        self.url_t1 = QtCore.QUrl.fromLocalFile(
            'C:\\Users\\Owner\\PycharmProjects\\BF4 Deployment Timer\\sound\\friendly timers\\'
            'friendly tank timer\\tank pt1.wav')
        self.t1 = QtMultimedia.QMediaContent(self.url_t1)
        self.t1_player = QtMultimedia.QMediaPlayer()
        self.t1_player.setMedia(self.t1)


        self.url_t2 = QtCore.QUrl.fromLocalFile(
            'C:\\Users\\Owner\\PycharmProjects\\BF4 Deployment Timer\\sound\\friendly timers\\'
            'friendly tank timer\\tank pt2.wav')
        self.t2 = QtMultimedia.QMediaContent(self.url_t2)
        self.t2_player = QtMultimedia.QMediaPlayer()
        self.t2_player.setMedia(self.t2)

        self.url_t3 = QtCore.QUrl.fromLocalFile(
            'C:\\Users\\Owner\\PycharmProjects\\BF4 Deployment Timer\\sound\\friendly timers\\'
            'friendly tank timer\\tank pt3.wav')
        self.t3 = QtMultimedia.QMediaContent(self.url_t3)
        self.t3_player = QtMultimedia.QMediaPlayer()
        self.t3_player.setMedia(self.t3)

        self.url_t4 = QtCore.QUrl.fromLocalFile(
            'C:\\Users\\Owner\\PycharmProjects\\BF4 Deployment Timer\\sound\\friendly timers\\'
            'friendly tank timer\\tank pt4.wav')
        self.t4 = QtMultimedia.QMediaContent(self.url_t4)
        self.t4_player = QtMultimedia.QMediaPlayer()
        self.t4_player.setMedia(self.t4)


        #6. LAV

        self.url_lav1 = QtCore.QUrl.fromLocalFile(
            'C:\\Users\\Owner\\PycharmProjects\\BF4 Deployment Timer\\sound\\friendly timers\\'
            'friendly lav\\lav pt1.wav')
        self.lav1 = QtMultimedia.QMediaContent(self.url_lav1)
        self.lav1_player = QtMultimedia.QMediaPlayer()
        self.lav1_player.setMedia(self.lav1)


        self.url_lav2 = QtCore.QUrl.fromLocalFile(
            'C:\\Users\\Owner\\PycharmProjects\\BF4 Deployment Timer\\sound\\friendly timers\\'
            'friendly lav\\lav pt2.wav')
        self.lav2 = QtMultimedia.QMediaContent(self.url_lav2)
        self.lav2_player = QtMultimedia.QMediaPlayer()
        self.lav2_player.setMedia(self.lav2)

        self.url_lav3 = QtCore.QUrl.fromLocalFile(
            'C:\\Users\\Owner\\PycharmProjects\\BF4 Deployment Timer\\sound\\friendly timers\\'
            'friendly lav\\lav pt3.wav')
        self.lav3 = QtMultimedia.QMediaContent(self.url_lav3)
        self.lav3_player = QtMultimedia.QMediaPlayer()
        self.lav3_player.setMedia(self.lav3)

        self.url_lav4 = QtCore.QUrl.fromLocalFile(
            'C:\\Users\\Owner\\PycharmProjects\\BF4 Deployment Timer\\sound\\friendly timers\\'
            'friendly lav\\lav pt4.wav')
        self.lav4 = QtMultimedia.QMediaContent(self.url_lav4)
        self.lav4_player = QtMultimedia.QMediaPlayer()
        self.lav4_player.setMedia(self.lav4)


        #7. Jet

        self.url_j1 = QtCore.QUrl.fromLocalFile(
            'C:\\Users\\Owner\\PycharmProjects\\BF4 Deployment Timer\\sound\\friendly timers\\friendly jet\\'
            'jet pt1.wav')
        self.j1 = QtMultimedia.QMediaContent(self.url_j1)
        self.j1_player = QtMultimedia.QMediaPlayer()
        self.j1_player.setMedia(self.j1)


        self.url_j2 = QtCore.QUrl.fromLocalFile(
            'C:\\Users\\Owner\\PycharmProjects\\BF4 Deployment Timer\\sound\\friendly timers\\friendly jet\\'
            'jet pt2.wav')
        self.j2 = QtMultimedia.QMediaContent(self.url_j2)
        self.j2_player = QtMultimedia.QMediaPlayer()
        self.j2_player.setMedia(self.j2)

        self.url_j3 = QtCore.QUrl.fromLocalFile(
            'C:\\Users\\Owner\\PycharmProjects\\BF4 Deployment Timer\\sound\\friendly timers\\friendly jet\\'
            'jet pt3.wav')
        self.j3 = QtMultimedia.QMediaContent(self.url_j3)
        self.j3_player = QtMultimedia.QMediaPlayer()
        self.j3_player.setMedia(self.j3)

        self.url_j4 = QtCore.QUrl.fromLocalFile(
            'C:\\Users\\Owner\\PycharmProjects\\BF4 Deployment Timer\\sound\\friendly timers\\friendly jet\\'
            'jet pt4.wav')
        self.j4 = QtMultimedia.QMediaContent(self.url_j4)
        self.j4_player = QtMultimedia.QMediaPlayer()
        self.j4_player.setMedia(self.j4)


        #8. Fighter Bomber

        self.url_fb1 = QtCore.QUrl.fromLocalFile(
            'C:\\Users\\Owner\\PycharmProjects\\BF4 Deployment Timer\\sound\\friendly timers\\'
            'friendly fighter bomber\\fighter bomber pt1.wav')
        self.fb1 = QtMultimedia.QMediaContent(self.url_fb1)
        self.fb1_player = QtMultimedia.QMediaPlayer()
        self.fb1_player.setMedia(self.fb1)


        self.url_fb2 = QtCore.QUrl.fromLocalFile(
            'C:\\Users\\Owner\\PycharmProjects\\BF4 Deployment Timer\\sound\\friendly timers\\'
            'friendly fighter bomber\\fighter bomber pt2.wav')
        self.fb2 = QtMultimedia.QMediaContent(self.url_fb2)
        self.fb2_player = QtMultimedia.QMediaPlayer()
        self.fb2_player.setMedia(self.fb2)

        self.url_fb3 = QtCore.QUrl.fromLocalFile(
            'C:\\Users\\Owner\\PycharmProjects\\BF4 Deployment Timer\\sound\\friendly timers\\'
            'friendly fighter bomber\\fighter bomber pt3.wav')
        self.fb3 = QtMultimedia.QMediaContent(self.url_fb3)
        self.fb3_player = QtMultimedia.QMediaPlayer()
        self.fb3_player.setMedia(self.fb3)

        self.url_fb4 = QtCore.QUrl.fromLocalFile(
            'C:\\Users\\Owner\\PycharmProjects\\BF4 Deployment Timer\\sound\\friendly timers\\'
            'friendly fighter bomber\\fighter bomber pt4.wav')
        self.fb4 = QtMultimedia.QMediaContent(self.url_fb4)
        self.fb4_player = QtMultimedia.QMediaPlayer()
        self.fb4_player.setMedia(self.fb4)



                                            # End of audio file upload



    #                                         CREATE VEHICLE BUTTONS


        #1. Anti Air
        self.AA_button = QtWidgets.QPushButton(self)                         # create AA button
        self.AA_button.setGeometry(QtCore.QRect(1450, 600, 146, 89))         # create size of icon
        self.AA_icon = QtGui.QIcon()                                              # create an icon object
        self.AA_icon.addPixmap(QtGui.QPixmap(
            'C:/Users/Owner/PycharmProjects/BF4 Deployment Timer/images/vehicle icons/blue icons/AA blue.jpg'),
            QtGui.QIcon.Normal, QtGui.QIcon.Off)  # give object a picture attribute
        self.AA_icon_green = QtGui.QIcon()
        self.AA_icon_green.addPixmap(QtGui.QPixmap(
            'C:/Users/Owner/PycharmProjects/BF4 Deployment Timer/images/vehicle icons/green icons/AA green.jpg'),
            QtGui.QIcon.Normal, QtGui.QIcon.Off)           # give it an green icon to switch to when pressed
        self.AA_button.setIcon(self.AA_icon)
        self.AA_button.setIconSize(QtCore.QSize(350, 350))
        self.AA_button.setObjectName("AA_button")
        self.AA_button.clicked.connect(self.AA_click)           # connect button to its click method
        self.AA_button.clicked.connect(self.timer_AA_start)     # connect button to it's timer


        #2. Tank
        self.tank_button = QtWidgets.QPushButton(self)
        self.tank_button.setGeometry(QtCore.QRect(1450, 475, 146, 89))
        self.tank_icon = QtGui.QIcon()
        self.tank_icon.addPixmap(QtGui.QPixmap(
            'C:/Users/Owner/PycharmProjects/BF4 Deployment Timer/images/vehicle icons/blue icons/tank blue.jpg'),
            QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tank_icon_green = QtGui.QIcon()
        self.tank_icon_green.addPixmap(QtGui.QPixmap(
            'C:/Users/Owner/PycharmProjects/BF4 Deployment Timer/images/vehicle icons/green icons/tank green.jpg'),
                                QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tank_button.setIcon(self.tank_icon)
        self.tank_button.setIconSize(QtCore.QSize(350, 350))
        self.tank_button.setObjectName("tank_button")
        self.tank_button.clicked.connect(self.tank_click)
        self.tank_button.clicked.connect(self.timer_tank_start)


        #3. Jet
        self.jet_button = QtWidgets.QPushButton(self)
        self.jet_button.setGeometry(QtCore.QRect(1650, 225, 146, 89))
        self.jet_icon = QtGui.QIcon()
        self.jet_icon.addPixmap(QtGui.QPixmap(
            'C:/Users/Owner/PycharmProjects/BF4 Deployment Timer/images/vehicle icons/blue icons/jet blue.jpg'),
            QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.jet_icon_green = QtGui.QIcon()
        self.jet_icon_green.addPixmap(QtGui.QPixmap(
            'C:/Users/Owner/PycharmProjects/BF4 Deployment Timer/images/vehicle icons/green icons/jet green.jpg'),
                                QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.jet_button.setIcon(self.jet_icon)
        self.jet_button.setIconSize(QtCore.QSize(350, 350))
        self.jet_button.setObjectName("jet_button")
        self.jet_button.clicked.connect(self.jet_click)
        self.jet_button.clicked.connect(self.timer_jet_start)


        #4. Scout Helicopter
        self.scout_heli_button = QtWidgets.QPushButton(self)
        self.scout_heli_button.setGeometry(QtCore.QRect(1650, 350, 146, 89))
        self.scout_heli_icon = QtGui.QIcon()
        self.scout_heli_icon.addPixmap(QtGui.QPixmap(
            'C:/Users/Owner/PycharmProjects/BF4 Deployment Timer/images/vehicle icons/blue icons/'
            'scout heli blue.png'),
            QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.scout_heli_icon_green = QtGui.QIcon()
        self.scout_heli_icon_green.addPixmap(QtGui.QPixmap(
            'C:/Users/Owner/PycharmProjects/BF4 Deployment Timer/images/vehicle icons/green icons/'
            'scout heli green.png'),
                                QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.scout_heli_button.setIcon(self.scout_heli_icon)
        self.scout_heli_button.setIconSize(QtCore.QSize(350, 350))
        self.scout_heli_button.setObjectName("scout heli button")
        self.scout_heli_button.clicked.connect(self.scout_helo_click)
        self.scout_heli_button.clicked.connect(self.timer_scout_helo_start)


        #5. Boat
        self.boat_button = QtWidgets.QPushButton(self)
        self.boat_button.setGeometry(QtCore.QRect(1650, 600, 146, 89))
        self.boat_icon = QtGui.QIcon()
        self.boat_icon.addPixmap(QtGui.QPixmap(
            'C:/Users/Owner/PycharmProjects/BF4 Deployment Timer/images/vehicle icons/blue icons/boat blue.jpg'),
            QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.boat_icon_green = QtGui.QIcon()
        self.boat_icon_green.addPixmap(QtGui.QPixmap(
            'C:/Users/Owner/PycharmProjects/BF4 Deployment Timer/images/vehicle icons/green icons/boat green.jpg'),
                                QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.boat_button.setIcon(self.boat_icon)
        self.boat_button.setIconSize(QtCore.QSize(350, 350))
        self.boat_button.setObjectName("boat icon")
        self.boat_button.clicked.connect(self.boat_click)
        self.boat_button.clicked.connect(self.timer_boat_start)


        #6. LAV
        self.lav_button = QtWidgets.QPushButton(self)
        self.lav_button.setGeometry(QtCore.QRect(1650, 475, 146, 89))
        self.lav_icon = QtGui.QIcon()
        self.lav_icon.addPixmap(QtGui.QPixmap(
            'C:/Users/Owner/PycharmProjects/BF4 Deployment Timer/images/vehicle icons/blue icons/lav blue.jpg'),
            QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.lav_icon_green = QtGui.QIcon()
        self.lav_icon_green.addPixmap(QtGui.QPixmap(
            'C:/Users/Owner/PycharmProjects/BF4 Deployment Timer/images/vehicle icons/green icons/lav green.jpg'),
                                QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.lav_button.setIcon(self.lav_icon)
        self.lav_button.setIconSize(QtCore.QSize(350, 350))
        self.lav_button.setObjectName("LAV button")
        self.lav_button.clicked.connect(self.lav_click)
        self.lav_button.clicked.connect(self.timer_lav_start)


        #7. attack helo
        self.attack_helo_button = QtWidgets.QPushButton(self)
        self.attack_helo_button.setGeometry(QtCore.QRect(1450, 350, 146, 89))
        self.attack_helo_icon = QtGui.QIcon()
        self.attack_helo_icon.addPixmap(QtGui.QPixmap(
            'C:/Users/Owner/PycharmProjects/BF4 Deployment Timer/images/vehicle icons/blue icons/'
            'attack helo blue.jpg')
            , QtGui.QIcon.Normal, QtGui.QIcon.Off)

        self.attack_helo_icon_green = QtGui.QIcon()
        self.attack_helo_icon_green.addPixmap(QtGui.QPixmap(
            'C:/Users/Owner/PycharmProjects/BF4 Deployment Timer/images/vehicle icons/green icons/'
            'attack helo green.jpg'),
                                QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.attack_helo_button.setIcon(self.attack_helo_icon)
        self.attack_helo_button.setIconSize(QtCore.QSize(350, 350))
        self.attack_helo_button.setObjectName("attack helo icon")
        self.attack_helo_button.clicked.connect(self.attack_helo_click)
        self.attack_helo_button.clicked.connect(self.timer_attack_helo_start)


        #8. fighter bomber
        self.fighter_bomber_button = QtWidgets.QPushButton(self)
        self.fighter_bomber_button.setGeometry(QtCore.QRect(1450, 225, 146, 89))
        self.fighter_bomber_icon = QtGui.QIcon()
        self.fighter_bomber_icon.addPixmap(QtGui.QPixmap(
            'C:/Users/Owner/PycharmProjects/BF4 Deployment Timer/images/vehicle icons/blue icons/bomber blue.jpg'),
            QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.fighter_bomber_icon_green = QtGui.QIcon()
        self.fighter_bomber_icon_green.addPixmap(QtGui.QPixmap(
            'C:/Users/Owner/PycharmProjects/BF4 Deployment Timer/images/vehicle icons/green icons/bomber green.jpg'),
                                QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.fighter_bomber_button.setIcon(self.fighter_bomber_icon)
        self.fighter_bomber_button.setIconSize(QtCore.QSize(350, 350))
        self.fighter_bomber_button.setObjectName("Fighter Bomber button")
        self.fighter_bomber_button.clicked.connect(self.fighter_bomber_click)
        self.fighter_bomber_button.clicked.connect(self.timer_fighter_bomber_start)




        #                                CREATE TIMERS (OBJECTS) FOR EACH VEHICLE

        #1. AA
        self.countdown_AA = QtCore.QTimer()
        self.countdown_AA.timeout.connect(self.print_timer)
        self.countdown_AA.timeout.connect(self.AA_click)

        #2. Scout Helo
        self.countdown_scout_helo = QtCore.QTimer()
        self.countdown_scout_helo.timeout.connect(self.print_timer)
        self.countdown_scout_helo.timeout.connect(self.scout_helo_click)

        #3. Attack Helo
        self.countdown_attack_helo = QtCore.QTimer()
        self.countdown_attack_helo.timeout.connect(self.print_timer)
        self.countdown_attack_helo.timeout.connect(self.attack_helo_click)

        #4. Boat
        self.countdown_boat = QtCore.QTimer()
        self.countdown_boat.timeout.connect(self.print_timer)
        self.countdown_boat.timeout.connect(self.boat_click)

        #5. Tank
        self.countdown_tank = QtCore.QTimer()
        self.countdown_tank.timeout.connect(self.print_timer)
        self.countdown_tank.timeout.connect(self.tank_click)

        #6. LAV
        self.countdown_lav = QtCore.QTimer()
        self.countdown_lav.timeout.connect(self.print_timer)
        self.countdown_lav.timeout.connect(self.lav_click)

        #7. Jet
        self.countdown_jet = QtCore.QTimer()
        self.countdown_jet.timeout.connect(self.print_timer)
        self.countdown_jet.timeout.connect(self.jet_click)

        #8. Fighter Bomber
        self.countdown_fighter_bomber = QtCore.QTimer()
        self.countdown_fighter_bomber.timeout.connect(self.print_timer)
        self.countdown_fighter_bomber.timeout.connect(self.fighter_bomber_click)





        # Create lists for buttons and timer objects. For loops will be used to reset default states of each.


        self.vehicle_audio_list = [self.AA1_player, self.AA2_player, self.AA3_player, self.AA4_player,
                                   self.sh1_player, self.sh2_player, self.sh3_player, self.sh4_player,
                                   self.ah1_player, self.ah2_player, self.ah3_player, self.ah4_player,
                                   self.b1_player, self.b2_player, self.b3_player, self.b4_player,
                                   self.t1_player, self.t2_player, self.t3_player, self.t4_player,
                                   self.lav1_player, self.lav2_player, self.lav3_player, self.lav4_player,
                                   self.j1_player, self.j2_player, self.j3_player, self.j4_player,
                                   self.fb1_player, self.fb2_player, self.fb3_player, self.fb4_player]


        self.timer_obj_list = [self.countdown_AA, self.countdown_scout_helo, self.countdown_attack_helo,
                               self.countdown_boat, self.countdown_tank, self.countdown_fighter_bomber,
                               self.countdown_jet, self.countdown_lav]

        # self.vehicle_button_list = [self.fighter_bomber_button, self.attack_helo_button, self.lav_button,
        #                             self.boat_button, self.scout_heli_button, self.jet_button, self.tank_button,
        #                             self.AA_button]



        # create dictionary pairing buttons and their default icons to make resetting to default easy
        self.button_icon_dict = {
            self.fighter_bomber_button: self.fighter_bomber_icon,
            self.attack_helo_button: self.attack_helo_icon,
            self.lav_button: self.lav_icon,
            self.boat_button: self.boat_icon,
            self.scout_heli_button: self.scout_heli_icon,
            self.jet_button: self.jet_icon,
            self.tank_button: self.tank_icon,
            self.AA_button: self.AA_icon,

        }



                                #           END OF INITIALIZATION





    #                                METHODS NEEDED FOR WIDGET FUNCTIONALITY


    # Manually Adjust Timer
    def down_button_click(self):
        MyWindow.timer_countdown -= 1                               # increment timer by -1
        self.timeUp_player.play()                           # play sound effect for this button
        self.timer_label.setText(str(MyWindow.timer_countdown))     # update the timer text


    def up_button_click(self):
        MyWindow.timer_countdown += 1                               # increment the timer by +1
        self.timeDown_player.play()                         # play the sound effect for this button
        self.timer_label.setText(str(MyWindow.timer_countdown))     # update the timer text

                                                # RESET METHODS

    # this method resets other active timers so user can start a new timer with a new vehicle without conflicts
    def cancel_timers(self):
        font4 = QtGui.QFont()
        font4.setFamily("Agency FB")
        font4.setPointSize(38)

        for timer_obj in self.timer_obj_list:
            if timer_obj.isActive() == True:                     # if a timer is active, stop it
                timer_obj.stop()
                MyWindow.timer_countdown = 90                            # reset the time timer_countdown to 90
                self.timer_label.setText('Awaiting Orders')      # return to default message of timer
                self.timer_label.setFont(font4)
                self.timer_label.setStyleSheet(                  # resets timer label background to default
                    "border-image: url('C:/Users/Owner/PycharmProjects/BF4 Deployment Timer/images/"
                    "blue tile background pic.jpg'); color: rgb(136, 204, 241)")



    # this method resets button icons to default blue (using above dictionary)
    def reset_button_colors(self):
        for vehicle_button in self.button_icon_dict.keys():
            vehicle_button.setIcon(self.button_icon_dict.get(vehicle_button))


    # this method stops mp3 playback
    def reset_audio(self):
        for mp3 in self.vehicle_audio_list:
            if mp3.state() == 1:                   # if any vehicle audio is active, stop it
                mp3.stop()


    # combines all needed resets in a single method. Together they are a total reset
    def reset_process(self):
        self.cancel_timers()
        self.reset_button_colors()
        self.reset_audio()

                                                # end of reset methods

                                       # create 'cancel orders' method (reset)
    def cancel_clicked(self):
        self.error_player.play()                 # plays the cancel orders sound effect
        self.reset_process()                     # resets the page
        self.cancel_button.hide()                # hides the cancel button after it has been pressed


                                            #  Vehicle Timer Start Methods

    def timer_AA_start(self):
        self.radio_player.play()                       # makes a sound effect to confirm button press
        self.reset_process()                           # resets the screen and time
        self.AA_button.setIcon(self.AA_icon_green)     # changes the selected vehicle's icon to green
        self.countdown_AA.start(1000)                  # starts the countdown

    def timer_scout_helo_start(self):
        self.radio_player.play()
        self.reset_process()
        self.scout_heli_button.setIcon(self.scout_heli_icon_green)
        self.countdown_scout_helo.start(1000)

    def timer_attack_helo_start(self):
        self.radio_player.play()
        self.reset_process()
        self.attack_helo_button.setIcon(self.attack_helo_icon_green)
        self.countdown_attack_helo.start(1000)

    def timer_boat_start(self):
        self.radio_player.play()
        self.reset_process()
        self.boat_button.setIcon(self.boat_icon_green)
        self.countdown_boat.start(1000)

    def timer_tank_start(self):
        self.radio_player.play()
        self.reset_process()
        self.tank_button.setIcon(self.tank_icon_green)
        self.countdown_tank.start(1000)

    def timer_lav_start(self):
        self.radio_player.play()
        self.reset_process()
        self.lav_button.setIcon(self.lav_icon_green)
        self.countdown_lav.start(1000)

    def timer_jet_start(self):
        self.radio_player.play()
        self.reset_process()
        self.jet_button.setIcon(self.jet_icon_green)
        self.countdown_jet.start(1000)

    def timer_fighter_bomber_start(self):
        self.radio_player.play()
        self.reset_process()
        self.fighter_bomber_button.setIcon(self.fighter_bomber_icon_green)
        self.countdown_fighter_bomber.start(1000)



                                                # Display Countdown Method

    def print_timer(self):

        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(88)

        font2 = QtGui.QFont()
        font2.setFamily("Agency FB")
        font2.setPointSize(38)

        self.timer_label.setFont(font)
        self.timer_label.setText(str(MyWindow.timer_countdown))
        MyWindow.timer_countdown -= 1
        self.cancel_button.show()

        if MyWindow.timer_countdown in range(10, 90):   # sets color for text and label background for timer for 79 seconds
            self.timer_label.setStyleSheet(
                "border-image: url('C:/Users/Owner/PycharmProjects/BF4 Deployment Timer/images/"
                "blue tile background pic.jpg'); color: rgb(136, 204, 241)")

        if MyWindow.timer_countdown in range(0, 10):    # changes timer text to red in final 10 seconds
            self.timer_label.setStyleSheet(
                "border-image: url('C:/Users/Owner/PycharmProjects/BF4 Deployment Timer/images/"
                "blue tile background pic.jpg'); color: red")

        if MyWindow.timer_countdown in range(-4, 0):    # after hitting 0, a new message is displayed
            self.timer_label.setFont(font2)
            self.timer_label.setStyleSheet(
                "border-image: url('C:/Users/Owner/PycharmProjects/BF4 Deployment Timer/images/"
                "blue tile background pic.jpg'); color: rgb(98, 255, 0)")
            self.timer_label.setText('Ready to Deploy')
            self.reset_button_colors()          # set colors to default

        if MyWindow.timer_countdown == -4:             # stop the timer at -4, resets all attributes to default state
            self.cancel_timers()
            MyWindow.timer_countdown = 90
            self.timer_label.setStyleSheet(
                "border-image: url('C:/Users/Owner/PycharmProjects/BF4 Deployment Timer/images/"
                "blue tile background pic.jpg'); color: rgb(136, 204, 241)")
            self.timer_label.setText('Awaiting Orders')
            self.reset_audio()
            self.cancel_button.setDisabled(True)
            self.cancel_button.hide()
            print('process ended')


                                             # Vehicle Button Click Methods

    def AA_click(self):

        # self.AA_button.setIcon(self.AA_icon_green)
        if MyWindow.timer_countdown == 89:
            self.AA1_player.play()
        if MyWindow.timer_countdown == 65:
            self.AA2_player.play()
        if MyWindow.timer_countdown == 31:
            self.AA3_player.play()
        if MyWindow.timer_countdown == 12:
            self.AA4_player.play()
        if self.countdown_AA.isActive() == False:
            self.AA_button.setIcon(self.AA_icon)

    def tank_click(self):

        self.tank_button.setIcon(self.tank_icon_green)
        if MyWindow.timer_countdown == 89:
            self.t1_player.play()
        if MyWindow.timer_countdown == 63:
            self.t2_player.play()
        if MyWindow.timer_countdown == 32:
            self.t3_player.play()
        if MyWindow.timer_countdown == 12:
            self.t4_player.play()
        if self.countdown_tank.isActive() == False:
            self.tank_button.setIcon(self.tank_icon)


    def jet_click(self):

        self.jet_button.setIcon(self.jet_icon_green)
        if MyWindow.timer_countdown == 89:
            self.j1_player.play()
        if MyWindow.timer_countdown == 62:
            self.j2_player.play()
        if MyWindow.timer_countdown == 32:
            self.j3_player.play()
        if MyWindow.timer_countdown == 12:
            self.j4_player.play()
        if self.countdown_jet.isActive() == False:
            self.jet_button.setIcon(self.jet_icon)


    def scout_helo_click(self):

        self.scout_heli_button.setIcon(self.scout_heli_icon_green)
        if MyWindow.timer_countdown == 89:
            self.sh1_player.play()
        if MyWindow.timer_countdown == 63:
            self.sh2_player.play()
        if MyWindow.timer_countdown == 31:
            self.sh3_player.play()
        if MyWindow.timer_countdown == 12:
            self.sh4_player.play()
        if self.countdown_scout_helo.isActive() == False:
            self.scout_heli_button.setIcon(self.scout_heli_icon)

    def boat_click(self):

        self.boat_button.setIcon(self.boat_icon_green)
        if MyWindow.timer_countdown == 89:
            self.b1_player.play()
        if MyWindow.timer_countdown == 63:
            self.b2_player.play()
        if MyWindow.timer_countdown == 31:
            self.b3_player.play()
        if MyWindow.timer_countdown == 12:
            self.b4_player.play()
        if self.countdown_boat.isActive() == False:
            self.boat_button.setIcon(self.boat_icon)

    def lav_click(self):

        self.lav_button.setIcon(self.lav_icon_green)
        if MyWindow.timer_countdown == 89:
            self.lav1_player.play()
        if MyWindow.timer_countdown == 62:
            self.lav2_player.play()
        if MyWindow.timer_countdown == 32:
            self.lav3_player.play()
        if MyWindow.timer_countdown == 11:
            self.lav4_player.play()
        if self.countdown_lav.isActive() == False:
            self.lav_button.setIcon(self.lav_icon)

    def fighter_bomber_click(self):

        self.fighter_bomber_button.setIcon(self.fighter_bomber_icon_green)
        if MyWindow.timer_countdown == 89:
            self.fb1_player.play()
        if MyWindow.timer_countdown == 64:
            self.fb2_player.play()
        if MyWindow.timer_countdown == 31:
            self.fb3_player.play()
        if MyWindow.timer_countdown == 12:
            self.fb4_player.play()
        if self.countdown_fighter_bomber.isActive() == False:
            self.fighter_bomber_button.setIcon(self.fighter_bomber_icon)


    def attack_helo_click(self):

        self.attack_helo_button.setIcon(self.attack_helo_icon_green)
        if MyWindow.timer_countdown == 89:
            self.ah1_player.play()
        if MyWindow.timer_countdown == 63:
            self.ah2_player.play()
        if MyWindow.timer_countdown == 32:
            self.ah3_player.play()
        if MyWindow.timer_countdown == 12:
            self.ah4_player.play()
        if self.countdown_attack_helo.isActive() == False:
            self.attack_helo_button.setIcon(self.attack_helo_icon)


                                                # APP READY TO RUN
def run_app():
    created_app = QApplication(sys.argv)
    application = MyWindow()
    application.show()
    sys.exit(created_app.exec_())



# last step -- call the run_app function to launch the application

run_app()