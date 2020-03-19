import runpy
from tkinter import *
from PIL import ImageTk, Image
import os
import csv
from classes import *


# with open("Datafolder\\7.02671.29.0.csv", "r") as f:
#         lines = csv.reader(f, delimiter=";", dialect = "excel")
#         liste = list(lines)
#         for element in liste:
#             if "WASSER" in element[4]:
#                 if "D" in element[2]:
#                     KomponentennummerPumpe = sel1
#                     print(KomponentennummerPumpe)
#Functions

class data:
    def __init__(self, KomponentennummerPumpe, Sachnummer):
        self.KomponentennummerPumpe = KomponentennummerPumpe
        self.Sachnummer = Sachnummer

def save():
    runpy.run_module("objectseeker")
    runpy.run_module("temptolog")
    # runpy.run_module("Finallogfile") 

def update_button(*arg):
        files_list.delete(0,END)
        # b2 = Button(l3, background = "DodgerBlue4", fg="white", text = "Zurück", border = 0, command = search_in_folder)
        # b2.place(anchor = CENTER, rely = 0.52, relx = 0.71)

def auswahl(*args):
    soll_zahl = get_soll()
    try:
        def update_auswahl(liste):
            files_list.delete(0,END)
            for elements in liste:
                files_list.insert(END, elements)
        def temp(zu_speichern):
            with open("Temp\\temp2.py", "w") as f:
                f.truncate(0)
                f.write(zu_speichern)
                f.close
        sel = files_list.curselection()
        sel1 = files_list.get(sel[0])
        liste = []
        liste2 = []
        with open("Datafolder\\"+sel1, "r") as f:
            lines = csv.reader(f, delimiter=";", dialect = "excel")
            liste = list(lines)
            f.close()
        for element in liste:
            # print(str(element[3])[0])
            if (str(element[3])[0] == "5") and "WASSER" in element[4]:
                if element[3] in liste2:
                    continue
                else:
                    liste2.append(element[3])
                continue
        if len(liste2) == 0:
            # global dat
            dat = data(sel1, sel1)
            liste3 = []
            liste3.append(soll_zahl)
            liste3.append(dat.KomponentennummerPumpe)
            liste3.append(dat.Sachnummer)
            temp("data = "+str(liste3))
            save()
        else:
            dat = data("", sel1)
            update_auswahl(liste2)
            return dat ##!!HIER IST DER FEHLER
    except:
        sel = files_list.curselection() ##"DAT" MUSS HIERHER "TRANSPORTIERT" WERDEN; NACHDEM ELSE AUSGEFÜHRT WURDE
        sel1 = files_list.get(sel[0])
        ndat = data(sel1,dat.Sachnummer)
        liste3 = []
        liste3.append(soll_zahl)
        liste3.append(ndat.KomponentennummerPumpe)
        liste3.append(ndat.Sachnummer)  
        temp("data = "+str(liste3))
        files_list.delete(0, END)
        search_in_folder()
        save()
        # print(ndat.KomponentennummerPumpe, ndat.Sachnummer)

def update_listbox(*args): #PLS UNDERSTAND!
  search_term = search_var.get()
  files_list.delete(0, END)
  for item in all_items:
    if search_term.lower() in item.lower():
      files_list.insert(END, item)

def get_soll(*args):
    try:
        soll_zahl = soll_var.get()
        if soll_zahl >= 1:
            return soll_zahl
        # print(soll_zahl)
        else:
            raise ValueError("Bitte Zahl für Sollstückzahl eingeben!")
    except:
        raise ValueError("Sollstückzahl muss einer Zahl entsprechen")


#Ground_Structure
app = Tk()
app.geometry("500x600")
app.title("Describing Plot for Material Consumption")
app.configure(background = "white")
# app.iconbitmap("")
#Mainlabels
l1 = Label(app, background = "white")
l1.place(rely = 0.10, relx=0.1,height = 400, width =450)
n = len(os.listdir("Datafolder"))
image = Image.open("Pierburglogo.png")
image = image.resize((250,150), Image.ANTIALIAS)
photo = ImageTk.PhotoImage(image)
Label(l1,image=photo, background = "white" ).place(rely = 0, relx = 0.15)#Titlelabel
l2 = Label(app, background = "white")
l2.place(rely = 0.35, relx = 0.2) #Infolabel
Label(l2, background = "white", text = "Es sind "+str(n)+" Objekte registriert!").grid(row=1, column = 0, sticky = "E")
Label(l2, text = "Pumpensuche: ", background = "white").grid(row = 3, column = 0) #Entrylabel
Label(l2, text = "Sollzahl: ", background = "white").grid(row = 2, column = 0)
l3 = Label(app, background = "white")
l3.place(rely = 0.71, relx = 0.1957, width=320)#Buttons
#Infolabeltxt
# def info_label():
#     with open("Temp\\log.py", "r") as f:
#         for element in f.readlines():           
#Textbox
files_list = Listbox(app, height=8, width=50, selectmode=SINGLE)
files_list.place(rely=0.6, relx= 0.5, anchor=CENTER)
def search_in_folder():
    for r, d, f in os.walk("Datafolder"):
        for file in f:
            if '.csv' in file:
                files_list.insert(END, file)
    return file
search_in_folder()
scrollbar = Scrollbar(app)
scrollbar.place(in_=files_list,height=132,relx=1, rely=-0.017)
files_list.configure(yscrollcommand=scrollbar.set)
scrollbar.configure(command=files_list.yview)
#SearchEntry
all_items = files_list.get(0, END)
search_var = StringVar()
search_var.trace('w', update_listbox)
Entry(l2, textvariable=search_var).grid(row=3, column = 1, sticky = "W")
#SOLLEntry
soll_var = IntVar()
Entry(l2, textvariable = soll_var).grid(row=2, column= 1 , sticky ="W")
#Buttons
b1 = Button(l3, background = "DodgerBlue4", fg="white", text = "Quit", border = 0, command = app.quit)
b1.place(anchor = CENTER, rely = 0.5, relx = 0.04) # Quit
b2 = Button(l3, background = "DodgerBlue4", fg="white", text = "Auswählen", border = 0, command = auswahl)
b2.place(anchor = CENTER, rely = 0.5, relx = 0.9) # Auswahl Button


app.mainloop()




