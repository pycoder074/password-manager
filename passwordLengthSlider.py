from PyQt6.QtWidgets import QApplication, QMainWindow, QSlider, QFormLayout, QLabel
from PyQt6.QtCore import Qt

class PasswordLengthSlider(QSlider):
    def __init__(self, maxlength):
        super().__init__()
        self.layout = QFormLayout()
        self.setLayout(self.layout)
        self.valueLabel = QLabel('Length:')
        self.layout.addWidget(self.valueLabel)
        self.setOrientation(Qt.Orientation.Horizontal)
        self.setMaximum(maxlength)
        self.setMinimum(5)
        self.valueChanged.connect(self.updateValue)
    def updateValue(self):
        self.valueLabel.setText(f"Length: {str(self.value())}")
    def returnValue(self):
        return self.value()
    def addWidget(self, layout):
        layout.addWidget(self.valueLabel)
        layout.addWidget(self)
        
if __name__ == '__main__':
    app = QApplication([])
    window = QMainWindow()
    slider = PasswordLengthSlider(50)
    window.setCentralWidget(slider)
    window.show()
    app.exec()