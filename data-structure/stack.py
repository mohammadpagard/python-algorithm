from typing import Any


class Stack:
    """Simple implementation of stacks, using a list

    """
    
    def __init__(self):
        self.stack = [] # initialize an empty list -stack-

    def size(self) -> int:
        """Get the length of stack
        """

        return len(self.stack)

    def is_empty(self) -> bool:
        """Check the stack is empty or not, if is empty, return True and print some msg
        otherwise, return False.
        """
        
        if self.size() == 0:
            print("The stack is empty...")
            return True
        return False

    def push(self, element: Any) -> list:
        """Add an item to the top of the stack, and then return the stack.
        """

        self.stack.append(element)
        return self.stack

    def pop(self) -> list:
        """Remove and return the item from the top of the stack.
        If stack is empty, show the `stack is empty` message.
        Otherwise, remove a top item and return the stack.
        """

        if self.is_empty():
            return "Stack is empty..."
        self.stack.pop()
        return self.stack

    def peek(self) -> Any:
        """Return the top item
        If the stack is empty, show the `stack is empty` message.
        Otherwise, return the top item of stack.
        """

        if self.is_empty():
            return "Stack is empty..."
        return self.stack[-1]


stack = Stack()
