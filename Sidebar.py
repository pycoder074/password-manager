from PyQt6.QtWidgets import QFrame, QVBoxLayout, QSizePolicy
from circle_buttons import CircularButton  # Assuming CircularButton is defined elsewhere
from PyQt6.QtCore import Qt

class SideBar(QFrame):
    def __init__(self):
        super().__init__()
        
        self.setStyleSheet("""
                           border: 2px solid black
                           """)
        
        self.button_frame_layout = QVBoxLayout(self)
        self.button_frame_layout.setAlignment(Qt.AlignmentFlag.AlignTop)
        
        settings = CircularButton('Settings', None, '#004AAD', height=200, width=200)
        self.button_frame_layout.addWidget(settings)
        
        new_password = CircularButton('Save New Password', None, color='#004AAD', height=200, width=200)
        self.button_frame_layout.addWidget(new_password)
        
        password_generator = CircularButton('Generate Password', None, color='#004AAD', height=200, width=200)
        self.button_frame_layout.addWidget(password_generator)
        
        self.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)