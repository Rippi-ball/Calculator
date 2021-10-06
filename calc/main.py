from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(300, 395)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 300, 50))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(41, 55, 183, 255), stop:1 rgba(255, 17, 255, 255));\n"
"color: rgb(255, 255, 255);")
        self.label.setObjectName("label")
        self.btn_0 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_0.setGeometry(QtCore.QRect(0, 315, 100, 60))
        self.btn_0.setStyleSheet("background-color: rgb(85, 0, 255);\n"
"color: rgb(255, 255, 255);")
        self.btn_0.setObjectName("btn_0")
        self.btn_1 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_1.setGeometry(QtCore.QRect(0, 230, 75, 85))
        self.btn_1.setStyleSheet("background-color: rgb(85, 0, 255);\n"
"color: rgb(255, 255, 255);")
        self.btn_1.setObjectName("btn_1")
        self.btn_2 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_2.setGeometry(QtCore.QRect(70, 230, 75, 85))
        self.btn_2.setStyleSheet("background-color: rgb(85, 0, 255);\n"
"color: rgb(255, 255, 255);")
        self.btn_2.setObjectName("btn_2")
        self.btn_3 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_3.setGeometry(QtCore.QRect(140, 230, 75, 85))
        self.btn_3.setStyleSheet("background-color: rgb(85, 0, 255);\n"
"color: rgb(255, 255, 255);")
        self.btn_3.setObjectName("btn_3")
        self.btn_4 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_4.setGeometry(QtCore.QRect(0, 140, 75, 90))
        self.btn_4.setStyleSheet("background-color: rgb(85, 0, 255);\n"
"color: rgb(255, 255, 255);")
        self.btn_4.setObjectName("btn_4")
        self.btn_5 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_5.setGeometry(QtCore.QRect(70, 140, 75, 90))
        self.btn_5.setStyleSheet("background-color: rgb(85, 0, 255);\n"
"color: rgb(255, 255, 255);")
        self.btn_5.setObjectName("btn_5")
        self.btn_6 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_6.setGeometry(QtCore.QRect(140, 140, 75, 90))
        self.btn_6.setStyleSheet("background-color: rgb(85, 0, 255);\n"
"color: rgb(255, 255, 255);")
        self.btn_6.setObjectName("btn_6")
        self.btn_7 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_7.setGeometry(QtCore.QRect(0, 50, 75, 90))
        self.btn_7.setStyleSheet("background-color: rgb(85, 0, 255);\n"
"color: rgb(255, 255, 255);")
        self.btn_7.setObjectName("btn_7")
        self.btn_9 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_9.setGeometry(QtCore.QRect(140, 50, 75, 90))
        self.btn_9.setStyleSheet("background-color: rgb(85, 0, 255);\n"
"color: rgb(255, 255, 255);")
        self.btn_9.setObjectName("btn_9")
        self.btn_8 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_8.setGeometry(QtCore.QRect(70, 50, 75, 90))
        self.btn_8.setStyleSheet("background-color: rgb(85, 0, 255);\n"
"color: rgb(255, 255, 255);")
        self.btn_8.setObjectName("btn_8")
        self.btn_sub = QtWidgets.QPushButton(self.centralwidget)
        self.btn_sub.setGeometry(QtCore.QRect(210, 140, 90, 90))
        self.btn_sub.setStyleSheet("background-color: rgb(0, 0, 127);\n"
"color: rgb(255, 255, 255);")
        self.btn_sub.setObjectName("btn_sub")
        self.btn_multi = QtWidgets.QPushButton(self.centralwidget)
        self.btn_multi.setGeometry(QtCore.QRect(210, 230, 90, 85))
        self.btn_multi.setStyleSheet("background-color: rgb(0, 0, 127);\n"
"color: rgb(255, 255, 255);")
        self.btn_multi.setObjectName("btn_multi")
        self.btn_del = QtWidgets.QPushButton(self.centralwidget)
        self.btn_del.setGeometry(QtCore.QRect(200, 315, 101, 60))
        self.btn_del.setStyleSheet("background-color: rgb(0, 0, 127);\n"
"color: rgb(255, 255, 255);")
        self.btn_del.setObjectName("btn_del")
        self.btn_sum = QtWidgets.QPushButton(self.centralwidget)
        self.btn_sum.setGeometry(QtCore.QRect(210, 50, 90, 90))
        self.btn_sum.setStyleSheet("background-color: rgb(0, 0, 127);\n"
"color: rgb(255, 255, 255);")
        self.btn_sum.setObjectName("btn_sum")
        self.btn_equal = QtWidgets.QPushButton(self.centralwidget)
        self.btn_equal.setGeometry(QtCore.QRect(100, 315, 100, 60))
        self.btn_equal.setStyleSheet("background-color: rgb(0, 0, 127);\n"
"color: rgb(255, 255, 255);")
        self.btn_equal.setObjectName("btn_equal")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.add_func()

        self.is_equel = False

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Калькулятор"))
        self.label.setText(_translate("MainWindow", "0"))
        self.btn_0.setText(_translate("MainWindow", "0"))
        self.btn_1.setText(_translate("MainWindow", "1"))
        self.btn_2.setText(_translate("MainWindow", "2"))
        self.btn_3.setText(_translate("MainWindow", "3"))
        self.btn_4.setText(_translate("MainWindow", "4"))
        self.btn_5.setText(_translate("MainWindow", "5"))
        self.btn_6.setText(_translate("MainWindow", "6"))
        self.btn_7.setText(_translate("MainWindow", "7"))
        self.btn_9.setText(_translate("MainWindow", "9"))
        self.btn_8.setText(_translate("MainWindow", "8"))
        self.btn_sub.setText(_translate("MainWindow", "-"))
        self.btn_multi.setText(_translate("MainWindow", "*"))
        self.btn_del.setText(_translate("MainWindow", "/"))
        self.btn_sum.setText(_translate("MainWindow", "+"))
        self.btn_equal.setText(_translate("MainWindow", "="))

    def add_func(self):
        self.btn_0.clicked.connect(lambda: self.write_number(self.btn_0.text()))
        self.btn_1.clicked.connect(lambda: self.write_number(self.btn_1.text()))
        self.btn_2.clicked.connect(lambda: self.write_number(self.btn_2.text()))
        self.btn_3.clicked.connect(lambda: self.write_number(self.btn_3.text()))
        self.btn_4.clicked.connect(lambda: self.write_number(self.btn_4.text()))
        self.btn_5.clicked.connect(lambda: self.write_number(self.btn_5.text()))
        self.btn_6.clicked.connect(lambda: self.write_number(self.btn_6.text()))
        self.btn_7.clicked.connect(lambda: self.write_number(self.btn_7.text()))
        self.btn_8.clicked.connect(lambda: self.write_number(self.btn_8.text()))
        self.btn_9.clicked.connect(lambda: self.write_number(self.btn_9.text()))
        self.btn_sub.clicked.connect(lambda: self.write_number(self.btn_sub.text()))
        self.btn_multi.clicked.connect(lambda: self.write_number(self.btn_multi.text()))
        self.btn_del.clicked.connect(lambda: self.write_number(self.btn_del.text()))
        self.btn_sum.clicked.connect(lambda: self.write_number(self.btn_sum.text()))
        self.btn_equal.clicked.connect(self.results)

    def write_number(self, number):
        if self.label.text() == '0' or self.is_equel == True:
            self.label.setText(number)
            self.is_equel = False
        else:
            self.label.setText(self.label.text() + str(number))

    def results(self):
        if not self.is_equel:
            res = eval(self.label.text())
            self.label.setText(str(res))
            self.is_equel = True
        else:
            error = QMessageBox()
            error.setWindowTitle('Ошибка')
            error.setText('Сейчас это действие выполнить нельзя.')
            error.setIcon(QMessageBox.Warning)
            error.setStandardButtons(QMessageBox.Ok|QMessageBox.Cancel|QMessageBox.Reset)
            error.setDefaultButton(QMessageBox.Ok)
            error.setInformativeText("Два раза действие не выполнить.")
            error.setDetailedText('Детали')

            error.buttonClicked.connect(self.popup_action)

            error.exec_()

    def popup_action(self, btn):
        if btn.text() == 'Ok':
            print('Ok')
        elif btn.text() == 'Reset':
            self.label.setText('0')
            self.is_equel = False


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())