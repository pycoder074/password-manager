from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QGridLayout, QWidget, QFrame, QPushButton, QMessageBox
from PyQt6.QtCore import Qt
from circle_buttons import CircularButton

class Home(QMainWindow):
    def __init__(self):
        super().__init__()
        self.centralWidget = QWidget()
        self.setCentralWidget(self.centralWidget)
        self.layout = QGridLayout(self.centralWidget)

        settings = CircularButton('Settings', None, '#004AAD', height=200, width = 200)
        new_passwrd = CircularButton(' Save New Password', None, color ='#004AAD', height = 200, width = 200)
        passwrd_generator = CircularButton('Generate Password', None, color= '#004AAD', height = 200, width = 200)

        
        self.layout.addWidget(settings, 0, 0)
        self.layout.addWidget(new_passwrd, 1, 0)
        self.layout.addWidget(passwrd_generator, 2, 0)
if __name__ == '__main__':
    app = QApplication([])
    win = Home()
    win.show()
    app.exec()

