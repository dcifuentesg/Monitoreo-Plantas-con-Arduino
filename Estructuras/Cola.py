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