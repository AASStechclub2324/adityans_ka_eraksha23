# from PyQt5.QtWidgets import *

# class MainWindow(QMainWindow):
#     def __init__(self):
#         super().__init__()

#         self.centralwidget = QWidget()
#         self.setCentralWidget(self.centralwidget)

#         lay = QHBoxLayout(self.centralwidget)


# stylesheet = """
#     MainWindow {
#         background-image: url("world_map.jpg"); 
#         background-repeat: no-repeat; 
#         background-size: cover;
#         background-position: center;
#     }
# """

# if __name__ == "__main__":
#     import sys
#     app = QApplication(sys.argv)
#     app.setStyleSheet(stylesheet)     # <---
#     window = MainWindow()
#     window.resize(1950, 9400)
#     window.show()
#     sys.exit(app.exec_())


import sys
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QMainWindow, QApplication, QLabel

class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()
        self.title = "Image Viewer"
        self.setWindowTitle(self.title)

        label = QLabel(self)
        pixmap = QPixmap('world_map.jpg')
        label.setPixmap(pixmap)
        label.setScaledContents(True)
        self.setCentralWidget(label)
        self.resize(pixmap.width(), pixmap.height())


app = QApplication(sys.argv)
w = MainWindow()
w.resize(1200, 720)
w.show()
sys.exit(app.exec())
