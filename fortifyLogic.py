import sys, qdarktheme
from PyQt6 import QtWidgets, QtGui
from PyQt6.QtWidgets import QMainWindow, QHeaderView
from fortifyUI import Ui_MainWindow
from API import *


class FortifyLogic(QMainWindow, Ui_MainWindow):

    def __init__(self, app):
        super(FortifyLogic, self).__init__()
        self.setupUi(self)

        # Resize the tables headers, set the chains policies and load rules
        self.resize_table_headers()
        self.set_chain_policies()
        self.load_rules()

        # Connect the Dark and Light mode buttons to set_theme
        self.actionDark_Mode.triggered.connect(lambda: self.set_theme(self.actionDark_Mode.text()))
        self.actionLight_Mode.triggered.connect(lambda: self.set_theme(self.actionLight_Mode.text()))

    def set_chain_policies(self):
        """
        Sets all the chains policies.
        """
        self.set_chain_policy(self.inputLbl.text(), self.inputPolicyLbl)
        self.set_chain_policy(self.forwardLbl.text(), self.forwardPolicyLbl)
        self.set_chain_policy(self.outputLbl.text(), self.outputPolicyLbl)

    def set_chain_policy(self, chain_label, widget):
        """
        Sets a chain policy.
        :param chain_label: chain to get policy
        :param widget: widget to set policy
        """
        policy = ui_chain_policy(chain_label)
        self.set_text(f'({policy})', widget)

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

    def load_rules(self):
        """
        Loads the rules for the chains.
        :return:
        """
        self.set_table_rules(self.inputTable, self.inputLbl.text())
        self.set_table_rules(self.forwardTable, self.forwardLbl.text())
        self.set_table_rules(self.outputTable, self.outputLbl.text())

    def set_table_rules(self, table, chain):
        """
        Sets the table rules that are currently in iptables.
        :param table: table widget to set
        :param chain: chain to get rules
        """
        rules = ui_chain_rules(chain)
        row = 0
        table.setRowCount(len(rules))

        for rule in rules:
            table.setItem(row, 0, QtWidgets.QTableWidgetItem(rule['target']))
            table.setItem(row, 1, QtWidgets.QTableWidgetItem(rule['protocol']))
            table.setItem(row, 2, QtWidgets.QTableWidgetItem(rule['source']))
            table.setItem(row, 3, QtWidgets.QTableWidgetItem(rule['destination']))
            table.setItem(row, 4, QtWidgets.QTableWidgetItem(rule['sport']))
            table.setItem(row, 5, QtWidgets.QTableWidgetItem(rule['dport']))
            table.setItem(row, 6, QtWidgets.QTableWidgetItem(rule['state']))
            row += 1

    def set_text(self, text, widget):
        """
        Sets the text of a widget.
        :param text: text to set
        :param widget: widget to set text
        """
        widget.setText(str(text))
        widget.adjustSize()

    def set_theme(self, mode):
        """
        Sets the theme of the app.
        :param mode: Dark Mode or Light Mode
        """
        if mode == 'Dark Mode':
            qdarktheme.setup_theme('dark')
        elif mode == 'Light Mode':
            qdarktheme.setup_theme('light')


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    qdarktheme.setup_theme('auto')
    fortifyLogic = FortifyLogic(app)
    fortifyLogic.show()
    sys.exit(app.exec())
