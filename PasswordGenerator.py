from PyQt6.QtWidgets import QMainWindow, QApplication, QFrame, QLabel, QVBoxLayout, QWidget
from Entries import Entry

class PasswordGenerator(QMainWindow):
  def __init__(self):
    super().__init__()
    self.mainWidget = QWidget()
    self.layout = QVBoxLayout()
    self.mainWidget.setLayout(self.layout)
    self.title = QLabel('Generate a new password')
    self.layout.addWidget(self.title)
    
