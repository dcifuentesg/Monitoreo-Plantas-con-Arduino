from tkinter.tix import Tree

class node:
    def __init__(self,value=None):
        self.value=value
        self.left_child=None
        self.right_child=None
    
class arbol_busqueda:
    def __init__(self):
        self.root=None
        self.size=0
        
    def insert(self,value):
        if self.root==None:
            self.root=node(value)
        else :
            self._insert(value,self.root)
        self.size+=1
    def _insert(self,value,current):
        if value<current.value:
            if current.left_child==None:
                current.left_child=node(value)
            else:
                self._insert(value,current.left_child)
        else:
            if current.right_child==None:
                current.right_child=node(value)
            else:
                self._insert(value,current.right_child)
    def searchMax(self):
        if self.root==None:
            return -1
        current=self.root
        while(current.right_child!=None):
            current=current.right_child
        return current.value
    def searchMin(self):
        if self.root==None:
            return -1
        current=self.root
        while(current.left_child!=None):
            current=current.left_child
        return current.value

def inserta_array(tree,array):
    for i in range(len(array)):
        tree.insert(array[i])
    return tree   
def inorder1(tree):
    array=[]
    array=inorder2(tree.root,array)
    return array  
def inorder2(current,array):
    if(current!=None):
        inorder2(current.left_child,array)
        array.append(current.value)
        inorder2(current.right_child,array)
    return array
def calculaMediana(tree):
    numero_dato=((tree.size)+1)/2
    arrayinorder=inorder1(tree)
    if(((tree.size)+1)%2==0):
        return arrayinorder[int(numero_dato)]
    else:
        return (arrayinorder[int(numero_dato-0.5)]+arrayinorder[int(numero_dato+0.5)])/2
def calculaPromedio(tree):
    arrayinorder=inorder1(tree)
    suma=0
    for i in range(len(arrayinorder)):
        suma+=arrayinorder[i]
    return (suma/len(arrayinorder))