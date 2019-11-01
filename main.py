import sys

from PyQt5.QtWidgets import QApplication
from Studying import Learning

if __name__ == '__main__':
    app = QApplication(sys.argv)

    py_learning = Learning()
    py_learning.show()

    sys.exit(app.exec_())
