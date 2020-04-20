from tkinter import *
from PIL import ImageTk, Image
import os
import csv
import runpy
import sys

def resource_path(relative_path):
    # """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)
sys.path.append(resource_path("Temp"))

class HoverButton(Button): #Buttonsclass
    def __init__(self, master, **kw):
        Button.__init__(self,master=master,**kw)
        self.defaultBackground = self["background"]
        self.bind("<Enter>", self.on_enter)
        self.bind("<Leave>", self.on_leave)

    def on_enter(self, e):
        self['background'] = self['activebackground']

    def on_leave(self, e):
        self['background'] = self.defaultBackground
          
def update_listbox(*args): #listbox
  search_term = search_var.get()
  files_list.delete(0, END)
  for item in all_items:
    if search_term.lower() in item.lower():
      files_list.insert(END, item)

#Ground_Structure
app = Tk()
app.geometry("500x600")
app.title("Describing Plot for Material Consumption")
app.configure(background = "white")
app.iconbitmap("imgs//icon.ico")


#Mainlabels
image = Image.open("imgs//Pierburglogo.png")
image = image.resize((250,150), Image.ANTIALIAS)
photo = ImageTk.PhotoImage(image)
Label(app,image=photo, background = "white" ).place(rely = 0.1, relx = 0.25)#Titlelabel

class infolabel:
    def __init__(self): 
        self.info_txt()
    def SollError(self, m):
        self.txt_label.destroy()
        self.l2 = Frame(app, background = "white")
        self.l2.place(rely = 0.35, relx = 0.2) 
        if m == 0:
            txt = "ERROR 1: Sollstückzahl muss >0 sein!"
            self.txt_label = Label(self.l2, background = "white", text = txt)
            self.txt_label.grid(row=1,columnspan = 2)
        elif m ==1:
            txt = "INFO: Alle Objekte wurden erfolgreich gelöscht!"
            self.txt_label = Label(self.l2, background = "white", text = txt)
            self.txt_label.grid(row=1,columnspan = 2)
        elif m == 3:
            txt = "ERROR 3: Bitte Objekt auswählen!"
            self.txt_label = Label(self.l2, background = "white", text = txt)
            self.txt_label.grid(row=1,columnspan = 2)
        else:
            txt = "ERROR 2: Bitte natürliche Zahl für Sollstückzahl eingeben!"
            self.txt_label = Label(self.l2, background = "white", text = txt)
            self.txt_label.grid(row=1,columnspan = 2)
        app.update()
    def info_txt(self):
        try: 
            self.txt_label.destroy()
        except:
            pass
        self.l2 = Frame(app, background = "white")
        self.l2.place(rely = 0.35, relx = 0.2) 
        with open("Temp\\log.py", "r") as f:
            n = len(f.readlines())
            f.close()
            if n == 0:
                n = len(os.listdir("Datafolder"))
                txt = "Es sind "+str(n)+" Objekte in der Datenbank vorhanden!"
                self.txt_label = Label(self.l2, background = "white", text = txt)
                self.txt_label.grid(row=1,columnspan = 2) 
            else:
                if n < 10:  
                    txt = "Es wurden "+str(n)+" Objekte erfasst!"
                else: 
                    txt = "Es wurde das Max. von "+str(n)+" Objekten erreicht!"
                self.txt_label = Label(self.l2, background = "white", text = txt)
                self.txt_label.grid(row=1,columnspan = 2)

class auswahl(): #Befehlsreihe Auswahl!
    def __init__(self, selection):
        self.liste = []
        self.liste2 = []
        self.liste3 = []
        self.sel1 = selection
        self.b4 = HoverButton(l3, background = "DodgerBlue4", fg="white", text = "Zurück", border = 0, command = self.search_in_folder, activebackground = "grey", width = 100)

    def save(self):
        runpy.run_module("objectseeker")
        runpy.run_module("Logfile")
        #if error occurs try os.startsystem("python module.py")

    def search_in_folder(self):
        files_list.delete(0, END)
        for r, d, f in os.walk("Datafolder"):
            for file in f:
                if '.csv' in file:
                    files_list.insert(END, file)
        with open("Temp\\temp2.py", "w") as f:
            f.truncate(0)
            f.close()   
        self.b4.destroy()
        app.update()
        return file

    def update_auswahl(self,liste):
        files_list.delete(0,END)
        for elements in self.liste2:
            files_list.insert(END, elements)
        self.b4.place(anchor = CENTER, rely = 0.7, relx = 0.5)

    def temp(self,zu_speichern):
        with open("Temp\\temp2.py", "w") as f:
            f.truncate(0)
            f.write(zu_speichern)
            f.close
    
    def auswahl(self,*args):
        soll_zahl = self.get_soll()
        with open("Datafolder\\"+self.sel1, "r") as f:
            lines = csv.reader(f, delimiter=";", dialect = "excel")
            self.liste = list(lines)
            f.close()
        for element in self.liste:
            if (str(element[3])[0] == "5") and "WASSER" in element[4]:
                if element[3] in self.liste2:
                    continue
                else:
                    self.liste2.append(element[3])
                continue
        if len(self.liste2) == 0:
            self.liste3.append(soll_zahl)
            self.liste3.append(self.sel1)
            self.liste3.append(self.sel1)
            self.temp("data = "+str(self.liste3))
            self.save()
            app.update()
        else:
            self.update_auswahl(self.liste2)
            Sachnummer = self.sel1
            self.temp("Sachnummer ="+str(Sachnummer))
        self.info(soll_zahl)
        
    def auswahl2(self, Sachnummer):  
        soll_zahl = self.get_soll() 
        liste3 = []
        liste3.append(soll_zahl)
        liste3.append(self.sel1)
        liste3.append(Sachnummer)  
        self.search_in_folder()
        self.temp("data = "+str(liste3))
        self.save()
        self.info(soll_zahl)
        app.update()

    def get_soll(self): # get SOLLZAHL
        try:
            soll_zahl = soll_var.get()
        except:
            infolabel.SollError(2)
            raise ValueError("Bitte natürliche Zahl für Sollstückzahl eingeben!")
        if soll_zahl == 0:
            infolabel.SollError(soll_zahl)
            raise ValueError("Sollstückzahl muss >0 sein!")        
        return soll_zahl

    def info(self, soll_zahl):
        if soll_zahl >= 1:
            infolabel.info_txt()

