import csv
import os
from classes import *
import sys
sys.path.append("Temp")
from temp2 import data




SOLL = data[0]
KomponentennummerPumpe = data[1]
Sachnummer = data[2]
if ".csv" not in str(Sachnummer):
    Sachnummer = Sachnummer+".csv"
if ".csv" in KomponentennummerPumpe:
    KomponentennummerPumpe = KomponentennummerPumpe.replace(".csv", "")


# with open(log, "r+") as f:
#                 f.truncate(0)
#                 f.close()
#             objectsearch()

def objectsearch():
    fdict = {} #temp_dict
    y = 0
    i = 0
    for element in liste:
        fdict["Komponentennummer"] = element[3]
        fdict["Objektkurztext"] = element[4]
        fdict["Menge"]= element[5]
        if y == 0:
            if (str(KomponentennummerPumpe)+".csv" == file):
                P1 = Pumpe(KomponentennummerPumpe,SOLL)
                i=0
                P1.descript(str(i))
                y = y+1    
            elif str(KomponentennummerPumpe) == str(fdict["Komponentennummer"]) and "0" == str(fdict["Menge"]) and (len(element[2]) == 0):
                P1 = Pumpe(KomponentennummerPumpe,SOLL)
                i=0
                P1.descript(str(i))
                y = y+1
            else:
                continue
                #y1 = y1+1 #?
        elif y == 1:
            if ("0" == str(element[5])) and str(KomponentennummerPumpe) != str(element[3]):
                #(len(str(element[2])) == " ") and 
                break
            elif "GEHAEUSE" in str(fdict["Objektkurztext"])[0:8]:
                G1 = Gehaeuse(fdict["Komponentennummer"],fdict["Menge"])
                G1.descript(str(i))
                i = i+1  
                #Gehauese
            elif "PUMPEN" in str(fdict["Objektkurztext"])[0:6]:
                GP = Pumpengehaeuse(fdict["Komponentennummer"],fdict["Menge"])
                GP.descript(str(i))
                i = i+1   
                #Pumpengehäuse
            elif "ROTOR" in str(fdict["Objektkurztext"]):
                R = Rotor(fdict["Komponentennummer"],fdict["Menge"])
                R.descript(str(i))
                i = i+1 
                #Rotor
            elif "LEITER" in str(fdict["Objektkurztext"]):
                L = Leiterplatte(fdict["Komponentennummer"],fdict["Menge"])
                L.descript(str(i)) 
                i = i+1  
                #Leiterplatte
            elif ("SCHUTZHUELSE" or "SCHUTZKAPPE") in str(fdict["Objektkurztext"]):
                S = Schutzhuelse(fdict["Komponentennummer"],fdict["Menge"])  
                S.descript(str(i))
                i=i+1
            elif "SCHRAUBE" in str(fdict["Objektkurztext"]):
                SC = Schraube(fdict["Komponentennummer"],fdict["Menge"])
                SC.descript(str(i))
                i=i+1
                # j = a
                # SC.classifize(str(j))
                # a = a+1
            elif "O-RING" in str(fdict["Objektkurztext"]):
                O = ORing(fdict["Komponentennummer"],fdict["Menge"])
                O.descript(str(i))
                i=i+1
                #O-RIng 
            elif "SCHEIBE" in str(fdict["Objektkurztext"]):
                A = Anlaufscheibe(fdict["Komponentennummer"],fdict["Menge"])
                A.descript(str(i))
                i = i+1
                #Anlaufscheibe
            elif "KUEHL" in str(fdict["Objektkurztext"]):
                K = Kuehlblech(fdict["Komponentennummer"],fdict["Menge"])
                K.descript(str(i)) 
                i = i+1
                #Kuehlblech
            elif ("DECKEL" or "STECKERKAPPE") in str(fdict["Objektkurztext"])[0:5]:
                D = Deckel(fdict["Komponentennummer"],fdict["Menge"])
                D.descript(str(i))
                i = i+1
                #Deckel
            elif "STATOR" in str(fdict["Objektkurztext"]):
                ST = Stator(fdict["Komponentennummer"],fdict["Menge"])
                ST.descript(str(i))
                i = i+1
            # elif "STECKERKAPPE" in str(fdict["Objektkurztext"]):
            #     DU = Staubschutz(fdict["Komponentennummer"],fdict["Menge"])
            #     DU.descript(str(i))
            #     i = i+1
            elif "LOT" in str(fdict["Objektkurztext"]):
                L = Lot(fdict["Komponentennummer"],fdict["Menge"])
                L.descript(str(i))
                i = i+1
                #Lot
            elif "SCHMIER" in str(fdict["Objektkurztext"]):
                SS = Schmierstoff(fdict["Komponentennummer"],fdict["Menge"])
                SS.descript(str(i))
                i = i+1
                #Schmierstoff
            print(element)
           

if (len(str(Sachnummer)) > 4):
    for files in os.walk("Datafolder"):
        for file in files[2]:
            if str(file) == Sachnummer:
                with open("Datafolder\\"+str(Sachnummer)) as f:
                    csv_reader = csv.reader(f, dialect="excel",delimiter=";")
                    liste = list(csv_reader)
                    f.close
                objectsearch()
else:
    for files in os.walk("Datafolder"):
        Path = files[0]
        for file in files[2]:
            with open(Path+"\\"+file, "r") as f:
                csv_reader = csv.reader(f, dialect="excel",delimiter=";")
                liste = list(csv_reader)
                f.close
            objectsearch()
















    



# for element in liste:
#     if "WASSER" in str(element):
        