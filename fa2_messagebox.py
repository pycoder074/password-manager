from PyQt6.QtWidgets import QDialog, QVBoxLayout, QApplication, QMainWindow, QLabel
from PyQt6.QtGui import QPixmap
from PyQt6.QtCore import Qt
from Entries import Entry  # Assuming this is a custom module for password entry
from fa2 import generate_qr  # Assuming this function generates QR code

class MessageBox(QDialog):
    def __init__(self, title: str):
        super().__init__()

        # Generate QR code
        generate_qr()
        # Load the QR code image
        pixmap = QPixmap('qr_code.png').scaled(200, 200, Qt.AspectRatioMode.KeepAspectRatio)

        # Create QLabel for QR code
        qr_label = QLabel()
        qr_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        qr_label.setPixmap(pixmap)

        # Layout setup
        layout = QVBoxLayout(self)
        
        # Add widgets to layout
        self.title = QLabel(title)
        self.title.setStyleSheet("""
font: 25px solid black
                                 """)
        layout.addWidget(self.title)
        self.title.setAlignment(Qt.AlignmentFlag.AlignVCenter)
        layout.addWidget(qr_label)
    async def send_callback(self):
        await callback



if __name__ == '__main__':
    app = QApplication([])
    window = QMainWindow()
    message = MessageBox('Scan QR Code to continue')
    window.setCentralWidget(message)
    window.show()
    app.exec()
