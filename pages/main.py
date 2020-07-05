from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from pages.setting import Setting
from pages.project import Project


class MainWindow(QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setWindowTitle("Mando")
        self.index = 0

        layout = QStackedLayout()
        self.pages = [
            Setting(self),
            Project(self)
        ]

        for page in self.pages:
            layout.addWidget(page)

        layout.setCurrentIndex(self.index)
        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

    def nextPage(self):
        total_page_count = len(self.pages)
        if self.index < total_page_count:
            self.index += 1

    def prePage(self):
        if self.index > 0:
            self.index -= 1
