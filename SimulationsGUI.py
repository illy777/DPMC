from tkinter import *
import os
def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)
sys.path.append(resource_path("Temp"))
from log import *
import matplotlib.pyplot as plt
import numpy as np

locals = locals().copy()
def get_dicts(locals):
    dic = {}
    for keys in locals:
        if "Pumpe" in keys:
            dic[keys] = locals.get(keys)
    return dic
dic = get_dicts(locals)
del locals

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

root = Tk()
root.geometry("500x300")
root.configure(background = "white")
root.title("Describing Plot for Material Consumption - Simulator")
root.iconbitmap("imgs//icon.ico")
l2 = Frame(root, background = "white")
l2.place(relx=0.1,rely=0.1, width = 400, height= 410)

class simulations():
    def __init__(self, dic):
        l5 = Label(l2, background = "white")
        l5.place(rely = 0.02, relx = 0.145, width = 300, height=50)
        Label(l5, text="Takt in Sekunden:", background="white").grid(column=0)
        Label(l5, text="Regelkreiszeit in Sekunden", background="white").grid(column=1, row=0)
        self.e1 = Entry(l5)
        self.e2 = Entry(l5)
        self.e1.grid(row=1, column=0)
        self.e2.grid(row=1, column=1,padx = 10)
        self.e1.insert(1,8) ###Standartsetting
        self.e2.insert(1,7200)
        self.b4 = HoverButton(l5, text = "Ok",background = "DodgerBlue4", fg="white", border = 0, activebackground = "grey", command = self.getvalues)
        self.b4.place(relx = 0.9, rely = 0.5)
        self.Takt,self.RKT = self.getvalues() #Regelkreistakt
        self.Bauteil = []
        self.Mengenliste = []
        self.Xdata, self.Ydata, self.SOLL = self.convert_toplot(self.material_organizer(dic))

    def getvalues(self):
        self.Takt = int(self.e1.get())
        self.RKT = int(self.e2.get())
        return self.Takt, self.RKT

    def material_organizer(self,dic): #erstellt endgültiges passendes Datenformat für Plots.
        dic2 = set()
        liste = []
        def remove_digits(string):
            for chars in string:
                if chars.isdigit() is True:
                    string = string.replace(chars, "")
            return string
        for key in dic["Pumpe0"]:
            if "Pumpe" in key and "Pumpe" not in dic2:
                dic2.add("Pumpe")
            else:
                newvalue = remove_digits(key)
            try:
                if newvalue not in dic2:
                    dic2.add(newvalue)
            except: 
                continue
        def reload():
            liste = []
            for i in range(len(dic)):
                liste.append(0)
            liste2 = [liste,""]
            return liste2
        def reload2(liste2,i):
            liste = [[],""]
            j = 0
            while j <= i:
                liste[0].append(0)
                j = j+1
            liste[0][i] = liste2[0][0]
            liste[1] = liste2[1]
            return liste
        def arrange(dic):                
            for key in dic2:
                j = 0
                for item in dic[key]:
                    l = len(item[0])
                    while l < (i+1):
                        dic2[key][j][0].append(0)
                        l = l+1
                    j = j+1
            return dic
        liste = reload() #[0,0,0,0,0,0,0,0,0...], zeros the list
        dic2 = {keys:[] for keys in dic2 }
        for i in range(len(dic)):
            # print(i)
            if i == 0: #Pump0 builds fundament. Adds Items to dic2.
                for key in dic["Pumpe"+str(i)]:
                    liste[0][i] = dic["Pumpe"+str(i)][key][0][0]
                    liste[1] = dic["Pumpe"+str(i)][key][1]
                    dic2[remove_digits(key)].append(liste)
                    liste = reload()
            else:
                for key in dic["Pumpe"+str(i)]:
                    if remove_digits(key) not in [keys for keys in dic2]:
                        dic2[remove_digits(key)] = []
                    liste = [values for values in dic["Pumpe"+str(i)][key]]    
                    liste = reload2(liste,i)
                    j = 0
                    if "Pumpe" == key:
                        dic2[key].append(liste)
                    else:
                        for item in dic2[remove_digits(key)]:
                            if liste[1] == item[1] and liste != item:
                                dic2[remove_digits(key)][j][0][i] = liste[0][i]
                            j = j+1
                        if liste[1] not in [item[1] for item in dic2[remove_digits(key)]]:
                            dic2[remove_digits(key)].append(liste)
                        dic2 = arrange(dic2)
                    
        return dic2

    def convert_toplot(self,dic):
        Ydata = []
        Komponentenname = []
        Xdata = []
        SOLL = []
        for key in dic:
            Komponentenname.append(key)
            liste = []
            liste2 = []
            if key == "Pumpe":
                liste3 = [elements[0] for elements in dic[key]]
                for i, value in enumerate(liste3):    
                    SOLL.append(value[i])
            else:
                for objects in dic[key]:
                    liste.append(objects[0])
                    liste2.append(objects[1]+" "+key )
                Xdata.append(liste)
                Ydata.append(liste2) # Mainoperation..
        return Xdata, Ydata, SOLL
    
    def plot_1(self):   
        index = [("Pumpe"+str(i)) for i in range(len(self.Xdata[0][0]))] 
        Pumpen = [[] for i in range(len(index))]
        for elements in self.Xdata:
            for items in elements:
                j = 0
                for value in items:
                    Pumpen[j].append(value)
                    j = j+1
        Komponenten = []
        for elements in self.Ydata:
            for items in elements:
                Komponenten.append(items)
        #Darstellung:
        fig,ax = plt.subplots()
        width = 0.15
        for i, elements in enumerate(Pumpen):
            N = len(elements)
            ind = np.arange(N)
            elements = [self.SOLL[i] * elements for elements in elements]
            p = ax.barh(ind + width*i,elements, width)
            ax.legend(index)
        ax.grid(True, axis="x")
        ax.set_yticklabels([Components for Components in Komponenten])
        ax.set_title('Materialverbrauch pro Pumpe')
        ax.set_yticks(ind + width)
        ax.autoscale_view()
        plt.show() 
        # this list  shalls plot all components for every Pump.

    def plot_2(self):
        index = [("Pumpe"+str(i)) for i in range(len(self.Xdata[0][0]))] 
        Pumpen = [[] for i in range(len(index))]
        for elements in self.Xdata:
            for items in elements:
                j = 0
                for value in items:
                    Pumpen[j].append(value)
                    j = j+1
        Komponenten = []
        for elements in self.Ydata:
            for items in elements:
                Komponenten.append(items)
        liste = []
        for i, elements in enumerate(Pumpen):
            liste.append([self.SOLL[i] * elements for elements in elements])
        Pumpen = [sum(i) for i in zip(*liste)]
        del liste
        a = self.RKT/(self.Takt*sum(self.SOLL))
        if sum(self.SOLL)*self.Takt > self.RKT:
            Medium =[a*elements for elements in Pumpen]
        else:
            Medium = Pumpen
        del a
        #Darstellung:
        fig,ax = plt.subplots()
        width = 0.15
        N = len(Pumpen)
        ind = np.arange(N)
        p1 = ax.barh(ind,Pumpen, width)
        p2 = ax.barh(ind+width, Medium, width )
        ax.grid(True, axis="x")
        ax.legend((p1[0],p2[0]),("Mengen", "Durchschnitt/Regelkreis"))
        ax.set_yticklabels([Components for Components in Komponenten])
        ax.set_title('Gesamtanzahl an benötigten Materialien')
        ax.set_yticks(ind + width)
        ax.autoscale_view()
        plt.show() 

    def plot_3(self):
        index = [("Pumpe"+str(i)) for i in range(len(self.Xdata[0][0]))] 
        Pumpen = [[] for i in range(len(index))]
        for elements in self.Xdata:
            for items in elements:
                j = 0
                for value in items:
                    Pumpen[j].append(value)
                    j = j+1
        Komponenten = []
        for elements in self.Ydata:
            for items in elements:
                Komponenten.append(items)
        #SIMULATION
        PDauer = [(self.Takt*SOLL)/self.RKT for SOLL in self.SOLL] # Wie viele Regelkreise nehmen die Pumpen ein?
        RKL = []
        i = 0
        j = 0
        k = 0
        x= round(sum(PDauer),4)-0.0001
        PDauerCopy = [elements for elements in PDauer]
        summe2 = 0
        while j <= x:
            if "PK" not in locals():
                PK = []
            # Dauer = PDauer[i]
            while PDauer[i] >= 1:
                PDauer[i] = round(PDauer[i]-1,4) # PDauer wird pro Regelkreis um 1 reduziert
                j = j+1
                k = 0
                if len(PK) == 0:
                    PK.append([elements for elements in Pumpen[i]])
                    RKL.append([items for items in PK[0]])
                    PK = [] #Unterscheidung um falls diese Schleife übersprungen wird.
                else:
                    PK.append([(1-PDauer[i-1])*elements for elements in Pumpen[i]]) #TESTE
                    RKL.append([sum(z) for z in zip(*PK)])
                    PK = []
            if (PDauer[i] < 1) and (j < x):
                if k == 1:
                    PK.append([PDauerCopy[i]*elements for elements in Pumpen[i]])
                else:
                    PK.append([PDauer[i]*elements for elements in Pumpen[i]])
                if i !=0:
                    j = j+(PDauer[i]-PDauer[i-1])
                else: 
                    j = j+PDauer[i]
                try:
                    k = 1
                    PDauer[i+1] = round(PDauer[i+1]+PDauer[i], 4)
                except:
                    pass
            i = i+1
            if j >= x:
                if 0<PDauer[-1]<1:
                    if len(PK) == 0:
                        PK.append([(PDauer[-1])*elements for elements in Pumpen[-1]])
                        RKL.append([items for items in PK[0]])
                        break
                    if len(PK) == 1:
                        RKL.append([items for items in PK[0]])
                        break
                    else:
                        RKL.append([sum(z) for z in zip(*PK)])
                    j = j+1
                else:
                    pass
        ###Darstellung
        nums = []
        for items in RKL:
            items = np.array(items)*(self.RKT/self.Takt)
            items= [round(values,6) for values in items.tolist()]
            nums.append(items)
        RKL = nums
        fig,ax = plt.subplots()
        width = 0.05
        index = []
        for i,elements in enumerate(RKL):
            index.append("Regelkreislauf "+str(i))
        for i, elements in enumerate(RKL):
            N = len(elements)
            ind = np.arange(N)
            elements = [elements for elements in elements]
            p = ax.barh(ind + width*i,elements, width)
            ax.legend(index)
        ax.grid(True, axis="x")
        ax.set_yticklabels([Components for Components in Komponenten])
        ax.set_title('Materialverbrauch pro Regelkreislauf')
        ax.set_yticks(ind + 0.5*width*len(index))
        ax.autoscale_view()
        plt.show() 

