import ConexionBd
from Estructuras import Pila
from Estructuras import Lista
from Estructuras import Cola
from Estructuras import searchBinaryTree


data=ConexionBd.random_data()

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