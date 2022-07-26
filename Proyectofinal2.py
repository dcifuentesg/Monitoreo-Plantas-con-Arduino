import interfazGrafica
import ConexionBd
from Estructuras import Pila
from Estructuras import Lista
from Estructuras import Cola
from Estructuras import searchBinaryTree
from Estructuras import Grafo


data=ConexionBd.data()
temp=ConexionBd.ArrayTem(data)
humS=ConexionBd.ArrayHuS(data)
humA=ConexionBd.ArrayHumA(data)
lig=ConexionBd.ArrayLi(data)


def agregaTemperatura(tree,array):
    for i in range(len(array)):
        tree.insert(array[i])
    return tree
tree=searchBinaryTree.arbol_busqueda()
tree=agregaTemperatura(tree,temp)
print(temp)
print(tree.searchMax())
print(tree.searchMin())

conexiones = [
    (data[0][0],data[1][0]),(data[0][0],data[3][0]),
    (data[1][0],data[0][0]),(data[1][0],data[2][0]),(data[1][0],data[1][4]),
    (data[2][0],data[1][0]),(data[2][0],data[5][0]),
    (data[3][0],data[0][0]),(data[3][0],data[4][0]),(data[3][0],data[6][0]),
    (data[4][0],data[1][0]),(data[4][0],data[3][0]),(data[4][0],data[5][0]),(data[4][0],data[7][0]),
    (data[5][0],data[2][0]),(data[5][0],data[4][0]),(data[5][0],data[8][0]),
    (data[6][0],data[3][0]),(data[6][0],data[7][0]),
    (data[7][0],data[6][0]),(data[7][0],data[8][0]),
    (data[8][0],data[5][0]),(data[8][0],data[7][0])
]