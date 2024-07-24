def zigzag(array1: list[int], array2: list[int]):
    """
    Two Pointer Technique
    """

    i, j = 0, 0
    result = []

    while i < len(array1) and j < len(array2):
        if array1[i] not in result:
            result.append(array1[i])
            i += 1
        if array2[j] not in result:
            result.append(array2[j])
            j += 1
    return result


class ZigZag:
    """
    Queue Data Structure
    """
    def __init__(self, seq1: list[int], seq2: list[int]):
        self.queue = [seq1, seq2]

    def next(self):
        move = self.queue.pop(0)
        item = move.pop(0)
        if move:
            self.queue.append(move)
        return item

    def has_next(self):
        if self.queue:
            return True
        return False

