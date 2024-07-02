import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QMessageBox

class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    
    def initUI(self):
        self.setWindowTitle('Contoh PyQt5')
        self.setGeometry(100, 100, 300, 200)
        
        layout = QVBoxLayout()
        
        self.button = QPushButton('Klik Saya', self)
        self.button.clicked.connect(self.showMessage)
        
        layout.addWidget(self.button)
        self.setLayout(layout)
    
    def showMessage(self):
        QMessageBox.information(self, 'Pesan', 'Anda mengklik tombol!')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    ex.show()
    sys.exit(app.exec_())
