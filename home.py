from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QGridLayout, QWidget, QFrame, QHBoxLayout
from circle_buttons import CircularButton
from passwordFrame import PasswordFrame
from Sidebar import SideBar
from PyQt6.QtCore import Qt
class Home(QMainWindow):
    def __init__(self):
        super().__init__()
        centralWidget = QWidget()
        self.setCentralWidget(centralWidget)
        layout = QHBoxLayout(centralWidget)
        sidebar = SideBar()
        layout.addWidget(sidebar)

        passwrd_box = PasswordFrame(locked = False, passwords = [['bbc.com', 'Elliott', 'Pandek2008'], ['google.com', 'Elliott', 'EK200828'], ['itv.co.uk', 'Elliott', 'EK200828'], ['lego.com', 'Elliott', 'Pandek2008']])
        layout.setAlignment(Qt.AlignmentFlag.AlignTop)
        layout.addWidget(passwrd_box)

        layout.addStretch(1)
        
if __name__ == '__main__':
    app = QApplication([])
    win = Home()
    win.show()
    app.exec()

