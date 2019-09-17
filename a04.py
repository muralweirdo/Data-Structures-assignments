class Node:
    def __init__(self,val = None):
        self.val = val
        self.next = None

class Ring:
    def __init__(self):
        self.head = None
        
    def __str__(self):
        fin = "["
        temp = self.head
        while temp is not None:
            fin = fin + str(temp.val) + ", "
            temp = temp.next
            if temp == self.head:
                break
                
        fin = fin.rstrip(", ")
        fin = fin + "]"
        return fin

def _get_last(self):
    if self.head is None:
        return None
    temp = self.head.next
    while temp.next != self.head:
        temp = temp.next
    return temp

Ring._get_last = _get_last

def insert(self,index,val):
    new_node = Node(val)
    last = self._get_last()
    
    if index == 0:
        new_node.next = self.head
        self.head = new_node
        
        if last is None:
            self.head.next = self.head
        else:
            last.next = new_node   
        return
    
    if self.head is None:
        raise IndexError("Cannot insert at " + str(index) + " because list is empty.")
    
    temp = self.head
    
    counter = 0
    while temp is not None and counter < index:
        prev = temp
        temp = temp.next
        counter = counter + 1
    prev.next = new_node
    new_node.next = temp
    
Ring.insert = insert  

def remove(self,val):
    if self.head is None:
        return
    temp = self.head
    last = self._get_last()
    
    if temp.val == val:
        if last == self.head:
            self.head = None
        else:
            self.head = temp.next
            last.next = self.head
        return
    
    prev = temp
    temp = temp.next
    while temp != self.head:
        if temp.val == val:
            break
        prev = temp
        temp = temp.next
    if temp == self.head:
        return
    prev.next = temp.next
    
Ring.remove = remove

def pop(self):
    
    last = self._get_last()
    self.remove(last.val)
    return(last.val)
    
Ring.pop = pop

def push(self, val):
        new_node = Node(val)
        last = self._get_last()
        if self.head is None:
            self.head = new_node
            self.head.next = self.head
            return
        last.next = new_node
        last.next.next = self.head

Ring.push = push

def len(self):
    temp = self.head
    count = 0
    
    if temp is None:
        return count
    count = count + 1
    while temp.next != self.head:
        count = count + 1
        temp = temp.next
    return count

Ring.len = len

def get(self, index):
    temp = self.head
    if self.head is None:
        raise IndexError("index out of bound")
        return
    if index == 0:
        return self.head.val
    
    counter = 0
    while counter < index:
        prev = temp
        temp = temp.next
        counter = counter + 1
        
    return temp.val

Ring.get = get

def remove_at(self,index):
    last = self._get_last()
    temp = self.head
    
    if self.head is None:
        return ("cant remove, list empty")
    
    if index == 0:
        if last == self.head:
            self.head = None
        else:
            self.head = temp.next
            last.next = self.head
        return
    
    counter = 0
    while temp.next != self.head and counter < index:
        prev = temp
        temp = temp.next
        counter = counter + 1
    prev.next = temp.next
    
Ring.remove_at = remove_at

if __name__ == '__main__': 
    r = Ring()
    # r.insert(1, 1)
    r.insert(0, 1)
    r.insert(0, 2)
    r.insert(1, 3)
    r.insert(7, 5)  # different behavrior since it's a ring! 
    print(r)
