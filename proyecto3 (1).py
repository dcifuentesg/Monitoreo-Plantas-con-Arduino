import time
from math import *
import random
from xmlrpc.server import *
start = time.time()


class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None
    def __str__(self):
        return str(self.dato)
class Pila:
    def __init__(self):
        self.superior = None
        self.size = 0
    def __len__(self):
        return self.size
    def apilar(self, dato):
        if self.superior == None:
            self.superior = Nodo(dato)
            self.size+=1
            return
        nuevo_nodo = Nodo(dato)
        nuevo_nodo.siguiente = self.superior
        self.superior = nuevo_nodo
        self.size+=1
    def __str__(self):
        st = "["
        cur = self.superior
        for i in range(self.size):
            st += str(cur)
            if i != len(self) - 1:
                st += str(", ")
            cur = cur.siguiente
        st += "]"
        return st
    def desapilar(self):
        a = 0
        if self.superior == None:
            return print("No hay ningún elemento en la pila para desapilar")
        a = self.superior.dato
        self.superior = self.superior.siguiente
        self.size-=1
        return a 
    def get(self,index):
        if index >= self.size:
            return None
        cur_id = 0
        curNode = self.superior
        while True:
            if cur_id == index: return curNode.dato
            curNode = curNode.siguiente
            cur_id += 1
    def actualizar(self,index,valor):
        if index >= self.size:
            return None
        cur_id = 0
        curNode = self.superior
        while True:
            if cur_id == index: 
                curNode.dato= valor 
                return
            curNode = curNode.siguiente
            cur_id += 1
class nodeCola:
    def __init__(self,Value):
        self.Value = Value
        self.next = None
    def __str__(self):
        return str(self.Value)  
class cola:
    def __init__(self):
        self.First = None
        self.Last = None
        self.size = 0
    def __len__(self):
        return self.size
    def encolar(self,x):
        nuevoNodo = nodeCola(x)
        if self.Last:
            self.Last.next = nuevoNodo
            self.Last = nuevoNodo
        else:
            self.First  = nuevoNodo
            self.Last = nuevoNodo
        self.size += 1
    def __str__(self):
        st = "["
        cur = self.First
        for i in range(len(self)):
            st += str(cur)
            if i != len(self) - 1:
                st += str(", ")
            cur = cur.next
        st += "]"
        return st
    def desencolar(self):
        if self.First != None:
            valor = self.First.Value
            self.First = self.First.next
            self.size -=1
            if self.First == None:
                self.Last = None    
            return valor 
        else:     
            raise ValueError("La cola está vacía")
    def get(self,index):
        if index >= self.size:
            return None
        cur_id = 0
        curNode = self.First
        while True:
            if cur_id == index: return curNode.Value
            curNode = curNode.next
            cur_id += 1
    def actualizar(self,index,valor):
        if index >= self.size:
            return None
        cur_id = 0
        curNode = self.First
        while True:
            if cur_id == index: 
                curNode.Value= valor 
                return
            curNode = curNode.next
            cur_id += 1
class node:
    def __init__(self,Value):
        self.Value = Value
        self.next = None
    def __str__(self):
        return str(self.Value)
class linkedList:
    def __init__(self):
        self.first = None
        self.size = 0
    def append(self, value):
        miNode = node(value)
        if self.size == 0:
            self.first =miNode
        else:
            cur = self.first
            while cur.next != None:
                cur = cur.next
            cur.next = miNode
        self.size += 1
        return miNode
    def __len__(self):
        return self.size
    def __str__(self):
        st = "["
        cur = self.first
        for i in range(len(self)):
            st += str(cur)
            if i != len(self) - 1:
                st += str(", ")
            cur = cur.next
        st += "]"
        return st
    def get(self,index):
        if index >= self.size:
            return None
        cur_id = 0
        curNode = self.first
        while True:
            if cur_id == index: return curNode.Value
            curNode = curNode.next
            cur_id += 1
            
#los datos de entrada AHORA tienen el siguiente orden:  
# 1. id
# 2. temperatura
# 3. húmedad aire
# 4. humedad suelo 
# 5. luz
#------------------orden anterior-----------------
# no1-Numero de la medicion el cual actuaria como un tipo de hora de la medicion 
# no2-Numero de huerta
# 3-temperatura general promedio 
# 4-Humedad del aire general promedio
# 5-luz promedio
# 6-Humedad de la tierra
# Por cada medicion se tiene que recibir un unico dato de : hora o numero representativo , temperatura , humedad
# Por cada medicion se tiene que recibir los datos de cada cuadrilla
# Es decir que cada cuadrilla se debe recicibir su humedad

