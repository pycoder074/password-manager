from PyQt6.QtWidgets import QMainWindow, QApplication, QLabel, QVBoxLayout, QWidget, QPushButton
from PyQt6.QtWebEngineWidgets import QWebEngineView
from generate_password import generate_password
import sys

class PasswordGenerator(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Password Generator')
        self.mainWidget = QWidget()
        self.layout = QVBoxLayout()
        self.mainWidget.setLayout(self.layout)

        self.title_label = QLabel('Generate a new password')
        self.layout.addWidget(self.title_label)

        self.result_label = QLabel('Result: ')
        self.layout.addWidget(self.result_label)

        self.generate_button = QPushButton('Generate Password')
        self.generate_button.clicked.connect(self.generate_password)
        self.layout.addWidget(self.generate_button)

        self.password_label = QLabel()
        self.layout.addWidget(self.password_label)

        self.setCentralWidget(self.mainWidget)
    
    def generate_password(self):
        password = generate_password()
        self.password_label.setText(password)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = PasswordGenerator()
    window.show()
    sys.exit(app.exec())