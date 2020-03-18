import tkinter as tk

# root = tk.Tk()
# def update_listbox(*args):
#   search_term = search_var.get()
#   listbox.delete(0, tk.END)
#   for item in all_items:
#     if search_term.lower() in item.lower():
#       listbox.insert(tk.END, item)

# search_var = tk.StringVar()
# search_var.trace('w', update_listbox)
# searchbox = tk.Entry(root, textvariable=search_var)
# searchbox.pack(fill=tk.X, expand=False)

# listbox = tk.Listbox(root)
# for i in ['Adam', 'Lucy', 'Barry', 'Bob']:
#   listbox.insert(tk.END, i)
# listbox.pack()
# all_items = listbox.get(0, tk.END)
# root.mainloop()

class data:
    def __init__(self, KomponentennummerPumpe, Sachnummer):
        self.Sachnummer = Sachnummer
        self.KomponentennummerPumpe = KomponentennummerPumpe


def test(a,b):
    Versuch = data(a, b)
    Nummer = b
    return Versuch , b

Versuch = test("5555","66666")

print("ok")

# if len(liste2) == 0:
#             KomponentennummerPumpe = sel1
#             Sachnummer = KomponentennummerPumpe
#         else:
#             KomponentennummerPumpe = liste2.copy()
#             Sachnummer = sel1
#             update_auswahl(liste2)
#         print(KomponentennummerPumpe)
#         print(Sachnummer)
#         return KomponentennummerPumpe, Sachnummer