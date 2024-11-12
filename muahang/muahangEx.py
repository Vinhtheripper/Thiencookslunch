from muahangdesign import Ui_MainWindow  # Import your design class
class MainWindowProductUIExt(Ui_MainWindow):
    price_laptop = 25
    price_robot = 100
    num_xachtay_laptop = 0
    num_xachtay_robot = 0
    num_chinhhang_laptop = 0
    num_chinhhang_robot = 0
    money_xachtay_laptop = 0
    money_xachtay_robot = 0
    money_chinhhang_laptop = 0
    money_chinhhang_robot = 0

    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow = MainWindow
        self.setupSignalAndSlot()
    def showWindow(self):
        self.MainWindow.show()
    def setupSignalAndSlot(self):
        self.pushButton.clicked.connect(self.process_mua)
    def process_mua(self):
        n_laptop = 0
        n_robot = 0
        try:
            n_laptop = int(self.lineEdit.text())
        except ValueError:
            n_laptop = 0
        try:
            n_robot = int(self.lineEdit_2.text())
        except ValueError:
            n_robot = 0
        if self.radioButton.isChecked():
            money_laptop = n_laptop * self.price_laptop * 0.9
            money_robot = n_robot * self.price_robot * 0.9
            self.num_xachtay_laptop =self.num_xachtay_laptop + n_laptop
            self.num_xachtay_robot = self.num_xachtay_robot + n_robot
            self.money_xachtay_laptop = self.money_xachtay_laptop + money_laptop
            self.money_xachtay_robot = self.money_xachtay_robot + money_robot
        else:
            money_laptop = n_laptop * self.price_laptop
            money_robot = n_robot * self.price_robot
            self.num_chinhhang_laptop =self.num_chinhhang_laptop + n_laptop
            self.num_chinhhang_robot = self.num_chinhhang_robot + n_robot
            self.money_chinhhang_robot = self.money_chinhhang_robot + money_robot
            self.num_xachtay_laptop = self.num_xachtay_laptop + money_laptop
        self.lineEdit_3.setText(str(self.num_xachtay_laptop))
        self.lineEdit_4.setText(str(self.num_xachtay_robot))
        self.lineEdit_7.setText(str(self.num_chinhhang_laptop))
        self.lineEdit_9.setText(str(self.num_chinhhang_robot))
        self.lineEdit_5.setText(str(self.money_xachtay_laptop))
        self.lineEdit_6.setText(str(self.money_xachtay_robot))
        self.lineEdit_8.setText(str(self.money_chinhhang_laptop))
        self.lineEdit_10.setText(str(self.money_chinhhang_robot))
