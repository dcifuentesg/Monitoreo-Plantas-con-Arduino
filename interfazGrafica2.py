from ast import And
from cProfile import label
from ctypes import alignment
from email.mime import image
from re import M
from tkinter import *
from tkinter import font
from tkinter import messagebox
from turtle import bgcolor, left, width
import xdrlib
import os

from Estructuras import Pila
from Estructuras import Lista
from Estructuras import Cola
from Estructuras import HashTable

Usuario = ""
inicio =Tk()
Hash=HashTable.HashTable()
if os.path.isfile('datos.txt'):
    arch = open('datos.txt','r')
    cont = arch.read()
    Hash.arr = eval(cont)
print(Hash.arr)

def menu5():
    return "xd"

def menu4():
    return "xd"

def menu3():
    return "xd"
def menu2():
    cola=Cola.cola()
    inicio.geometry("1000x640")
    frame1=Frame(bg="white")
    frame1.place(x=0,y=0,width=1000,height=640)
    global Usuario
    
    label2=Label(frame1,text="Inicio",font=("Little Comet Bubling Demo Version",42),bg="white")
    label2.place(x=360,y=40)
    
    label3=Label(frame1,text="Bienvenido"+" "+Usuario ,font=("Little Comet Bubling Demo Version",24),bg="white")
    label3.place(x=360,y=100)
    
    img=PhotoImage(file="Imagenes/Fondo2.png")
    img_label=Label(image=img)
    img_label.image= img
    img_label.place(x=-10,y=-10)
    
    firtsbutton=PhotoImage(file='Imagenes/boton2_1.png')
    button1=Button(inicio,image=firtsbutton,command=menu2,borderwidth=0)
    button1.image=firtsbutton
    button1.place(x=2,y=64)
    
    secondbutton=PhotoImage(file='Imagenes/boton2_2.png')
    button2=Button(inicio,image=secondbutton,command=menu3,borderwidth=0)
    button2.image=secondbutton
    button2.place(x=2,y=162)
    
    thirdbutton=PhotoImage(file='Imagenes/boton2_3.png')
    button3=Button(inicio,image=thirdbutton,command=menu4,borderwidth=0)
    button3.image=thirdbutton
    button3.place(x=2,y=268)
    
    fourthbutton=PhotoImage(file='Imagenes/boton2_4.png')
    button4=Button(inicio,image=fourthbutton,command=menu5,borderwidth=0)
    button4.image=fourthbutton
    button4.place(x=2,y=393)
    
    
    
def menu1_1():
    inicio.geometry("440x640")
    frame1=Frame(bg="white")
    frame1.place(x=0,y=0,width=440,height=640)
    
    img=PhotoImage(file="Imagenes/log_in.png")
    img_label=Label(image=img)
    img_label.image= img
    img_label.place(x=-10,y=-10)
    
    user= Entry(inicio, width=25,font=("Little Comet Bubling Demo Version",15))
    user.place(x=120,y=235)
    
    password=Entry(inicio, width=25,font=("Little Comet Bubling Demo Version",15), show="*")
    password.place(x=120,y=380)
    
    def returnValues():
        string1=str(user.get())
        string2=str(password.get())
        if str(Hash[string1])==string2:
            global Usuario
            Usuario = string1
            menu2()
        else:
            messagebox.showinfo("Error","Error en la autenticacion")
            menu1_1()

    
    firtsbutton=PhotoImage(file='Imagenes/boton1_1_1.png')
    button1=Button(inicio,image=firtsbutton,command=returnValues,borderwidth=0)
    button1.image=firtsbutton
    button1.place(x=120,y=450)
    
    
def menu1_2():
    inicio.geometry("440x640")
    frame1=Frame(bg="white")
    frame1.place(x=0,y=0,width=440,height=640)
    
    img=PhotoImage(file="Imagenes/sing_up.png")
    img_label=Label(image=img)
    img_label.image= img
    img_label.place(x=-10,y=-10)
    
    user= Entry(inicio, width=25,font=("Little Comet Bubling Demo Version",15))
    user.place(x=120,y=215)
    
    password=Entry(inicio, width=25,font=("Little Comet Bubling Demo Version",15), show="*")
    password.place(x=120,y=320)
    
    Cpassword=Entry(inicio, width=25,font=("Little Comet Bubling Demo Version",15), show="*")
    Cpassword.place(x=120,y=425)
    
    def returnValues():
        string1=str(user.get())
        string2=str(password.get())
        string3=str(Cpassword.get())
        if Hash[string1] == None and string2 == string3:
            Hash[string1]=string2
            arch = open("datos.txt","w")
            arch.write(str(Hash.arr))
            arch.close()
            menu1_1()
        else:
            if Hash[string1] != None:
                messagebox.showinfo("Error","Nombre de ususario ya existente")
            elif string2 != string3:
                messagebox.showinfo("Error","Las contraseñas no coinciden")
            menu1_2()
    
    firtsbutton=PhotoImage(file='Imagenes/boton1_1_1.png')
    button1=Button(inicio,image=firtsbutton,command=returnValues,borderwidth=0)
    button1.image=firtsbutton
    button1.place(x=120,y=500)
   
def menu1():
    inicio.geometry("440x640")
    frame1=Frame(bg="white")
    frame1.place(x=0,y=0,width=440,height=640)
    
    img=PhotoImage(file="Imagenes/Fondo_inicial.png")
    img_label=Label(image=img)
    img_label.image= img
    img_label.place(x=-10,y=-10)
    
    firtsbutton=PhotoImage(file='Imagenes/boton1_1.png')
    button1=Button(inicio,image=firtsbutton,command=menu1_1,borderwidth=0)
    button1.image=firtsbutton
    button1.place(x=120,y=290)
    
    secondbutton=PhotoImage(file='Imagenes/boton1_2.png')
    button2=Button(inicio,image=secondbutton,command=menu1_2,borderwidth=0)
    button2.image=secondbutton
    button2.place(x=120,y=408)
    
    thirdbutton=PhotoImage(file='Imagenes/boton1_3.png')
    button3=Button(inicio,image=thirdbutton,command=menu4,borderwidth=0)
    button3.image=thirdbutton
    button3.place(x=120,y=508)
menu1()

inicio.mainloop()