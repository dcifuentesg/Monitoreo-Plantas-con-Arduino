from ast import And
from re import M
from tkinter import *
from matplotlib import pyplot as plt


from Estructuras import Pila
from Estructuras import Lista
from Estructuras import Cola
from Estructuras import HashTable
from Estructuras import searchBinaryTree
from Estructuras import Grafo
import ConexionBd
import Proyectofinal
import os

inputs=[]
path = []
Usuario = ""
data=ConexionBd.random_data()
inicio =Tk()
Hash=HashTable.HashTable()
if os.path.isfile('datos.txt'):
    arch = open('datos.txt','r')
    cont = arch.read()
    Hash.arr = eval(cont)

def menu6():
    def menu10():
        tuberias = Grafo.Graph(Proyectofinal.conexiones)
        path = tuberias.get_shortest_path(inputs[0],inputs[1])
        #print(tuberias.get_shortest_path(inputs[0],inputs[1]))
        #camino = tuberias.get_shortest_path(inputs[0],inputs[1])
        print(path)
        inputs.pop(0)
        inputs.pop(0)
    
    def menu11():
        inputs.append(1.0)
        return inputs
    def menu12():
        inputs.append(2.0)
        return inputs
    def menu13():
        inputs.append(3.0)
        return inputs
    def menu14():
        inputs.append(4.0)
        return inputs
    def menu15():
        inputs.append(5.0)
        return inputs
    def menu16():
        inputs.append(6.0)
        return inputs
    def menu17():
        inputs.append(7.0)
        return inputs
    def menu18():
        inputs.append(8.0)
        return inputs
    def menu19():
        inputs.append(9.0)
        return inputs
    
    inicio.geometry("1000x640")
    frame1=Frame(bg="white")
    frame1.place(x=0,y=0,width=1000,height=640)
    
    
    label2=Label(frame1,text="Inicio",font=("Little Comet Bubling Demo Version",42),bg="white")
    label2.place(x=360,y=40)
    
    label3=Label(frame1,text="Bienvenido",font=("Little Comet Bubling Demo Version",24),bg="white")
    label3.place(x=360,y=100)

    label10=Label(frame1,text="Mejor Camino: ",font=("Little Comet Bubling Demo Version",24),bg="white")
    label10.place(x=360,y=140)

    label11=Label(frame1,text=path,font=("Little Comet Bubling Demo Version",24),bg="white")
    label11.place(x=440,y=140)
    
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
    
    c1button=PhotoImage(file='Imagenes/boton2_4.png')
    button11=Button(inicio,image=c1button,command=menu11,borderwidth=0)
    button11.image=c1button
    button11.place(x=400,y=200)

    c2button=PhotoImage(file='Imagenes/boton2_4.png')
    button12=Button(inicio,image=c2button,command=menu12,borderwidth=0)
    button12.image=c2button
    button12.place(x=520,y=200)
    
    c3button=PhotoImage(file='Imagenes/boton2_4.png')
    button13=Button(inicio,image=c3button,command=menu13,borderwidth=0)
    button13.image=c3button
    button13.place(x=640,y=200)

    c4button=PhotoImage(file='Imagenes/boton2_4.png')
    button14=Button(inicio,image=c4button,command=menu14,borderwidth=0)
    button14.image=c4button
    button14.place(x=400,y=350)

    c5button=PhotoImage(file='Imagenes/boton2_4.png')
    button15=Button(inicio,image=c5button,command=menu15,borderwidth=0)
    button15.image=c5button
    button15.place(x=520,y=350)

    c6button=PhotoImage(file='Imagenes/boton2_4.png')
    button16=Button(inicio,image=c6button,command=menu16,borderwidth=0)
    button16.image=c6button
    button16.place(x=640,y=350)

    c7button=PhotoImage(file='Imagenes/boton2_4.png')
    button17=Button(inicio,image=c7button,command=menu17,borderwidth=0)
    button17.image=c7button
    button17.place(x=400,y=500)

    c8button=PhotoImage(file='Imagenes/boton2_4.png')
    button18=Button(inicio,image=c8button,command=menu18,borderwidth=0)
    button18.image=c8button
    button18.place(x=520,y=500)

    c9button=PhotoImage(file='Imagenes/boton2_4.png')
    button19=Button(inicio,image=c9button,command=menu19,borderwidth=0)
    button19.image=c9button
    button19.place(x=640,y=500)

    c10button=PhotoImage(file='Imagenes/boton2_4.png')
    button20=Button(inicio,image=c10button,command=menu10,borderwidth=0)
    button20.image=c10button
    button20.place(x=400,y=600)
