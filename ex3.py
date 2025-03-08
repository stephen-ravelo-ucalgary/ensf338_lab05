import random
import timeit
from matplotlib import pyplot as plt
import pandas as pd
import numpy as np

class MyArrayStack:
    def __init__(self):
        self._storage = []
        
    def push(self, value):
        self._storage.append(value)
        
    def pop(self):
        # Note that in Python "not <list>" evaluates to True if the list is empty
        if not self._storage:
            return None
        else:
            return self._storage.pop()
        
    def peek(self):
        if not self._storage:
            return None
        else:
            return self._storage[-1]
    
    def doTasks(self, tasks):
        for task in tasks:
            if task[0] == 0:
                self.push(task[1])
            else:
                self.pop()
        
class ListNode:
    def __init__(self, value):
        self._value = value
        self._next = None

    def getData(self):
        return self._value

    def setData(self, value):
        self._value = value

    def getNext(self):
        return self._next

    def setNext(self, next):
        self._next = next

    def toString(self):
        return str(self._value)
    
class MyListStack:
    def __init__(self):
        self._head = None

    def push(self, value):
        node = ListNode(value)
        node.setNext(self._head)
        self._head = node

    def pop(self):
        if self._head is None:
            return None
        else:
            retval = self._head.getData()
            self._head = self._head.getNext()
            return retval
        
    def peek(self):
        if self._head is None:
            return None
        else:
            return self._head.getData()
    
    def doTasks(self, tasks):
        for task in tasks:
            if task[0] == 0:
                self.push(task[1])
            else:
                self.pop()
            
def generate_tasks(num):
    tasks = []
    for i in range(num):
        if random.random() <= 0.7:
            tasks.append([0, random.randrange(1000)])
        else:
            tasks.append([1])
    return tasks

if __name__ == "__main__":
    numTasks = 10000
    numLists = 100
    numTimeit = 1
    
    arrayAverages = []
    listAverages = []
    
    for i in range(numLists):
        arrayStack = MyArrayStack()
        listStack = MyListStack()
        
        tasks = generate_tasks(numTasks)
        
        arrayTime = timeit.timeit(lambda: arrayStack.doTasks(tasks), number=numTimeit)
        arrayAverage = arrayTime * 1000 / numTimeit
        arrayAverages.append(arrayAverage)
        listTime = timeit.timeit(lambda: listStack.doTasks(tasks), number=numTimeit)
        listAverage = listTime * 1000 / numTimeit
        listAverages.append(listAverage)
        
        df_data = np.array([[arrayAverage, listAverage]])
        df = pd.DataFrame(df_data, columns=['array stack (ms)', 'list stack (ms)'])
        print(df.to_string(index=False))
    
    print("\nOverall results:")
    df_data = np.array([[sum(arrayAverages)/len(arrayAverages), sum(listAverages)/len(arrayAverages)]])
    df = pd.DataFrame(df_data, columns=['array stack (ms)', 'list stack (ms)'])
    print(df.to_string(index=False))
    
    ax = plt.figure().add_subplot()
    ax.scatter(range(1, 101), arrayAverages,  c="red", label="array stack")
    ax.scatter(range(1, 101), listAverages,  c="blue", label="list stack")
    ax.set_title("array stack vs. list stack")
    ax.set_xlabel("")
    ax.set_ylabel("time (ms)")
    ax.set_xlim(0)
    ax.set_ylim(0)
    ax.legend()
    plt.show()