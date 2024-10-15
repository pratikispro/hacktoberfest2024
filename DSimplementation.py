# Data Structures Implementation in Python

# 1. Stack Implementation
class Stack:
    def __init__(self):
        self.stack = []

    def push(self, value):
        self.stack.append(value)

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        return None

    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        return None

    def is_empty(self):
        return len(self.stack) == 0

    def size(self):
        return len(self.stack)

# 2. Queue Implementation
class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, value):
        self.queue.append(value)

    def dequeue(self):
        if not self.is_empty():
            return self.queue.pop(0)
        return None

    def is_empty(self):
        return len(self.queue) == 0

    def size(self):
        return len(self.queue)

# 3. Linked List Implementation
class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def print_list(self):
        cur_node = self.head
        while cur_node:
            print(cur_node.data, end=" -> ")
            cur_node = cur_node.next
        print(None)

# 4. Binary Tree Implementation
class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if not self.root:
            self.root = TreeNode(data)
        else:
            self._insert(self.root, data)

    def _insert(self, node, data):
        if data < node.data:
            if node.left:
                self._insert(node.left, data)
            else:
                node.left = TreeNode(data)
        else:
            if node.right:
                self._insert(node.right, data)
            else:
                node.right = TreeNode(data)

    def inorder_traversal(self, node):
        if node:
            self.inorder_traversal(node.left)
            print(node.data, end=" ")
            self.inorder_traversal(node.right)

# 5. Graph Implementation using Adjacency List
class Graph:
    def __init__(self):
        self.graph = {}

    def add_vertex(self, vertex):
        if vertex not in self.graph:
            self.graph[vertex] = []

    def add_edge(self, vertex, edge):
        if vertex in self.graph:
            self.graph[vertex].append(edge)

    def print_graph(self):
        for vertex in self.graph:
            print(f"{vertex}: {self.graph[vertex]}")

# Example Usage
if __name__ == "__main__":
    # Stack Example
    stack = Stack()
    stack.push(10)
    stack.push(20)
    print("Stack after pushing 10 and 20:", stack.stack)
    stack.pop()
    print("Stack after popping:", stack.stack)

    # Queue Example
    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    print("Queue after enqueuing 1 and 2:", queue.queue)
    queue.dequeue()
    print("Queue after dequeuing:", queue.queue)

    # Linked List Example
    linked_list = LinkedList()
    linked_list.append(5)
    linked_list.append(10)
    print("Linked List after appending 5 and 10:")
    linked_list.print_list()

    # Binary Tree Example
    tree = BinaryTree()
    tree.insert(15)
    tree.insert(10)
    tree.insert(20)
    print("Inorder traversal of Binary Tree:")
    tree.inorder_traversal(tree.root)
    print()

    # Graph Example
    graph = Graph()
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_edge(1, 2)
    graph.add_edge(2, 1)
    print("Graph adjacency list:")
    graph.print_graph()
