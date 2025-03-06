import random
import timeit
import matplotlib.pyplot as plt

class ArrayQueue:
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
            # print("Queue is full, unable to enqueue item.")
            return
        elif(self.isEmpty()):
            self.head = 0
            self.tail = 0
        else:
            self.head = (self.head - 1) % self.capacity
        self.queue[self.head] = item
        
    def dequeue(self):
        if(self.isEmpty()):
            # print("Queue is empty, unable to dequeue item.")
            return None
        
        item = self.queue[self.tail]
        
        if(self.head == self.tail):
            self.head = -1
            self.tail = -1
        else:
            self.tail = (self.tail - 1) % self.capacity
        
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
            # print("Queue is empty, unable to dequeue item")
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

def genTasks(numTasks):
    tasks = []
    
    for _ in range(numTasks):
        if (random.random() < 0.7):
            tasks.append(("enqueue", random.randint(1, 100)))
        else:
            tasks.append(("dequeue", None))
            
    return tasks

def runTasks(queue, tasks):
    for op, val in tasks:
        if (op == "enqueue"):
            queue.enqueue(val)
        elif (op == "dequeue"):
            queue.dequeue()

def testArrQueue():
    tasks = genTasks(10000)
    queue = ArrayQueue(10000)
    runTasks(queue, tasks)

def testLinkedListQueue():
    tasks = genTasks(10000)
    queue = linkedListQueue()
    runTasks(queue, tasks)

        
if __name__ == "__main__":
    iterations = 100
    repititions = 10
    setupArr = "from __main__ import testArrQueue"
    setupLl = "from __main__ import testLinkedListQueue"
    
    arrQueueTimes = timeit.repeat("testArrQueue()", setup=setupArr, repeat=repititions, number=iterations)
    llQueueTimes = timeit.repeat("testLinkedListQueue()", setup=setupLl, repeat=repititions, number=iterations) 

    avgArrQueueTime = sum(arrQueueTimes) / len(arrQueueTimes)
    avgLlQueueTime = sum(llQueueTimes) / len(llQueueTimes)
    
    print(f"Array Queue Average Execution Time: {avgArrQueueTime}")
    print(f"Linked List Queue Average Execution Time: {avgLlQueueTime}")
    
    plt.figure(figsize=(10,6))
    bins = 5
    plt.hist(arrQueueTimes, bins=bins, alpha=0.5, label="Array Queue")
    plt.hist(llQueueTimes, bins=bins, alpha=0.5, label="Linked List Queue")
    plt.xlabel("Execution Time (Seconds)")
    plt.ylabel("Frequency")
    plt.title(f"Distribution of Execution Times for Array and Linked List Queues")
    plt.legend()
    plt.show()
    
    #   The array-based queue has more consistent performance, as enqueue and dequeue for an array
    #   has a O(1) complexity. The linked list based queue requires traversal through the list for each
    #   dequeue. This is shown on the plot, as the array-based queue has a constant time throughout the histogram
    #   while the linked list queue has times that vary within a range.