import sys, qdarktheme
from PyQt6 import QtWidgets, QtGui
from PyQt6.QtWidgets import QMainWindow, QHeaderView
from fortifyUi import Ui_MainWindow


class FortifyLogic(QMainWindow, Ui_MainWindow):

    def __init__(self, app):
        super(FortifyLogic, self).__init__()
        self.setupUi(self)

        self.resize_table_headers()
        self.actionDark_Mode.triggered.connect(lambda: self.set_theme(self.actionDark_Mode.text()))
        self.actionLight_Mode.triggered.connect(lambda: self.set_theme(self.actionLight_Mode.text()))

    def resize_table_headers(self):
        """
        Resizes the table headers to fit the width of the table.
        QtDesigner does not do it automatically
        """
        input_table_headers = self.inputTable.horizontalHeader()
        output_table_headers = self.outputTable.horizontalHeader()
        forward_table_headers = self.forwardTable.horizontalHeader()
        input_table_headers.setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        output_table_headers.setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        forward_table_headers.setSectionResizeMode(QHeaderView.ResizeMode.Stretch)

    def set_theme(self, mode):
        if mode == 'Dark Mode':
            qdarktheme.setup_theme('dark')
        elif mode == 'Light Mode':
            qdarktheme.setup_theme('light')


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    qdarktheme.setup_theme()
    fortifyLogic = FortifyLogic(app)
    fortifyLogic.show()
    sys.exit(app.exec())
