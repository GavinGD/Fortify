import ipaddress
import PyQt6
from PyQt6.QtGui import QIntValidator
from PyQt6.QtWidgets import QDialog, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, \
    QComboBox, QLineEdit, QMessageBox, QWidget
from PyQt6.QtGui import QRegularExpressionValidator
from PyQt6.QtCore import Qt, QRegularExpression
from API import ui_add_rule


class AddRulePopup(QDialog):
    def __init__(self, parent):
        super().__init__(parent)
        self.setWindowTitle("Add Rule")
        self.setGeometry(parent.geometry().x(), parent.geometry().y(), 800, 150)
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
        self.submit.clicked.connect(self.submit_rule)

        # Adding input widgets to horizontal layout
        self.layout.addWidget(self.chain)
        self.layout.addWidget(self.protocol)
        self.layout.addWidget(self.source)
        self.layout.addWidget(self.dest)
        self.layout.addWidget(self.sPort)
        self.layout.addWidget(self.dPort)
        self.layout.addWidget(self.state)
        self.layout.addWidget(self.target)

        # Add input widget and button to vertical layout
        self.layout2.addLayout(self.layout)
        self.layout2.addWidget(self.submit, alignment=Qt.AlignmentFlag.AlignCenter)

        self.setLayout(self.layout2)

    def submit_rule(self):
        """
        Submits the rule and adds it to iptables.
        """

        combo_box_widgets = self.findChildren(QComboBox)

        if self.check_valid_ips([self.source, self.dest]):

            if self.check_combo_value(combo_box_widgets):
                input_widgets = self.findChildren((QComboBox, QLineEdit))
                self.create_rule(input_widgets)
                ui_add_rule(self.rule)
                self.close()

    def check_combo_value(self, combo_boxes):
        """
        Checks the combo boxes for valid inputs. If invalid, displays an error box.
        :param combo_boxes: children widgets of the window
        :return: False if invalid, True if ALL valid
        """

        for combo in combo_boxes:
            if combo.placeholderText() != 'protocol':
                if len(combo.currentText()) == 0:
                    QMessageBox.warning(self, "Warning", f"One of the {combo.placeholderText()} must be selected")
                    return False

        return True

    def check_valid_ips(self, ip_widgets):
        """
        Checks for valid IPs. If the text is not empty, check for valid IP.
        :param ip_widgets: ip widgets to validate
        :return: False if invalid, True if valid
        """

        for widget in ip_widgets:
            ip = widget.text()

            if ip == '':
                continue

            try:
                ipaddress.ip_address(ip)
            except ValueError:
                error = ''
                if widget.objectName() == '-s':
                    error = 'Source IP'
                else:
                    error = 'Destination IP'
                QMessageBox.warning(self, "Warning", f"Invalid {error} Address!")
                return False

        return True

    def create_rule(self, input_widgets):
        """
        Updated the values in the rule dictionary.
        :param input_widgets: children widgets of the window
        """

        for widget in input_widgets:
            key = str(widget.objectName())

            if type(widget) == PyQt6.QtWidgets.QComboBox:
                if widget.currentText() != '':
                    self.rule[key] = widget.currentText()

            elif type(widget) == PyQt6.QtWidgets.QLineEdit:
                if widget.text() != '':
                    self.rule[key] = widget.text()
