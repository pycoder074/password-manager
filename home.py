from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget, QFrame, QHBoxLayout, QLineEdit
from circle_buttons import CircularButton
from passwordFrame import PasswordFrame
from Sidebar import SideBar
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont

class Home(QMainWindow):
    def __init__(self):
        super().__init__()
        sidebar = SideBar()
        
        passwrd_box_layout = QHBoxLayout(self)
        passwrd_box_layout.addWidget(sidebar)
        passwrd_box = PasswordFrame(locked=True, passwords=[['bbc.com', 'Elliott', 'Pandek2008'], 
                                                             ['google.com', 'Elliott', 'EK200828'], 
                                                             ['itv.co.uk', 'Elliott', 'EK200828'], 
                                                             ['lego.com', 'Elliott', 'Pandek2008']])
        passwrd_box_layout.setAlignment(Qt.AlignmentFlag.AlignTop)
        passwrd_box_layout.addWidget(passwrd_box)

        passwrd_box_layout.addStretch(1)

        self.search_bar_frame = QWidget()
        search_bar_layout = QVBoxLayout(self.search_bar_frame)
        self.search_bar = QLineEdit(self)
        font_size = int(self.search_bar.height() * 0.5)
        font = QFont()
        font.setPointSize(font_size)
        self.search_bar.setFont(font)
        self.search_bar.setPlaceholderText("Search...")
        self.search_bar.setStyleSheet("""QLineEdit { padding-left: 10px; }
                                            QLineEdit {
                                            background-color: white;
                                            border-radius: 4px;
                                            }""")
        search_bar_layout.addWidget(self.search_bar)
        
        # Add the search bar frame to the main layout
        main_layout = QVBoxLayout()
        main_layout.addWidget(self.search_bar_frame)
        main_layout.addLayout(passwrd_box_layout)

        central_widget = QWidget()
        central_widget.setLayout(main_layout)
        self.setCentralWidget(central_widget)

if __name__ == '__main__':
    app = QApplication([])
    win = Home()
    win.show()
    app.exec()
