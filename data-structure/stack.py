from typing import Any


class StackList:
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

    def pop(self) -> list:
        """Remove and return the item from the top of the stack.
        If stack is empty, show the `stack is empty` message.
        Otherwise, remove a top item and return the stack.
        """

        if self.is_empty():
            return "Stack is empty..."
        popped = self.stack.pop()
        print("Removed element {} in stack.".format(popped))

    def peek(self) -> Any:
        """Return the top item
        If the stack is empty, show the `stack is empty` message.
        Otherwise, return the top item of stack.
        """

        if self.is_empty():
            return "Stack is empty..."
        return self.stack[-1]

    def display(self):
        """Display the stack
        """
        if self.is_empty():
            print("The stack is empty...")
        return "Stack: {}".format(self.stack)


stack_list = StackList()


class StackString:
    """Simple implementation of stacks, using a string
    """

    def __init__(self):
        self.stack = '' # initialize an empty string -stack-

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

    def push(self, element: Any) -> str:
        """Add an item to the top of the stack, and then return the stack.
        """

        self.stack += str(element)
        return self.stack

    def pop(self) -> str:
        """Remove and return the item from the top of the stack.
        If stack is empty, show the `stack is empty` message.
        Otherwise, remove a top item and return the stack.
        """

        if self.is_empty():
            return "Stack is empty..."

        stack = self.stack
        length = len(stack) - 1 # get the top item of the stack
        self.stack = stack.rstrip(stack[length])    # strip stack from right
        length -= 1 # decreasing the pointer
        return self.stack

    def peek(self) -> Any:
        """Return the top item
        If the stack is empty, show the `stack is empty` message.
        Otherwise, return the top item of stack.
        """

        if self.is_empty():
            return "Stack is empty..."
        return self.stack[-1]


stack_string = StackString()

""" Another way to pop() action in Stack String:

    stack = self.stack
    stack = stack.rstring(stack[-1])
"""
