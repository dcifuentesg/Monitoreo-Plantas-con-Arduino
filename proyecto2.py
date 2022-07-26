from operator import contains
import time

class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None
    def getDato(self):
        return self.dato
class Pila:
    def __init__(self):
        self.superior = None
        self.size = 0
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
        for i in range(len(self)):
            st += str(cur)
            if i != len(self) - 1:
                st += str(", ")
            cur = cur.next
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
    def retornarValor(self):
        if self.superior == None:
            print("No hay ningún elemento en la pila para desapilar")
            return
        return self.superior.dato
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

#los datos de entrada tienen el siguiente orden:
# 1-Numero de la medicion el cual actuaria como un tipo de hora de la medicion 
# 2-Numero de huerta
# 3-temperatura general promedio 
# 4-Humedad del aire general promedio
# 5-luz promedio
# 6-Humedad de la tierra
# Por cada medicion se tiene que recibir un unico dato de : hora o numero representativo , temperatura , humedad
# Por cada medicion se tiene que recibir los datos de cada cuadrilla
# Es decir que cada cuadrilla se debe recicibir su humedad
global contador

#Si se hacen lecturas cada 10 min serian 144 lecturas en un dia
dato1=(1,1,-49,122,34,(716,728,735,758,754,751,734,761,724,784))
dato2=(2,1,152,122,35,(716,728,735,758,754,751,734,761,724,784))
dato3=(3,1,158,119,37,(716,728,735,758,754,751,734,761,724,784))
dato4=(4,1,159,119,37,(716,728,735,758,754,751,734,761,724,784))
dato5=(5,1,160,117,36,(716,728,735,758,754,751,734,761,724,784))
Datos=(dato1,dato2,dato3,dato4,dato5)
#Si se hacen lecturas cada 10 min serian 144 lecturas en un dia
def lectura(Datos):
    contador=1
    while contador<=5:
        if Datos[contador-1][0]!=contador:
            print("La ultima medicion requerida no a sido entregada")
        else:
            pilaContingencias=Pila()
            humedadcuadrillas=Datos[contador-1][5]
            if(compruebahumedad(humedadcuadrillas)):
                colaRegar=cola()
                colaRegar=creaColaRegar(Datos[contador-1],len(Datos[contador-1]))
                pilaContingencias.apilar(colaRegar)
            temperatura=Datos[contador-1][2]
            if(comprueba_temperatura(temperatura,contador)):
                pilaContingencias.apilar("Temperatura")
            valor=pilaContingencias.desapilar
            print(valor)
            if(pilaContingencias.size!=0):
                Contingencia(Pila)
        contador+=1
            

def comprueba_temperatura(temperatura,contador):
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
    
def compruebahumedad(Datos):
    i=0
    numeroDatos=len(Datos)
    suma=0
    while(i<numeroDatos):
        """
            Sacaremos el promedio de humedad de todas las mediciones de humedad del suelo 
            la cual nos permitira decidir si es necesario el proximo rriego 
            
            teniendo en cuenta que en la escala del sensor utilizado 1023 es 0 porciento humedo 
            y 0 es 100 porciento humedo
        """
        suma+=Datos[i]
        i+=1
    suma=suma/numeroDatos
    i=0
    while(i<numeroDatos):
        """
            Ademas se verificara que ninguno de los valores se encuentre en valores extremos
            asumiremos que la humedad del suelo no debe sobrepasar un 30 porciento de humedad ni
            debe estar por debajo de un 5 porciento de la humedad , ademas para poder definir si
            la medicion de una cuadrilla es realmente un valor critico teine que estar desviado un 
            10 porciento del promedio aritmetico de todas las mediociones
        """
        if((Datos[i]>972 or Datos[i]<716) and (abs(Datos[i]-suma)>10)):
            Contingencia()
        i+=1
    if(suma>972):
        return True
    else : 
        return False
def creaColaRegar(Datos,numeroDatos):
    miCola = cola()
    arregloaux1=sorted(Datos)
    i=0
    while(i<numeroDatos):
        j=0
        while(j<numeroDatos):
            if(Datos[j]==arregloaux1[i]):
                miCola.encolar(j)
            j+=1
        i+=1
def Contingencia(pilacontingecias):
    valor=pilacontingecias.desapilar
    if((type(valor).__name__)==cola):
        print("se tienen que regar las parcelas en el siguiente orden"+cola.__str__)
    else:
        print(valor)

lectura(Datos)