import sys

from PyQt4.QtCore import *
from PyQt4.QtGui import *

class CropWindow(QMainWindow):
    """This Class Creates a Main Window"""

    #constructor
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Crop Simulator")

def main():
    crop_simulation = QApplication(sys.argv)
    crop_window = CropWindow()
    crop_window.show()
    crop_window.raise_()
    crop_simulation.exec_() #execute the program

if __name__ == "__main__":
    main()
