# skapa en klass Bil med 4 attribut:
# märke
# modell
# mil
# topphastighet

from re import M


class Bil:
    def __init__(self, märke, modell, mil, topphastighet):
        self.märke = märke
        self.modell = modell
        self.mil = mil
        self.topphastighet = topphastighet
