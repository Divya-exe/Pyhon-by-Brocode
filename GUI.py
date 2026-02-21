import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow, QLabel, QWidget, QVBoxLayout, QHBoxLayout, QGridLayout)
# from PyQt5.QtGui import QPixmap
# from PyQt5.QtGui import QIcon
# from PyQt5.QtGui import QFont
# from PyQt5.QtCore import Qt
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(700, 300, 500, 500)
        self.initUI()
        
    def initUI(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        label1 = QLabel("#1", self)
        label2 = QLabel("#2", self) 
        label3 = QLabel("#3", self)
        label4 = QLabel("#4", self)
        label5 = QLabel("#5", self)
        
        label1.setStyleSheet("background-color: red;")
        label2.setStyleSheet("background-color: yellow;")
        label3.setStyleSheet("background-color: green;")
        label4.setStyleSheet("background-color: blue;")
        label5.setStyleSheet("background-color: purple;")
        
        grid =  QGridLayout()
        grid.addWidget(label1, 0, 0)
        grid.addWidget(label2, 0, 1)
        grid.addWidget(label3, 1, 0)
        grid.addWidget(label4, 1, 1)
        grid.addWidget(label5, 2, 2)
        
        central_widget.setLayout(grid)
        
        
        # label = QLabel(self)
        # label.setGeometry(0,0,250,250)
        
        # pixmap= QPixmap("divya.jpg")
        # label.setPixmap(pixmap)
        
        # label.setScaledContents(True)
        
        # label.setGeometry((self.width() - label.width()) // 2,
        #                   (self.height() - label.height()) // 2,
        #                   label.width(), 
        #                   label.height() )
        
        # label = QLabel("Hello", self)
        # label.setFont(QFont("Arial", 30))
        # label.setGeometry(0,0,500,100)
        # label.setStyleSheet("color: #A020F0;"
        #                     "background-color: yellow;"
        #                     "font-weight: bold;"
        #                     "font-styel: italic;"
        #                     "text-decoration: underline;")
        # label.setAlignment(Qt.AlignBottom) vertically Bottom
        # label.setAlignment(Qt.AlignTop) vertically top
        #label.setAlignment(Qt.AlignVCenter) #vertically center
        
        # label.setAlignment(Qt.AlignRight) horizontally right
        #label.setAlignment(Qt.AlignHCenter) #horizontally center
        # label.setAlignment(Qt.AlignLeft) horizontally Left
        
        # label.setAlignment(Qt.AlignHCenter | Qt.AlignTop)
        # label.setAlignment(Qt.AlignHCenter | Qt.AlignBottom )
        #label.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        # # label.setAlignment(Qt.AlignHCenter | Qt.AlignBottom )
        # label.setAlignment(Qt.AlignCenter)
        
        
def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
