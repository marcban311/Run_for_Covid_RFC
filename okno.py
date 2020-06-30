from PyQt5 import QtCore, QtGui, QtWidgets
import pic
import rfc
class Ui_MainWindow(object):
    
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(998, 556)
        MainWindow.setAutoFillBackground(True)
        MainWindow.setStyleSheet("background-image: url(:/tło/background.jpg);\n"
"")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
#przycisk graj
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(320, 360, 160, 31))
        self.pushButton.setStyleSheet("background-color: rgb(221, 62, 41);\n"
"font: 12pt \"Proxy 8\";")
        self.pushButton.setObjectName("pushButton")

        self.pushButton1 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton1.setGeometry(QtCore.QRect(490, 360, 160, 31))
        self.pushButton1.setStyleSheet("background-color: rgb(221, 62, 41);\n"
"font: 12pt \"Proxy 8\";")
        self.pushButton1.setObjectName("pushButton")
#globalne połączenie dwóch programów 

     
#spinbox 
     
# ilość graczy globalna 

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 998, 21))
        self.menubar.setObjectName("menubar")

        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
    
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("Najlepsza gra roku", "Najlepsza gra roku"))
        self.pushButton.setText(_translate("Najlepsza gra roku", "Dzień"))
        self.pushButton1.setText(_translate("Najlepsza gra roku", "NOC"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())