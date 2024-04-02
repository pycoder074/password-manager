import random
import string
from PyQt6.QtWidgets import QApplication, QMainWindow, QSlider
from PyQt6.QtCore import Qt
def create_password(length):
    password = []
    break_length_start = random.randint(0, 10)
    break_length_end = random.randint(break_length_start, 2**32)  # Corrected to 2**32
    break_length = random.randint(break_length_start, break_length_end)  # Randomly determine break length
    for i in range(length):
        # Choose a random character type (number, letter, symbol)
        char_type = random.choice(['number', 'letter', 'symbol'])
        
        if char_type == 'number':
            character = str(random.randint(0, 9))  # Generate a random digit
        elif char_type == 'letter':
            character = random.choice(string.ascii_letters)  # Generate a random letter
        else:
            character = random.choice(string.punctuation.replace('-', ''))  # Generate a random symbol excluding '-'
        
        password.append(character)
        
    
    return ''.join(password)

if __name__ == '__main__':
    app = QApplication([])
    window = QMainWindow()
    slider = QSlider(orientation = Qt.Orientation.Horizontal)
    window.setCentralWidget(slider)
    print(create_password(20))
    window.show()
    app.exec()
