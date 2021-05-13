import sounddevice as sd
import logging

from PySide6 import QtCore, QtWidgets
from PySide6.QtWidgets import QInputDialog, QLineEdit, QProgressBar, QLabel, QPushButton
from src.constants import SAMPLE_RATE
from src.speech_recognition import register_new_word
from src.utils import record
from src.widgets import IdentifyWidget

logger = logging.getLogger(__name__)


class RecordWidget(QtWidgets.QWidget):

    def __init__(self):

        super().__init__()

        self.layout = QtWidgets.QVBoxLayout()
        self.layout.addWidget(self.recordBox())

        self.setLayout(self.layout)

        self.word_data = None

    def record_clicked(self):

        logger.info('Recording audio')

        self.record_button.setText('Gravando')
        self.record_button.repaint()

        word = self.line.text()

        data = record()

        self.word_data = (word, data)
        
        self.record_button.setText('Gravar')

        logger.info('Record finished')

    def save_clicked(self):

        logger.info('Saving audio')

        if self.word_data :
            word, data = self.word_data

            logger.debug(f'Word saved: {word}')

            register_new_word(word, data, SAMPLE_RATE)

            self.word_data = None

    def play_clicked(self):

        logger.info('Trying to play a audio')

        if self.word_data:

            logger.debug('Playing')

            sd.play(self.word_data[1], SAMPLE_RATE)

    def recordBox(self):

        # create box
        box = QtWidgets.QGroupBox('Grave seu audio')

        outer_layout = QtWidgets.QVBoxLayout()

        # add input box
        layout = QtWidgets.QHBoxLayout()
        line = QtWidgets.QLineEdit(self)
        line.setGeometry(20, 20, 200, 20)
        layout.addWidget(line)

        self.line = line

        # add button
        record_button = QtWidgets.QPushButton('Gravar', self)
        record_button.setGeometry(250, 20, 50, 20)

        record_button.clicked.connect(self.record_clicked)

        self.record_button = record_button
        layout.addWidget(record_button)

        outer_layout.addLayout(layout)


        inner_layout = QtWidgets.QHBoxLayout()

        save_button = QPushButton('Salvar', self)
        save_button.setGeometry(250, 20, 50, 20)
        save_button.clicked.connect(self.save_clicked)

        play_button = QPushButton('Ouvir', self)
        play_button.setGeometry(250, 20, 50, 20)
        play_button.clicked.connect(self.play_clicked)


        inner_layout.addWidget(save_button)
        inner_layout.addWidget(play_button)

        outer_layout.addLayout(inner_layout)
        box.setLayout(outer_layout)

        return box

