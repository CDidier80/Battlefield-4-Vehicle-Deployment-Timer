

##########################################  TEMPLATE for GUI CREATION in PYQT5 ###################################



from PyQt5 import QtWidgets, QtMultimediaWidgets,QtMultimedia,QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow            # QMainWindow class used to create window for GUI
import sys                                                       # will need sys to properly close the GUI later


# part 1: set up main window of app

class MyWindow(QMainWindow):                               # MyWindow subclass will inherit from QMainWindow
    def __init__(self):                                    # class constructor
        super(MyWindow, self).__init__()                   # initializes superclass properties
        self.setGeometry(0, 0, 1920, 1080)                 # these coordinates make a full screen app - adjust as needed
        self.setWindowTitle("BF4 Deployment Timer")        # set title of app
        self.initGUI()       # optional run the "content creation" method during app initialization -- see part 2 below


# part 2: define contents of the application (widgets, labels, buttons, etc)

    def initGUI(self):                                     # running this method during initialization creates the content of the app. Helpful for organizing code
        self.setStyleSheet('background-color: rgba(0,0,0,0)')
    # code creating the content of the app goes here.



# part 3 :  create additional methods (as many as needed) to interact with the widgets, labels, buttons, etc. These
#           are the things that will happen when a widget is used


        def clicked(self):                                      # below are example methods used to add functionality
            pass

        def playvideo(self):
            pass
        def pausevideo(self):
            pass


# part 4: create a function that will run the application (technically, the class instance) set up above when called

def run_app():
    created_app = QApplication(sys.argv)                  # make a Q application and configures it with this needed line
    application = MyWindow()                              # creates the application as an instance of MyWindow() class (as inherited by QMainWindow)
    application.show()                                    # this line is needed to actually show the app on the screen
    sys.exit(created_app.exec_())                         # this allows program to be terminated upon closing of GUI window



# part 4 -- last step -- call the run_app function to launch the application

run_app()