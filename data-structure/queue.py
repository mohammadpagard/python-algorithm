from typing import Any


class Queue:
    """Simple implementation of queue, using a list
    """

    def __init__(self):
        self.queue = [] # initialize an empty list -queue-

    def size(self) -> int:
        """Get the length of queue
        """
        return len(self.queue)

    def is_empty(self) -> bool:
        """Check the stack is empty or not, if is empty, return True and print some msg
        otherwise, return False.
        """
        if self.size() == 0:
            print("The queue is empty...")
            return True
        return False

    def enqueue(self, value: Any) -> None:
        """Add an element to the end of the queue.
        """
        self.queue.append(value)

    def dequeue(self):
        """Remove an element from the front of the queue.
        """
        if self.is_empty():
            return "The queue is empty..."
        popped = self.queue.pop(0)
        print("Removed element {} in queue.".format(popped))

    def get_front(self):
        """Get the front element of the queue.
        """
        if self.is_empty():
            return "The queue is empty..."
        return self.queue[0]

    def get_rear(self):
        """Get the last element of the queue.
        """
        if self.is_empty():
            return "The queue is empty..."
        return self.queue[-1]
    
    def display(self):
        """Display the queue
        """
        if self.is_empty():
            print("The queue is empty...")
        return "Queue: {}".format(self.queue)


queue_obj = Queue()