def menu5():
    cola=Cola.cola()
    inicio.geometry("1000x640")
    frame1=Frame(bg="white")
    frame1.place(x=0,y=0,width=1000,height=640)
    
    label2=Label(frame1,text="Contingencias",font=("Little Comet Bubling Demo Version",42),bg="white")
    label2.place(x=360,y=10)
    
    label3=Label(frame1,text="Contingencias es el apartado donde se muestra si se debe\nrealizar alguna accion de emergancia ya que se han detectado \nvalores criticos para la medion" ,font=("Little Comet Bubling Demo Version",16),bg="white",justify="left")
    label3.place(x=360,y=70)
    
    img=PhotoImage(file="Imagenes/Fondo2.png")
    img_label=Label(image=img)
    img_label.image= img
    img_label.place(x=-10,y=-10)
    
    img2=PhotoImage(file="Imagenes/pila.png")
    img2_label=Label(image=img2)
    img2_label.image= img2
    img2_label.place(x=750,y=150)
    
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
    
    def revisaTemperatura():
        temp=ConexionBd.ArrayTem(data)
        promedio=0
        for i in range(len(temp)):
            promedio+=temp[i]
        promedio=promedio/len(temp)
        if promedio<20 and promedio>15:
            cola.encolar("Dejar a la interperie \npara que aumente \nla temperatura 1(H)")
            label4=Label(frame1,text="-La temperatura esta normal , aunque es un poco baja ",font=("Little Comet Bubling Demo Version",14),bg="white",justify="left")
            label4.place(x=360,y=180)
        elif promedio<45 and promedio>20:
            cola.encolar("Dejar a la interperie \npara que aumente \nla temperatura 15(min)")
            label4=Label(frame1,text="-Deberias revisar las tareas ya que la temperatura esta\ncerca de valores muy bajos",font=("Little Comet Bubling Demo Version",14),bg="white",justify="left")
            label4.place(x=360,y=180)
        elif promedio<65 and promedio>45:
            label4=Label(frame1,text="-La temperatura esta normal , aunque es un poco alta",font=("Little Comet Bubling Demo Version",14),bg="white",justify="left")
            label4.place(x=360,y=180)
            cola.encolar("dejar con algo cubierto \npara reducir un poco la \ntemperatura 1(H)")
        elif promedio<85 and promedio>65:
            label4=Label(frame1,text="-Deberias revisar las tareas ya que la temperatura esta\ncerca de valores muy altos",font=("Little Comet Bubling Demo Version",14),bg="white",justify="left")
            label4.place(x=360,y=180)
            cola.encolar("Dejar con algo cubierto \npara reducir un poco \nla temperatura 15(min)")
        else:
            label4=Label(frame1,text="-Parece que las mediciones de temperatura tienen valores \ncriticos por favor revisa el apartado de contingencias",font=("Little Comet Bubling Demo Version",14),bg="white",justify="left")
            label4.place(x=360,y=180)
            
    def revisaAire():
        humA=ConexionBd.ArrayHumA(data)
        promedio=0
        
        for i in range(len(humA)):
            promedio+=humA[i]
        promedio=promedio/len(humA)
        
        if promedio<50 and promedio>35:
            cola.encolar("Dejar a la interperie \npara que reciba mas \nhumedad 1(H)")
            label4=Label(frame1,text="-La humedad de aire  esta normal , aunque \nes un poco baja ",font=("Little Comet Bubling Demo Version",14),bg="white",justify="left")
            label4.place(x=360,y=230)
        elif promedio<35 and promedio>20:
            cola.encolar("Dejar a la interperie para \nque reciba mas \nhumedad 15(min)")
            label4=Label(frame1,text="-Deberias revisar las tareas ya que la humedad del aire\nesta cerca de valores muy bajos",font=("Little Comet Bubling Demo Version",14),bg="white",justify="left")
            label4.place(x=360,y=230)
        elif promedio<65 and promedio>50:
            label4=Label(frame1,text="-La humedad del aire esta normal , aunque es \nun poco alta",font=("Little Comet Bubling Demo Version",14),bg="white",justify="left")
            label4.place(x=360,y=230)
            cola.encolar("Dejar con algo cubierto \npara reducir un poco \nla humedad 1(H)")
        elif promedio<80 and promedio>65:
            label4=Label(frame1,text="-Deberias revisar las tareas ya que la humedad del aire\nestacerca de valores muy altos",font=("Little Comet Bubling Demo Version",14),bg="white",justify="left")
            label4.place(x=360,y=230)
            cola.encolar("Dejar con algo cubierto \npara reducir un poco \nla humedad 15(min)")
        else:          
            label4=Label(frame1,text="-Parece que las mediciones de humedad \ndel aire tienen valores criticos por favor revisa \nel apartado de contingencias",font=("Little Comet Bubling Demo Version",14),bg="white",justify="left")
            label4.place(x=360,y=230)
            
    def revisaHumedad():
        humS=ConexionBd.ArrayHuS(data)
        promedio=0
        
        for i in range(len(humS)):
            promedio+=humS[i]
        promedio=promedio/len(humS)
        if promedio<700 and promedio>600:
            cola.encolar("Regar en \n aproximadamente \n2 o 4 horas")
            label7=Label(frame1,text="-Deberias revisar las tareas ya que la humedad del suelo \nesta cerca de valores muy bajos",font=("Little Comet Bubling Demo Version",14),bg="white",justify="left")
            label7.place(x=360,y=300)
        elif promedio<800 and promedio>700:
            cola.encolar("Regar el siguiente dia ")
            label7=Label(frame1,text="-La humedad del suelo esta normal , aunque es \nun poco baja ",font=("Little Comet Bubling Demo Version",14),bg="white",justify="left")
            label7.place(x=360,y=300)
        elif promedio<900 and promedio>800:
            label7=Label(frame1,text="-La humedad del suelo esta normal , aunque es \nun poco alta",font=("Little Comet Bubling Demo Version",14),bg="white",justify="left")
            label7.place(x=360,y=300)
            cola.encolar("Dejar la planta bajo el \nsol 1(H)")
        elif promedio<1000 and promedio>900:
            label7=Label(frame1,text="-Deberias revisar las tareas ya que la humedad esta\ncerca de valores muy altos",font=("Little Comet Bubling Demo Version",14),bg="white",justify="left")
            label7.place(x=360,y=300)
            cola.encolar("Drenar un poco el agua\nde la planta")
        else:
            label7=Label(frame1,text="-Parece que las mediciones de humedad del suelo \ntienen valores criticos por favor revisa el \napartado de contingencias",font=("Little Comet Bubling Demo Version",14),bg="white",justify="left")
            label7.place(x=360,y=300)
            
    def revisaLuz():
        li=ConexionBd.ArrayLi(data)
        promedio=0
        for i in range(len(li)):
            promedio+=li[i]
        promedio=promedio/len(li)
        if promedio<0.35 and promedio>0.2:
            cola.encolar("Dejar a la luz 1(H)")
            label9=Label(frame1,text="-Deberias revisar las tareas ya que la luz \nesta cerca de valores muy bajos",font=("Little Comet Bubling Demo Version",14),bg="white",justify="left")
            label9.place(x=360,y=380)
        elif promedio<0.5 and promedio>0.35:
            cola.encolar("Dejar a la luz 15(min)")
            label9=Label(frame1,text="-La luz esta normal , aunque es un poco baja ",font=("Little Comet Bubling Demo Version",14),bg="white",justify="left")
            label9.place(x=360,y=380)
        elif promedio<0.65 and promedio>0.5:
            label9=Label(frame1,text="-La luz normal , aunque es un poco alta",font=("Little Comet Bubling Demo Version",14),bg="white",justify="left")
            label9.place(x=360,y=380)
            cola.encolar("Evitar que le llegue \nluz 15(min)")
        elif promedio<0.8 and promedio>0.65:
            label9=Label(frame1,text="-Deberias revisar las tareas ya que la luz esta\ncerca de valores muy altos",font=("Little Comet Bubling Demo Version",14),bg="white",justify="left")
            label9.place(x=360,y=380)
            cola.encolar("Evitar que le llegue \nluz 1(H)")
        else:
            label9=Label(frame1,text="-Parece que las mediciones de luz tienen valores \ncriticos por favor revisa el apartado de contingencias",font=("Little Comet Bubling Demo Version",14),bg="white",justify="left")
            label9.place(x=360,y=380)
    
    def imprimeTareas():
        particiones=cola.size
        largo=261
        ancho=140
        if particiones>=1:
            string1=str(cola.desencolar())
            frame2=Frame(bg="#3DD6FE")
            frame2.place(x=800,y=435,width=ancho-5,height=(int(largo/4)-5))
            label5=Label(frame2,text=string1,font=("Little Comet Bubling Demo Version",11),bg="#3DD6FE",justify="left")
            label5.place(x=0,y=0)
        if particiones>=2:
            string2=str(cola.desencolar())
            frame3=Frame(bg="#3DD6FE")
            frame3.place(x=800,y=370,width=ancho-5,height=(int(largo/4)-5))
            label6=Label(frame3,text=string2,font=("Little Comet Bubling Demo Version",11),bg="#3DD6FE",justify="left")
            label6.place(x=0,y=0)
        if particiones>=3:
            string2=str(cola.desencolar())
            frame4=Frame(bg="#3DD6FE")
            frame4.place(x=800,y=305,width=ancho-5,height=(int(largo/4)-5))
            label8=Label(frame4,text=string2,font=("Little Comet Bubling Demo Version",11),bg="#3DD6FE",justify="left")
            label8.place(x=0,y=0)
        if particiones>=4:
            string2=str(cola.desencolar())
            frame5=Frame(bg="#3DD6FE")
            frame5.place(x=800,y=240,width=ancho-5,height=(int(largo/4)-5))
            label10=Label(frame5,text=string2,font=("Little Comet Bubling Demo Version",11),bg="#3DD6FE",justify="left")
            label10.place(x=0,y=0)
    
    revisaHumedad()
    revisaAire()
    revisaTemperatura()
    revisaLuz()
    imprimeTareas()