#Si se hacen lecturas cada 10 min serian 144 lecturas en un dia
pilaContingencias=Pila()
def lectura(Datos,pilaContingencias):
    contador=1
    while contador<=5:
        if Datos[contador-1][0]!=contador:
            print("La ultima medicion requerida no a sido entregada")
        else:
            humedad=Datos[contador-1][3]
            start1 = time.time()

            numero1=compruebahumedad(humedad)
            print("el tiempo usado por la funcion comprueba humedad es: ")
            end1 = time.time()
            print(end1 - start1)
            if(numero1==1):
                pilaContingencias.apilar("Regar")
            elif(numero1!=1 and numero1!=-1):
                colaRegar= cola()
                colaRegar= crearColaRegar(Datos[contador-1][3],1,numero1)
                pilaContingencias.apilar(colaRegar)
            temperatura=Datos[contador-1][1]
            if(comprueba_temperatura(temperatura,contador)):
                pilaContingencias.apilar("Temperatura")
            if(pilaContingencias.size!=0):
                Contingencia(pilaContingencias)
        contador+=1
            

def comprueba_temperatura(temperatura,contador):
    print("temp comprobandose",temperatura)
    """
        La temperatura esperada depende de la hora de medicion 
        Primeramente se tendra en cuenta que no supere valores extremos
        los valores extremos seran considerados como 0 grados y 30 grados celcius
        Luego verificara que los valores esten entre los valores esperadose por cada hora
    """
    if(temperatura<0 or temperatura>300):
        return True
    else:
        #Entre las 6 de la tarde y las 6 de la mañana se espera que temperatura no baje de 5 grados
        if((contador<36 or contador>108) and temperatura<50):
            return True
        #Entre las 6am-9am y 3pm-6pm se espera que la temperatura no sea menor a 5 grados y que no sea mayor a 15 grados
        elif(((contador>=36 and contador<=54) or (contador>=90 and contador<=18)) and (temperatura<50 or temperatura>150)):
            return True
        elif((contador>54 and contador<90) and temperatura<250):
            return True
        return False

def compruebahumedad(humedad):
    print("humedad comprandose",humedad)
    if humedad>972:
        return 0
        """
            teniendo en cuenta que en la escala del sensor utilizado 1023 es 0 porciento humedo 
            y 0 es 100 porciento humedo
        """
   
        """
            se verificara que ninguno de los valores se encuentre en valores extremos
            asumiremos que la humedad del suelo no debe sobrepasar un 30 porciento de humedad ni
            debe estar por debajo de un 5 porciento de la humedad , ademas para poder definir si
            la medicion de una cuadrilla es realmente un valor critico teine que estar desviado un 
            10 porciento del promedio aritmetico de todas las mediociones
        """
    if((humedad>972 or humedad<716) and (abs(humedad)>51)):
        return humedad
    else: 
        return -1

def crearColaRegar(Datos,numeroDatos,suma): 
    miCola = cola()
    i=0
    while(i<numeroDatos):
        if(abs(Datos-suma)>51):
            miCola.encolar(i)
        i+=1
    return miCola

def Contingencia(pilacontingecias):
    pila=Pila()
    pila=pilacontingecias
    hd=pila.desapilar()
    print(hd.size)

lista = random.choices(range(1023), k=20)
lista2 =random.choices(range(1023), k=20)
lista3 = random.choices(range(1023), k=20)
lista4 =random.choices(range(1023), k=20)
lista5 = random.choices(range(1023), k=20)

dato1=[1,1,150,125,34,lista]
dato2=[2,1,152,122,35,lista2]
dato3=[3,1,158,119,37,lista3]
dato4=[4,1,159,119,37,lista4]
dato5=[5,1,160,117,36,lista5]
#antes:hora, huerta, temperatura, humedad aire, luz, humedad tierra,
#nuevo:id, temperatura, húmedad aire, humedad suelo, luz
data1= [1,150,125,130,34]
data2= [2,152,122,115,35]
data3= [3,158,119,120,37]
data4= [4,159,119,135,37]
data5= [5,160,117,111,36]


#Datos=[dato1,dato2,dato3,dato4,dato5]
#lectura(Datos,pilaContingencias)
datos = [data1,data2,data3,data4,data5]
lectura(datos,pilaContingencias)
print("The time used to execute this is given below")
end = time.time()
print(end - start)