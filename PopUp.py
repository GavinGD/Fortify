from PyQt6.QtGui import QIntValidator
from PyQt6.QtWidgets import QDialog, QFormLayout, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QComboBox, QLineEdit
from PyQt6.QtGui import QRegularExpressionValidator
from PyQt6.QtCore import Qt, QRegularExpression
import re
import ipaddress

# Can change the filename/class name to something that shows this is adding a rule
class PopupWindow(QDialog):
    def __init__(self, parent):
        super().__init__(parent)
        self.setWindowTitle("Add Rule")
        self.setGeometry(parent.geometry().x(), parent.geometry().y(), 800, 150)

        # Should probably make all layouts, labels widgets class variables
        # i.e. self.submitBtn = QPushButton
        # Makes it so other classes can modify the widgets

        # Creating layout and labels (Horizontal and Vertical)
        layout = QHBoxLayout()
        layout2 = QVBoxLayout()

        # port validator
        onlyInt = QIntValidator()
        onlyInt.setRange(0, 65535)

        # ip validator
        ip_reg = "(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)(\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)){3}"
        ip_validator = QRegularExpressionValidator(self)
        ip_validator.setRegularExpression(QRegularExpression(ip_reg))


        self.error = QLabel("")

        # chain dropdown
        self.chain = QComboBox()
        self.chain.setPlaceholderText("chain")
        self.chain.addItem("INPUT")
        self.chain.addItem("OUTPUT")
        self.chain.addItem("FORWARD")
        self.chain.setFixedWidth(100)

        # protocol dropdown
        self.protocol = QComboBox()
        self.protocol.setPlaceholderText("protocol")
        self.protocol.addItem("tcp")
        self.protocol.addItem("udp")
        self.protocol.addItem("icmp")
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
        self.sPort.setValidator(onlyInt)
        self.sPort.setFixedWidth(80)

        # destination port field
        self.dPort = QLineEdit()
        self.dPort.setPlaceholderText("dst Port")
        self.dPort.setValidator(onlyInt)
        self.dPort.setFixedWidth(80)

        # state dropdown
        self.state = QComboBox()
        self.state.addItem("ESTABLISHED")
        self.state.addItem("RELATED")
        self.state.addItem("NEW")
        self.state.addItem("INVALID")
        self.state.setFixedWidth(140)

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
        val_protocol = self.protocol.currentText()
        val_source = self.source.text()
        val_dest = self.dest.text()
        val_sPort = self.sPort.text()
        val_dPort = self.dPort.text()
        val_state = self.state.currentText()

        # TODO: - if self.validate_ip(val_source) == "INVALID IP" display error message => not close box
        #       -                                 != "INVALID IP" save in dictionary
        #       - if protocol, src(ip, port), dst(ip, port), has none value => set to any
        print(val_chain)
        print(val_protocol)
        print(val_source)
        print(val_dest)
        print(val_sPort)
        print(val_dPort)
        print(val_state)

