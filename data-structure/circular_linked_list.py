class Node:
    """A class to represent a node in Circular Linked List.
    Attributes:
        - data(Any): The data stored in the node.
        - next(Node): The next node in the list.
    """

    def __init__(self, data):
        self.data = data
        self.next = None


class CircularLinkedList:
    """A class to represent a Circular Linked List.
    Attributes:
        - head(Node): The head/start node of the list.
    """

    def __init__(self):
        self.head = None

    def insert_begin(self, data) -> None:
        """Insert at begin of the list.
        Check if `head` is None, then a new node is the `head` node, otherwise, traverse the list
        until the last node, and then, the `next` item of the last node points to the new node, then 
        the `next` item of the new node points to the `head` node and finally sets the new node to the `head` node.
        """
        new_node = Node(data)
        current = self.head

        if self.head is None:
            self.head = new_node
            new_node.next = new_node
        else:
            new_node.next = self.head

            # traverse the list until the last node
            while current.next != self.head:
                current = current.next

            current.next = new_node # last node points to the new node
            self.head = new_node    # set the new node to `head`

    def insert_end(self, data) -> None:
        """Insert at begin of the list.
        Check if `head` is None, then a new node is the `head` node, otherwise, traverse the list
        until the last node, and then, the `next` item of the last node points to the new node, and the new node
        points to the `head` node.
        """
        new_node = Node(data=data)
        current = self.head

        if self.head is None:
            self.head = new_node
            new_node.next = new_node
        else:
            # traverse the list until the last node
            while current.next != self.head:
                current = current.next 
            current.next = new_node # set a new node to the last node
            new_node.next = self.head   # last node -new node- points to the `head` node

    def insert_at_position(self, position: int, data) -> None:
        """Insert at position
        Check if the position is not valid, show the Invalid message, and if the position is 0, then
        insert data at the beginning of the list, otherwise, traverse the list until the (counter less than position-1)
        and (last node), then move the pointers -count, current-, if the counter is equal to position-1,
        then the new node equal to the current node, after this, the new node is inserted at the position,
        and the current node points to the new node.
        """

        new_node = Node(data=data)
        current = self.head
        count = 0

        if position < 0:
            print("Invalid Position...")
            return
        elif position == 0:
            # if the position is 0, insert a new node at the beginning of the list
            self.insert_begin(data=data)
        else:
            while (count < position - 1) and (current.next != self.head):
                current = current.next
                count += 1
            if count == position - 1:
                new_node.next = current.next    # insert a new node at the position
                current.next = new_node # current node point to the new node
            else:
                print("Position Out Of Range...")

    def delete_begin(self):
        """Delete the node at the beginning of the list.
        This method handle the following cases:
        - If the list is empty, it prints a message indicating the list is empty.
        - If the list contains only one node, it removes that node and sets the `head` to none.
        - Otherwise -the list contains multiple nodes-, traverse the list until the last node, and then
            move/sets the `head` node to the next of the `head` nodes, and then the last node points to the `head`.
        """
        current = self.head

        if self.head is None:
            print("List is empty...")
            return
        if self.head.next == self.head:
            print("Deleted {} ".format(self.head.data))
            self.head = None
        else:
            # traverse the list until the last node
            while current.next != self.head:
                current = current.next

            self.head = self.head.next  # move the `head` to next node
            current.next = self.head    # last node points to the `head` node

    def delete_end(self):
        """Delete the node at the end of the list
        This method handle the following cases:
        - If the list is empty, it prints message indicating the list is empty.
        - If the list contains only one node, it removes that node and sets the `head` to None.
        - Otherwise -list contains multiple nodes-, traverse to the list until the last node, and
            during the traversing, the `current_pointer` sets to the previous `current`, and finally,
            the `current_pointer` sets to the last node.
        """
        current = self.head
        current_pointer = self.head # previous of `current`

        if not self.head:
            print("The list is empty.")
            return
        if self.head.next == self.head:
            print("Deleted {} ".format(self.head.data))
            self.head = None
        else:
            # traverse the list until the last node
            while current.next != self.head:
                current_pointer = current   # save the previous node of current
                current = current.next

        current_pointer.next = self.head    # previous node of last node points to the `head` node

    def display(self) -> str:
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


circular_list = CircularLinkedList()
