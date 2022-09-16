from PyQt5.QtWidgets import QApplication,QLineEdit,QWidget,QFormLayout, QPushButton

from PyQt5.QtCore import Qt
import sys
app = QApplication(sys.argv)
class AppGUI (QWidget):
        def __init__(self,parent=None):
                super().__init__(parent)
                
                self.setGeometry(100, 100, 400, 400)
                self.user_time = None
                self.e3 = QLineEdit()
                self.e3.setInputMask("99:99:99")

               

                self.button = QPushButton('set', self)
                self.button.clicked.connect(self.textchanged)

                self.button.move(100,100)

                flo = QFormLayout()
               
                flo.addRow("Input Mask",self.e3)
              
               
                self.setLayout(flo)
                self.setWindowTitle("QLineEdit Example")

        def textchanged(self,text):
                self.button.setEnabled(False)
                self.user_time = self.e3.text()
                app.exit()

if __name__ == "__main__":
        app = QApplication(sys.argv)
        win = lineEditDemo()
        win.show()
        sys.exit(app.exec_())