from PyQt6.QtWidgets import QApplication, QMainWindow, QFrame, QTableWidget, QTableWidgetItem, QVBoxLayout
from PyQt6.QtCore import Qt
class PasswordFrame(QFrame):
    def __init__(self, locked: bool, passwords: list):
        super().__init__()
        self.layout = QVBoxLayout(self)
        data_length = len(passwords)
        self.data_table = QTableWidget(len(passwords), 3)
        self.data_table.setHorizontalHeaderLabels(["Website", "Username", "Password"])
        print(self.width(), self.height())
        self.layout.setAlignment(Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignCenter)
        self.data_table.setStyleSheet("""
                                      QTableWidget {
                                      background-color: none;
                                      }
                                      QTableWidgetItem {
                                      color: black;
                                      }
                                      QTableWidgetItem:selected {
                                      background-color: none;
                                      color: white;
                                      }
                                      """)
        for j, (website, username, password) in enumerate(passwords):
            self.data_table.setItem(j, 0, QTableWidgetItem(website))
            self.data_table.setItem(j, 1, QTableWidgetItem(username))
            self.data_table.setItem(j, 2, QTableWidgetItem(password))
            
        self.layout.addWidget(self.data_table)

if __name__ == '__main__':
    app = QApplication([])
    window = QMainWindow()
    passwords = [['bbc.com', 'Elliott', 'Pandek2008'], ['google.com', 'Elliott', 'EK200828'], ['itv.co.uk', 'Elliott', 'EK200828'], ['lego.com', 'Elliott', 'Pandek2008']]
    frame = PasswordFrame(locked=False, passwords=passwords)
    window.setCentralWidget(frame)
    window.show()
    app.exec()
