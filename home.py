from PyQt6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QHBoxLayout, QLineEdit
from passwordFrame import PasswordFrame
from Sidebar import SideBar
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont

class Home(QMainWindow):
    def __init__(self):
        super().__init__()
        
        # Sidebar
        sidebar = SideBar()
        sidebar_layout = QVBoxLayout()
        sidebar_layout.addWidget(sidebar)
        
        # Password Frame
        passwrd_box = PasswordFrame(locked=True, passwords=[
            ['bbc.com', 'Elliott', 'Pandek2008'], 
            ['google.com', 'Elliott', 'EK200828'], 
            ['itv.co.uk', 'Elliott', 'EK200828'], 
            ['lego.com', 'Elliott', 'Pandek2008']
        ])
        
        # Search Bar
        self.search_bar_frame = QWidget()
        search_bar_layout = QVBoxLayout(self.search_bar_frame)
        self.search_bar = QLineEdit(self)
        font_size = int(self.search_bar.height() * 0.5)
        font = QFont()
        font.setPointSize(font_size)
        self.search_bar.setFont(font)
        self.search_bar.setPlaceholderText("Search...")
        self.search_bar.setStyleSheet("""
            QLineEdit { padding-left: 10px; }
            QLineEdit { background-color: white; border-radius: 4px; }
        """)
        search_bar_layout.addWidget(self.search_bar)
        
        # Layout for sidebar and password frame
        sidebar_password_layout = QHBoxLayout()
        sidebar_password_layout.addLayout(sidebar_layout)
        sidebar_password_layout.addWidget(passwrd_box)
        
        # Main Layout
        main_layout = QVBoxLayout()
        main_layout.addWidget(self.search_bar_frame)
        main_layout.addLayout(sidebar_password_layout)
        
        central_widget = QWidget()
        central_widget.setLayout(main_layout)
        self.setCentralWidget(central_widget)

if __name__ == '__main__':
    app = QApplication([])
    win = Home()
    win.show()
    app.exec()
