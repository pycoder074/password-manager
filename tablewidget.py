import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("QTableWidget Example")
        self.setGeometry(100, 100, 600, 400)

        self.tableWidget = QTableWidget(self)
        self.tableWidget.setGeometry(50, 50, 500, 300)

        # Set number of rows and columns
        self.tableWidget.setRowCount(3)
        self.tableWidget.setColumnCount(3)

        # Add text to specific cell
        self.tableWidget.setItem(0, 0, QTableWidgetItem("Row 1, Column 1"))
        self.tableWidget.setItem(1, 1, QTableWidgetItem("Row 2, Column 2"))
        self.tableWidget.setItem(2, 2, QTableWidgetItem("Row 3, Column 3"))

def main():
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()
