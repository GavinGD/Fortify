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

        # Creating layout and labels
        layout = QHBoxLayout()
        layout2 = QVBoxLayout()
        self.error = QLabel("")

        chain = QComboBox()
        chain.setPlaceholderText("chain")
        chain.addItem("INPUT")
        chain.addItem("OUTPUT")
        chain.addItem("FORWARD")
        chain.setFixedWidth(100)

        protocol = QComboBox()
        protocol.setPlaceholderText("protocol")
        protocol.addItem("tcp")
        protocol.addItem("udp")
        protocol.addItem("icmp")
        protocol.setFixedWidth(100)

        source = QLineEdit()
        source.setPlaceholderText("src IP")
        source.setFixedWidth(120)

        dest = QLineEdit()
        dest.setPlaceholderText("dst IP")
        dest.setFixedWidth(120)

        sPort = QLineEdit()
        sPort.setPlaceholderText("src Port")
        sPort.setFixedWidth(80)

        dPort = QLineEdit()
        dPort.setPlaceholderText("dst Port")
        dPort.setFixedWidth(80)

        state = QComboBox()
        state.addItem("ESTABLISHED")
        state.addItem("RELATED")
        state.addItem("NEW")
        state.addItem("INVALID")
        state.setFixedWidth(140)

        button = QPushButton("submit")
        button.setFixedWidth(120)

        # Adding widgets to layout
        layout.addWidget(chain)
        layout.addWidget(protocol)
        layout.addWidget(source)
        layout.addWidget(dest)
        layout.addWidget(sPort)
        layout.addWidget(dPort)
        layout.addWidget(state)
        layout.addWidget(self.error)

        layout2.addLayout(layout)
        layout2.addWidget(button, alignment=Qt.AlignmentFlag.AlignCenter)
        # Connecting buttons to functions
        # button2.clicked.connect(self.show_error)
        button.clicked.connect(self.close)

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
