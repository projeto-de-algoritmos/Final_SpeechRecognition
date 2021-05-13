import sys

from PySide6 import QtWidgets
from src.windown import Windown

if __name__ == '__main__':
    app = QtWidgets.QApplication([])

    widget = Windown()

    widget.resize(400, 200)

    widget.show()

    sys.exit(app.exec())
