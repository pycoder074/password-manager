from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget, QFrame, QPushButton, QMessageBox
from Entries import Entry
from PyQt6.QtCore import Qt
import sqlite3
import bcrypt
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
        self.regbtn = QPushButton('Register')
        self.regbtn.clicked.connect(self.register)
        
        self.layout.addWidget(self.username_box)
        self.layout.addWidget(self.email_box)
        self.layout.addWidget(self.passwd_box)
        self.layout.addWidget(self.confirm_passwd)
        self.layout.addWidget(self.regbtn)
        
        # Create the database table
        self.create_table()

    def create_table(self):
        conn = sqlite3.connect('users.sqlite3')
        c = conn.cursor()
        try:
            c.execute('''
                    CREATE TABLE IF NOT EXISTS users (
                    id INTEGER PRIMARY KEY,
                    username TEXT UNIQUE NOT NULL,
                    passwd TEXT NOT NULL,
                    salt TEXT NOT NULL,
                    email TEXT NOT NULL
    );
                    ''')
        except sqlite3.IntegrityError as e:
            warning = QMessageBox()
            warning.setText('Username is already taken')
            warning.setIcon(QMessageBox.Icon.Warning)
            warning.exec()
            
        conn.commit()
        c.close()
    def register(self):
        self.create_table()
        username = self.username_box.get_value()
        email = self.email_box.get_value()
        passwd = self.passwd_box.get_value()
        confirm_passwd = self.confirm_passwd.get_value()
        if passwd != confirm_passwd:
            warning = QMessageBox()
            warning.setText('Passwords are not the same')
            warning.setIcon(QMessageBox.Icon.Warning)
            warning.exec()
        else:
            passwd = passwd.encode('utf-8')
            salt = bcrypt.gensalt()
            passwd = bcrypt.hashpw(passwd, salt)
            try:
                # Insert user data into the database
                conn = sqlite3.connect('users.sqlite3')
                c = conn.cursor()
                c.execute('INSERT INTO users (username, passwd, salt, email) VALUES (?, ?, ?, ?)', (username, passwd, salt, email))
                conn.commit()
                c.close()
                print('User registered')
            except sqlite3.IntegrityError as e:
                # Handle the case where username already exists
                warning = QMessageBox()
                warning.setText('Username is already taken')
                warning.setIcon(QMessageBox.Icon.Warning)
                warning.exec()


if __name__ == '__main__':
    app = QApplication([])
    window = RegWin()
    window.show()
    app.exec()
