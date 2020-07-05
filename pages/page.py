from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from utilities.color import Color


def getFooterWidget():
    next_button = QPushButton(text="Next")
    next_button.setMinimumWidth(2)
    next_button.setMinimumWidth(2)
    palette = next_button.palette()
    palette.setColor(QPalette.Window, QColor('red'))
    next_button.setPalette(palette)
    return next_button


class Page(QWidget):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setAutoFillBackground(True)
        palette = self.palette()
        palette.setColor(QPalette.Window, QColor("teal"))
        self.setPalette(palette)

        layout = QVBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        layout.addWidget(getFooterWidget())
        self.setLayout(layout)
