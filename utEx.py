from PyQt6.QtWidgets import QApplication, QMainWindow
from untitled import Ui_MainWindow  # Import file giao diện đã chuyển đổi
from testcase130 import tinhkhauhao, tinhchitietkhauhao  # Import các hàm tính khấu hao

class MyApp(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton_2.clicked.connect(self.calculate_depreciation)

    def calculate_depreciation(self):
        try:
            # Lấy dữ liệu từ các ô nhập liệu
            giamua = float(self.lineEdit.text())
            phivanchuyen = float(self.lineEdit_2.text())
            chiphilapdat = float(self.lineEdit_3.text())
            sonam = int(self.lineEdit_4.text())

            # Gọi các hàm tính khấu hao
            nguyengia, khauhaonam, khauhaothang = tinhkhauhao(giamua, phivanchuyen, chiphilapdat, sonam)
            chitiet = tinhchitietkhauhao(giamua, phivanchuyen, chiphilapdat, sonam)

            # Hiển thị kết quả lên giao diện
            self.lineEdit_5.setText(f"{nguyengia:.2f}")
            self.lineEdit_6.setText(f"{khauhaonam:.2f}")
            self.lineEdit_7.setText(f"{khauhaothang:.2f}")
            self.lineEdit_8.setPlainText(chitiet)  # Sử dụng QTextEdit cho chitiet

        except ValueError:
            self.lineEdit_5.setText("Lỗi nhập liệu")
            self.lineEdit_6.setText("Lỗi nhập liệu")
            self.lineEdit_7.setText("Lỗi nhập liệu")
            self.lineEdit_8.setPlainText("Lỗi nhập liệu")
