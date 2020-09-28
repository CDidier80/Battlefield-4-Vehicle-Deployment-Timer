('C:\\Users\\Owner\\PycharmProjects\\BF4 Deployment Timer\\sound\\friendly timers\\friendly AA r\\Friendly AA pt1.mp4')
self.timer = QtCore.QTimer(self)
self.timer.timeout.connect(self.Time)

self.start = QtGui.QPushButton("Start", self)
self.start.clicked.connect(self.Start)


def Start(self):
    global s, m, h

    self.timer.start(1000)


def Time(self):
    global s, m, h

    if s < 59:
        s += 1
    else:
        if m < 59:
            s = 0
            m += 1
        elif m == 59 and h < 24:
            h += 1
            m = 0
            s = 0
        else:
            self.timer.stop()

    time = "{0}:{1}:{2}".format(h, m, s)

    self.lcd.setDigitCount(len(time))
    self.lcd.display(time)