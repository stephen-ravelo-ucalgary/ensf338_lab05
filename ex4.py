class ArrayQueue:
    def __init__(self, capacity):
        self.capacity = capacity
        self.queue = [None] * capacity
        self.head = -1
        self.tail = -1
        
    def isEmpty(self):
        return (self.head == -1)
    
    def isFull(self):
        return (((self.tail + 1) % self.capacity) == self.head)
    
    def enqueue(self, item):
        if(self.isFull()):
            print("Queue is full, unable to enqueue item.")
            return
        elif(self.isEmpty()):
            self.head = 0
            self.tail = 0
        else:
            self.tail = (self.tail + 1) % self.capacity
        self.queue[self.tail] = item
        
    def dequeue(self):
        if(self.isEmpty()):
            print("Queue is empty, unable to dequeue item.")
            return None
        
        item = self.queue[self.head]
        
        if(self.head == self.tail):
            self.head = -1
            self.tail = -1
        else:
            self.head = (self.head + 1) % self.capacity
        
        return item

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class linkedListQueue:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def isEmpty(self):
        return (self.head is None)
    
    def enqueue(self, item):
        newNode = Node(item)
        
        if (self.isEmpty()):
            self.head = newNode
            self.tail = newNode
        else:
            newNode.next = self.head
            self.head = newNode
    
    def dequeue(self):
        if(self.isEmpty()):
            print("Queue is empty, unable to dequeue")
            return None
        
        if(self.head == self.tail):
            item = self.tail.value
            self.head = None
            self.tail = None
            return item
        
        current = self.head
        while(current.next != self.tail):
            current = current.next
        
        item = self.tail.value
        current.next = None
        self.tail = current
        return item

def genList():
    

if __name__ == "__main__":
    