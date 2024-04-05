from PyQt6.QtWidgets import QMainWindow, QApplication, QLabel, QVBoxLayout, QWidget, QPushButton
from PyQt6.QtCore import Qt
from generate_password import create_password
from passwordLengthSlider import PasswordLengthSlider
import sys
from save_gen_passwrd import save_gen_passwrd
from passwrdAddInfo import addInfo

class PasswordGenerator(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Password Generator')
        self.centralWidget = QWidget()
        self.setCentralWidget(self.centralWidget)
        self.layout = QVBoxLayout(self.centralWidget)

        self.title_label = QLabel('Generate a new password')
        self.layout.addWidget(self.title_label)

        self.result_label = QLabel()
        self.layout.addWidget(self.result_label)

        self.length_slider = PasswordLengthSlider(20)
        self.length_label = QLabel(f"Length: {self.length_slider.value()}")
        self.length_slider.valueChanged.connect(self.update_length_label)
        self.layout.addWidget(self.length_slider)
        self.layout.addWidget(self.length_label)

        self.generate_button = QPushButton('Generate Password')
        self.generate_button.clicked.connect(self.generate_password)
        self.layout.addWidget(self.generate_button)

        self.save_button = QPushButton('Save password')
        self.save_button.clicked.connect(self.add_extra_info)
        self.layout.addWidget(self.save_button)

        self.password_label = QLabel()
        self.layout.addWidget(self.password_label)

    def update_length_label(self, value):
        self.length_label.setText(f"Length: {value}")

    def generate_password(self):
        length = self.length_slider.value()
        self.password = create_password(length)
        self.result_label.setText(f"Result: {self.password}")

    def add_extra_info(self):
        if hasattr(self, 'password'):
            self.add_info_dialog = addInfo(self.password, self)
            self.add_info_dialog.show()
        else:
            self.result_label.setText("Please generate a password first.")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = PasswordGenerator()
    window.show()
    sys.exit(app.exec())