infolabel = infolabel()

l4 = Label(app,background = "white") # Label für Entries
l4.place(rely = 0.39, relx = 0.2) 
Label(l4, text = "Pumpensuche: ", background = "white").grid(row = 1, column = 0) #Entrylabel
Label(l4, text = "Sollzahl: ", background = "white").grid(row = 0, column = 0)


l5 = Label(app,background = "DodgerBlue4")
l5.place(width=500, rely = 0) #Menubar


#Textbox
files_list = Listbox(app, height=8, width=50, selectmode=SINGLE)
files_list.place(rely=0.6, relx= 0.5, anchor=CENTER) 

def search_in_folder():
    files_list.delete(0, END)
    for r, d, f in os.walk("Datafolder"):
        for file in f:
            if '.csv' in file:
                files_list.insert(END, file)
    return file

search_in_folder()
scrollbar = Scrollbar(app)
scrollbar.place(in_=files_list,height=128.5,relx=0.95, rely=0)
files_list.configure(yscrollcommand=scrollbar.set)
scrollbar.configure(command=files_list.yview)

#SearchEntry
all_items = files_list.get(0, END)
search_var = StringVar()
search_var.trace('w', update_listbox)
Entry(l4, textvariable=search_var).grid(row=1, column = 1, sticky = "W")
#SOLLEntry
soll_var = IntVar()
Entry(l4, textvariable = soll_var).grid(row=0, column= 1 , sticky ="W")
#Buttons
def readme():
    os.startfile("README.txt")

b1 = HoverButton(l5, background = "DodgerBlue4", fg="white", text = "Quit", border = 0, command = app.quit, activebackground = "grey", width = 7)
b1.place(anchor = CENTER, rely = 0.5, relx = 0.95) # Quit, 0.29
b6 = HoverButton(l5, background = "DodgerBlue4", fg="white", text = "?", border = 0, command = readme, activebackground = "grey", width = 2)
b6.place(anchor = CENTER, rely = 0.5, relx = 0.88)
def choice(*args):
    sel = files_list.curselection()
    sel1 = files_list.get(sel[0])
    choice = auswahl(sel1)
    with open("Temp\\temp2.py", "r") as f:
        Sachnummer = f.read()
        f.close()
    if "Sachnummer" in Sachnummer:
        Sachnummer = Sachnummer.split("=")
        choice.auswahl2(Sachnummer[1])
    else:
        choice.auswahl()

l3 = Frame(app, background = "white")
l3.place(rely = 0.71, relx = 0.1957, width=304.3, height =50)
b2 = HoverButton(l3, background = "DodgerBlue4", fg="white", text = "Auswählen", border = 0, command = choice, activebackground = "grey", width=100)
b2.place(anchor = CENTER, rely = 0.2, relx = 0.5) # Auswahl Button

def clear_temp():
    for r,d,f in os.walk("Temp"):
        for file in f:
            if ".pyc" not in file:
                with open("Temp\\"+file, "r+") as file:
                    file.truncate(0)
                    file.close
    infolabel.SollError(1)

b3 = HoverButton(l5, background = "DodgerBlue4", fg = "white", text = "Clear Temp", border = 0, command = clear_temp, activebackground = "grey" )
b3.place(anchor = CENTER, rely = 0.5, relx = 0.191) # Clear Temp

def simulieren():
    with open("Temp\\log.py", "r") as f:
            n = len(f.readlines())
            f.close()
    if n != 0:
        runpy.run_module("SimulationsGUI")
    else:
        infolabel.SollError(3)

b5 = HoverButton(l5, background = "DodgerBlue4", fg = "white", text = "Simulieren", border = 0, command = simulieren, activebackground = "grey" )
b5.place(anchor = CENTER, rely = 0.5, relx = 0.06) #Simulieren




f1 = Label(app, background = "white", text = "Copyright® Isaac L.L. Yuki")
f1.place(relx= 0.34, rely = 0.93, width= 150)
app.resizable(0,0)
app.mainloop()



