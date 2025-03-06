class CircularArrQueue:
    def __init__(self, capacity):
        self.capacity = capacity
        self.queue = [None] * capacity
        self.head = -1
        self.tail = -1
        
    def isEmpty(self):
        return (self.head == -1)
    
    def isFull(self):
        if(self.isEmpty()):
            return False
        
        return (((self.head - 1) % self.capacity) == self.tail)
    
    def enqueue(self, item):
        if(self.isFull()):
            print("enqueue None")
            return
        
        if(self.isEmpty()):
            self.head = 0
            self.tail = 0
        else:
            self.head = (self.head - 1) % self.capacity
        
        self.queue[self.head] = item
        print(f"enqueue {item}")
    
    def dequeue(self):
        if (self.isEmpty()):
            print("dequeue None")
            return None
        
        item = self.queue[self.tail]
        if (self.head == self.tail):
            self.head = -1
            self.tail = -1
        else:
            self.tail = ((self.tail - 1) % self.capacity)
        
        print(f"dequeue {item}")
        return item
    
    def peek(self):
        if (self.isEmpty()):
            print("peek None")
            return None

        item = self.queue[self.tail]
        print(f"peek {item}")
        return item

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        
class CircularLlQueue:
    def __init__(self, capacity):
        self.capacity = capacity
        self.size = 0
        self.tail = None
    
    def isEmpty(self):
        return(self.size == 0)
    
    def isFull(self):
        return (self.size == self.capacity)
    
    def enqueue(self, item):
        if (self.isFull()):
            print("enqueue None")
            return

        newNode = Node(item)
        
        if (self.isEmpty()):
            newNode.next = newNode
            self.tail = newNode
            
        else:
            newNode.next = self.tail.next
            self.tail.next = newNode
            self.tail = newNode
            
        self.size += 1
        print(f"enqueue {item}")
    
    def dequeue(self):
        if (self.isEmpty()):
            print("dequeue None")
            return None
        
        head = self.tail.next
        item = head.value
        
        if(self.size == 1):
            self.tail = None
        
        else:
            self.tail.next = head.next
        
        self.size -= 1
        print(f"dequeue {item}")
        return item
    
    def peek(self):
        if(self.isEmpty()):
            print("peek None")
            return None
        
        head = self.tail.next
        item = head.value
        
        print(f"peek {item}")
        return item

def test(queue):
    queue.peek()
    queue.dequeue()
    queue.enqueue(1)
    queue.peek()
    queue.enqueue(2)
    queue.enqueue(3)
    queue.enqueue(4)
    queue.enqueue(5)
    queue.enqueue(6)
    queue.peek()
    queue.dequeue()
    queue.dequeue()
    queue.peek()
    queue.enqueue(7)
    queue.enqueue(8)
    queue.enqueue(9)
    queue.peek()
    queue.dequeue()
    queue.dequeue()
    queue.dequeue()
    queue.dequeue()
    queue.peek()
    queue.enqueue(10)
    queue.enqueue(11)
    queue.enqueue(12)
    queue.enqueue(13)
    queue.enqueue(14)
    queue.peek()
    queue.enqueue(15)
    queue.dequeue()
    queue.dequeue()
    queue.peek()
    queue.enqueue(16)
    queue.enqueue(17)
    queue.dequeue()
    queue.dequeue()
    queue.dequeue()
    queue.dequeue()
    queue.peek()
    queue.dequeue()
    

if __name__ == "__main__":
    print("Testing for Array Implementation of Circular Queue: ")
    arrQueue = CircularArrQueue(5)
    test(arrQueue)
    
    print("Testing for Linked List Implementation of Circular Queue: ")
    llQueue = CircularLlQueue(5)
    test(llQueue)