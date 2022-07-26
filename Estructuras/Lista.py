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
            