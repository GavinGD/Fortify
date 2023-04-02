import ipaddress

import PyQt6
from PyQt6.QtGui import QIntValidator
from PyQt6.QtWidgets import QDialog, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, \
    QComboBox, QLineEdit, QMessageBox, QWidget
from PyQt6.QtGui import QRegularExpressionValidator
from PyQt6.QtCore import Qt, QRegularExpression
import subprocess
import API


# Can change the filename/class name to something that shows this is adding a rule
class AddRulePopup(QDialog):
    def __init__(self, parent):
        super().__init__(parent)
        self.setWindowTitle("Add Rule")
        self.setGeometry(parent.geometry().x(), parent.geometry().y(), 800, 150)

        # Should probably make all layouts, labels widgets class variables
        # i.e. self.submitBtn = QPushButton
        # Makes it so other classes can modify the widgets
        self.rule = {"-A": None,
                     "-p": None,
                     "-s": None,
                     "-d": None,
                     "--sport": None,
                     "--dport": None,
                     "-m state --state": None,
                     "-j": None}

        # Creating layout and labels (Horizontal and Vertical)
        self.layout = QHBoxLayout()
        self.layout2 = QVBoxLayout()

        # port validator
        port_reg = r"^(0|[1-9][0-9]{0,3}|[1-5][0-9]{4}|6[0-5]{2}[0-3][0-5])$"
        port_validator = QRegularExpressionValidator(self)
        port_validator.setRegularExpression(QRegularExpression(port_reg))

        # ip validator
        ip_reg = "(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)(\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)){3}"
        ip_validator = QRegularExpressionValidator(self)
        ip_validator.setRegularExpression(QRegularExpression(ip_reg))

        self.error = QLabel("")

        # chain dropdown
        self.chain = QComboBox()
        self.chain.setObjectName('-A')
        self.chain.setPlaceholderText("chain")
        self.chain.addItems(["INPUT", "OUTPUT", "FORWARD"])
        self.chain.setValidator(QIntValidator(0, self.chain.count() - 1, self))
        self.chain.setFixedWidth(100)

        # protocol dropdown
        self.protocol = QComboBox()
        self.protocol.setObjectName('-p')
        self.protocol.setPlaceholderText("protocol")
        self.protocol.addItems(["tcp", "udp", "icmp"])
        self.protocol.setFixedWidth(100)

        # source ip field
        self.source = QLineEdit()
        self.source.setObjectName('-s')
        self.source.setPlaceholderText("src IP")
        self.source.setFixedWidth(120)
        self.source.setValidator(ip_validator)

        # destination ip field
        self.dest = QLineEdit()
        self.dest.setObjectName('-d')
        self.dest.setPlaceholderText("dst IP")
        self.dest.setFixedWidth(120)
        self.dest.setValidator(ip_validator)
        # source port field
        self.sPort = QLineEdit()
        self.sPort.setObjectName('--sport')
        self.sPort.setPlaceholderText("src Port")
        self.sPort.setValidator(port_validator)
        self.sPort.setFixedWidth(80)

        # destination port field
        self.dPort = QLineEdit()
        self.dPort.setObjectName('--dport')
        self.dPort.setPlaceholderText("dst Port")
        self.dPort.setValidator(port_validator)
        self.dPort.setFixedWidth(80)

        # state dropdown
        self.state = QComboBox()
        self.state.setObjectName('-m state --state')
        self.state.setPlaceholderText("state")
        self.state.addItems(["ESTABLISHED", "RELATED", "NEW", "INVALID"])
        self.state.setFixedWidth(140)

        # target column
        self.target = QComboBox()
        self.target.setObjectName('-j')
        self.target.setPlaceholderText("target")
        self.target.addItems(["ACCEPT", "DROP", "REJECT"])
        self.target.setFixedWidth(100)

        # submit button
        self.submit = QPushButton("submit")
        self.submit.setFixedWidth(120)
        self.submit.clicked.connect(self.get_value)

        # Adding input widgets to horizontal layout
        self.layout.addWidget(self.chain)
        self.layout.addWidget(self.protocol)
        self.layout.addWidget(self.source)
        self.layout.addWidget(self.dest)
        self.layout.addWidget(self.sPort)
        self.layout.addWidget(self.dPort)
        self.layout.addWidget(self.state)
        self.layout.addWidget(self.target)
        self.layout.addWidget(self.error)
        # Add input widget and button to vertical layout
        self.layout2.addLayout(self.layout)
        self.layout2.addWidget(self.submit, alignment=Qt.AlignmentFlag.AlignCenter)

        self.setLayout(self.layout2)

    def set_text(self, text, widget):
        """
        Sets the text of a widget and readjusts label to fit text.
        :param text: text to set
        :param widget: widget to set text
        """
        widget.setText(str(text))
        widget.adjustSize()

    def get_value(self):

        combo_box_widgets = self.findChildren(QComboBox)

        if self.check_combo_value(combo_box_widgets):

            input_widgets = self.findChildren((QComboBox, QLineEdit))
            self.create_rule(input_widgets)

        # self.submit_rule()

    def check_combo_value(self, combo_boxes):

        for combo in combo_boxes:

            if combo.placeholderText() != 'protocol':

                if len(combo.currentText()) == 0:
                    QMessageBox.warning(self, "Warning", f"One of the {combo.placeholderText()} must be selected")
                    return False

        return True

    def create_rule(self, input_widgets):

        for widget in input_widgets:
            key = str(widget.objectName())

            if type(widget) == PyQt6.QtWidgets.QComboBox:

                if widget.currentText() != '':
                    self.rule[key] = widget.currentText()

            elif type(widget) == PyQt6.QtWidgets.QLineEdit:

                if widget.text() != '':
                    self.rule[key] = widget.text()


    def submit_rule(self):
        rule = "iptables "

        if (self.rule["-A"] and self.rule["-m state --state"] and self.rule["-j"]) is not None \
                and (self.rule["-d"] and self.rule["-s"]) is not "ERROR":

            for flag, val in self.rule.items():
                if val is not None:
                    rule += f"{flag} {val} "

            print(rule)
            self.__execute_command(rule.strip())
            self.close()

    def __execute_command(self, rule: str):
        # Run the command using subprocess
        process = subprocess.Popen(rule, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

        # Wait for the command to complete and capture the output
        stdout, stderr = process.communicate()

        # Print the output
        print("STDOUT:", stdout)
        print("STDERR:", stderr)
