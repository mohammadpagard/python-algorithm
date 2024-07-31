from typing import Any


class Node:
    """A class to represent a node in Circular Linked List.
    Attributes:
        - data(Any): The data stored in the node.
        - next(Node): The next node in the list.
    """

    def __init__(self, data):
        self.data = data
        self.next = None


class StackLinkedList:
    """A class to represent a Stack Linked List.
    Attributes:
        - head(Node): The head/start node of the list, this is a top item of the stack
    """

    def __init__(self):
        self.head = None    # Top node/item of the stack

    def is_empty(self) -> bool:
        """Check the stack/list is empty or not, if is empty, return True and print some msg
        otherwise, return False.
        """

        if self.head == None:
            print("List is empty...")
            return True
        return False

    def push(self, data: Any) -> None:
        """Insert at top of the list.
        Check if `head` is None, then a new node is the `head` node, otherwise, the next pointer
        of the new node is points to the `head node/top item` and the new node is new head/top.
        """
        new_node = Node(data)   # create a new node

        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node
    
    def pop(self) -> Any:
        """Delete the top node of the stack.
        This method handle the following cases:
        If the list is empty, it prints message indicating the list is empty.
        Otherwise, top node change to the next node of the head/top and then, the next pointer of the
        pointer(top_node) is equal to None and then print the top element that removed.
        """
        top_node = self.head

        if self.is_empty():
            return "List is empty..."
        else:
            self.head = self.head.next
            top_node.next = None
            return "Popped the {} element of the list".format(top_node.data)
    
    def peek(self) -> Any:
        """Return the head/top node
        If stack is empty, return a msg.
        Otherwise, return the head/top node of the stack/list
        """
 
        if self.is_empty():
            return "List is empty..."
        else:
            return self.head.data
    
    def display(self) -> str:
        """Display the stack.
        """
        top_node = self.head

        if self.is_empty():
            print("List is empty...")
        else:
            while top_node != None:
                print(top_node.data, end=" -> ")
                top_node = top_node.next
            print("None")


sll = StackLinkedList()
