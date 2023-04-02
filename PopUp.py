from PyQt6.QtWidgets import QDialog, QFormLayout, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QComboBox, QLineEdit
from PyQt6.QtCore import Qt

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
        self.error = QLabel("")

        # chain dropdown
        chain = QComboBox()
        chain.setPlaceholderText("chain")
        chain.addItem("INPUT")
        chain.addItem("OUTPUT")
        chain.addItem("FORWARD")
        chain.setFixedWidth(100)

        # protocol dropdown
        protocol = QComboBox()
        protocol.setPlaceholderText("protocol")
        protocol.addItem("tcp")
        protocol.addItem("udp")
        protocol.addItem("icmp")
        protocol.setFixedWidth(100)

        # source ip field
        source = QLineEdit()
        source.setPlaceholderText("src IP")
        source.setFixedWidth(120)

        # destination ip field
        dest = QLineEdit()
        dest.setPlaceholderText("dst IP")
        dest.setFixedWidth(120)

        # source port field
        sPort = QLineEdit()
        sPort.setPlaceholderText("src Port")
        sPort.setFixedWidth(80)

        # destination port field
        dPort = QLineEdit()
        dPort.setPlaceholderText("dst Port")
        dPort.setFixedWidth(80)

        # state dropdown
        state = QComboBox()
        state.addItem("ESTABLISHED")
        state.addItem("RELATED")
        state.addItem("NEW")
        state.addItem("INVALID")
        state.setFixedWidth(140)

        # submit button
        button = QPushButton("submit")
        button.setFixedWidth(120)

        # Adding input widgets to horizontal layout
        layout.addWidget(chain)
        layout.addWidget(protocol)
        layout.addWidget(source)
        layout.addWidget(dest)
        layout.addWidget(sPort)
        layout.addWidget(dPort)
        layout.addWidget(state)
        layout.addWidget(self.error)

        # Add input widget and button to vertical layout
        layout2.addLayout(layout)
        layout2.addWidget(button, alignment=Qt.AlignmentFlag.AlignCenter)

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
