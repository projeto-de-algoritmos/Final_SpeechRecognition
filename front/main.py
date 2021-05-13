import sounddevice as sd
import sys

from PySide6 import QtCore, QtWidgets, QtGui
from PySide6.QtWidgets import QInputDialog, QLineEdit, QProgressBar, QLabel
from io import BytesIO
from scipy.io.wavfile import write
from speech_recognition import register_new_word, query_word, words
from time import sleep

SAMPLE_RATE= 18000  # Sample rate
SECONDS = 3  # Duration of recording

def record():

    myrecording = sd.rec(int(SECONDS*SAMPLE_RATE), samplerate=SAMPLE_RATE, channels=1)
    sd.wait()  # Wait until recording is finished

    return myrecording


class RecordWidget(QtWidgets.QWidget):

    def __init__(self):

        super().__init__()

        self.layout = QtWidgets.QVBoxLayout()
        self.layout.addWidget(self.recordBox())

        self.layout.addWidget(self.identifyBox())

        self.setLayout(self.layout)

    def identifyBox(self):

        box = QtWidgets.QGroupBox('Voice Identifier')

        layout = QtWidgets.QVBoxLayout()

        button = QtWidgets.QPushButton('Reconhecimento')
        button.setGeometry(250, 20, 50, 20)
        button.clicked.connect(self.identify_clicked)

        self.identify_button = button
        layout.addWidget(button)

        label = QtWidgets.QLabel('1ª')
        label.setAlignment(QtCore.Qt.AlignCenter)
        layout.addWidget(label)


        label1 = QtWidgets.QLabel('2ª')
        label1.setAlignment(QtCore.Qt.AlignCenter)
 
        label2 = QtWidgets.QLabel('3ª')
        label2.setAlignment(QtCore.Qt.AlignCenter)

        layout.addWidget(label1)
        layout.addWidget(label2)
 

        box.setLayout(layout)

        return box

    def record_clicked(self):

        self.record_button.setText('Gravando')
        self.record_button.repaint()

        sleep(1)
        word = self.line.text()

        data = record()
        
        register_new_word(word, data, SAMPLE_RATE)
        #self.record_sig.emit(filename)

        print(words)
        self.record_button.setText('Record')


    def identify_clicked(self):
        print('Identificando')
        pass

    def recordBox(self):

        # create box
        box = QtWidgets.QGroupBox('Record your audio')

        # add input box
        layout = QtWidgets.QHBoxLayout()
        line = QtWidgets.QLineEdit(self)
        line.setGeometry(20, 20, 200, 20)
        layout.addWidget(line)

        self.line = line

        # add button
        record_button = QtWidgets.QPushButton('Record', self)
        record_button.setGeometry(250, 20, 50, 20)

        record_button.clicked.connect(self.record_clicked)

        self.record_button = record_button
        layout.addWidget(record_button)

        box.setLayout(layout)

        return box

    def record_action(self):
        """
        Record audio
        """



class RecordedTab(QtWidgets.QWidget):

    def __init__(self):
        super().__init__()


        box = QtWidgets.QGroupBox()


        layout = QtWidgets.QFormLayout()

        self.buttons = []

        for i in range(10):
            button = QtWidgets.QPushButton('Excluir', self)
            button.setGeometry(0, 20, 50, 20)

            label = QLabel('...')
            label.setGeometry(0, 20, 50, 20)

            layout.addRow(label, button)

            self.buttons.append(button)

        box.setLayout(layout)

        self.setLayout(layout)




class Windown(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.layout = QtWidgets.QVBoxLayout(self)


        self.tabs = QtWidgets.QTabWidget()

        record_tab = RecordWidget()
        registed_tab = RecordedTab()

        self.tabs.addTab(record_tab, 'Record')
        self.tabs.addTab(registed_tab, 'Gravacoes')

        self.layout.addWidget(self.tabs)

        # exit button

        self.exit_button = QtWidgets.QPushButton('Exit')
        self.exit_button.clicked.connect(lambda: self.close())

        self.layout.addWidget(self.exit_button)

if __name__ == '__main__':
    app = QtWidgets.QApplication([])

    widget = Windown()

    widget.resize(400, 300)

    widget.show()

    sys.exit(app.exec_())
