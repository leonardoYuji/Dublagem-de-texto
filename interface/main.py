import sys
import subprocess
from PyQt4 import QtGui, QtCore

class Window(QtGui.QMainWindow):

    def __init__(self):
        super(Window, self).__init__()
        self.setGeometry(50, 50, 500, 300)
        self.setWindowTitle("PyQT tuts!")
        self.setWindowIcon(QtGui.QIcon('pythonlogo.png'))
        
        self.home()

    def home(self):
        btn = QtGui.QPushButton("Start", self)
        btn.clicked.connect(self.close_application)
        btn.move(200,150)
	btn.setStyleSheet("background:#ff6347; border-radius:10px; border:0; color:white; padding:10px 15px;")
        self.show()

    def close_application(self):
	subprocess.call(["python", "geodet.py"])


def run():
    app = QtGui.QApplication(sys.argv)
    GUI = Window()
    sys.exit(app.exec_())


run()
