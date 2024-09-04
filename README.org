#+title: Røversprogsoversætter udviklet i ~Pyside6~ vha ~Designer~
#+subtitle: Programmering
#+author: Vibenshus Gymnasium

* Introduktion

I denne opgave skal I udvikle en grafisk brugerflade til en *røversprogsoversætter*. Den grafiske brugerflade vil blive udviklet ved hjælp af ~QtDesigner~, mens logikken vil blive skrevet i ~python 3~. Vi tager udgangspunkt i /google translate/, som ser nogenlunde således ud:

[[./img/google_translate.png]]

* Opsætningskrav
Følgende skal være installeret og aktiveret.

- ~Python 3~
- ~PyCharm~ eller andet IDE (eller teksteditor)
- ~pyside6~ installeret og aktiveret i et virtuelt miljø.
- ~QtDesigner~ (installeres normalt automatisk, når man installere pyside6 vha ~pip~)

  
I de følgende afsnit får I skriftlig forklaring på, hvad og hvordan I skal gøre.

* Klargøring af projekt (i ~pycharm~)

- Klon denne opgave fra github classroom. (Det har I nok allerede gjort, når I læser dette.)

- Brug jeres nye repository som projekt. Sørg for at have installeret ~PySide6~ enten i et virtuelt miljø under jeres projekt eller mere centralt. I ved selv, hvor I kan installere ~PySide6~ i ~pycharm~. Det er noget med =settings= og =intepreter=.

- I skal selv skrive jeres ~python~-program i en separat fil, eller I kan anvende de to skabeloner =roeversprogsoversaetter_direkte_indlaesning.py= eller =roeversprogsoversaetter_konvertering_med_uic.py=, som I kan finde her i git-repo'et eller i de to respektive afsnit. 

- Selve koden til at oversætte fra dansk til røversprog (og tilbage igen) skal I skrive i modulet(filen) =roeversprog.py= som også ligger i git-repo'et. Se mere om denne adskillelse mellem logik og brugerflade i næste afsnit.

* Udvikling af logik

Når der udvikles logik til programmer, som ikke direkte har noget at gøre med den grafiske brugegrænseflade, er det en rigtig god idé at skrive koden i en pythonfil for sig selv. På denne måde kan logikken importeres i mange forskellige brugerflader uafhængigt af hinanden. Som det kan ses i skabelonen kan man vælge at kalde filen for ~roeversprog.py~ og lægge den i samme mappe som hovedprogrammet.

*Reglerne for røversprog er ganske simple*. Der er faktisk kun tre.

1. Hver konsonant bliver erstattet af to gange sig selv med et o igemmem. "S" bliver altså til "sos".
2. Hver vokal er bare sig selv.
3. Når røversprog skal udtales, skal man stave sig gennem det, hvor "S" læses som "sos" og "a" som "a".
     "Røversprog" læses altså højt som: Ror-ø-vov-e-ror-sos-pop-ror-o-gog.

Begynd med at udvikle en funktion, som tager en tekststreng som input og returnere en ny tekststring ud fra de førnævnte regler.

Efterfølgende skal I udvikle en funktion, som kan oversætte fra røversprog tilbage til almindeligt sprog. Hvis der er konstruktionsfejl i røversproget, må funktionen meget gerne gøre opmærksom på dette.

Brug følgende skabelon i filen ~roeversprog.py~ til jeres logik.

#+begin_src python :exports both :results output :eval never-export :comments link :tangle roeversprog.py
# Dette er et modul til oversættelse mellem almindelige sprog og røversprog

def oversaet_til_roeversprog(inputtekst):
    outputtekst = "Denne funktion skal kunne oversætte til røversprog."
    return outputtekst


def oversaet_fra_roeversprog_til_andet_sprog(inputtekst):
    outputtekst = "Her skal røversproget fjernes og almindeligt sprog skal returneres.\nGiv gerne fejlmeddelelser, hvis røversproget ikke er korrekt."
    return outputtekst
