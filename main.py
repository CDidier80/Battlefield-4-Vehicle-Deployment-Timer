# BF4 Deployment Timer Main Excecutable

from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent, QMediaPlaylist
from PyQt5.QtMultimediaWidgets import QVideoWidget
from PyQt5.QtWidgets import QLabel, QPushButton
from PyQt5.QtGui import QFont, QPixmap, QIcon
from PyQt5.QtWidgets import QApplication, QMainWindow, QFrame
from PyQt5.QtCore import QTimer, QUrl, QRect, Qt, QSize
import sys


# noinspection PyAttributeOutsideInit
class BF4TimerGUI(QMainWindow):
    """Class which inherits QMainWindow to produce the GUI object of the program."""
    counter = 90
    """This variable stores the default (90 seconds) OR remaining seconds in the countdown."""

    def __init__(self):
        """Sets window size, window title and calls 10 """
        super(BF4TimerGUI, self).__init__()
        self.setGeometry(0, 0, 1920, 1080)
        self.setWindowTitle("BF4 Deployment Timer")
        self.vehicle_audio_index = 0  # sets a default index value for selecting an audio video_playlist later
        print("Main Window Configuration successful")
        # Content initialization methods
        self.init_default_variable_states()
        print("init_default_variable_states() successful")
        self.init_fonts()
        print("init_fonts() successful")
        self.init_video_background()
        print("init_video_background() successful")
        self.init_background_music()
        print("init_background_music() successful")
        self.init_background_images()
        print("init_background_images() sucessful")
        self.init_buttons()
        print("init_buttons() successful")
        self.init_sound_effects()
        print("init_sound_effects() successful")
        self.init_vehicle_audio()
        print("init_vehicle_audio() successful")
        self.init_vehicle_buttons()
        print("init_vehicle_buttons() successful")
        self.init_timer()
        print("init_timer() successful")
        self.init_timer_audio_lists()
        print("init_timer_audio_lists() successful")
        self.init_icon_dict()
        print("init_icon_dict() successful")

    def init_default_variable_states(self):
        """Defines and sets default values for important, miscellaneous class variables."""

        self.blacktile_default_style = "border-image: url('./media/images/backgrounds/control console.png');"
        self.logo_label_default_style = "border-image: url('./media/images/backgrounds/title background.png'); " \
                                        "background-color:black; color: rgb(136, 204, 241)"
        self.timer_label_default_style = "border-image: url('./media/images/backgrounds/tile background.jpg'); color:" \
                                         "rgb(136, 204, 241) "
        self.timer_label_10sec_style = "border-image: url('./media/images/backgrounds/tile background.jpg'); color: " \
                                       "red; "
        self.timer_label_deploy_style = "border-image: url('./media/images/backgrounds/tile background.jpg'); color: " \
                                        "rgb(98, 255, 0);"

    def init_fonts(self):
        """In this method font attributes are passed to QFont Objects.

        These QFont objects are then passed to other text-based PyQt5 objects to set their font style.
        """

        self.cancel_font = QFont("Agency FB", 12)
        self.logo_font = QFont('Agency FB', 26)
        self.standard_font = QFont('Agency FB', 38)
        self.timer_display_font = QFont("Agency FB", 88)

        # CREATE VIDEO BACKGROUND

    def init_video_background(self):
        """Creates/configures the PyQt5 objects necessary to launch the video background of the application.

         A new QVideoWidget is passed to a QMediaPlayer object ( a general media playback object in PyQt5). The
         QMediaPlayer is configured as a 'VideoSurface' for video compatibility. The url to the video background is
         passed to a QMediaPlaylist set to loop. The video_playlist is then passed to the QMediaPlayer and playback
         starts.
         """

        self.video_widget = QVideoWidget()
        # QVideoWidget must be set as Central Widget to play in background - otherwise it plays in a separate window
        self.setCentralWidget(self.video_widget)

        self.video_player = QMediaPlayer(None, QMediaPlayer.VideoSurface)
        self.video_player.setVideoOutput(self.video_widget)

        self.video_playlist = QMediaPlaylist()
        self.video_playlist.setCurrentIndex(0)
        self.video_playlist.setPlaybackMode(QMediaPlaylist.Loop)
        self.video_playlist.addMedia(QMediaContent(QUrl.fromLocalFile('./media/video/background_video.mp4')))

        self.video_player.setPlaylist(self.video_playlist)
        self.video_player.play()

    def init_background_music(self):
        """Creates/configures the PyQt5 objects necessary to play the background music of the application.

        A url to the background music is passed to a QMediaPlaylist object set to loop. The video_playlist is passed to
        a QMediaPlayer object which sets the volume and plays the music.
        """

        self.background_music_playlist = QMediaPlaylist()
        self.background_music_playlist.setPlaybackMode(QMediaPlaylist.Loop)
        self.background_music_playlist.addMedia(
            QMediaContent(QUrl.fromLocalFile('./media/audio/Deadline background music.mp3')))

        self.backgroundMusic_player = QMediaPlayer(None, QMediaPlayer.LowLatency)
        self.backgroundMusic_player.setPlaylist(self.background_music_playlist)
        self.backgroundMusic_player.setVolume(35)
        self.backgroundMusic_player.play()

    def init_background_images(self):
        """ Creates/styles the PyQt5 objects that serve as image backgrounds for various GUI widgets."""

        self.blacktile_label = QLabel(self)
        self.blacktile_label.setGeometry(QRect(1313, 0, 601, 1080))
        self.blacktile_label.setFrameShadow(QFrame.Raised)
        self.blacktile_label.setStyleSheet(self.blacktile_default_style)
        self.blacktile_label.show()

        self.logo_label = QLabel(self)
        self.logo_label.setGeometry(QRect(1400, 90, 425, 100))
        self.logo_label.setFrameShadow(QFrame.Raised)
        self.logo_label.setTextFormat(Qt.AutoText)
        self.logo_label.setAlignment(Qt.AlignCenter)
        self.logo_label.setLayoutDirection(Qt.RightToLeft)
        self.logo_label.setText('Reinforcements Available')
        self.logo_label.setFont(self.logo_font)
        self.logo_label.setStyleSheet(self.logo_label_default_style)
        self.logo_label.show()

        self.timer_label = QLabel(self)
        self.timer_label.setGeometry(QRect(1411, 720, 417, 271))
        self.timer_label.setFrameShadow(QFrame.Raised)
        self.timer_label.setStyleSheet(self.timer_label_default_style)
        self.timer_label.setFont(self.standard_font)
        self.timer_label.setTextFormat(Qt.AutoText)
        self.timer_label.setText('Awaiting Orders')
        self.timer_label.setAlignment(Qt.AlignCenter)
        self.timer_label.setLayoutDirection(Qt.RightToLeft)
        self.timer_label.show()

    def init_buttons(self):
        """Creates, styles and connects buttons on the GUI to their "on-click" functions.

        Attributes:
            self.timer_down         A down-arrow button that increments active timer by -1
            self.timer_up           An up-arrow button that increments active timer by +1
            self.cancel_button      Cancels timer and resets GUI to default state
        """

        # TIMER DOWN BUTTON
        self.timer_down = QPushButton(self)
        self.timer_down.setGeometry(QRect(1747, 938, 30, 30))
        downbutton_icon = QIcon()
        downbutton_icon.addPixmap(QPixmap('./media/images/controls/down arrow.png'), QIcon.Normal, QIcon.Off)
        self.timer_down.setIcon(downbutton_icon)
        self.timer_down.setIconSize(QSize(30, 30))
        self.timer_down.setObjectName("timer down button")
        self.timer_down.clicked.connect(self.timer_down_click)

        # TIMER UP BUTTON
        self.timer_up = QPushButton(self)
        self.timer_up.setGeometry(QRect(1777, 938, 30, 30))
        up_button_icon = QIcon()
        up_button_icon.addPixmap(QPixmap('./media/images/controls/up arrow.jpg'), QIcon.Normal, QIcon.Off)
        self.timer_up.setIcon(up_button_icon)
        self.timer_up.setIconSize(QSize(30, 30))
        self.timer_up.setObjectName("timer up button")
        self.timer_up.clicked.connect(self.up_button_click)

        # "Cancel Timer" BUTTON

        self.cancel_button = QPushButton(self)
        self.cancel_button.setFont(self.cancel_font)
        self.cancel_button.setGeometry(QRect(1396, 980, 160, 30))
        self.cancel_button.setText('Cancel Orders')
        self.cancel_button.setStyleSheet('color: rgb(136, 204, 241); background-color: black;')
        self.cancel_button.hide()
        self.cancel_button.clicked.connect(self.cancel_clicked)

                            # CREATE QMEDIAPLAYER OBJECTS FOR SOUND EFFECTS (menu clicks)

    def init_sound_effects(self):
        """Links sound effects to various menu button clicks."""

        # TIMER DOWN BEEP
        self.url_timeDown = QUrl.fromLocalFile('./media/audio/sound effects/timer down.mp3')
        self.timeDown = QMediaContent(self.url_timeDown)
        self.timeDown_player = QMediaPlayer(None, QMediaPlayer.LowLatency)
        self.timeDown_player.setMedia(self.timeDown)

        # TIMER UP BEEP
        self.url_timeUp = QUrl.fromLocalFile('./media/audio/sound effects/timer up.mp3')
        self.timeUp = QMediaContent(self.url_timeUp)
        self.timeUp_player = QMediaPlayer(None, QMediaPlayer.LowLatency)
        self.timeUp_player.setMedia(self.timeUp)

        # ERROR SOUND
        self.url_error = QUrl.fromLocalFile('./media/audio/sound effects/error sound.mp3')
        self.error = QMediaContent(self.url_error)
        self.error_player = QMediaPlayer(None, QMediaPlayer.LowLatency)
        self.error_player.setMedia(self.error)
        self.error_player.setVolume(18)

        # RADIO BEEP
        self.url_radio = QUrl.fromLocalFile('./media/audio/sound effects/double radio beep.wav')
        self.radio = QMediaContent(self.url_radio)
        self.radio_player = QMediaPlayer(None, QMediaPlayer.LowLatency)
        self.radio_player.setMedia(self.radio)
        # self.radio_player.setVolume(100)

    def init_vehicle_audio(self):
        """Creates QMediaPlayer objects to play audio files for command center dialogue."""

        # 1. Anti-Air

        # Audio File #1
        self.url_AA1 = QUrl.fromLocalFile('./media/audio/friendly timers/AA/AA1.mp3')
        self.AA1 = QMediaContent(self.url_AA1)
        self.AA1_player = QMediaPlayer(None, QMediaPlayer.LowLatency)
        self.AA1_player.setMedia(self.AA1)

        # Audio File #2
        self.url_AA2 = QUrl.fromLocalFile('./media/audio/friendly timers/AA/AA2.mp3')
        self.AA2 = QMediaContent(self.url_AA2)
        self.AA2_player = QMediaPlayer(None, QMediaPlayer.LowLatency)
        self.AA2_player.setMedia(self.AA2)

        # Audio File #3
        self.url_AA3 = QUrl.fromLocalFile('./media/audio/friendly timers/AA/AA3.mp3')
        self.AA3 = QMediaContent(self.url_AA3)
        self.AA3_player = QMediaPlayer(None, QMediaPlayer.LowLatency)
        self.AA3_player.setMedia(self.AA3)

        # Audio File #4
        self.url_AA4 = QUrl.fromLocalFile('./media/audio/friendly timers/AA/AA4.mp3')
        self.AA4 = QMediaContent(self.url_AA4)
        self.AA4_player = QMediaPlayer(None, QMediaPlayer.LowLatency)
        self.AA4_player.setMedia(self.AA4)

        # 2. Scout Helicopter

        # Audio File #1
        self.url_sh1 = QUrl.fromLocalFile('./media/audio/friendly timers/scout heli/SH1.mp3')
        self.sh1 = QMediaContent(self.url_sh1)
        self.sh1_player = QMediaPlayer(None, QMediaPlayer.LowLatency)
        self.sh1_player.setMedia(self.sh1)

        # Audio File #2
        self.url_sh2 = QUrl.fromLocalFile('./media/audio/friendly timers/scout heli/SH2.mp3')
        self.sh2 = QMediaContent(self.url_sh2)
        self.sh2_player = QMediaPlayer(None, QMediaPlayer.LowLatency)
        self.sh2_player.setMedia(self.sh2)

        # Audio File #3
        self.url_sh3 = QUrl.fromLocalFile('./media/audio/friendly timers/scout heli/SH3.mp3')
        self.sh3 = QMediaContent(self.url_sh3)
        self.sh3_player = QMediaPlayer(None, QMediaPlayer.LowLatency)
        self.sh3_player.setMedia(self.sh3)

        # Audio File #4
        self.url_sh4 = QUrl.fromLocalFile('./media/audio/friendly timers/scout heli/SH4.mp3')
        self.sh4 = QMediaContent(self.url_sh4)
        self.sh4_player = QMediaPlayer(None, QMediaPlayer.LowLatency)
        self.sh4_player.setMedia(self.sh4)

        # 3. Attack Helicopter

        # Audio File 1
        self.url_ah1 = QUrl.fromLocalFile('./media/audio/friendly timers/attack heli/AH1.wav')
        self.ah1 = QMediaContent(self.url_ah1)
        self.ah1_player = QMediaPlayer(None, QMediaPlayer.LowLatency)
        self.ah1_player.setMedia(self.ah1)

        # Audio File #2
        self.url_ah2 = QUrl.fromLocalFile('./media/audio/friendly timers/attack heli/AH2.wav')
        self.ah2 = QMediaContent(self.url_ah2)
        self.ah2_player = QMediaPlayer(None, QMediaPlayer.LowLatency)
        self.ah2_player.setMedia(self.ah2)

        # Audio File #3
        self.url_ah3 = QUrl.fromLocalFile('./media/audio/friendly timers/attack heli/AH3.wav')
        self.ah3 = QMediaContent(self.url_ah3)
        self.ah3_player = QMediaPlayer(None, QMediaPlayer.LowLatency)
        self.ah3_player.setMedia(self.ah3)

        # Audio File #4
        self.url_ah4 = QUrl.fromLocalFile('./media/audio/friendly timers/attack heli/AH4.wav')
        self.ah4 = QMediaContent(self.url_ah4)
        self.ah4_player = QMediaPlayer(None, QMediaPlayer.LowLatency)
        self.ah4_player.setMedia(self.ah4)

        # 4. Attack Boat

        # Audio File #1
        self.url_b1 = QUrl.fromLocalFile('./media/audio/friendly timers/attack boat/B1.wav')
        self.b1 = QMediaContent(self.url_b1)
        self.b1_player = QMediaPlayer(None, QMediaPlayer.LowLatency)
        self.b1_player.setMedia(self.b1)

        # Audio File #2
        self.url_b2 = QUrl.fromLocalFile('./media/audio/friendly timers/attack boat/B2.wav')
        self.b2 = QMediaContent(self.url_b2)
        self.b2_player = QMediaPlayer(None, QMediaPlayer.LowLatency)
        self.b2_player.setMedia(self.b2)

        # Audio File #3
        self.url_b3 = QUrl.fromLocalFile('./media/audio/friendly timers/attack boat/B3.wav')
        self.b3 = QMediaContent(self.url_b3)
        self.b3_player = QMediaPlayer(None, QMediaPlayer.LowLatency)
        self.b3_player.setMedia(self.b3)

        # Audio File #4
        self.url_b4 = QUrl.fromLocalFile('./media/audio/friendly timers/attack boat/B4.wav')
        self.b4 = QMediaContent(self.url_b4)
        self.b4_player = QMediaPlayer(None, QMediaPlayer.LowLatency)
        self.b4_player.setMedia(self.b4)

        # 5. Tank

        # Audio File #1
        self.url_t1 = QUrl.fromLocalFile('./media/audio/friendly timers/tank/T1.wav')
        self.t1 = QMediaContent(self.url_t1)
        self.t1_player = QMediaPlayer(None, QMediaPlayer.LowLatency)
        self.t1_player.setMedia(self.t1)

        # Audio File #2
        self.url_t2 = QUrl.fromLocalFile('./media/audio/friendly timers/tank/T2.wav')
        self.t2 = QMediaContent(self.url_t2)
        self.t2_player = QMediaPlayer(None, QMediaPlayer.LowLatency)
        self.t2_player.setMedia(self.t2)

        # Audio File #3
        self.url_t3 = QUrl.fromLocalFile('./media/audio/friendly timers/tank/T3.wav')
        self.t3 = QMediaContent(self.url_t3)
        self.t3_player = QMediaPlayer(None, QMediaPlayer.LowLatency)
        self.t3_player.setMedia(self.t3)

        # Audio File #4
        self.url_t4 = QUrl.fromLocalFile('./media/audio/friendly timers/tank/T4.wav')
        self.t4 = QMediaContent(self.url_t4)
        self.t4_player = QMediaPlayer(None, QMediaPlayer.LowLatency)
        self.t4_player.setMedia(self.t4)

        # 6. LAV

        # Audio File #1
        self.url_lav1 = QUrl.fromLocalFile('./media/audio/friendly timers/lav/LAV1.wav')
        self.lav1 = QMediaContent(self.url_lav1)
        self.lav1_player = QMediaPlayer(None, QMediaPlayer.LowLatency)
        self.lav1_player.setMedia(self.lav1)

        # Audio File #2
        self.url_lav2 = QUrl.fromLocalFile('./media/audio/friendly timers/lav/LAV2.wav')
        self.lav2 = QMediaContent(self.url_lav2)
        self.lav2_player = QMediaPlayer(None, QMediaPlayer.LowLatency)
        self.lav2_player.setMedia(self.lav2)

        # Audio File #3
        self.url_lav3 = QUrl.fromLocalFile('./media/audio/friendly timers/lav/LAV3.wav')
        self.lav3 = QMediaContent(self.url_lav3)
        self.lav3_player = QMediaPlayer(None, QMediaPlayer.LowLatency)
        self.lav3_player.setMedia(self.lav3)

        # Audio File #4
        self.url_lav4 = QUrl.fromLocalFile('./media/audio/friendly timers/lav/LAV4.wav')
        self.lav4 = QMediaContent(self.url_lav4)
        self.lav4_player = QMediaPlayer(None, QMediaPlayer.LowLatency)
        self.lav4_player.setMedia(self.lav4)

        # 7. Jet

        # Audio File #1
        self.url_j1 = QUrl.fromLocalFile('./media/audio/friendly timers/jet/J1.wav')
        self.j1 = QMediaContent(self.url_j1)
        self.j1_player = QMediaPlayer(None, QMediaPlayer.LowLatency)
        self.j1_player.setMedia(self.j1)

        # Audio File #2
        self.url_j2 = QUrl.fromLocalFile('./media/audio/friendly timers/jet/J2.wav')
        self.j2 = QMediaContent(self.url_j2)
        self.j2_player = QMediaPlayer(None, QMediaPlayer.LowLatency)
        self.j2_player.setMedia(self.j2)

        # Audio File #3
        self.url_j3 = QUrl.fromLocalFile('./media/audio/friendly timers/jet/J3.wav')
        self.j3 = QMediaContent(self.url_j3)
        self.j3_player = QMediaPlayer(None, QMediaPlayer.LowLatency)
        self.j3_player.setMedia(self.j3)

        # Audio File #4
        self.url_j4 = QUrl.fromLocalFile('./media/audio/friendly timers/jet/J4.wav')
        self.j4 = QMediaContent(self.url_j4)
        self.j4_player = QMediaPlayer(None, QMediaPlayer.LowLatency)
        self.j4_player.setMedia(self.j4)

        # 8. Fighter Bomber

        # Audio File #1
        self.url_fb1 = QUrl.fromLocalFile('./media/audio/friendly timers/fighter bomber/FB1.wav')
        self.fb1 = QMediaContent(self.url_fb1)
        self.fb1_player = QMediaPlayer(None, QMediaPlayer.LowLatency)
        self.fb1_player.setMedia(self.fb1)

        # Audio File #2
        self.url_fb2 = QUrl.fromLocalFile('./media/audio/friendly timers/fighter bomber/FB2.wav')
        self.fb2 = QMediaContent(self.url_fb2)
        self.fb2_player = QMediaPlayer(None, QMediaPlayer.LowLatency)
        self.fb2_player.setMedia(self.fb2)

        # Audio File #3
        self.url_fb3 = QUrl.fromLocalFile('./media/audio/friendly timers/fighter bomber/FB3.wav')
        self.fb3 = QMediaContent(self.url_fb3)
        self.fb3_player = QMediaPlayer(None, QMediaPlayer.LowLatency)
        self.fb3_player.setMedia(self.fb3)

        # Audio File #4
        self.url_fb4 = QUrl.fromLocalFile('./media/audio/friendly timers/fighter bomber/FB4.wav')
        self.fb4 = QMediaContent(self.url_fb4)
        self.fb4_player = QMediaPlayer(None, QMediaPlayer.LowLatency)
        self.fb4_player.setMedia(self.fb4)

        # END OF VEHICLE AUDIO FILE UPLOADS

    def init_vehicle_buttons(self):
        """Creates, styles and connects buttons representing Battlefield 4 vehicles to their corresponding methods.

        QIcon objects containing images of each vehicle are applied to QPushbuttons. There are 2 variants of QIcon for
        each vehicle - green and blue. Green is applied to the button when it has been pressed.
        """

        # 1. Anti Air Button
        self.AA_button = QPushButton(self)
        self.AA_button.setGeometry(QRect(1450, 600, 146, 89))
        self.AA_icon = QIcon()
        self.AA_icon.addPixmap(QPixmap('./media/images/vehicle icons/blue icons/AA blue.jpg'), QIcon.Normal, QIcon.Off)
        self.AA_icon_green = QIcon()
        self.AA_icon_green.addPixmap(QPixmap('./media/images/vehicle icons/green icons/AA green.jpg'), QIcon.Normal,
                                     QIcon.Off)
        self.AA_button.setIcon(self.AA_icon)
        self.AA_button.setIconSize(QSize(350, 350))
        self.AA_button.clicked.connect(self.AA_click)

        # 2. Tank Button
        self.tank_button = QPushButton(self)
        self.tank_button.setGeometry(QRect(1450, 475, 146, 89))
        self.tank_icon = QIcon()
        self.tank_icon.addPixmap(QPixmap('./media/images/vehicle icons/blue icons/tank blue.jpg'), QIcon.Normal,
                                 QIcon.Off)
        self.tank_icon_green = QIcon()
        self.tank_icon_green.addPixmap(QPixmap('./media/images/vehicle icons/green icons/tank green.jpg'),
                                       QIcon.Normal, QIcon.Off)
        self.tank_button.setIcon(self.tank_icon)
        self.tank_button.setIconSize(QSize(350, 350))
        self.tank_button.clicked.connect(self.tank_click)

        # 3. Jet Button
        self.jet_button = QPushButton(self)
        self.jet_button.setGeometry(QRect(1650, 225, 146, 89))
        self.jet_icon = QIcon()
        self.jet_icon.addPixmap(QPixmap('./media/images/vehicle icons/blue icons/jet blue.jpg'), QIcon.Normal,
                                QIcon.Off)
        self.jet_icon_green = QIcon()
        self.jet_icon_green.addPixmap(QPixmap('./media/images/vehicle icons/green icons/jet green.jpg'),
                                      QIcon.Normal, QIcon.Off)
        self.jet_button.setIcon(self.jet_icon)
        self.jet_button.setIconSize(QSize(350, 350))
        self.jet_button.clicked.connect(self.jet_click)

        # 4. Scout Helicopter Button
        self.scout_heli_button = QPushButton(self)
        self.scout_heli_button.setGeometry(QRect(1650, 350, 146, 89))
        self.scout_heli_icon = QIcon()
        self.scout_heli_icon.addPixmap(QPixmap('./media/images/vehicle icons/blue icons/scout heli blue.png'),
                                       QIcon.Normal, QIcon.Off)
        self.scout_heli_icon_green = QIcon()
        self.scout_heli_icon_green.addPixmap(QPixmap('./media/images/vehicle icons/green icons/'
                                                     'scout heli green.png'), QIcon.Normal, QIcon.Off)
        self.scout_heli_button.setIcon(self.scout_heli_icon)
        self.scout_heli_button.setIconSize(QSize(350, 350))
        self.scout_heli_button.clicked.connect(self.scout_helo_click)

        # 5. Attack Boat Button
        self.boat_button = QPushButton(self)
        self.boat_button.setGeometry(QRect(1650, 600, 146, 89))
        self.boat_icon = QIcon()
        self.boat_icon.addPixmap(QPixmap('./media/images/vehicle icons/blue icons/boat blue.jpg'), QIcon.Normal,
                                 QIcon.Off)
        self.boat_icon_green = QIcon()
        self.boat_icon_green.addPixmap(QPixmap('./media/images/vehicle icons/green icons/boat green.jpg'), QIcon.Normal,
                                       QIcon.Off)
        self.boat_button.setIcon(self.boat_icon)
        self.boat_button.setIconSize(QSize(350, 350))
        self.boat_button.clicked.connect(self.boat_click)

        # 6. LAV Button
        self.lav_button = QPushButton(self)
        self.lav_button.setGeometry(QRect(1650, 475, 146, 89))
        self.lav_icon = QIcon()
        self.lav_icon.addPixmap(QPixmap('./media/images/vehicle icons/blue icons/lav blue.jpg'), QIcon.Normal,
                                QIcon.Off)
        self.lav_icon_green = QIcon()
        self.lav_icon_green.addPixmap(QPixmap('./media/images/vehicle icons/green icons/lav green.jpg'), QIcon.Normal,
                                      QIcon.Off)
        self.lav_button.setIcon(self.lav_icon)
        self.lav_button.setIconSize(QSize(350, 350))
        self.lav_button.clicked.connect(self.lav_click)

        # 7. Attack Helicopter Button
        self.attack_helo_button = QPushButton(self)
        self.attack_helo_button.setGeometry(QRect(1450, 350, 146, 89))
        self.attack_helo_icon = QIcon()
        self.attack_helo_icon.addPixmap(QPixmap('./media/images/vehicle icons/blue icons/attack helo blue.jpg'),
                                        QIcon.Normal, QIcon.Off)
        self.attack_helo_icon_green = QIcon()
        self.attack_helo_icon_green.addPixmap(QPixmap('./media/images/vehicle icons/green icons/attack helo green.jpg'),
                                              QIcon.Normal, QIcon.Off)
        self.attack_helo_button.setIcon(self.attack_helo_icon)
        self.attack_helo_button.setIconSize(QSize(350, 350))
        self.attack_helo_button.clicked.connect(self.attack_helo_click)

        # 8. Fighter Bomber Button
        self.fighter_bomber_button = QPushButton(self)
        self.fighter_bomber_button.setGeometry(QRect(1450, 225, 146, 89))
        self.fighter_bomber_icon = QIcon()
        self.fighter_bomber_icon.addPixmap(QPixmap('./media/images/vehicle icons/blue icons/bomber blue.jpg'),
                                           QIcon.Normal, QIcon.Off)
        self.fighter_bomber_icon_green = QIcon()
        self.fighter_bomber_icon_green.addPixmap(QPixmap('./media/images/vehicle icons/green icons/bomber green.jpg'),
                                                 QIcon.Normal, QIcon.Off)
        self.fighter_bomber_button.setIcon(self.fighter_bomber_icon)
        self.fighter_bomber_button.setIconSize(QSize(350, 350))
        self.fighter_bomber_button.clicked.connect(self.fighter_bomber_click)

    def init_timer(self):
        """Creates QTimer object that serves as countdown mechanism for the application.

        The connected method is called every 1 second when timer is active.
        """

        self.timer = QTimer()
        self.timer.timeout.connect(self.timer_start)

    def init_timer_audio_lists(self):
        """Creates two lists comprised of audio file objects and playlists.

        The self.timer_start and self."vehicle"_click methods reference self.vehicle_audio_playlists by index to start
        playback of audio files according to corresponding button clicks by the user. self.vehicle_audio_list is
        referenced by the self.reset_audio method to stop audio playback.
        """

        self.vehicle_audio_playlists = [self.aa_playlist, self.tank_playlist, self.jet_playlist,
                                        self.scout_helo_playlist, self.boat_playlist, self.lav_playlist,
                                        self.fighter_bomber_playlist, self.attack_helo_playlist]

        self.vehicle_audio_list = [self.AA1_player, self.AA2_player, self.AA3_player, self.AA4_player,
                                   self.sh1_player, self.sh2_player, self.sh3_player, self.sh4_player,
                                   self.ah1_player, self.ah2_player, self.ah3_player, self.ah4_player,
                                   self.b1_player, self.b2_player, self.b3_player, self.b4_player,
                                   self.t1_player, self.t2_player, self.t3_player, self.t4_player,
                                   self.lav1_player, self.lav2_player, self.lav3_player, self.lav4_player,
                                   self.j1_player, self.j2_player, self.j3_player, self.j4_player,
                                   self.fb1_player, self.fb2_player, self.fb3_player, self.fb4_player]

    def init_icon_dict(self):
        """Creates a dictionary linking vehicle buttons with their default blue icons.

        The self.reset_button_colors() method references the dictionary to set all vehicle icons to their default blue.
        """

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

        #                                 END OF INITIALIZATION METHODS

    #                                METHODS NEEDED FOR WIDGET FUNCTIONALITY

    def timer_down_click(self):
        """Called by when user clicks self.timer_down_button. Increments timer by -1 second."""
        BF4TimerGUI.counter -= 1
        self.timeUp_player.play()
        self.timer_label.setText(str(BF4TimerGUI.counter))

    def up_button_click(self):
        """Called by when user clicks self.timer_up_button. Increments timer by -1 second."""
        BF4TimerGUI.counter += 1
        self.timer_label.setText(str(BF4TimerGUI.counter))
        self.timeDown_player.play()

        # RESET METHODS

    def reset_timer(self):
        """Stops current timer, resets time and sets default timer background."""
        self.timer.stop()
        BF4TimerGUI.counter = 90
        self.timer_label.setStyleSheet(self.timer_label_default_style)

    def reset_button_colors(self):
        """Resets all button icons to default blue color representing an 'unclicked' button state."""
        for vehicle_button in self.button_icon_dict.keys():
            vehicle_button.setIcon(self.button_icon_dict.get(vehicle_button))

    def reset_audio(self):
        """Stops all vehicle-audio playback. state() == 1 identifies actively playing audio files."""
        for audio_file in self.vehicle_audio_list:
            if audio_file.state() == 1:
                audio_file.stop()

    def reset_process(self):
        """Combines self.reset_timer, self.reset_button_colors and self.reset_audio in a comprehensive reset process."""
        self.reset_timer()
        self.reset_button_colors()
        self.reset_audio()

        # END OF RESET METHODS

    def cancel_clicked(self):
        """Cancels/resets timer, plays click sound effect and returns GUI to default state."""
        self.error_player.play()
        self.reset_process()
        self.timer_label.setFont(self.standard_font)
        self.timer_label.setText('Awaiting Orders')
        self.cancel_button.hide()

        # VEHICLE SOUND PLAYLIST/TIMING METHODS

    def aa_playlist(self):
        """Called by self.timer_start each second during countdown and plays AA audio at specified times."""
        if BF4TimerGUI.counter == 90:
            self.AA1_player.play()
        if BF4TimerGUI.counter == 65:
            self.AA2_player.play()
        if BF4TimerGUI.counter == 31:
            self.AA3_player.play()
        if BF4TimerGUI.counter == 12:
            self.AA4_player.play()
            self.AA_button.setIcon(self.AA_icon)

    def tank_playlist(self):
        """Called by self.timer_start each second during countdown and plays Tank audio at specified times."""
        if BF4TimerGUI.counter == 90:
            self.t1_player.play()
        if BF4TimerGUI.counter == 63:
            self.t2_player.play()
        if BF4TimerGUI.counter == 32:
            self.t3_player.play()
        if BF4TimerGUI.counter == 12:
            self.t4_player.play()
        if not self.timer.isActive():
            self.tank_button.setIcon(self.tank_icon)

    def jet_playlist(self):
        """Called by self.timer_start each second during countdown and plays Jet audio at specified times."""
        if BF4TimerGUI.counter == 90:
            self.j1_player.play()
        if BF4TimerGUI.counter == 62:
            self.j2_player.play()
        if BF4TimerGUI.counter == 32:
            self.j3_player.play()
        if BF4TimerGUI.counter == 12:
            self.j4_player.play()
        if not self.timer.isActive():
            self.jet_button.setIcon(self.jet_icon)

    def scout_helo_playlist(self):
        """Called by self.timer_start each second during countdown and plays Scout Helo audio at specified times."""
        if BF4TimerGUI.counter == 90:
            self.sh1_player.play()
        if BF4TimerGUI.counter == 63:
            self.sh2_player.play()
        if BF4TimerGUI.counter == 31:
            self.sh3_player.play()
        if BF4TimerGUI.counter == 12:
            self.sh4_player.play()
        if not self.timer.isActive():
            self.scout_heli_button.setIcon(self.scout_heli_icon)

    def boat_playlist(self):
        """Called by self.timer_start each second during countdown and plays Attack Boat audio at specified times."""
        if BF4TimerGUI.counter == 90:
            self.b1_player.play()
        if BF4TimerGUI.counter == 63:
            self.b2_player.play()
        if BF4TimerGUI.counter == 31:
            self.b3_player.play()
        if BF4TimerGUI.counter == 12:
            self.b4_player.play()
        if not self.timer.isActive():
            self.boat_button.setIcon(self.boat_icon)

    def lav_playlist(self):
        """Called by self.timer_start each second during countdown and plays LAV audio at specified times."""
        if BF4TimerGUI.counter == 90:
            self.lav1_player.play()
        if BF4TimerGUI.counter == 62:
            self.lav2_player.play()
        if BF4TimerGUI.counter == 32:
            self.lav3_player.play()
        if BF4TimerGUI.counter == 11:
            self.lav4_player.play()
        if not self.timer.isActive():
            self.lav_button.setIcon(self.lav_icon)

    def fighter_bomber_playlist(self):
        """Called by self.timer_start each second during countdown and plays fighter bomber audio at specified times."""
        if BF4TimerGUI.counter == 90:
            self.fb1_player.play()
        if BF4TimerGUI.counter == 64:
            self.fb2_player.play()
        if BF4TimerGUI.counter == 31:
            self.fb3_player.play()
        if BF4TimerGUI.counter == 12:
            self.fb4_player.play()
        if not self.timer.isActive():
            self.fighter_bomber_button.setIcon(self.fighter_bomber_icon)

    def attack_helo_playlist(self):
        """Called by self.timer_start each second during countdown and plays Attack Helo audio at specified times."""
        if BF4TimerGUI.counter == 90:
            self.ah1_player.play()
        if BF4TimerGUI.counter == 63:
            self.ah2_player.play()
        if BF4TimerGUI.counter == 32:
            self.ah3_player.play()
        if BF4TimerGUI.counter == 12:
            self.ah4_player.play()
        if not self.timer.isActive():
            self.attack_helo_button.setIcon(self.attack_helo_icon)

    def timer_start(self):
        """Called by active QTimer to update timer, time-display, audio playback and GUI style elements by the second.

        While the display counts down to 0, but the QTimer runs for an additional 4 seconds during which additional
        styling/display variables are updated. The QTimer resets the GUI to it's default state upon reaching -4.
        This method references self.vehicle_audio_playlists by index to play audio for user-selected vehicle.
        """

        # Checks countdown against the selected vehicle's video_playlist method and plays audio when triggered
        self.vehicle_audio_playlists[self.vehicle_audio_index]()
        self.timer_label.setFont(self.timer_display_font)
        self.timer_label.setText(str(BF4TimerGUI.counter))
        BF4TimerGUI.counter -= 1
        self.cancel_button.show()

        if BF4TimerGUI.counter in range(10, 90):
            self.timer_label.setStyleSheet(self.timer_label_default_style)
        if BF4TimerGUI.counter in range(0, 10):
            self.timer_label.setStyleSheet(self.timer_label_10sec_style)
        if BF4TimerGUI.counter in range(-4, 0):
            self.timer_label.setFont(self.standard_font)
            self.timer_label.setStyleSheet(self.timer_label_deploy_style)
            self.timer_label.setText('Ready to Deploy')
            self.reset_button_colors()
        if BF4TimerGUI.counter == -4:
            self.reset_process()
            self.cancel_button.hide()
            self.timer_label.setText('Awaiting Orders')
            self.timer_label.setFont(self.standard_font)
            # print('process ended')

    def changing_orders(self):
        """Displays message 'changing orders' when user switches vehicle timers while another countdown is active."""
        if self.timer.isActive():
            self.timer_label.setFont(self.standard_font)
            self.timer_label.setText('Changing Orders')

    #                                       VEHICLE BUTTON CLICK METHODS

    # The following 8 "vehicle_click" methods reset the GUI (and display "Changing Orders" if a timer was already
    # active), prepare the audio files of the respective vehicle, update the vehicle icon color to green to indicate
    # it's selection, and starts the countdown.

    def AA_click(self):
        self.changing_orders()
        self.vehicle_audio_index = self.vehicle_audio_playlists.index(self.aa_playlist)
        # sets vehicle audio index to the correct video_playlist for use in self.timer_start()
        self.reset_process()
        self.radio_player.play()
        self.AA_button.setIcon(self.AA_icon_green)
        self.timer.start(1000)

    def tank_click(self):
        self.changing_orders()
        self.vehicle_audio_index = self.vehicle_audio_playlists.index(self.tank_playlist)
        self.reset_process()
        self.radio_player.play()
        self.tank_button.setIcon(self.tank_icon_green)
        self.timer.start(1000)

    def jet_click(self):
        self.changing_orders()
        self.vehicle_audio_index = self.vehicle_audio_playlists.index(self.jet_playlist)
        self.reset_process()
        self.radio_player.play()
        self.jet_button.setIcon(self.jet_icon_green)
        self.timer.start(1000)

    def scout_helo_click(self):
        self.changing_orders()
        self.vehicle_audio_index = self.vehicle_audio_playlists.index(self.scout_helo_playlist)
        self.reset_process()
        self.radio_player.play()
        self.scout_heli_button.setIcon(self.scout_heli_icon_green)
        self.timer.start(1000)

    def boat_click(self):
        self.changing_orders()
        self.vehicle_audio_index = self.vehicle_audio_playlists.index(self.boat_playlist)
        self.reset_process()
        self.radio_player.play()
        self.boat_button.setIcon(self.boat_icon_green)
        self.timer.start(1000)

    def lav_click(self):
        self.changing_orders()
        self.vehicle_audio_index = self.vehicle_audio_playlists.index(self.lav_playlist)
        self.reset_process()
        self.radio_player.play()
        self.lav_button.setIcon(self.lav_icon_green)
        self.timer.start(1000)

    def fighter_bomber_click(self):
        self.changing_orders()
        self.vehicle_audio_index = self.vehicle_audio_playlists.index(self.fighter_bomber_playlist)
        self.reset_process()
        self.radio_player.play()
        self.fighter_bomber_button.setIcon(self.fighter_bomber_icon_green)
        self.timer.start(1000)

    def attack_helo_click(self):
        self.changing_orders()
        self.vehicle_audio_index = self.vehicle_audio_playlists.index(self.attack_helo_playlist)
        self.reset_process()
        self.radio_player.play()
        self.attack_helo_button.setIcon(self.attack_helo_icon_green)
        self.timer.start(1000)

        # APP READY TO RUN


def run_app():
    """Instantiates PyQt5 objects needed to configure, launch and display the GUI application."""
    created_app = QApplication(sys.argv)
    application = BF4TimerGUI()
    application.show()
    sys.exit(created_app.exec_())


run_app()
