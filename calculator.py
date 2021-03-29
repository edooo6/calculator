from tkinter import*      #import tkinter for gui
def click(event):         #function for clicking button
    global scvalue        #setting input value as global
    text=event.widget.cget("text")     #cget function extracts text assigned on the button
    print(text)             #print the text assigned on button
    if text == '=':     #assigning a condition for "=" to work
        if scvalue.get().isdigit():   #if value is digit
            value = int(scvalue.get())
        else:
            try:
                value = eval(screen.get())
            except Exception as e:  #exception statement for an error
                value ="Error"  
        scvalue.set(value)
        screen.update()  #update the screen


    elif text == 'C':
        scvalue.set("")
        screen.update()
    else:
        scvalue.set(scvalue.get() + text)
        screen.update()
        


core = Tk()
core.geometry('900x900')
core.title("Calculator")
core.wm_iconbitmap("calc.png")
scvalue = StringVar()
scvalue.set("")
screen = Entry(core, textvar = scvalue, font = 'Impact, 40')
screen.pack(fill=X,ipadx=8,pady=10, padx=14)


f=Frame(core, bg="green")

b=Button(f,text="9",padx=14,pady=10,font='Impact, 25')
b.pack(side=LEFT,padx=8,pady=5)
b.bind("<Button-1   >",click)

b=Button(f,text="8",padx=14,pady=10,font='Impact, 25')
b.pack(side=LEFT, padx=8,pady=5)
b.bind("<Button-1   >", click)


b = Button(f, text="7", padx=14, pady=10, font='Impact, 25')
b.pack(side=LEFT, padx=8,pady=5)
b.bind("<Button-1   >", click)


f.pack()


f = Frame(core, bg="green")

b = Button(f, text="6", padx=14, pady=10, font='Impact, 25')
b.pack(side=LEFT, padx=8, pady=5)
b.bind("<Button-1   >", click)

b = Button(f, text="5", padx=14, pady=10, font='Impact, 25')
b.pack(side=LEFT, padx=8, pady=5)
b.bind("<Button-1   >", click)


b = Button(f, text="4", padx=14, pady=10, font='Impact, 25')
b.pack(side=LEFT, padx=8, pady=5)
b.bind("<Button-1   >", click)


f.pack()

f = Frame(core, bg="green")

b = Button(f, text="3", padx=14, pady=10, font='Impact, 25')
b.pack(side=LEFT, padx=8, pady=5)
b.bind("<Button-1   >", click)

b = Button(f, text="2", padx=14, pady=10, font='Impact, 25')
b.pack(side=LEFT, padx=8, pady=5)
b.bind("<Button-1   >", click)


b = Button(f, text="1", padx=14, pady=10, font='Impact, 25')
b.pack(side=LEFT, padx=8, pady=5)
b.bind("<Button-1   >", click)


f.pack()


f = Frame(core, bg="green")

b = Button(f, text="0", padx=14, pady=10, font='Impact, 25')
b.pack(side=LEFT, padx=8, pady=5)
b.bind("<Button-1   >", click)

b = Button(f, text="+", padx=14, pady=10, font='Impact, 25')
b.pack(side=LEFT, padx=8, pady=5)
b.bind("<Button-1   >", click)


b = Button(f, text="-", padx=14, pady=10, font='Impact, 25')
b.pack(side=LEFT, padx=8, pady=5)
b.bind("<Button-1   >", click)


f.pack()

f = Frame(core, bg="green")

b = Button(f, text="/", padx=14, pady=10, font='Impact, 25')
b.pack(side=LEFT, padx=8, pady=5)
b.bind("<Button-1   >", click)

b = Button(f, text="*", padx=14, pady=10, font='Impact, 25')
b.pack(side=LEFT, padx=8, pady=5)
b.bind("<Button-1   >", click)


b = Button(f, text="%", padx=14, pady=10, font='Impact, 25')
b.pack(side=LEFT, padx=8, pady=5)
b.bind("<Button-1   >", click)


f.pack()


f = Frame(core, bg="green")

b = Button(f, text="C", padx=14, pady=10, font='Impact, 25')
b.pack(side=LEFT, padx=8, pady=5)
b.bind("<Button-1   >", click)

b = Button(f, text="=", padx=14, pady=10, font='Impact, 25')
b.pack(side=LEFT, padx=8, pady=5)
b.bind("<Button-1   >", click)


b = Button(f, text=".", padx=14, pady=10, font='Impact, 25')
b.pack(side=LEFT, padx=8, pady=5)
b.bind("<Button-1   >", click)


f.pack()



core.mainloop()
