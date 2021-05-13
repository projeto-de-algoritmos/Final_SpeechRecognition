from PySide6 import QtCore, QtWidgets
from PySide6.QtWidgets import QInputDialog, QLineEdit, QProgressBar, QLabel, QPushButton
from src.constants import SAMPLE_RATE
from src.speech_recognition import query_word, words
from src.utils import record


class IdentifyWidget(QtWidgets.QWidget):

    def __init__(self):

        super().__init__()

        self.layout = QtWidgets.QVBoxLayout()

        self.layout.addWidget(self.identifyBox())

        self.setLayout(self.layout)

    def identifyBox(self):

        box = QtWidgets.QGroupBox('Identificação por voz')

        layout = QtWidgets.QVBoxLayout()

        button = QtWidgets.QPushButton('Reconhecimento')
        button.setGeometry(250, 20, 50, 20)
        button.clicked.connect(self.identify_clicked)

        self.identify_button = button
        layout.addWidget(button)

        label1 = QtWidgets.QLabel('1ª')
        label1.setAlignment(QtCore.Qt.AlignCenter)
        layout.addWidget(label1)

        self.label1 = label1


        label2 = QtWidgets.QLabel('2ª')
        label2.setAlignment(QtCore.Qt.AlignCenter)
        layout.addWidget(label2)

        self.label2 = label2
 
        label3 = QtWidgets.QLabel('3ª')
        label3.setAlignment(QtCore.Qt.AlignCenter)
        layout.addWidget(label3)

        self.label3 = label3
        box.setLayout(layout)

        return box

    def identify_clicked(self):
        print('Identificando')

        # TODO(felipe) write error handling

        data = record()

        words = query_word(data, SAMPLE_RATE)

        self.label1.setText(f'1ª) {words[0][1]}')
        self.label2.setText(f'2ª) {words[1][1]}')
        self.label3.setText(f'3ª) {words[2][1]}')

