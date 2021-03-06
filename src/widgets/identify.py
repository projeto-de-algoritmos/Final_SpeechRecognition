import logging

from PySide6 import QtCore, QtWidgets
from PySide6.QtWidgets import QInputDialog, QLineEdit, QProgressBar, QLabel, QPushButton
from src.constants import SAMPLE_RATE
from src.speech_recognition import query_word, words
from src.utils import record

logger = logging.getLogger(__name__)


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

        logger.info('Trying to identify audio')


        if len(words) >= 3:

            data = record()
            candidate_words = query_word(data, SAMPLE_RATE)
            logger.debug(f'Ranking words')

            self.label1.setText(f'1ª) {candidate_words[0][1]}')
            self.label2.setText(f'2ª) {candidate_words[1][1]}')
            self.label3.setText(f'3ª) {candidate_words[2][1]}')

        else:
            logger.warning('Tried to identify without recording 3 audios')

