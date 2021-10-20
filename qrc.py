import qrcode
from tkinter import *
oni = Tk()

oni.title('QR CODE GENERATOR')
oni.geometry('400x300')
label = Label(oni, text='Encoder', height=2,
              font=("Felix Titling", 20)).pack()


ent = Entry(oni, width=60, borderwidth=3)
ent.pack()
ent.insert(0, "Enter the Information you wanna store in QR CODE ")
ent.configure(state=DISABLED)

label = Label(oni, text=' ', height=1,
              font=("Felix Titling", 8)).pack()

ent1 = Entry(oni, width=30, borderwidth=3)
ent1.pack()
ent1.insert(0, "Write image name with entension")
ent1.configure(state=DISABLED)

label = Label(oni, text='(jpg recommended)', height=2,
              font=("Felix Titling", 10)).pack()


def mainc():
    v = str(ent.get())
    img = qrcode.make(v)
    b = str(ent1.get())
    img.save(b)


def on_click(event):
    ent.configure(state=NORMAL)
    ent.delete(0, END)


ent.bind("<Button-1>", on_click)


def on_click(event):
    ent1.configure(state=NORMAL)
    ent1.delete(0, END)


ent1.bind("<Button-1>", on_click)


bt = Button(oni, text="Encode", font=("Felix Titling", 10),
            bg='white', fg='black', command=mainc).pack()

oni.mainloop()
