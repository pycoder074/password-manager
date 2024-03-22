from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget, QFrame, QPushButton, QMessageBox
from Entries import Entry
from PyQt6.QtCore import Qt
import sqlite3
import bcrypt

class LoginWin(QMainWindow):
    def __init__(self):
        super().__init__()
        self.centralWidget = QWidget()
        self.setCentralWidget(self.centralWidget)
        self.layout = QVBoxLayout(self.centralWidget)
        self.title = QLabel('Login')
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
        self.passwd_box = Entry.PasswordEntry()
        self.regbtn = QPushButton('Login')
        self.regbtn.clicked.connect(self.login)
        
        self.layout.addWidget(self.username_box)
        self.layout.addWidget(self.passwd_box)
        self.layout.addWidget(self.regbtn)
    
    def login(self):
        username = self.username_box.get_value()
        passwd = self.passwd_box.get_value()
        passwd = passwd.encode('utf-8')

        try:
            conn = sqlite3.connect('users.sqlite3')
            c = conn.cursor()
            query = "SELECT passwd, salt FROM users WHERE username = ?"
            c.execute(query, (username,))
            result = c.fetchone()  # Fetch one row
            if result:  # If user exists
                stored_passwd_hash = result[0]
                salt = result[1]
                hashed_passwd = bcrypt.hashpw(passwd, salt)
                # Compare the hashed passwords
                if hashed_passwd == stored_passwd_hash:
                    print("Login successful!")
                else:
                    print("Incorrect username or password.")
            else:
                print("User not found.")
            conn.commit()
            c.close()
        except sqlite3.Error as e:
            print("Error:", e)

if __name__ == '__main__':
    app = QApplication([])
    win = LoginWin()
    win.show()
    app.exec()