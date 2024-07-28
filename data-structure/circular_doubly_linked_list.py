class Node:
    """A class to represent a node in Circular Doubly Linked List.
    Attributes:
        - data(Any): The data stored in the node.
        - next(Node): The next node in the list.
        - prev(Node): The previous node in the list.
    """

    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None
    

class CircularDoublyLinkedList:
    """A class to represent a Circular Doubly Linked List.
    Attributes:
        - head(Node): The head/start node of the list.
    """
    
    def __init__(self):
        self.head = None
    
    def insert_begin(self, data):
        """Insert a new node at the beginning of the list.
        If the list is empty, then the new node is points to the `head` node of the list
        and points to itself for both the next and previous pointers.
        If the list is not empty, then the new node is placed before the current `head` node 
        and the important pointers are updated.

        Parameters:
            - data(Any): The data to be stored in a new node
        """
        new_node = Node(data)
        
        if self.head is None:
            new_node.next = new_node.prev = new_node
            self.head = new_node
        else:
            tail = self.head.prev   # get last node

            tail.next = new_node    # last node point to the new node
            new_node.prev = tail    # `new node previous` points to the last node
            new_node.next = self.head   # new node points to the `head` node
            self.head.prev = new_node   # `head node previous` points to the new node 
            self.head = new_node    # new node is `head` node

    def insert_end(self, data):
        """Inserts a new node at the end of the list.
        If the list is empty, then the new node is points to the `head` node of the list
        and points to itself for both the next and previous pointers.
        If the list is not empty, then the new node is placed after 
        the current `tail` node (wich is the previous node to the `head` node) and the important 
        pointers are updated.

        Parameters
            - data(Any): The data to be stored in the new node.
        """
        new_node = Node(data)

        if self.head is None:
            new_node.next = new_node.prev = new_node
            self.head = new_node
        else:
            tail = self.head.prev   # get last node

            tail.next = new_node    # last node points to the new node
            new_node.prev = tail    # `new node previous` points to the last node
            new_node.next = self.head
            self.head.prev = new_node

    def display(self):
        """Displays the nodes in the Circular Doubly Linked List
        """
        nodes = []
        current = self.head

        if self.head is None:
            print("List is empty...")
            return

        while True:
            nodes.append(current.data)
            current = current.next
            if current == self.head:
                break

        result = ' -> '.join(str(data) for data in nodes)
        print(result, '->', nodes[0])   # print result and last node point to first node


cdll = CircularDoublyLinkedList()
