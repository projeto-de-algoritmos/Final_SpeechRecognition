import sys
from PySide6 import QtCore, QtWidgets, QtGui

class RecordWidget(QtWidgets.QWidget):

    def __init__(self):

        super().__init__()

class Windown(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.layout = QtWidgets.QVBoxLayout(self)


        self.tabs = QtWidgets.QTabWidget()

        record_tab = RecordWidget()

        self.tabs.addTab(record_tab, 'Record')

        self.layout.addWidget(self.tabs)

if __name__ == '__main__':
    app = QtWidgets.QApplication([])

    widget = Windown()

    widget.resize(800, 600)

    widget.show()

    sys.exit(app.exec_())
