from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(800, 500)  # Adjusting the size of the dialog
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(100, 20, 400, 40))  # Adjusting the size and position
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(50, 80, 100, 30))  # Adjusting the size and position
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(50, 140, 100, 30))  # Adjusting the size and position
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(50, 260, 500, 40))  # Adjusting the size and position
        font.setPointSize(14)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(50, 220, 500, 40))  # Adjusting the size and position
        font.setPointSize(14)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.widget = QtWidgets.QWidget(Dialog)
        self.widget.setGeometry(QtCore.QRect(150, 80, 200, 120))  # Adjusting the size and position
        self.widget.setObjectName("widget")
        self.gridLayout = QtWidgets.QGridLayout(self.widget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.lineEdit = QtWidgets.QLineEdit(self.widget)
        font.setPointSize(12)
        self.lineEdit.setFont(font)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 0, 0, 1, 1)
        self.comboBox = QtWidgets.QComboBox(self.widget)
        self.comboBox.setFont(font)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.gridLayout.addWidget(self.comboBox, 1, 0, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.widget)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 2, 0, 1, 1)

        self.retranslateUi(Dialog)
        self.pushButton.clicked.connect(self.calculate_tax)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "PERHITUNGAN PAJAK"))
        self.label_2.setText(_translate("Dialog", "Harga"))
        self.label_3.setText(_translate("Dialog", "Pajak"))
        self.label_4.setText(_translate("Dialog", ""))
        self.label_5.setText(_translate("Dialog", "Total harga beserta pajak adalah:"))
        self.comboBox.setItemText(0, _translate("Dialog", "5%"))
        self.comboBox.setItemText(1, _translate("Dialog", "10%"))
        self.comboBox.setItemText(2, _translate("Dialog", "15%"))
        self.pushButton.setText(_translate("Dialog", "Hitung Pajak"))

    def calculate_tax(self):
        try:
            price = float(self.lineEdit.text())
            tax_rate_str = self.comboBox.currentText()
            tax_rate = float(tax_rate_str.strip('%')) / 100
            tax_amount = price * tax_rate
            total_price = price + tax_amount
            self.label_4.setText(f"Total Pajak: {tax_amount:.2f}")
            self.label_5.setText(f"Total harga beserta pajak adalah: {total_price:.2f}")
        except ValueError:
            self.label_4.setText("Input tidak valid")
            self.label_5.setText("")

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
