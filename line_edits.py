import sys 
from PyQt5.QtWidgets import QApplication ,QMainWindow, QLineEdit, QPushButton, QRadioButton

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(700, 300, 500, 500)
        self.line_edit = QLineEdit(self)
        self.email_edit= QLineEdit(self)
        self.psw_edit= QLineEdit(self)
        self.radio1 = QRadioButton("Male", self)
        self.radio2 = QRadioButton("Female", self)
        self.radio3 = QRadioButton("Other", self)
        self.button = QPushButton("Submit", self)
        self.initUI()
    
    def initUI(self):
        self.line_edit.setGeometry(10, 10 , 300, 40)
        self.email_edit.setGeometry(10, 60 , 300, 40)
        self.psw_edit.setGeometry(10, 110, 300, 40)
        
        self.radio1.setGeometry(0, 160, 300, 50)
        self.radio2.setGeometry(100, 160, 300, 50)
        self.radio3.setGeometry(230, 160, 300, 50)
        
        self.button.setGeometry(10, 210, 100,40)
        self.line_edit.setStyleSheet("font-size: 25px;"
                                     "font-family: Arial;")
        self.email_edit.setStyleSheet("font-size: 25px;"
                                     "font-family: Arial;" )
        self.psw_edit.setStyleSheet("font-size: 25px;"
                                     "font-family: Arial;" )
        self.setStyleSheet("QRadioButton{"
                           "font-size: 25px;"
                           "font-family: Arial;"
                           "padding: 10px; ""}")
        self.button.setStyleSheet("font-size: 25px;"
                                     "font-family: Arial;" )
        
        self.line_edit.setPlaceholderText("Enter your Name")
        self.email_edit.setPlaceholderText("Enter your Email")
        self.psw_edit.setPlaceholderText("Enter your password")
        
        self.radio1.toggled.connect(self.radio_button_changed)
        self.radio2.toggled.connect(self.radio_button_changed)
        self.radio3.toggled.connect(self.radio_button_changed)
        
        self.button.clicked.connect(self.submit)
        
    def radio_button_changed(self):
        radio_button = self.sender()
        
    def submit(self):
        name = self.line_edit.text()
        email = self.email_edit.text()
        psw = self.psw_edit.text()
        print(f"Hello {name}")
        print(f"your Email is: {email}")
        print(f"your Current password is: {psw}")
        
def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()