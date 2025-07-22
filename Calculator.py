#import statement
from tkinter import *

#GUI Interaction
wn = Tk()
wn.title("Calculator")
wn.geometry("500x500")

#Entry Box
ent = Entry(wn , width=43 , borderwidth=5)
ent.place(x= 0,y= 0)

#Buttons
def click(num):
    result=ent.get()
    ent.delete(0,END)
    ent.insert(0,str(result) + str(num))

b = Button(wn , text="1", width = 12 , command = lambda : click(1))
b.place(x= 10,y= 60)

b = Button(wn , text="2", width = 12 , command = lambda : click(2) )
b.place(x= 80,y= 60)

b = Button(wn , text="3", width = 12 , command = lambda : click(3) )
b.place(x= 170,y= 60)

b = Button(wn , text="4", width = 12 , command = lambda : click(4) )
b.place(x= 10,y= 120)

b = Button(wn , text="5", width = 12 , command = lambda : click(5) )
b.place(x= 80,y= 120)

b = Button(wn , text="6", width = 12 , command = lambda : click(6) )
b.place(x= 170,y= 120)

b = Button(wn , text="7", width = 12 , command = lambda : click(7) )
b.place(x= 10,y= 180)

b = Button(wn , text="8", width = 12 , command = lambda : click(8) )
b.place(x= 80,y= 180)

b = Button(wn , text="9", width = 12 , command = lambda : click(9) )
b.place(x= 170,y= 180)

def mult():
    n1 = ent.get()
    global math
    math = "Multiplication"
    global i
    i = int(n1)
    ent.delete(0,END)

b = Button(wn , text="*", width = 12 , command=mult)
b.place(x= 10,y= 240)

b = Button(wn , text="0", width = 12 , command = lambda : click(0))
b.place(x= 80,y= 240)

def add():
    n1 = ent.get()
    global math
    math = "Addition"
    global i
    i = int(n1)
    ent.delete(0,END)

b = Button(wn , text="+", width = 12 , command = add )
b.place(x= 170,y= 240)

def minus():
    n1 = ent.get()
    global math
    math = "Subtraction"
    global i
    i = int(n1)
    ent.delete(0,END)

b = Button(wn , text="-", width = 12 , command = minus )
b.place(x= 10,y= 300)

def div():
    n1 = ent.get()
    global math
    math = "Division"
    global i
    i = int(n1)
    ent.delete(0,END)

b = Button(wn , text="/", width = 12 , command = div )
b.place(x= 80,y= 300)

def equal():
    n2 = ent.get()
    ent.delete(0,END)
    if math == "Addition":
        ent.insert(0,i + int(n2))
    elif math == "Subtraction":
        ent.insert(0,i - int(n2))
    elif math == "Division":
        ent.insert(0,i / int(n2))
    elif math == "Multiplication":
        ent.insert(0,i * int(n2))

b = Button(wn , text="=", width = 12 , command = equal )
b.place(x= 170,y= 300)

def clear():
    ent.delete(0,END)

b = Button(wn , text="clear", width = 12 , command = clear )
b.place(x= 10,y= 350)

#mainloop
wn.mainloop()
