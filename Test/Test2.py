
# class Pumpe:
#     def __init__(self, Komponentennummer, Stueckzahl):
#         self.Komponentennummer = Komponentennummer
#         self.Stueckzahl = Stueckzahl
#     def descript(self):
#         print(self.Komponentennummer,self.Stueckzahl)

# class Gehaeuse(Pumpe):
#     def __init__(self, Komponentennummer, Stueckzahl):
#         self.Komponentennummer = Komponentennummer
#         self.Stueckzahl = Stueckzahl
   


# G1 = Gehaeuse("Peter", "Stueckzahl")
# G1.descript()

# string = "Peter5" 

# for chars in string:
#     if chars.isdigit() is True:
#         n = chars
#         nstring= string.replace(n,"")

# print(nstring)

# a = []
# for i in range(5):
#     a.append(i)
# print(a)

# def reduziere_verbrauch(mengen, verbraeuche):
#     neue_mengen = []
#     for menge, verbrauch in zip(mengen, verbraeuche):
#         neue_mengen.append(round(menge-verbrauch, 2))
#     return neue_mengen

# mengen = [50, 50, 50, 200, 100, 50, 50, 50, 50, 50, 50, 50, 21.0, 1.5, 100]
# verbraeuche = [1, 1, 1, 4, 2, 1, 1, 1, 1, 1, 1, 1, 0.42, 0.03, 2]
# zeitlicher_verlauf = []
# for t in range(0, 16, 8):
#     neue_mengen = reduziere_verbrauch(mengen, verbraeuche)
#     print(neue_mengen)
#     zeitlicher_verlauf.append(neue_mengen)
#     mengen = neue_mengen
# print(zeitlicher_verlauf)

# emt = "PETER"

# print(emt[0])

def info_label():
    with open("Temp\\log.py", "r") as f:
        liste = f.read()
        for element in liste:
            print(element)


info_label()