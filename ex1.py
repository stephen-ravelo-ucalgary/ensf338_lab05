import sys

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def push(self, data):
        new_node = Node(data)

        # check memory allocation for new node failed
        if not new_node:
            print("\nStack Overflow")
            return
        
        new_node.next = self.head
        self.head = new_node
    
    def pop(self):
        if self.is_empty():
            print("\nStack Underflow")
            return None
        else:
            temp = self.head
            value = self.head.data
            self.head = self.head.next
            del temp
            return value
        
    def peek(self):
        if not self.is_empty():
            return self.head.data
        else:
            print("\nStack is empty")

# Stack-based Parser
stk = Stack()
expression = sys.argv[1]
expression = expression.replace("(", "")
expression = expression.replace(")", "")
split_exp = expression.split()

for i in split_exp[:: -1]:
    print(i)

# 