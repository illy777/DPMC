import sys
sys.path.append("Temp")
from log2 import *
from matplotlib import pyplot as plt
import numpy

PTakt = 8
RKT = 7200
Bauteil = []
Mengenliste = []

def materialmenge():
    i = 0
    for element in Mengenliste:
        nelement =  element*SZ
        Mengenliste[i] = nelement
        i = i+1
    return Mengenliste

def ProdRKT(SZ,PTakt,Mengenliste,Verbrauchliste):
    Mengen = []
    V = []
    def reduziere_verbrauch(mengen, verbraeuche):
        neue_mengen = []
        for menge, verbrauch in zip(mengen, verbraeuche):
            neue_mengen.append(round(menge-verbrauch, 2))
        return neue_mengen
    for t in range((SZ*PTakt)+2):
        if (t/8).is_integer() is True and t !=0:
            neue_mengen = reduziere_verbrauch(Mengenliste, Verbrauchliste)
            Mengen.append(neue_mengen)
            Mengenliste = neue_mengen
        elif t == 0:
            Mengen.append(Mengenliste)
            time.append(t)
        elif RKT == t:
            for a, b in zip(AnfangM, Mengenliste):
                V.append(a-b)
            return V
        elif 0 in Mengenliste:
            for a, b in zip(AnfangM, Mengenliste):
                V.append(a-b)
            return V

try:
    for x,y in Pumpe0.items():
        Bauteil.append(str(x+"/"+y[1]))
        Mengenliste.append(y[0])
    SZ = Mengenliste[0]
    Bauteil.pop(0)
    Mengenliste.pop(0)
    Verbrauchliste = Mengenliste.copy()
    materialmenge()
    AnfangM = Mengenliste.copy()
    V = ProdRKT(SZ, PTakt, Mengenliste, Verbrauchliste)
    print(V)
except: 
    print("So EINE SCHEIßE")

#print(Verbrauchliste)
#print(AnfangM)





# def VerbrauchRKT(Werte, Bez):
plt.bar(Bauteil,V)
plt.ylabel("Menge")
plt.xlabel("Bezeichnung")
plt.grid(True)
plt.show()


# VerbrauchRKT(V,Bauteil)


# Mengen = []
# time = []
# for t in range(16):
#     if (t/8).is_integer() is True:
#         i= 0
#         time.append(t)
#         for element in Mengenliste:
#             nelement = round(element-Verbrauchliste[i],2)
#             Mengenliste[i] = nelement
#             i = i+1
#         Mengen.append(Mengenliste)
#         print(Mengenliste)

# plt.plot(time, Mengen)
# plt.show()
