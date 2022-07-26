import requests
import random
def data():
    r=requests.get("http://proyectoalcoholimetrohost.000webhostapp.com/RequiereDatos.php")
    respuesta=str(r.text)
    stringaux=""
    final_array=[]
    aux_array=[]
    for i in range(len(respuesta)):
        if(respuesta[i]!="," and respuesta[i]!=";"):
            stringaux+=respuesta[i]
        elif(respuesta[i]==","):
            aux_array.append(float(stringaux))
            stringaux=""   
        elif(respuesta[i]==";"):
            aux_array.append(float(stringaux))
            final_array.append(aux_array)
            aux_array=[]
            stringaux="" 
    return final_array
def ArrayId(array):
    array_aux=[]
    for i in range(len(array)):
        array_aux.append(array[i][0])
    return array_aux

def ArrayTem(array):
    array_aux=[]
    for i in range(len(array)):
        array_aux.append(array[i][1])
    return array_aux

def ArrayHumA(array):
    array_aux=[]
    for i in range(len(array)):
        array_aux.append(array[i][2])
    return array_aux

def ArrayHuS(array):
    array_aux=[]
    for i in range(len(array)):
        array_aux.append(array[i][3])
    return array_aux

def ArrayLi(array):
    array_aux=[]
    for i in range(len(array)):
        array_aux.append(array[i][4])
    return array_aux
def random_data():
    Datos=[]
    lista = random.choices(range(10,30), k=200)
    lista2 =random.choices(range(25,50), k=200)
    lista3 = random.choices(range(700,1024), k=200)
    lista4 =random.choices(range(0,2), k=200)
    datos_aux=[]
    for i in range(200):
        datos_aux.append(i+1)
        datos_aux.append(lista[i])
        datos_aux.append(lista2[i])
        datos_aux.append(lista3[i])
        datos_aux.append(lista4[i])
        Datos.append(datos_aux)
        datos_aux=[]
    return Datos


