log = "Temp\\temp.py"


class Pumpe:
    def __init__(self, Komponentennummer, Stueckzahl):
        self.Komponentennummer = Komponentennummer
        self.Stueckzahl = Stueckzahl
    def show(self):
        print(self.Komponentennummer, self.Stueckzahl)
    def descript(self, i):
        with open(log, "a") as f:
            if str(self.__class__.__name__) == "Pumpe":
                f.write(str(self.__class__.__name__)+" = [[" +str(self.Stueckzahl).replace(",",".")+"],'" +str(self.Komponentennummer)+"']\n")
                f.close()
            else:
                f.write(str(self.__class__.__name__)+i+" = [[" +str(self.Stueckzahl).replace(",",".")+"],'" +str(self.Komponentennummer)+"']\n")
                f.close()
class Gehaeuse(Pumpe):
    def __init__(self, Komponentennummer, Stueckzahl):
        self.Komponentennummer = Komponentennummer
        self.Stueckzahl = Stueckzahl
class Pumpengehaeuse(Pumpe):
    def __init__(self, Komponentennummer, Stueckzahl):
        self.Komponentennummer = Komponentennummer
        self.Stueckzahl = Stueckzahl
class Rotor(Pumpe):
    def __init__(self, Komponentennummer, Stueckzahl):
        self.Komponentennummer = Komponentennummer
        self.Stueckzahl = Stueckzahl
class Leiterplatte(Pumpe):
    def __init__(self, Komponentennummer, Stueckzahl):
        self.Komponentennummer = Komponentennummer
        self.Stueckzahl = Stueckzahl
class Schutzhuelse(Pumpe):
    def __init__(self, Komponentennummer, Stueckzahl):
        self.Komponentennummer = Komponentennummer
        self.Stueckzahl = Stueckzahl
class Stator(Pumpe):
    def __init__(self, Komponentennummer, Stueckzahl):
        self.Komponentennummer = Komponentennummer
        self.Stueckzahl = Stueckzahl
class Schraube(Pumpe):
    def __init__(self, Komponentennummer, Stueckzahl):
        self.Komponentennummer = Komponentennummer
        self.Stueckzahl = Stueckzahl
class ORing(Pumpe):
    def __init__(self, Komponentennummer, Stueckzahl):
        self.Komponentennummer = Komponentennummer
        self.Stueckzahl = Stueckzahl
class Anlaufscheibe(Pumpe):
    def __init__(self, Komponentennummer, Stueckzahl):
        self.Komponentennummer = Komponentennummer
        self.Stueckzahl = Stueckzahl
class Kuehlblech(Pumpe): 
    def __init__(self, Komponentennummer, Stueckzahl):
        self.Komponentennummer = Komponentennummer
        self.Stueckzahl = Stueckzahl
class Deckel(Pumpe):
    def __init__(self, Komponentennummer, Stueckzahl):
        self.Komponentennummer = Komponentennummer
        self.Stueckzahl = Stueckzahl
class Lot(Pumpe):
    def __init__(self, Komponentennummer, Stueckzahl):
        self.Komponentennummer = Komponentennummer
        self.Stueckzahl = Stueckzahl
class Schmierstoff(Pumpe):
    def __init__(self, Komponentennummer, Stueckzahl):
        self.Komponentennummer = Komponentennummer
        self.Stueckzahl = Stueckzahl
class PTSchraube(Pumpe):
    def __init__(self, Komponentennummer, Stueckzahl):
        self.Komponentennummer = Komponentennummer
        self.Stueckzahl = Stueckzahl

# class Staubschutz(Pumpe):
    # def __init__(self, Komponentennummer, Stueckzahl):
    #     self.Komponentennummer = Komponentennummer
    #     self.Stueckzahl = Stueckzahl

