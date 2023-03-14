import sys
from PyQt6 import QtWidgets, QtGui
from PyQt6.QtWidgets import QMainWindow, QHeaderView
from fortifyUi import Ui_MainWindow


class FortifyLogic(QMainWindow, Ui_MainWindow):

    def __init__(self, app):
        super(FortifyLogic, self).__init__()
        self.setupUi(self)

        self.resize_table_headers()

    def resize_table_headers(self):
        input_table_headers = self.inputTable.horizontalHeader()
        output_table_headers = self.outputTable.horizontalHeader()
        forward_table_headers = self.forwardTable.horizontalHeader()
        input_table_headers.setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        output_table_headers.setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        forward_table_headers.setSectionResizeMode(QHeaderView.ResizeMode.Stretch)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    fortifyLogic = FortifyLogic(app)
    fortifyLogic.show()
    sys.exit(app.exec())
