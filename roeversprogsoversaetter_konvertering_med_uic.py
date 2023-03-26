# [[file:README.org::*Konvertering af ui-fil til pythonfil][Konvertering af ui-fil til pythonfil:1]]
import sys 

# Import af filen/modulet roeversprog.py -
# Læg mærke til at .py ikke er taget med.
import roeversprog

# Import af de almindelige elementer i pyside6
from PySide6.QtWidgets import QApplication, QMainWindow
# Import af brugerfladen fra pythonfilen, som er generet vha pyside6-uic
from roeversprogsoversaetter_gui import Ui_MainWindow

# Vores nye klasse, som starter med at nedarve fra almindeligt QMainWindow
class Roeversprogsoversaetter(QMainWindow):
    def __init__(self):
        super().__init__()
        # Her oprettes self.ui ud fra den klasse som er i den genererede pythonfil
        self.ui = Ui_MainWindow()
        # Her sættes brugerfladen op.
        self.ui.setupUi(self)
        # Her sættes vinduestitlen til noget andet end i Designer.
        # Læg mærke til at self.ui IKKE anvendes men blot self.
        self.setWindowTitle("Konvertering vha pyside6-uic")
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
roeversprogsoversaetter.show()
program.exec()
# Konvertering af ui-fil til pythonfil:1 ends here
