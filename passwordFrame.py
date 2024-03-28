from PyQt6.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem, QLabel, QVBoxLayout, QPushButton, QMessageBox
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont
from fa2_messagebox import MessageBox
class PasswordFrame(QTableWidget):
    def __init__(self, locked: bool, passwords: list):
        super().__init__()
        self.passwords = passwords
        self.layout = QVBoxLayout(self)
        self.widgets = []
        if locked:
            self.lock()
        else:
            self.unlock()
    def unlock(self):
        unlock = QMainWindow()
        fa = MessageBox('Scan QR to unlock photos')
        unlock.setCentralWidget(fa)
        unlock.show()
        self.setShowGrid(True)
        self.setColumnCount(3)
        self.setHorizontalHeaderLabels(["Website", "Username", "Password"])
        for i in self.widgets:
            i.setParent(None)
        self.setStyleSheet("""
                           QTableWidget {
                                        background-color: none;
                                        border: none;
                                        }
                                        QTableWidgetItem {
                                        color: black;
                                        }
                                        QTableWidgetItem:selected {
                                        background-color: none;
                                        color: white;
                                        }
                                        """)
        data_font = QFont('Roboto', 16)
        self.setFont(data_font)
        self.setColumnCount(3)
        self.setRowCount(len(self.passwords))
        for j, (website, username, password) in enumerate(passwords):
            website = QTableWidgetItem(website)
            website.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
            self.setItem(j, 0, website)
            
            username = QTableWidgetItem(username)
            username.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
            self.setItem(j, 1, username)

            password = QTableWidgetItem(password)
            password.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
            self.setItem(j, 2, password)


        self.horizontalHeader().setMinimumSectionSize(200)
    
    def lock(self):
        self.setShowGrid(False)
        self.setStyleSheet("""
                            QTableWidget {
                           background-color: #D3D3D3
                            }""")
        self.locked_label = QLabel('Passwords are locked \U0001F512')
        self.widgets.append(self.locked_label)
        self.layout.addWidget(self.locked_label)
        self.layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.unlock_button = QPushButton('Unlock Passwords')
        self.unlock_button.setStyleSheet("""
                                            QPushButton {
                                            background-color: #CCCCCC
                                            }""")
        self.unlock_button.clicked.connect(self.unlock)
        self.layout.addWidget(self.unlock_button)
        self.widgets.append(self.unlock_button)

if __name__ == '__main__':
    app = QApplication([])
    window = QMainWindow()
    passwords = [
        ['bbc.com', 'Elliott', 'Pandek2008'],
        ['google.com', 'Elliott', 'EK200828'],
        ['itv.co.uk', 'Elliott', 'EK200828'],
        ['lego.com', 'Elliott', 'Pandek2008']
    ]
    frame = PasswordFrame(locked=True, passwords=passwords)
    window.setCentralWidget(frame)
    window.show()
    app.exec()