Simulation = simulations(dic) #funzt nicht mit 7200?

class Menubar:
    def __init__(self):
        self.l1 = Label(root, background = "DodgerBlue4")
        self.l1.place(relx=0,rely=0, width=500)
        self.b1 = HoverButton(self.l1, background = "DodgerBlue4", fg="white", text = "Zurück zum Start", border = 0, activebackground = "grey", width = 7, command= self.back_to_mainmenu)
        self.b1.place(relx=0.8, rely=-0.2, width = 100)
        self.b2 = HoverButton(self.l1, background = "DodgerBlue4", fg="white", text = "Material/Pumpe", border = 0, activebackground = "grey", width = 7, command= Simulation.plot_1)
        self.b2.place(relx=0, rely=-0.2, width = 100)
        self.b3 = HoverButton(self.l1, background = "DodgerBlue4", fg="white", text = "Gesamtanzahl", border = 0, activebackground = "grey", width = 7, command= Simulation.plot_2)
        self.b3.place(relx=0.2, rely = -0.2, width = 100)
        self.b4 = HoverButton(self.l1, background = "DodgerBlue4", fg="white", text = "Material/RK", border = 0, activebackground = "grey", width = 7, command= Simulation.plot_3)
        self.b4.place(relx=0.4, rely = -0.2, width = 100)
    def back_to_mainmenu(self):
        root.destroy()