#+end_src


* Design af den grafiske brugerflade i ~Designer~
- Forlad ~pycharm~ (eller en anden editor) for et øjeblik og åbn programmet ~PySide6-designer~. Vi har øvet os i at få åbnet programmet, så hjælp hinanden med det, hvis I har glemt det siden sidst.
- ~Designer~ ser nogenlunde således ud, når I åbner det:

  [[./img/designer_foerste_vindue.png]]

- I kan vælge at åbne skabelonen =roeversprogsoversaetter.ui= og arbejde videre med den. Eller I kan gøre følgende:
  
- Vælg =Main Window=. Nu skal I gerne have en brugerflade, som ser nogenlunde således ud:

  [[./img/designer_main_window.png]]

- Gem jeres (tomme) design i en ~.ui~-fil. Det gør I gennem menuen ~File->Save As~.

  Som udgangspunkt skal I sørge for at gemme filen i samme mappe som jeres pythonfil. Giv filen et passende navn. 

- Nu burde I være klar til at designe jeres brugerflade.

- Inden i går i gang med at opbygge jeres grafiske brugerflade, er det en god idé at udarbejde et /mockup/ på et stykke papir ved siden af. Jeg har givet et bud til et mockup på følgende figur.

  [[./img/mocup.png]]

- Oven på dette mockup kan I nu skrive, hvilke ~widgets~ de forskellige dele skal bestå af, og hvordan layoutet skal styres. I kan se mit forslag nedenfor.

  [[./img/mockup_widgets.png]]


- Gå tilbage til ~Designer~ og hav jeres mockup liggende ved siden af. Her er lidt inspiration til, hvordan brugerfladen kan opbygges:

  - Træk vinduet ud til den ønskede standardstørrelse.
  - Indsæt *mindst én* af de ønskede widgets i vinduet. Dette gøres ved at trække og slippe widgets fra venstre side. (Er gjort i skabelonen)
  - Højreklik nu et sted på vinduets baggrund (der med alle de små prikker) og vælg Lay out nederst i menuen. Herfra kan I vælge det overordnede layout for jeres vindue. Det kunne f.eks være ~Lay out in a Grid~. (er gjort i skabelonen)
  - Indsæt ~Label~​s hvor der skal være enlinjes tekster, som ikke kan editeres, ved at trække et label én ad gangen fra tabellen i venstre side ind i grid layoutet i vinduet.
  - Indsæt to knapper, en til at skifte oversættelsesretning og en til selve oversættelsen. En knap hedder ~Push Button~. (Én knap er indsat i skabelonen)
  - Intsæt to tekstfelter, kaldet ~Plain Text Edit~. Forskellen på ~Plain Text Edit~ og ~Text Edit~ er, at sidstnævnte kan formateres med forskellige skrifttyper, størrelser osv.
  - Sørg for at det ene tekstfelt *ikke* er redigérbart. Dette gøres ved markerer feltet i vinduet og sætte flueben ved ~readOnly~ i ~Property~ nede i højre hjørne.
  - Sørg for at give hvert element et passende navn. Dette gøres også under ~Property~-menuen nederst til højre, under ~objectName~. Man kan f.eks. kalde sit inputfelt: ~input_plainTextEdit~.
  - Angiv den ønskede tekst på labels og knapper.
  - Hvis I vil have et preview af, hvordan vinduet vil se ud, kan I trykke ~ctrl+r~, eller vælg ~Preview~ under drop down-menuen ~Form~ øverst.
  - Mit bud på en brugerflade ser således ud:

    [[./img/faerdigt_design.png]]

  - Sørg for at gemme jeres designfil.

* Programmering af brugeflade i ~pycharm~
Nu skal I vende tilbage til ~pycharm~ (eller anden editor). Der findes 2 forskellige måder at få sat jeres brugerflade op på i python. De to måder er /direkte indlæsning af jeres designfil (.ui)/ eller /konvertering af designfil til pythonfil/. Der er fordele op ulemper ved begge metoder. Forskellene vil blive beskrevet i de følgende afsnit.

