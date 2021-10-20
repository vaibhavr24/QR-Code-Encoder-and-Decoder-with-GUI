#from qrc import *
import cv2
from tkinter import *
oni = Tk()

d = cv2.QRCodeDetector()


oni.title('QR CODE GENERATOR')
oni.geometry('400x300')
label = Label(oni, text='Decoder', height=2,
              font=("Felix Titling", 20)).pack()


ent = Entry(oni, width=45, borderwidth=3)
ent.pack()
ent.insert(0, "Enter the Image name with extension to decode it")
ent.configure(state=DISABLED)


def mainc():
    v = str(ent.get())
    d = cv2.QRCodeDetector()
    val, point, str_rq = d.detectAndDecode(cv2.imread(v))
    print(val)
    myLabel1 = Label(oni, text=val).pack()


def on_click(event):
    ent.configure(state=NORMAL)
    ent.delete(0, END)


ent.bind("<Button-1>", on_click)

label = Label(oni, text=' ', height=1,
              font=("Felix Titling", 5)).pack()


bt = Button(oni, text="Decode", font=("Felix Titling", 10),
            bg='white', fg='black', command=mainc).pack()

oni.mainloop()
