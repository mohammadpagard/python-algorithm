"""
Moving of disks should follow the following rules:
    - Only one disk can moved at a time.
    - A disk can only be moved if it's the uppermost disk on a stack.
    - No disk may be placed on top of a smalled disk.

"""

def hanoi_tower(n: int, source: str, target: str, auxiliary: str) -> str:
    move = 0

    if n == 1:
        print("Move disk 1 from {} to {}".format(source, target))
        return
    # move `n-1` disks from `source` to `auxiliary`
    hanoi_tower(n - 1, source, auxiliary, target)
    # move the `nth` disk from `source` to `target`
    print("Move disk {} from {} to {}".format(n, source, target))
    # move the `n-1` disks from `auxiliary` to `target`
    hanoi_tower(n - 1, auxiliary, target, source)

    move = 2**n - 1 # number of move
    return f"Number of moves: {move}"

# example
print(hanoi_tower(3, 'A', 'B', 'C'))
