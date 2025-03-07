import random
import timeit
from matplotlib import pyplot as plt
import pandas as pd
import numpy as np

class ArrayPriorityQueueMergeSort:
    def __init__(self, capacity):
        self.capacity = capacity
        self.queue = [None] * capacity
        self.head = -1
        self.tail = -1

    def is_empty(self):
        return self.head == -1

    def is_full(self):
        return self.tail + 1 == self.capacity

    def enqueue(self, item):
        if self.is_full():
            #print("Queue is full. Unable to enqueue item.")
            return
        elif self.is_empty():
            self.head = 0
            self.tail = 0
        else:
            self.tail += 1
        self.queue[self.tail] = item
        merge_sort(self.queue, self.head, self.tail)

    def dequeue(self):
        if self.is_empty():
            #print("Queue is empty. Unable to dequeue item.")
            return None
        item = self.queue[self.head]
        if self.head == self.tail:
            self.head = -1
            self.tail = -1
        else:
            self.head += 1
        return item

    def peek(self):
        if self.is_empty():
            #print("Queue is empty. Unable to peek item.")
            return None
        return self.queue[self.head]
    
    def execute_tasks(self, tasks):
        for task in tasks:
            if task[0] == 0:
                self.enqueue(task[1])
            else:
                self.dequeue()

class ArrayPriorityQueueSortedInsertion:
    def __init__(self, capacity):
        self.capacity = capacity
        self.queue = [None] * capacity
        self.head = -1
        self.tail = -1

    def is_empty(self):
        return self.head == -1

    def is_full(self):
        return self.tail + 1 == self.capacity

    def enqueue(self, item):
        if self.is_full():
            #print("Queue is full. Unable to enqueue item.")
            return
        elif self.is_empty():
            self.head = 0
            self.tail = 0
            self.queue[self.tail] = item
        else:
            cur = self.head
            while(cur <= self.tail and item > self.queue[cur]):
                cur += 1

            self.tail += 1

            for i in range(self.tail, cur - 1, -1):
                self.queue[i] = self.queue[i - 1]

            self.queue[cur] = item

    def dequeue(self):
        if self.is_empty():
            #print("Queue is empty. Unable to dequeue item.")
            return None
        item = self.queue[self.head]
        if self.head == self.tail:
            self.head = -1
            self.tail = -1
        else:
            self.head += 1
        return item

    def peek(self):
        if self.is_empty():
            #print("Queue is empty. Unable to peek item.")
            return None
        return self.queue[self.head]

    def execute_tasks(self, tasks):
        for task in tasks:
            if task[0] == 0:
                self.enqueue(task[1])
            else:
                self.dequeue()

def merge(arr, low, mid, high):
    # Get length of left and right arrays
    l_length = mid - low + 1
    r_length = high - mid

    # Allocate two new arrays and fill them with their respective elements
    left_arr = [0] * l_length
    right_arr = [0] * r_length
    for i in range(l_length):
        left_arr[i] = arr[low + i]
    for i in range(r_length):
        right_arr[i] = arr[mid + i + 1]

    # Fill original array in sorted order until we reach the end of one sub-array
    i = 0
    j = 0
    k = low
    while i < l_length and j < r_length:
        if left_arr[i] <= right_arr[j]:
            arr[k] = left_arr[i]
            i += 1
        else:
            arr[k] = right_arr[j]
            j += 1
        k += 1
    
    # Insert remaining elements
    while i < l_length:
        arr[k] = left_arr[i]
        i += 1
        k += 1
    while j < r_length:
        arr[k] = right_arr[j]
        j += 1
        k += 1

def merge_sort(arr, low, high):
    if low < high:
        mid = (low + high) // 2
        merge_sort(arr, low, mid)
        merge_sort(arr, mid + 1, high)
        merge(arr, low, mid, high)

def generate_tasks(num):
    tasks = []
    for i in range(num):
        if random.random() <= 0.7:
            tasks.append([0, random.randrange(1000)])
        else:
            tasks.append([1])
    return tasks

if __name__ == "__main__":
    DEBUG = False


    if (DEBUG):
        tasks = generate_tasks(1000)
        capacity = 1000

        mergeQueue = ArrayPriorityQueueMergeSort(capacity)
        mergeQueue.execute_tasks(tasks)
        print(mergeQueue.queue)
        print(len(mergeQueue.queue))
        print(mergeQueue.head, mergeQueue.queue[mergeQueue.head])
        print(mergeQueue.tail, mergeQueue.queue[mergeQueue.tail], "\n\n")

        insertionQueue = ArrayPriorityQueueSortedInsertion(capacity)
        insertionQueue.execute_tasks(tasks)
        print(insertionQueue.queue)
        print(len(insertionQueue.queue))
        print(insertionQueue.head, insertionQueue.queue[insertionQueue.head])
        print(insertionQueue.tail, insertionQueue.queue[insertionQueue.tail])
    else:
        num_tasks = 1000

        mergeQueueAverages = []
        insertionQueueAverages = []

        for i in range(100):
            tasks = generate_tasks(num_tasks)
            mergeQueue = ArrayPriorityQueueMergeSort(1000)
            insertionQueue = ArrayPriorityQueueSortedInsertion(1000)
            mergeQueueTime = timeit.timeit(lambda: mergeQueue.execute_tasks(tasks), number=1)
            mergeQueueAverage = mergeQueueTime * 1000
            mergeQueueAverages.append(mergeQueueAverage)
            insertionQueueTime = timeit.timeit(lambda: insertionQueue.execute_tasks(tasks), number=1)
            insertionQueueAverage = insertionQueueTime * 1000
            insertionQueueAverages.append(insertionQueueTime)
            df_data = np.array([[mergeQueueAverage, insertionQueueAverage]])
            df = pd.DataFrame(df_data, columns=['priority queue with merge sort (ms)', 'priority queue with sorting on insertion (ms)'])
            print(df.to_string(index=False))


        print("Overall results:")
        df_data = np.array([[sum(mergeQueueAverages) / len(mergeQueueAverages), sum(insertionQueueAverages) / len(insertionQueueAverages)]])
        df = pd.DataFrame(df_data, columns=['priority queue with merge sort (ms)', 'priority queue with sorting on insertion (ms)'])
        print(df.to_string(index=False))

'''
Question 5

By inserting the element in its appropriate location, we have to iterate through the array
once each time. This is because we first traverse until the correct spot is found, and then
shift the rest of the elements right. So the complexity is O(n).

By running merge sort every enqueue, the worst case each task is O(nlogn).

Thus, inserting elements at their appropriate location is much faster.
'''