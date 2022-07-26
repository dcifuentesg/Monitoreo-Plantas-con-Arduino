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