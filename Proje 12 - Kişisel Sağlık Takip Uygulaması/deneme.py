from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1072, 760)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(10, 10, 1051, 731))
        self.frame.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                 "border-radius: 20px;")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")

        # Title label
        self.titleLabel = QtWidgets.QLabel(self.frame)
        self.titleLabel.setGeometry(QtCore.QRect(200, 20, 671, 81))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.titleLabel.setFont(font)
        self.titleLabel.setStyleSheet("color: white;\n"
                                        "background-color: rgb(0, 85, 255);\n"
                                        "border-radius: 20px;")
        self.titleLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.titleLabel.setObjectName("titleLabel")
        self.titleLabel.setText("i - NABIZ Kişisel Sağlık Sistemi")

        # Other widgets
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(110, 250, 141, 31))
        self.label_3.setStyleSheet("background-color: rgb(173, 216, 230);\n"
                                    "border-radius: 10px;")
        self.label_3.setObjectName("label_3")
        self.comboBox = QtWidgets.QComboBox(self.frame)
        self.comboBox.setGeometry(QtCore.QRect(280, 130, 151, 31))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.label_okuma = QtWidgets.QLabel(self.frame)
        self.label_okuma.setGeometry(QtCore.QRect(550, 120, 381, 151))
        self.label_okuma.setStyleSheet("border: 2px solid #000000;")
        self.label_okuma.setText("")
        self.label_okuma.setObjectName("label_okuma")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(110, 130, 141, 31))
        self.label.setStyleSheet("background-color: rgb(173, 216, 230);\n"
                                    "border-radius: 10px;")
        self.label.setObjectName("label")
        self.lineEdit_tansiyonB = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_tansiyonB.setGeometry(QtCore.QRect(280, 170, 191, 31))
        self.lineEdit_tansiyonB.setObjectName("lineEdit_tansiyonB")
        self.lineEdit_tansiyonK = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_tansiyonK.setGeometry(QtCore.QRect(280, 210, 191, 31))
        self.lineEdit_tansiyonK.setObjectName("lineEdit_tansiyonK")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(110, 210, 141, 31))
        self.label_2.setStyleSheet("background-color: rgb(173, 216, 230);\n"
                                    "border-radius: 10px;")
        self.label_2.setObjectName("label_2")
        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setGeometry(QtCore.QRect(110, 170, 141, 31))
        self.label_4.setStyleSheet("background-color: rgb(173, 216, 230);\n"
                                    "border-radius: 10px;")
        self.label_4.setObjectName("label_4")
        self.lineEdit_kansekeri = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_kansekeri.setGeometry(QtCore.QRect(280, 250, 191, 31))
        self.lineEdit_kansekeri.setObjectName("lineEdit_kansekeri")
        self.pushButton_kaydet = QtWidgets.QPushButton(self.frame)
        self.pushButton_kaydet.setGeometry(QtCore.QRect(200, 330, 431, 61))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_kaydet.setFont(font)
        self.pushButton_kaydet.setStyleSheet("background-color: rgb(0, 85, 255);\n"
                                                "color: white;\n"
                                                "border-radius: 30px;")
        self.pushButton_kaydet.setObjectName("pushButton_kaydet")
        self.pushButton_rapor = QtWidgets.QPushButton(self.frame)
        self.pushButton_rapor.setGeometry(QtCore.QRect(60, 460, 431, 61))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_rapor.setFont(font)
        self.pushButton_rapor.setStyleSheet("background-color: rgb(0, 85, 255);\n"
                                                "color: white;\n"
                                                "border-radius: 30px;")
        self.pushButton_rapor.setObjectName("pushButton_rapor")
        self.pushButton_egzersiz = QtWidgets.QPushButton(self.frame)
        self.pushButton_egzersiz.setGeometry(QtCore.QRect(540, 460, 431, 61))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_egzersiz.setFont(font)
        self.pushButton_egzersiz.setStyleSheet("background-color: rgb(0, 85, 255);\n"
                                                    "color: white;\n"
                                                    "border-radius: 30px;")
        self.pushButton_egzersiz.setObjectName("pushButton_egzersiz")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1072, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Kişisel Sağlık Takibi"))
        self.label_3.setText(_translate("MainWindow", "Kan Şekeri"))
        self.comboBox.setItemText(0, _translate("MainWindow", "100-160"))
        self.comboBox.setItemText(1, _translate("MainWindow", "70-120"))
        self.comboBox.setItemText(2, _translate("MainWindow", "60-100"))
        self.comboBox.setItemText(3, _translate("MainWindow", "40-60"))
        self.label.setText(_translate("MainWindow", "Nabız"))
        self.lineEdit_tansiyonB.setPlaceholderText(_translate("MainWindow", "Lütfen mmHg cinsinden giriniz."))
        self.lineEdit_tansiyonK.setPlaceholderText(_translate("MainWindow", "Lütfen mmHg cinsinden giriniz."))
        self.label_2.setText(_translate("MainWindow", "Tansiyon (Küçük)"))
        self.label_4.setText(_translate("MainWindow", "Tansiyon (Büyük)"))
        self.lineEdit_kansekeri.setPlaceholderText(_translate("MainWindow", "Lütfen mg/dl cinsinden giriniz."))
        self.pushButton_kaydet.setText(_translate("MainWindow", "Kaydet"))
        self.pushButton_rapor.setText(_translate("MainWindow", "Rapor Almak İçin Tıklayınız"))
        self.pushButton_egzersiz.setText(_translate("MainWindow", "Egzersiz Sayfasına Gitmek İçin Tıklayınız"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
