# Form implementation generated from reading ui file '/Users/quangvinh/Documents/Pythonfile/Thiencookslunch/untitled.ui'
#
# Created by: PyQt6 UI code generator 6.7.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(458, 508)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(160, 30, 151, 21))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.groupBox = QtWidgets.QGroupBox(parent=self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(79, 90, 301, 151))
        self.groupBox.setObjectName("groupBox")
        self.lineEdit = QtWidgets.QLineEdit(parent=self.groupBox)
        self.lineEdit.setGeometry(QtCore.QRect(140, 30, 113, 21))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(parent=self.groupBox)
        self.lineEdit_2.setGeometry(QtCore.QRect(140, 60, 113, 21))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(parent=self.groupBox)
        self.lineEdit_3.setGeometry(QtCore.QRect(140, 90, 113, 21))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(parent=self.groupBox)
        self.lineEdit_4.setGeometry(QtCore.QRect(140, 120, 113, 21))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.label_2 = QtWidgets.QLabel(parent=self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(50, 30, 60, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(parent=self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(50, 60, 91, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(parent=self.groupBox)
        self.label_4.setGeometry(QtCore.QRect(50, 90, 71, 16))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(parent=self.groupBox)
        self.label_5.setGeometry(QtCore.QRect(50, 120, 60, 16))
        self.label_5.setObjectName("label_5")
        self.groupBox_2 = QtWidgets.QGroupBox(parent=self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(80, 260, 301, 151))
        self.groupBox_2.setObjectName("groupBox_2")
        self.lineEdit_5 = QtWidgets.QLineEdit(parent=self.groupBox_2)
        self.lineEdit_5.setGeometry(QtCore.QRect(140, 30, 113, 21))
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.lineEdit_6 = QtWidgets.QLineEdit(parent=self.groupBox_2)
        self.lineEdit_6.setGeometry(QtCore.QRect(140, 60, 113, 21))
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.lineEdit_7 = QtWidgets.QLineEdit(parent=self.groupBox_2)
        self.lineEdit_7.setGeometry(QtCore.QRect(140, 90, 113, 21))
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.lineEdit_8 = QtWidgets.QLineEdit(parent=self.groupBox_2)
        self.lineEdit_8.setGeometry(QtCore.QRect(140, 120, 113, 21))
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.label_6 = QtWidgets.QLabel(parent=self.groupBox_2)
        self.label_6.setGeometry(QtCore.QRect(50, 30, 71, 16))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(parent=self.groupBox_2)
        self.label_7.setGeometry(QtCore.QRect(50, 60, 91, 16))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(parent=self.groupBox_2)
        self.label_8.setGeometry(QtCore.QRect(50, 90, 91, 16))
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(parent=self.groupBox_2)
        self.label_9.setGeometry(QtCore.QRect(50, 120, 60, 16))
        self.label_9.setObjectName("label_9")
        self.pushButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(310, 420, 113, 32))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(270, 240, 113, 32))
        self.pushButton_2.setObjectName("pushButton_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 458, 33))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.pushButton.clicked.connect(MainWindow.close) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "NguyenQuangVInh-K234111460"))
        self.label.setText(_translate("MainWindow", "Tính khấu hao"))
        self.groupBox.setTitle(_translate("MainWindow", "Nhập liệu"))
        self.label_2.setText(_translate("MainWindow", "gia mua"))
        self.label_3.setText(_translate("MainWindow", "phivanchuyen"))
        self.label_4.setText(_translate("MainWindow", "philapdat"))
        self.label_5.setText(_translate("MainWindow", "sonam"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Kết quả"))
        self.label_6.setText(_translate("MainWindow", "nguyengia"))
        self.label_7.setText(_translate("MainWindow", "khauhaonam"))
        self.label_8.setText(_translate("MainWindow", "khauhaothang"))
        self.label_9.setText(_translate("MainWindow", "chitiet"))
        self.pushButton.setText(_translate("MainWindow", "Close"))
        self.pushButton_2.setText(_translate("MainWindow", "Tính Toán"))
