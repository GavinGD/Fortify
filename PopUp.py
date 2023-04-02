import ipaddress
from PyQt6.QtGui import QIntValidator
from PyQt6.QtWidgets import QDialog, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, \
    QComboBox, QLineEdit, QMessageBox
from PyQt6.QtGui import QRegularExpressionValidator
from PyQt6.QtCore import Qt, QRegularExpression
import subprocess


# Can change the filename/class name to something that shows this is adding a rule
class PopupWindow(QDialog):
    def __init__(self, parent):
        super().__init__(parent)
        self.setWindowTitle("Add Rule")
        self.setGeometry(parent.geometry().x(), parent.geometry().y(), 800, 150)

        # Should probably make all layouts, labels widgets class variables
        # i.e. self.submitBtn = QPushButton
        # Makes it so other classes can modify the widgets
        self.dictionary = {"-A": None,
                           "-p": None,
                           "-s": None,
                           "-d": None,
                           "--sport": None,
                           "--dport": None,
                           "-m state --state": None,
                           "-j": None}

        # Creating layout and labels (Horizontal and Vertical)
        layout = QHBoxLayout()
        layout2 = QVBoxLayout()

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
        self.chain.setPlaceholderText("chain")
        self.chain.addItems(["INPUT", "OUTPUT", "FORWARD"])
        self.chain.setValidator(QIntValidator(0, self.chain.count() - 1, self))
        self.chain.setFixedWidth(100)

        # protocol dropdown
        self.protocol = QComboBox()
        self.protocol.setPlaceholderText("protocol")
        self.protocol.addItems(["tcp", "udp", "icmp"])
        self.protocol.setFixedWidth(100)

        # source ip field
        self.source = QLineEdit()
        self.source.setPlaceholderText("src IP")
        self.source.setFixedWidth(120)
        self.source.setValidator(ip_validator)

        # destination ip field
        self.dest = QLineEdit()
        self.dest.setPlaceholderText("dst IP")
        self.dest.setFixedWidth(120)
        self.dest.setValidator(ip_validator)

        # source port field
        self.sPort = QLineEdit()
        self.sPort.setPlaceholderText("src Port")
        self.sPort.setValidator(port_validator)
        self.sPort.setFixedWidth(80)

        # destination port field
        self.dPort = QLineEdit()
        self.dPort.setPlaceholderText("dst Port")
        self.dPort.setValidator(port_validator)
        self.dPort.setFixedWidth(80)

        # state dropdown
        self.state = QComboBox()
        self.state.setPlaceholderText("state")
        self.state.addItems(["ESTABLISHED", "RELATED", "NEW", "INVALID"])
        self.state.setFixedWidth(140)

        # target column
        self.target = QComboBox()
        self.target.setPlaceholderText("target")
        self.target.addItems(["ACCEPT", "DROP", "REJECT"])
        self.target.setFixedWidth(100)

        # submit button
        self.submit = QPushButton("submit")
        self.submit.setFixedWidth(120)
        self.submit.clicked.connect(self.get_value)

        # Adding input widgets to horizontal layout
        layout.addWidget(self.chain)
        layout.addWidget(self.protocol)
        layout.addWidget(self.source)
        layout.addWidget(self.dest)
        layout.addWidget(self.sPort)
        layout.addWidget(self.dPort)
        layout.addWidget(self.state)
        layout.addWidget(self.target)
        layout.addWidget(self.error)

        # Add input widget and button to vertical layout
        layout2.addLayout(layout)
        layout2.addWidget(self.submit, alignment=Qt.AlignmentFlag.AlignCenter)

        self.setLayout(layout2)

    def show_error(self):
        self.set_text('Validation Error', self.error)

    def set_text(self, text, widget):
        """
        Sets the text of a widget and readjusts label to fit text.
        :param text: text to set
        :param widget: widget to set text
        """
        widget.setText(str(text))
        widget.adjustSize()

    def get_value(self):
        val_chain = self.chain.currentText()
        if len(val_chain) == 0:
            QMessageBox.warning(self, "Warning", "One of the chain must be selected")
        else:
            self.dictionary["-A"] = val_chain

        # Protocol
        val_protocol = self.protocol.currentText().strip()
        self.dictionary["-p"] = val_protocol

        # Source IP
        try:
            src_ip = self.source.text()
            if len(src_ip) == 0:
                self.dictionary["-s"] = None
            else:
                source_ip = ipaddress.ip_address(src_ip)
                self.dictionary["-s"] = source_ip
        except ValueError:
            self.dictionary["-s"] = "ERROR"
            QMessageBox.warning(self, "Warning", "Invalid Source IP Address!")

        # Destination IP
        try:
            dest_ip = self.dest.text()
            if len(dest_ip) == 0:
                self.dictionary["-d"] = None
            else:
                dest_ip = ipaddress.ip_address(dest_ip)
                self.dictionary["-d"] = dest_ip
        except ValueError:
            self.dictionary["-d"] = "ERROR"
            QMessageBox.warning(self, "Warning", "Invalid Destination IP Address!")

        # Source Port
        val_sPort = self.sPort.text()
        if len(val_sPort) == 0 or val_protocol == "icmp":
            val_sPort = None
        self.dictionary["--sport"] = val_sPort

        # Destination Port
        val_dPort = self.dPort.text()
        if len(val_dPort) == 0 or val_protocol == "icmp":
            val_dPort = None
        self.dictionary["--dport"] = val_dPort

        # State
        val_state = self.state.currentText()
        if len(val_state) == 0:
            QMessageBox.warning(self, "Warning", "One of the state must be selected")
        else:
            self.dictionary["-m state --state"] = val_state

        # Target
        val_target = self.target.currentText()
        if len(val_target) == 0:
            QMessageBox.warning(self, "Warning", "One of the target must be selected")
        else:
            self.dictionary["-j"] = val_target

        self.submit_rule()

    def submit_rule(self):
        rule = "iptables "

        if (self.dictionary["-A"] and self.dictionary["-m state --state"] and self.dictionary["-j"]) is not None \
                and (self.dictionary["-d"] and self.dictionary["-s"]) is not "ERROR":

            for flag, val in self.dictionary.items():
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
