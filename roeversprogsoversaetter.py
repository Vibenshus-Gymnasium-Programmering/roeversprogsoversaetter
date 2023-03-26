import os
import sys

import roeversprog

from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile, QObject


loader = QUiLoader()


class Roeversprogsoversaetter(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = loader.load("roeversprogsoversaetter.ui", None)
        self.ui.setWindowTitle("en anden titel")
        self.ui.oversaet_knap.clicked.connect(self.oversaet)
        # self.ui.show()

    def oversaet(self):
        output_fra_oversaetteren = roeversprog.oversaet_til_roeversprog(
            "input som ikke bruges"
        )
        print(output_fra_oversaetteren)


program = QApplication.instance()
if program == None:
    program = QApplication(sys.argv)
roeversprogsoversaetter = Roeversprogsoversaetter()
roeversprogsoversaetter.ui.show()
program.exec()
