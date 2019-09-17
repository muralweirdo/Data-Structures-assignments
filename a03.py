class Node:
    def __init__(self,val = None):
        self.val = val
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        
    def __str__(self):
        fin = "["
        temp = self.head
        while temp:
            fin = fin + str(temp.val) + ", "
            temp = temp.next
        #print("ha")
        fin = fin.rstrip(", ")
        fin = fin + "]"
        return fin
    
    def push(self, val):
        new_node = Node(val)
        
        if self.head is None:
            self.head = new_node
            return
        
        last = self.head
        while last.next is not None:
            last = last.next
            
        last.next = new_node
    
    def pop(self):
        if self.head is None:
            return "cannot pop"
        if self.head.next is None:
            val = self.head.val
            self.head = None
            return val
    
        temp = self.head
        while temp.next is not None:
            prev = temp
            temp = temp.next
        
        val = temp.val
        prev.next = None
        return val

    def insert(self, index, val):
        new_node = Node(val)
    
        if index == 0:
            new_node.next = self.head
            self.head = new_node
            return
    
        temp = self.head
        counter = 0
        if self.head == None:
            return "cant insert"
        while temp is not None and counter < index:
            prev = temp
            temp = temp.next
            counter = counter +1
        
        prev.next = new_node
        new_node.next = temp
    
    def remove(self, val):
        temp = self.head
    
        if temp is not None:
            if temp.val == val:
                self.head = temp.next
                temp = None
                return
        try:
            while temp is not None:
                if temp.val == val:
                    break
        
                prev = temp
                temp = temp.next
        
            prev.next = temp.next
        except:
            print ("val noot found")
            return
        
    def get(self, index):
        temp = self.head
        
        if index == 0:
            return temp.val
    
        counter = 0
        try:
            while temp is not None and counter < index:
                prev = temp
                temp = temp.next
                counter = counter + 1
            return temp.val
        
        except:
            raise IndexError("IndexError: Index out of bound")
            #print ("IndexError: Index out of bound")
            return
    
    def len(self):
        temp = self.head
        count = 0
    
        while temp:
            count = count + 1
            temp = temp.next
        return count

    
if __name__ == "__main__": 
    l = LinkedList() 
    l.push(5) 
    l.push(6) 

    print(l)

    print(l.len())

    l.pop() 
    print(l.len())

    print(l.get(0))
    l.get(2) # Should say "IndexError: Index out of bound"

