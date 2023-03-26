# [[file:README.org::*Direkte indlæsning af designfil][Direkte indlæsning af designfil:1]]
import sys

# Import af filen/modulet roeversprog.py -
# Læg mærke til at .py ikke er taget med.
import roeversprog

from PySide6.QtWidgets import QApplication 
from PySide6.QtUiTools import QUiLoader
# Læg mærke tile at QMainWindow ikke importeres.
# I stedet importeres QObject i stedet for.
# QMainWindow er anvendt i Designer.
from PySide6.QtCore import QObject


# loader-objekt som bruges til at loade .ui-filen
loader = QUiLoader()


# Læg mærke til at klassen nedarver fra QObject i stedet for QMainWindow
class Roeversprogsoversaetter(QObject):
    def __init__(self):
        super().__init__()
        # Her loades brugerfladen fra Designer.
        self.ui = loader.load("roeversprogsoversaetter.ui", None)
        # self.ui refererer til selve brugerfladen som for nu er af typen
        # QMainWindow, og som indeholder et gridLayout og en pushbutton
        self.ui.setWindowTitle("Direkte indlæsning fra ui")
        # Her sættes signal og slot op for oversaetknap og metoden oversaet
        self.ui.oversaet_knap.clicked.connect(self.oversaet)
        # self.ui.show()

    def oversaet(self):
        # Denne metode anvender funktionen oversaet_til_roeversprog, som
        # ligger i modulet roeversprog (som er importeret i starten)
        output_fra_oversaetteren = roeversprog.oversaet_til_roeversprog(
            "input som ikke bruges"
        )
        print(output_fra_oversaetteren)
        # I skal selv sørge for at forbedre den metode, så den gør
        # som I ønsker


program = QApplication.instance()
if program == None:
    program = QApplication(sys.argv)
roeversprogsoversaetter = Roeversprogsoversaetter()
roeversprogsoversaetter.ui.show()
program.exec()
# Direkte indlæsning af designfil:1 ends here