** Direkte indlæsning af designfil
I dette eksempel er der genereret en ui-fil navngivet ~roeversprogsoversaetter.ui~. Brugerfladen består et ~QMainWindow~ med blot en enkelt ~QPushButton~, som er navngivet =oversaet_knap=. Layoutet er sat ti ~Grid layout~. (I kan åbne ui-filen og arbejde videre med den, eller I kan skabe jeres egen fra bunden, som beskrevet tidligere.)

Den følgende pythonkode, som også ligger i filen =roeversprogsoversaetter_direkte_indlaesning.py=, indlæser brugerfladen vha et QUiLoader-objekt.
#+begin_src python :exports both :results none :eval never-export :comments link :tangle roeversprogsoversaetter_direkte_indlaesning.py
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
#+end_src

*Fordelen* ved denne måde at opbygge sit program er, at brugerfladen opdateres automatisk, når/hvis I laver ændringer i brugerfladen gennem ~designer~. I skal bare sørge for at køre python-programmet igen. 

*Ulempen* er så til gengæld, at ~pycharm~ eller andre editorer ikke kan /autocomplete/ navne, objekter, metoder osv for de forskellige widgets i brugerfladen. F.eks. ville man *ikke* kunne skrive ~self.ui.~ og så få forslag til de forskellige widgets. I stedet bliver man nødt til at have ~designer~ åbent og så slå navnene op derigennem.

** Konvertering af ui-fil til pythonfil
I stedet for at loade .ui-filen direkte er det ofte bedre i udviklingsprocessen at generere en /rigtig/ pythonfil ud fra .ui-filen. Dette kan heldigvis gøres vha kommandoen ~pyside6-uic~. Denne kommando har man adgang til, når man har aktiveret et virtuelt miljø, som indeholder ~PySide6~. For jer, som anvender ~pycharm~ kan det nemt gøres på følgende måde:

1. Tryk på fanen =Terminal= i den nederste bjælke.
2. I terminalen skriver I nu f.eks. ~pyside6-uic roeversprogsoversaetter.ui -o roeversprogsoversaetter_gui.py~
3. Hver gang I laver ændringer i den grafiske brugerflade gennem ~Designer~, skal I huske at køre ovenstående kommando.

#+begin_src python :exports both :results none :eval never-export :comments link :tangle roeversprogsoversaetter_konvertering_med_uic.py
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
#+end_src

*Fordelen* ved denne fremgangsmåde er, at pycharm eller andre udviklingsværktøjer til python vil kunne autocomplete navne, funktioner, metoder osv i takt med at koden skrives. Det gør udviklingen nemmere.

*Ulempen* er, at man skal huske at køre kommandoen ~pyside6-uic roeversprogsoversaetter.ui > roeversprogsoversaetter_gui.py~ i en terminal hver gang, der er foretaget ændringer i ~Designer~.

** Opsætning signals and slots
Som det ser ud lige nu, er der én knap, som er forbundet til en metode. Det er dog ikke det rigtige, der bliver gjort. Dette skal I selv sørge for at få til at virke.

Ligeledes skal I også selv sætte andre signals og slots op, hvis I f.eks. har flere knapper, som skal gøre noget særligt, når der trykkes på dem.


* Ekstra udfordring
Som en ekstra udfordring kan I lege med at få googles text-to-speech-modul til at fungere. Modulet hedder ~gtts~ og kan installeres på samme måde som ~PySide6~ (og ~arcade~) blev installeret (~pip install gTTS~, eller installer ~gTTS~ vha pycharm).

I kan finde dokumentation her: [[https://gtts.readthedocs.io/en/latest/]].

Hvis jeres program skal udtale røversproget så korrekt som muligt, så skal =test= oversættes til =tot e sos tot=. Det virker særligt godt, hvis sproget er sat til tysk. :)

Rorigogtotigog gogodod arorbobejojdodsoslolysostot!
