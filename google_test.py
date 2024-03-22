from tkinter import *
from tkinter import ttk
from googletrans import Translator, LANGUAGES


def change(text="type", src="English", dest="Hindi") -> str:
    text1 = text
    src1 = src
    dest1 = dest
    trans = Translator()
    trans1 = trans.translate(text, src=src1, dest=dest1)
    return trans1.text


def data():
    s = comb1.get()
    d = combd.get()
    msg = s_txt.get(1.0, END)
    textget = change(text=msg, src=s, dest=d)
    d_txt.delete(1.0, END)
    d_txt.insert(END, textget)


root = Tk()
root.title("Translator")
root.geometry("500x700")
root.config(bg="blue")

lab_txt = Label(root, text="Translator", font=("Times New Roman", 40, "bold"), bg="blue")
lab_txt.place(x=100, y=40, height=50, width=300)

frame = Frame(root).pack(side=BOTTOM)

lab_txt = Label(root, text="SourceText", font=("Times New Roman", 20, "bold"), bg="blue")
lab_txt.place(x=100, y=100, height=20, width=300)

s_txt = Text(frame, font=("Times New Roman", 20, "bold"), wrap=WORD)
s_txt.place(x=10, y=130, height=150, width=480)

list_txt = list(LANGUAGES.values())

comb1 = ttk.Combobox(frame, values=list_txt)
comb1.place(x=10, y=300, height=40, width=150)
comb1.set("english")

button1 = Button(frame, text="Translate", relief=RAISED, command=data)
button1.place(x=170, y=300, height=40, width=150)

combd = ttk.Combobox(frame, values=list_txt)
combd.place(x=330, y=300, height=40, width=150)
combd.set("english")

lab_txt = Label(root, text="DestinationText", font=("Times New Roman", 20, "bold"), bg="blue")
lab_txt.place(x=100, y=360, height=20, width=300)

d_txt = Text(frame, font=("Times New Roman", 20, "bold"), wrap=WORD)
d_txt.place(x=10, y=400, height=150, width=480)

root.mainloop()
