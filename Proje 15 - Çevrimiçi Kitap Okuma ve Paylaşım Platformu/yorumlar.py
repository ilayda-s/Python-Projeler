# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'yorumlar.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(712, 537)
        MainWindow.setStyleSheet("#centralwidget{background-color: rgb(0, 0, 0);}\n"
"\n"
"\n"
"\n"
"\n"
"")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 10, 691, 501))
        self.label.setStyleSheet("border-radius:20;\n"
"background-color: rgb(194, 6, 15);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(20, 20, 71, 61))
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap(":/iku/1200px-Kültür_Üniversitesi_Logo.png"))
        self.label_3.setScaledContents(True)
        self.label_3.setWordWrap(False)
        self.label_3.setOpenExternalLinks(False)
        self.label_3.setObjectName("label_3")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(100, 10, 271, 41))
        font = QtGui.QFont()
        font.setFamily("Cascadia Code")
        font.setPointSize(18)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.label_5.setFont(font)
        self.label_5.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.label_5.setFocusPolicy(QtCore.Qt.NoFocus)
        self.label_5.setStyleSheet("color:white")
        self.label_5.setIndent(-1)
        self.label_5.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(110, 30, 251, 41))
        font = QtGui.QFont()
        font.setFamily("Cascadia Code")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        self.label_6.setFont(font)
        self.label_6.setFocusPolicy(QtCore.Qt.NoFocus)
        self.label_6.setStyleSheet("color:white")
        self.label_6.setIndent(-1)
        self.label_6.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse)
        self.label_6.setObjectName("label_6")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(130, 50, 171, 41))
        font = QtGui.QFont()
        font.setFamily("Cascadia Code")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        self.label_9.setFont(font)
        self.label_9.setFocusPolicy(QtCore.Qt.NoFocus)
        self.label_9.setStyleSheet("color:white")
        self.label_9.setIndent(-1)
        self.label_9.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse)
        self.label_9.setObjectName("label_9")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(80, 160, 511, 301))
        font = QtGui.QFont()
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.tableWidget.setFont(font)
        self.tableWidget.setMouseTracking(False)
        self.tableWidget.setStyleSheet("QTableWidget {\n"
"    border: 1px solid #ccc; /* Çevre kenarlık rengi */\n"
"      gridline-color: #ccc; /* Izgara çizgileri için açık gri renk */\n"
"\n"
"}\n"
"\n"
"\n"
"QTableWidget::item:selected {\n"
"    color: white; /* Seçili öğe metin rengi */\n"
"    background-color: rgb(94, 94, 94);\n"
"\n"
"}\n"
"\n"
"QHeaderView::section {\n"
"    border: 1px solid #ddd; /* Başlık kenarlık rengi */\n"
"    background-color: rgb(52, 52, 52);\n"
"\n"
"    color: white; /* Başlık metin rengi */\n"
"    padding: 6px;\n"
"    font-size: 9pt;\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"")
        self.tableWidget.setLineWidth(1)
        self.tableWidget.setAutoScroll(False)
        self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidget.setTabKeyNavigation(False)
        self.tableWidget.setProperty("showDropIndicator", False)
        self.tableWidget.setDragDropOverwriteMode(False)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setRowCount(9)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(1, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(1, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(1, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(2, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(2, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(2, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(3, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(3, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(3, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(4, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(4, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(4, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(5, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(5, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(5, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(6, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(6, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(6, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(7, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(7, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(7, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(8, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(8, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(8, 2, item)
        self.tableWidget.horizontalHeader().setVisible(True)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(162)
        self.tableWidget.horizontalHeader().setHighlightSections(False)
        self.tableWidget.horizontalHeader().setMinimumSectionSize(40)
        self.tableWidget.horizontalHeader().setSortIndicatorShown(False)
        self.tableWidget.horizontalHeader().setStretchLastSection(False)
        self.tableWidget.verticalHeader().setVisible(True)
        self.tableWidget.verticalHeader().setHighlightSections(False)
        self.pushButton_7 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_7.setGeometry(QtCore.QRect(510, 30, 171, 41))
        font = QtGui.QFont()
        font.setFamily("Cascadia Code SemiBold")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_7.setFont(font)
        self.pushButton_7.setStyleSheet("\n"
"QPushButton{\n"
"color:white;\n"
"    background-color: rgb(72, 105, 102);\n"
"border-radius:10;}\n"
"QPushButton::hover{background-color: rgb(117, 117, 117);}\n"
"\n"
"")
        self.pushButton_7.setObjectName("pushButton_7")
        self.label.raise_()
        self.label_3.raise_()
        self.label_6.raise_()
        self.label_5.raise_()
        self.label_9.raise_()
        self.tableWidget.raise_()
        self.pushButton_7.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_5.setText(_translate("MainWindow", "Kültür Üniversitesi"))
        self.label_6.setText(_translate("MainWindow", "Çevrimiçi Kitap Okuma ve"))
        self.label_9.setText(_translate("MainWindow", "Paylaşım Platformu"))
        item = self.tableWidget.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "1"))
        item = self.tableWidget.verticalHeaderItem(1)
        item.setText(_translate("MainWindow", "2"))
        item = self.tableWidget.verticalHeaderItem(2)
        item.setText(_translate("MainWindow", "3"))
        item = self.tableWidget.verticalHeaderItem(3)
        item.setText(_translate("MainWindow", "4"))
        item = self.tableWidget.verticalHeaderItem(4)
        item.setText(_translate("MainWindow", "5"))
        item = self.tableWidget.verticalHeaderItem(5)
        item.setText(_translate("MainWindow", "6"))
        item = self.tableWidget.verticalHeaderItem(6)
        item.setText(_translate("MainWindow", "7"))
        item = self.tableWidget.verticalHeaderItem(7)
        item.setText(_translate("MainWindow", "8"))
        item = self.tableWidget.verticalHeaderItem(8)
        item.setText(_translate("MainWindow", "9"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Kitap Adı"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Yorum Yapan Kullanıcı"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Yorumu"))
        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        self.tableWidget.setSortingEnabled(__sortingEnabled)
        self.pushButton_7.setText(_translate("MainWindow", "Geri"))
import iku_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
