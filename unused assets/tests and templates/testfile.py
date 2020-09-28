

from PyQt5 import QtCore, QtGui, QtWidgets, QtMultimediaWidgets, QtMultimedia

self.url_ah1 = QtCore.QUrl.fromLocalFile(
    'C:\\Users\\Owner\\PycharmProjects\\BF4 Deployment Timer\\sound\\friendly timers\\friendly scout helicopter\\scout helo pt1 rev.mp3')
self.ah1 = QtMultimedia.QMediaContent(self.url_ah1)
self.ah1_player = QtMultimedia.QMediaPlayer()
self.ah1_player.setMedia(self.ah1)

self.url_ah2 = QtCore.QUrl.fromLocalFile(
    'C:\\Users\\Owner\\PycharmProjects\\BF4 Deployment Timer\\sound\\friendly timers\\friendly scout helicopter\\scout helo pt2.wav')
self.ah2 = QtMultimedia.QMediaContent(self.url_ah2)
self.ah2_player = QtMultimedia.QMediaPlayer()
self.ah2_player.setMedia(self.ah2)

self.url_ah3 = QtCore.QUrl.fromLocalFile(
    'C:\\Users\\Owner\\PycharmProjects\\BF4 Deployment Timer\\sound\\friendly timers\\friendly scout helicopter\\scout helo pt3.wav')
self.ah3 = QtMultimedia.QMediaContent(self.url_ah3)
self.ah3_player = QtMultimedia.QMediaPlayer()
self.ah3_player.setMedia(self.ah3)

self.url_ah4 = QtCore.QUrl.fromLocalFile(
    'C:\\Users\\Owner\\PycharmProjects\\BF4 Deployment Timer\\sound\\friendly timers\\friendly scout helicopter\\scout helo pt4.wav')
self.ah4 = QtMultimedia.QMediaContent(self.url_ah4)
self.ah4_player = QtMultimedia.QMediaPlayer()
self.ah4_player.setMedia(self.ah4)




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
    if MyWindow.counter in range(0, 10):
        self.timer_label.setStyleSheet(
            "border-image: url('C:/Users/Owner/PycharmProjects/BF4 Deployment Timer/images/blue tile background pic.jpg'); color: red")
    if MyWindow.counter in range(-4, 0):
        self.timer_label.setFont(font2)
        self.timer_label.setStyleSheet(
            "border-image: url('C:/Users/Owner/PycharmProjects/BF4 Deployment Timer/images/blue tile background pic.jpg'); color: rgb(98, 255, 0)")
        self.timer_label.setText('Ready to Deploy')
    if MyWindow.counter == -4:
        self.countdown_AA.stop()
        MyWindow.counter = 90
        self.timer_label.setStyleSheet(
            "border-image: url('C:/Users/Owner/PycharmProjects/BF4 Deployment Timer/images/blue tile background pic.jpg'); color: rgb(136, 204, 241)")
        self.timer_label.setText('Awaiting Orders')
























def scout_helo_click(self):
    self.scout_heli_button.setIcon(self.scout_heli_icon_green)
    if MyWindow.counter == 89:
        self.sh1_player.play()
    if MyWindow.counter == 65:
        self.sh2_player.play()
    if MyWindow.counter == 31:
        self.sh3_player.play()
    if MyWindow.counter == 12:
        self.sh4_player.play()
    if MyWindow.counter <= 0:
        self.scout_heli_button.setIcon(self.scout_heli_icon)