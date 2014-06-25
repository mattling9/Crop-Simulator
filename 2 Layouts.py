import sys

from PyQt4.QtCore import *
from PyQt4.QtGui import *

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Hello")
        self.stacked_layout = QStackedLayout()
        self.create_initial_layout()
        self.create_second_layout()
        self.widget = QWidget()
        self.widget.setLayout(self.stacked_layout)
        self.setCentralWidget(self.widget)
        
    def switch_layout(self):
        self.stacked_layout.setCurrentIndex(1)

        name = self.text_box.text()
        self.label.setText("Hello {0}".format(name))

    def create_initial_layout(self):
        self.text_box = QLineEdit()
        self.button = QPushButton("Press Here")

        self.initial_layout = QVBoxLayout()
        self.initial_layout.addWidget(self.text_box)
        self.initial_layout.addWidget(self.button)

        self.initial_widget = QWidget()
        self.initial_widget.setLayout(self.initial_layout)
        self.setCentralWidget(self.initial_widget)
        self.stacked_layout.addWidget(self.initial_widget)
        self.button.clicked.connect(self.switch_layout)

    def create_second_layout(self):
        self.label = QLabel()
        self.button = QPushButton("Back")
        

        self.second_layout = QVBoxLayout()
        self.second_layout.addWidget(self.label)
        self.second_layout.addWidget(self.button)
        self.second_widget = QWidget()
        self.second_widget.setLayout(self.second_layout)


if __name__ == '__main__':
    application = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    window.raise_()
    application.exec_()
        
        
        
