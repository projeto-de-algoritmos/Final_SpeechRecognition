import sys
import logging

from PySide6 import QtWidgets
from src.windown import Windown

logging.basicConfig(level=logging.INFO)

logger = logging.getLogger(__name__)

if __name__ == '__main__':

    logger.info('Open application')

    app = QtWidgets.QApplication([])

    widget = Windown()
    widget.resize(400, 200)
    widget.show()

    sys.exit(app.exec())