def menu4():
    cola=Cola.cola()
    inicio.geometry("1000x640")
    frame1=Frame(bg="white")
    frame1.place(x=0,y=0,width=1000,height=640)
    
    label2=Label(frame1,text="Tareas",font=("Little Comet Bubling Demo Version",42),bg="white")
    label2.place(x=360,y=10)
    
    label3=Label(frame1,text="A continuacion se mostraran las tareas a realizar para mantener el cultivo \nen buen estado  tales como regar , dar ventilacion o darles mas iluminacion segun \nlas medidas obtenidas" ,font=("Little Comet Bubling Demo Version",16),bg="white",justify="left")
    label3.place(x=360,y=70)
    
    img=PhotoImage(file="Imagenes/Fondo2.png")
    img_label=Label(image=img)
    img_label.image= img
    img_label.place(x=-10,y=-10)
    
    img2=PhotoImage(file="Imagenes/cola.png")
    img2_label=Label(image=img2)
    img2_label.image= img2
    img2_label.place(x=750,y=150)
    
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
    
    def revisaTemperatura():
        temp=ConexionBd.ArrayTem(data)
        promedio=0
        for i in range(len(temp)):
            promedio+=temp[i]
        promedio=promedio/len(temp)
        if promedio<20 and promedio>15:
            cola.encolar("Dejar a la interperie \npara que aumente \nla temperatura 1(H)")
            label4=Label(frame1,text="-La temperatura esta normal , aunque es un poco baja ",font=("Little Comet Bubling Demo Version",14),bg="white",justify="left")
            label4.place(x=360,y=180)
        elif promedio<45 and promedio>20:
            cola.encolar("Dejar a la interperie \npara que aumente \nla temperatura 15(min)")
            label4=Label(frame1,text="-Deberias revisar las tareas ya que la temperatura esta\ncerca de valores muy bajos",font=("Little Comet Bubling Demo Version",14),bg="white",justify="left")
            label4.place(x=360,y=180)
        elif promedio<65 and promedio>45:
            label4=Label(frame1,text="-La temperatura esta normal , aunque es un poco alta",font=("Little Comet Bubling Demo Version",14),bg="white",justify="left")
            label4.place(x=360,y=180)
            cola.encolar("dejar con algo cubierto \npara reducir un poco la \ntemperatura 1(H)")
        elif promedio<85 and promedio>65:
            label4=Label(frame1,text="-Deberias revisar las tareas ya que la temperatura esta\ncerca de valores muy altos",font=("Little Comet Bubling Demo Version",14),bg="white",justify="left")
            label4.place(x=360,y=180)
            cola.encolar("Dejar con algo cubierto \npara reducir un poco \nla temperatura 15(min)")
        else:
            label4=Label(frame1,text="-Parece que las mediciones de temperatura tienen valores \ncriticos por favor revisa el apartado de contingencias",font=("Little Comet Bubling Demo Version",14),bg="white",justify="left")
            label4.place(x=360,y=180)
            
    def revisaAire():
        humA=ConexionBd.ArrayHumA(data)
        promedio=0
        
        for i in range(len(humA)):
            promedio+=humA[i]
        promedio=promedio/len(humA)
        
        if promedio<50 and promedio>35:
            cola.encolar("Dejar a la interperie \npara que reciba mas \nhumedad 1(H)")
            label4=Label(frame1,text="-La humedad de aire  esta normal , aunque \nes un poco baja ",font=("Little Comet Bubling Demo Version",14),bg="white",justify="left")
            label4.place(x=360,y=230)
        elif promedio<35 and promedio>20:
            cola.encolar("Dejar a la interperie para \nque reciba mas \nhumedad 15(min)")
            label4=Label(frame1,text="-Deberias revisar las tareas ya que la humedad del aire\nesta cerca de valores muy bajos",font=("Little Comet Bubling Demo Version",14),bg="white",justify="left")
            label4.place(x=360,y=230)
        elif promedio<65 and promedio>50:
            label4=Label(frame1,text="-La humedad del aire esta normal , aunque es \nun poco alta",font=("Little Comet Bubling Demo Version",14),bg="white",justify="left")
            label4.place(x=360,y=230)
            cola.encolar("Dejar con algo cubierto \npara reducir un poco \nla humedad 1(H)")
        elif promedio<80 and promedio>65:
            label4=Label(frame1,text="-Deberias revisar las tareas ya que la humedad del aire\nestacerca de valores muy altos",font=("Little Comet Bubling Demo Version",14),bg="white",justify="left")
            label4.place(x=360,y=230)
            cola.encolar("Dejar con algo cubierto \npara reducir un poco \nla humedad 15(min)")
        else:          
            label4=Label(frame1,text="-Parece que las mediciones de humedad \ndel aire tienen valores criticos por favor revisa \nel apartado de contingencias",font=("Little Comet Bubling Demo Version",14),bg="white",justify="left")
            label4.place(x=360,y=230)
            
    def revisaHumedad():
        humS=ConexionBd.ArrayHuS(data)
        promedio=0
        
        for i in range(len(humS)):
            promedio+=humS[i]
        promedio=promedio/len(humS)
        if promedio<700 and promedio>600:
            cola.encolar("Regar en \n aproximadamente \n2 o 4 horas")
            label7=Label(frame1,text="-Deberias revisar las tareas ya que la humedad del suelo \nesta cerca de valores muy bajos",font=("Little Comet Bubling Demo Version",14),bg="white",justify="left")
            label7.place(x=360,y=300)
        elif promedio<800 and promedio>700:
            cola.encolar("Regar el siguiente dia ")
            label7=Label(frame1,text="-La humedad del suelo esta normal , aunque es \nun poco baja ",font=("Little Comet Bubling Demo Version",14),bg="white",justify="left")
            label7.place(x=360,y=300)
        elif promedio<900 and promedio>800:
            label7=Label(frame1,text="-La humedad del suelo esta normal , aunque es \nun poco alta",font=("Little Comet Bubling Demo Version",14),bg="white",justify="left")
            label7.place(x=360,y=300)
            cola.encolar("Dejar la planta bajo el \nsol 1(H)")
        elif promedio<1000 and promedio>900:
            label7=Label(frame1,text="-Deberias revisar las tareas ya que la humedad esta\ncerca de valores muy altos",font=("Little Comet Bubling Demo Version",14),bg="white",justify="left")
            label7.place(x=360,y=300)
            cola.encolar("Drenar un poco el agua\nde la planta")
        else:
            label7=Label(frame1,text="-Parece que las mediciones de humedad del suelo \ntienen valores criticos por favor revisa el \napartado de contingencias",font=("Little Comet Bubling Demo Version",14),bg="white",justify="left")
            label7.place(x=360,y=300)
            
    def revisaLuz():
        li=ConexionBd.ArrayLi(data)
        promedio=0
        for i in range(len(li)):
            promedio+=li[i]
        promedio=promedio/len(li)
        if promedio<0.35 and promedio>0.2:
            cola.encolar("Dejar a la luz 1(H)")
            label9=Label(frame1,text="-Deberias revisar las tareas ya que la luz \nesta cerca de valores muy bajos",font=("Little Comet Bubling Demo Version",14),bg="white",justify="left")
            label9.place(x=360,y=380)
        elif promedio<0.5 and promedio>0.35:
            cola.encolar("Dejar a la luz 15(min)")
            label9=Label(frame1,text="-La luz esta normal , aunque es un poco baja ",font=("Little Comet Bubling Demo Version",14),bg="white",justify="left")
            label9.place(x=360,y=380)
        elif promedio<0.65 and promedio>0.5:
            label9=Label(frame1,text="-La luz normal , aunque es un poco alta",font=("Little Comet Bubling Demo Version",14),bg="white",justify="left")
            label9.place(x=360,y=380)
            cola.encolar("Evitar que le llegue \nluz 15(min)")
        elif promedio<0.8 and promedio>0.65:
            label9=Label(frame1,text="-Deberias revisar las tareas ya que la luz esta\ncerca de valores muy altos",font=("Little Comet Bubling Demo Version",14),bg="white",justify="left")
            label9.place(x=360,y=380)
            cola.encolar("Evitar que le llegue \nluz 1(H)")
        else:
            label9=Label(frame1,text="-Parece que las mediciones de luz tienen valores \ncriticos por favor revisa el apartado de contingencias",font=("Little Comet Bubling Demo Version",14),bg="white",justify="left")
            label9.place(x=360,y=380)
    
    def imprimeTareas():
        particiones=cola.size
        largo=261
        ancho=140
        if particiones>=1:
            string1=str(cola.desencolar())
            frame2=Frame(bg="#3DD6FE")
            frame2.place(x=800,y=435,width=ancho-5,height=(int(largo/4)-5))
            label5=Label(frame2,text=string1,font=("Little Comet Bubling Demo Version",11),bg="#3DD6FE",justify="left")
            label5.place(x=0,y=0)
        if particiones>=2:
            string2=str(cola.desencolar())
            frame3=Frame(bg="#3DD6FE")
            frame3.place(x=800,y=370,width=ancho-5,height=(int(largo/4)-5))
            label6=Label(frame3,text=string2,font=("Little Comet Bubling Demo Version",11),bg="#3DD6FE",justify="left")
            label6.place(x=0,y=0)
        if particiones>=3:
            string2=str(cola.desencolar())
            frame4=Frame(bg="#3DD6FE")
            frame4.place(x=800,y=305,width=ancho-5,height=(int(largo/4)-5))
            label8=Label(frame4,text=string2,font=("Little Comet Bubling Demo Version",11),bg="#3DD6FE",justify="left")
            label8.place(x=0,y=0)
        if particiones>=4:
            string2=str(cola.desencolar())
            frame5=Frame(bg="#3DD6FE")
            frame5.place(x=800,y=240,width=ancho-5,height=(int(largo/4)-5))
            label10=Label(frame5,text=string2,font=("Little Comet Bubling Demo Version",11),bg="#3DD6FE",justify="left")
            label10.place(x=0,y=0)
    
    revisaHumedad()
    revisaAire()
    revisaTemperatura()
    revisaLuz()
    imprimeTareas()
    
    