class objekte:
    def __init__(self):
        self.l3 = Label(l2, background = "white")
        self.l3.place(rely=0.15,relx=0.125, width=300, height=200)
        self.listbox1 = Listbox(self.l3, selectmode = SINGLE, background = "white", border = 1)
        self.lbutton = HoverButton(self.l3, background = "DodgerBlue4", fg="white", text = "Öffnen", border = 0, activebackground = "grey", width = 7, command= self.open_data)
        self.listbox1.place(rely=0.00,relx=0.01, width = 300, height=125)
        self.lbutton.place(rely=0.64,relx=0.01, width = 300)
        scrollbar = Scrollbar(root)
        scrollbar.place(in_=self.listbox1,height=121,relx=0.933, rely=0)
        self.listbox1.configure(yscrollcommand=scrollbar.set)
        scrollbar.configure(command=self.listbox1.yview)
        with open("Temp\\searchlog.py") as f:
            liste = f.readlines()
            f.close()
        liste = [elements+" Anzahl : "+str(Simulation.SOLL[i])+" Zeit:"+str(8*Simulation.SOLL[i]) for i, elements in enumerate(liste)]
        for elements in liste:
            self.listbox1.insert(END, elements)
    def open_data(self):
        sel = self.listbox1.curselection()
        sel1 = self.listbox1.get(sel[0])
        sel1 = sel1.split(" ")[1]
        sel1 = sel1.replace(" ","")
        sel1 = sel1.replace("\n","")
        os.startfile("Datafolder\\"+sel1)

Menubar()
objekte()

root.resizable(0,0)
root.mainloop()
