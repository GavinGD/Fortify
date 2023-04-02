from PyQt6.QtWidgets import QDialog, QVBoxLayout, QLabel, QPushButton


# Can change the filename/class name to something that shows this is adding a rule
class PopupWindow(QDialog):
    def __init__(self, parent):
        super().__init__(parent)
        self.setWindowTitle("Popup Window")
        self.setGeometry(parent.geometry().x() + 50, parent.geometry().y() + 50, 300, 200)

        # Should probably make all layouts, labels widgets class variables
        # i.e. self.submitBtn = QPushButton
        # Makes it so other classes can modify the widgets

        # Creating layout and labels
        layout = QVBoxLayout()
        label = QLabel("This is a popup window.")
        self.error = QLabel("")
        button = QPushButton("Close")
        button2 = QPushButton("aids")

        # Adding widgets to layout
        layout.addWidget(label)
        layout.addWidget(self.error)
        layout.addWidget(button)
        layout.addWidget(button2)

        # Connecting buttons to functions
        button2.clicked.connect(self.show_error)
        button.clicked.connect(self.close)

        self.setLayout(layout)

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
