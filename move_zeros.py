"""
    Move Zeros
    [0, False, 1, 0, 1, 2, 0, 1, 3, 'python', 0] => [False, 1, 1, 2, 1, 3, 'python', 0, 0, 0, 0]

    move zeros to end of the list
"""

def move_zeros(array: list) -> list:
    pointer = len(array) - 1
    zero = 0

    while pointer >= 0:
        element = array[pointer]

        if element == 0 and type(element) != bool:
            array.pop(pointer)
            zero += 1
        pointer -= 1

    array.extend([0] * zero)
    return array

print(move_zeros([0, False, 1, 0, 1, 2, 0, 1, 3, 'python', 0]))

