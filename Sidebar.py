from PyQt6.QtWidgets import QFrame, QGridLayout, QSizePolicy
from circle_buttons import CircularButton  # Assuming CircularButton is implemented correctly
from PyQt6.QtCore import Qt
class SideBar(QFrame):
    def __init__(self):
        super().__init__()
        
        self.button_frame_layout = QGridLayout(self)
        self.button_frame_layout.setAlignment(Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignLeft)
        
        
        settings = CircularButton('Settings', None, '#004AAD', height=200, width=200)
        new_password = CircularButton('Save New Password', None, color='#004AAD', height=200, width=200)
        password_generator = CircularButton('Generate Password', None, color='#004AAD', height=200, width=200)

        self.button_frame_layout.addWidget(settings, 0, 0)
        self.button_frame_layout.addWidget(new_password, 1, 0)
        self.button_frame_layout.addWidget(password_generator, 2, 0)
        
        # Set size policy for the buttons
        for button in (settings, new_password, password_generator):
            button.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)