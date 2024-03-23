from PyQt6.QtWidgets import QApplication, QMainWindow, QFrame, QLabel, QWidget, QGridLayout

class PasswordFrame(QFrame):
    def __init__(self, locked: bool, passwords: list):
        super().__init__()
        self.layout = QGridLayout(self)
        for j in range(len(passwords)):
            password = passwords[j][1]
            website = passwords[j][0]
            loaded_password = QLabel(password)
            loaded_website = QLabel(website)
            self.layout.addWidget(loaded_website, j, 1)
            self.layout.addWidget(loaded_password, j, 0)

if __name__ == '__main__':
    app = QApplication([])
    window = QMainWindow()
    passwords = [['bbc.com', 'Pandek2008'], ['google.com', 'EK200828']]
    frame = PasswordFrame(locked=False, passwords=passwords)
    window.setCentralWidget(frame)
    window.show()
    app.exec()
