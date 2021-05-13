import sys

from PySide6 import QtWidgets
from PySide6.QtWidgets import QInputDialog, QLineEdit, QProgressBar, QLabel, QPushButton
from src.widgets import IdentifyWidget, RecordWidget

class Windown(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.layout = QtWidgets.QVBoxLayout(self)


        self.tabs = QtWidgets.QTabWidget()

        record_tab = RecordWidget()

        self.tabs.addTab(record_tab, 'Gravar')
        self.tabs.addTab(IdentifyWidget(), 'Identificação')

        self.layout.addWidget(self.tabs)

        # exit button

        self.exit_button = QtWidgets.QPushButton('Sair do Programa')
        self.exit_button.clicked.connect(lambda: self.close())

        self.layout.addWidget(self.exit_button)

