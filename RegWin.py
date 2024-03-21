from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget, QFrame,QPushButton
from PyQt6.QtCore import Qt
from password_manager.Entries import Entry
class RegWin(QMainWindow):
    def __init__(self):
        super().__init__()
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.layout = QVBoxLayout(self.central_widget)
        self.title = QLabel('Register')
        self.title_frame = QFrame()
        self.title_frame.setStyleSheet(
            """
QFrame{
border: 2px solid black;
}
QLabel{
border: none
}
"""
        )
        self.title_frame_layout = QVBoxLayout()
        self.title_frame.setLayout(self.title_frame_layout)
        self.title_frame_layout.addWidget(self.title, alignment=Qt.AlignmentFlag.AlignCenter)
        self.layout.addWidget(self.title_frame)

        self.username_box = Entry.InfoEntry('Username:')
        self.email_box = Entry.InfoEntry('Email:')
        self.passwd_box = Entry.PasswordEntry()
        self.confirm_passwd = Entry.PasswordEntry(verify=True)

        self.layout.addWidget(self.username_box)
        self.layout.addWidget(self.email_box)
        self.layout.addWidget(self.passwd_box)
        self.layout.addWidget(self.confirm_passwd)

        self.regbtn = QPushButton('Register')


if __name__ == '__main__':
    app = QApplication([])
    window = RegWin()
    window.show()  # Show the window after setting up
    app.exec()  # Start the application event loop
