from PyQt6.QtWidgets import QPushButton, QApplication, QMainWindow

class CircularButton(QPushButton):
    def __init__(self, text: str, function, color: str, height: int, width: int, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setText(text)
        self.setFixedHeight(height)
        self.setFixedWidth(width)
        if function != None:
            self.clicked.connect(function)
        else:
            pass
        stylesheet = """QPushButton{border-radius: 100; 
        border: 2px solid black; 
        background-color: %s}""" %color
        
        self.setStyleSheet(stylesheet)
if __name__ == '__main__':
    app = QApplication([])
    
    def foo():
        print('foo')
    
    win = QMainWindow()
    button = CircularButton('foo', foo, color='#0000FF')  # Prepend color with #
    win.setCentralWidget(button)
    win.show()
    app.exec()