def menu3():  
    stringSelecion=""
    inicio.geometry("1000x640")
    frame1=Frame(bg="white")
    frame1.place(x=0,y=0,width=1000,height=640)
    
    
    label2=Label(frame1,text="Estadisticas",font=("Little Comet Bubling Demo Version",42),bg="white")
    label2.place(x=360,y=10)
    
    label3=Label(frame1,text="A continuacion podra consultar varias estadisticas , \nsobre su cultivo o planta",font=("Little Comet Bubling Demo Version",24),bg="white",justify="left")
    label3.place(x=360,y=70)
    
    selecion=Listbox(frame1,width=25,height=5,font=("Little Comet Bubling Demo Version",18))
    selecion.place(x=360,y=200)
    selecion.insert(END,"Temperetura")
    selecion.insert(END,"Humedad Aire")
    selecion.insert(END,"Humedad Suelo")
    selecion.insert(END,"Luz")
    
    label4=Label(frame1,text="Medidas de tendencia central de : "+stringSelecion,font=("Little Comet Bubling Demo Version",16),bg="white",justify="left")
    label4.place(x=360,y=420)
    
    img=PhotoImage(file="Imagenes/Fondo2.png")
    img_label=Label(image=img)
    img_label.image= img
    img_label.place(x=-10,y=-10)

    def grapichs():
        id1=ConexionBd.ArrayId(data)
        string1=selecion.get(ANCHOR)
        if(string1=="Temperetura"):
            temp=ConexionBd.ArrayTem(data)
            plt.plot(id1,temp)
            plt.xlabel("Numero de medicion")
            plt.ylabel("Temperatura en Cº")
            plt.title("Grafica de temperatura ")
            plt.show()
        elif(string1=="Humedad Aire"):
            humA=ConexionBd.ArrayHumA(data)
            plt.plot(id1,humA)
            plt.xlabel("Numero de medicion")
            plt.ylabel("Humedad del aire")
            plt.title("Grafica de Humedad del aire")
            plt.show()
        elif(string1=="Humedad Suelo"):
            humS=ConexionBd.ArrayHuS(data)
            plt.plot(id1,humS)
            plt.xlabel("Numero de medicion")
            plt.ylabel("Humedad del Suelo")
            plt.title("Grafica de Humedad del Suelo ")
            plt.show()
        elif(string1=="Luz"):
            lig=ConexionBd.ArrayLi(data)
            plt.plot(id1,lig)
            plt.xlabel("Numero de medicion")
            plt.ylabel("Kuz")
            plt.title("Grafica de la luz ")
            plt.show()
        else:
            messagebox.showinfo("Error","No has selecionado ninguna opcion")
    
    def tendencias():
        string1=selecion.get(ANCHOR)
        tree=searchBinaryTree.arbol_busqueda()
        if(string1=="Temperetura"):
            temp=ConexionBd.ArrayTem(data)
            tree=searchBinaryTree.inserta_array(tree,temp)
            minvalue=str(tree.searchMin())
            maxvalue=str(tree.searchMax())
            mediana=str(searchBinaryTree.calculaMediana(tree))
            promedio=str(searchBinaryTree.calculaPromedio(tree))
            label4=Label(frame1,text=("Medidas de tendencia central de la temperatura :\n\nMedida mas baja: "+minvalue+"\nMedida mas alta: "+maxvalue+"\nMediana de las mediciones : "+mediana+"\nPromedio de las mediciones :"+promedio),font=("Little Comet Bubling Demo Version",16),bg="white",justify="left")
            label4.place(x=360,y=420)
        elif(string1=="Humedad Aire"):
            humA=ConexionBd.ArrayHumA(data)
            tree=searchBinaryTree.inserta_array(tree,humA)
            minvalue=str(tree.searchMin())
            maxvalue=str(tree.searchMax())
            mediana=str(searchBinaryTree.calculaMediana(tree))
            promedio=str(searchBinaryTree.calculaPromedio(tree))
            label4=Label(frame1,text=("Medidas de tendencia central de la Humedad del aire :\n\nMedida mas baja: "+minvalue+"\nMedida mas alta: "+maxvalue+"\nMediana de las mediciones : "+mediana+"\nPromedio de las mediciones :"+promedio),font=("Little Comet Bubling Demo Version",16),bg="white",justify="left")
            label4.place(x=360,y=420)
        elif(string1=="Humedad Suelo"):
            humS=ConexionBd.ArrayHuS(data)
            tree=searchBinaryTree.inserta_array(tree,humS)
            minvalue=str(tree.searchMin())
            maxvalue=str(tree.searchMax())
            mediana=str(searchBinaryTree.calculaMediana(tree))
            promedio=str(searchBinaryTree.calculaPromedio(tree))
            label4=Label(frame1,text=("Medidas de tendencia central de la Humedad del aire :\n\nMedida mas baja: "+minvalue+"\nMedida mas alta: "+maxvalue+"\nMediana de las mediciones : "+mediana+"\nPromedio de las mediciones :"+promedio),font=("Little Comet Bubling Demo Version",16),bg="white",justify="left")
            label4.place(x=360,y=420)
        elif(string1=="Luz"):
            lig=ConexionBd.ArrayLi(data)
            tree=searchBinaryTree.inserta_array(tree,lig)
            minvalue=str(tree.searchMin())
            maxvalue=str(tree.searchMax())
            mediana=str(searchBinaryTree.calculaMediana(tree))
            promedio=str(searchBinaryTree.calculaPromedio(tree))
            label4=Label(frame1,text=("Medidas de tendencia central de la Humedad del aire :\n\nMedida mas baja: "+minvalue+"\nMedida mas alta: "+maxvalue+"\nMediana de las mediciones : "+mediana+"\nPromedio de las mediciones :"+promedio),font=("Little Comet Bubling Demo Version",16),bg="white",justify="left")
            label4.place(x=360,y=420)
        else:
            messagebox.showinfo("Error","No has selecionado ninguna opcion")
    
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
    
    button_5=PhotoImage(file='Imagenes/boton3_1.png')
    button5=Button(inicio,image=button_5,command=tendencias,borderwidth=0)
    button5.image=button_5
    button5.place(x=650,y=150)
    
    button_6=PhotoImage(file='Imagenes/boton3_2.png')
    button6=Button(inicio,image=button_6,command=grapichs,borderwidth=0)
    button6.image=button_6
    button6.place(x=650,y=260)
    
def menu2():
    inicio.geometry("1000x640")
    frame1=Frame(bg="white")
    frame1.place(x=0,y=0,width=1000,height=640)
    
    
    label2=Label(frame1,text="Inicio",font=("Little Comet Bubling Demo Version",42),bg="white")
    label2.place(x=360,y=10)
    
    label3=Label(frame1,text="Bienvenido"+" "+Usuario ,font=("Little Comet Bubling Demo Version",24),bg="white")
    label3.place(x=360,y=70)
    
    img=PhotoImage(file="Imagenes/Fondo2.png")
    img_label=Label(image=img)
    img_label.image= img
    img_label.place(x=-10,y=-10)
    
    img2=PhotoImage(file="Imagenes/inicio_1.png")
    img2_label=Label(image=img2)
    img2_label.image= img2
    img2_label.place(x=365,y=115)
    
    img3=PhotoImage(file="Imagenes/inicio_2.png")
    img3_label=Label(image=img3)
    img3_label.image= img3
    img3_label.place(x=365,y=350)
    
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
        if str(Hash[string1])==string2 and string1!="" and string2!="":
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
        if Hash[string1] == None and string2 == string3 and string1!="" and string2!="" :
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